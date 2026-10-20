"""Собирает базу знаний для агента: videos/<id>.md, by-tag/<тег>.md (слова авторов по теме), INDEX.md.
  assemble.py OUT_DIR hl/*.jsonl
"""
import collections, os, re, shutil, sys
sys.path.insert(0, ".")
import build_hl as B

out = sys.argv[1]
c, meta, items, skips, bad = B.build(sys.argv[2:])

SYN = {"ux": "UX", "ui": "UI", "ии": "ИИ", "adhd": "СДВГ", "сдвг": "СДВГ"}
def tag_norm(t):
    t = t.strip().lower().replace(" ", "-").replace("/", "-")
    return SYN.get(t, t)

for d in ("videos", "by-tag"):
    shutil.rmtree(f"{out}/{d}", ignore_errors=True); os.makedirs(f"{out}/{d}")

by_tag = collections.defaultdict(list)
nwords = ninsights = 0
for v, lst in items.items():
    _, title, ch, dur, lang, kind, words = meta[v]
    lst.sort(key=lambda x: x[0])
    parts = [f"# {title}\n",
             f"**Канал:** {ch} · {dur // 60} мин · субтитры: {lang} ({'ручные' if kind == 'manual' else 'авто YouTube'}) · https://youtu.be/{v}\n",
             "> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). "
             "«Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.\n"]
    for n, (t0, it, text) in enumerate(lst, 1):
        tags = [tag_norm(t) for t in it.get("tags", []) if t.strip()]
        link = f"https://youtu.be/{v}?t={t0}"
        head = f"## {n}. {it['label']}\n`{' · '.join(tags)}` · [{B.mmss(t0)}]({link})\n"
        body = f"**Мысль:** {it['why']}\n\n**Слова автора:**\n\n> {text}\n" + (f"\n**Для Напарника:** {it['app']}\n" if it.get("app") else "")
        parts.append("\n---\n\n" + head + "\n" + body)
        nwords += len(text.split()); ninsights += 1
        for t in set(tags):
            by_tag[t].append((title, ch, v, t0, it, text))
    open(f"{out}/videos/{v}.md", "w").write("\n".join(parts))

counts = {}
for t, lst in sorted(by_tag.items(), key=lambda kv: -len(kv[1])):
    if len(lst) < 3:
        continue
    fn = re.sub(r"[^\w\-]", "", t) or "x"
    counts[t] = (len(lst), len({x[2] for x in lst}), fn)
    lst.sort(key=lambda x: (x[0].lower(), x[3]))
    parts = [f"# Тема: {t}\n", f"Дословные слова авторов по теме «{t}»: {len(lst)} фрагментов из {len({x[2] for x in lst})} роликов. "
             "Читай подряд — это опыт практиков в их собственных словах; «Мысль» и «Для Напарника» — вывод разметчика.\n"]
    last_v = None
    for title, ch, v, t0, it, text in lst:
        if v != last_v:
            parts.append(f"\n\n# 🎬 {title} — {ch}\n")
            last_v = v
        parts.append(f"\n### {it['label']}  ·  [{B.mmss(t0)}](https://youtu.be/{v}?t={t0})\n**Мысль:** {it['why']}\n\n> {text}\n" +
                     (f"\n**Для Напарника:** {it['app']}\n" if it.get("app") else ""))
    open(f"{out}/by-tag/{fn}.md", "w").write("\n".join(parts))

idx = ["# Индекс базы знаний\n",
       f"{len(items)} роликов с дословными инсайтами · {ninsights} фрагментов · {nwords} слов авторов дословно.\n",
       "Открой файл темы из таблицы — там слова практиков по этой теме подряд, с таймкодами и ссылками. "
       "Полный текст любого ролика — в `transcripts/`.\n",
       "| Тема | Фрагментов | Роликов | Файл |", "|---|---:|---:|---|"]
for t, (n, nv, fn) in counts.items():
    idx.append(f"| {t} | {n} | {nv} | `by-tag/{fn}.md` |")
open(f"{out}/INDEX.md", "w").write("\n".join(idx) + "\n")
print(f"videos {len(items)}  insights {ninsights}  verbatim words {nwords}  tags {len(counts)}  rejected {dict(bad)}")
