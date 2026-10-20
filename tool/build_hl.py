"""Сборка дословных инсайтов: JSONL от агентов (диапазон + первые/последние слова) → md с текстом автора из транскрипта.
Слова берёт скрипт; агент их не пишет. Якоря start/end обязаны найтись в окне, иначе инсайт отбраковывается.

  build_hl.py hl/*.jsonl            собрать hl_out/<id>.md и сводный индекс hl_out/INDEX.md
"""
import collections, json, re, sqlite3, sys
sys.path.insert(0, ".")
from extract import FILLERS

DB = "ytr.sqlite"
OUT = "hl_out"


def tokens(text):
    """Слова с исходным написанием (для вывода) и нормализованные (для поиска)."""
    text = re.sub(r"\[[^\]]*\]", " ", text)  # служебные теги субтитров: [music], [applause]…
    orig = [w for w in text.split() if re.sub(r"\W", "", w.lower()) not in FILLERS]
    norm = [re.sub(r"[^\w']", "", w.lower()).strip("'") for w in orig]
    return orig, norm


def find(seq, pat, start=0):
    n = len(pat)
    for i in range(start, len(seq) - n + 1):
        if seq[i:i + n] == pat:
            return i
    return -1


def mmss(t):
    return f"{t // 60:02d}:{t % 60:02d}"


def sentence(words):
    s = " ".join(words)
    # убрать заикания: подряд идущие одинаковые слова
    s = re.sub(r"\b(\w+)( \1\b)+", r"\1", s, flags=re.I)
    if s and s[0].islower():
        s = s[0].upper() + s[1:]
    return s


def build(files):
    c = sqlite3.connect(DB)
    meta = {r[0]: r for r in c.execute("select id,title,channel,duration,lang,caption_kind,words from videos")}
    segs = {}
    items = collections.defaultdict(list)
    skips = {}
    bad = collections.Counter()
    for f in files:
        for ln, line in enumerate(open(f), 1):
            line = line.strip()
            if not line:
                continue
            try:
                it = json.loads(line)
            except Exception:
                bad["json"] += 1
                continue
            v = it.get("v")
            if v not in meta:
                bad["unknown_video"] += 1
                continue
            if "skip" in it:
                skips[v] = it["skip"]
                continue
            if v not in segs:
                segs[v] = json.loads(c.execute("select segments from videos where id=?", (v,)).fetchone()[0])
            t0, t1 = int(it["t0"]), int(it["t1"])
            window = " ".join(x[1] for x in segs[v] if t0 - 15 <= x[0] < t1 + 15)
            orig, norm = tokens(window)
            sa, _ = tokens(it["start"]); sa = [re.sub(r"[^\w']", "", w.lower()).strip("'") for w in sa]
            ea, _ = tokens(it["end"]); ea = [re.sub(r"[^\w']", "", w.lower()).strip("'") for w in ea]
            i = find(norm, sa)
            if i < 0 and len(sa) > 3:
                i = find(norm, sa[:3])
            j = find(norm, ea, max(i, 0)) if i >= 0 else -1
            if j < 0 and len(ea) > 3 and i >= 0:
                j = find(norm, ea[-3:], i)
                if j >= 0:
                    j -= len(ea) - 3
            if i < 0 or j < 0 or j + len(ea) <= i:
                bad["anchor_not_found"] += 1
                continue
            text = sentence(orig[i:j + len(ea)])
            if not text.endswith((".", "?", "!")):
                text += "."
            items[v].append((t0, it, text))
    return c, meta, items, skips, bad


def write(c, meta, items, skips, bad):
    import os
    os.makedirs(OUT, exist_ok=True)
    tagidx = collections.defaultdict(list)
    for v, lst in items.items():
        _, title, ch, dur, lang, kind, words = meta[v]
        lst.sort(key=lambda x: x[0])
        out = [f"# {title}\n", f"**Канал:** {ch} · {dur // 60} мин · язык субтитров: {lang} ({'ручные' if kind == 'manual' else 'авто YouTube'}) · "
               f"https://youtu.be/{v}\n",
               "> Блоки «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; "
               "знаков препинания в авто-субтитрах мало). «Мысль» и «Для Напарника» — вывод разметчика, не речь автора.\n"]
        for n, (t0, it, text) in enumerate(lst, 1):
            tags = " · ".join(it.get("tags", []))
            out.append(f"\n---\n\n## {n}. {it['label']}\n`{tags}` · [{mmss(t0)}](https://youtu.be/{v}?t={t0})\n")
            out.append(f"**Мысль:** {it['why']}\n")
            out.append("**Слова автора:**\n\n> " + text + "\n")
            if it.get("app"):
                out.append(f"**Для Напарника:** {it['app']}\n")
            for t in it.get("tags", []):
                tagidx[t].append((v, t0, it["label"], title))
        open(f"{OUT}/{v}.md", "w").write("\n".join(out))
    return tagidx


if __name__ == "__main__":
    files = sys.argv[1:]
    c, meta, items, skips, bad = build(files)
    tagidx = write(c, meta, items, skips, bad)
    n_items = sum(len(x) for x in items.values())
    words = sum(len(t.split()) for lst in items.values() for _, _, t in lst)
    print(f"videos with insights: {len(items)}  insights: {n_items}  verbatim words: {words}  skipped videos: {len(skips)}  rejected: {dict(bad)}")
