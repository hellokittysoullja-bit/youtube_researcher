"""Золотой набор: ролики с оценкой «высокая» (из конспектов и заметок аналитиков), речь автора на en/ru, достаточной длины."""
import collections, glob, re, sqlite3, json, sys
c = sqlite3.connect("ytr.sqlite")
meta = {r[0]: r for r in c.execute("select id,title,channel,lang,words,duration,views from videos")}
val = {}
for f in glob.glob("conspects/*.md"):
    for p in re.split(r"\n(?=## )", open(f).read()):
        m = re.search(r"`([\w-]{11})`", p[:400]); v = re.search(r"\*\*Ценность:\*\*\s*([а-яё/ ]+)", p[:900], re.I)
        if m and v: val[m.group(1)] = v.group(1).strip().lower()
for f in glob.glob("notes/*.md"):
    t = open(f).read()
    sec = t.split("## Знания")[0]
    for m in re.finditer(r"([\w-]{11})[^\n]{0,260}?ценност[а-яё]*:?\s*(высок|средн|низк|мусор)", sec, re.I):
        val.setdefault(m.group(1), m.group(2).lower() + ("ая" if m.group(2).lower() != "мусор" else ""))
cnt = collections.Counter(val.values())
print("value labels (conspects+notes):", cnt.most_common(6))
min_words = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
gold = [v for v, l in val.items() if l.startswith("высок") and v in meta and meta[v][3][:2] in ("en", "ru") and meta[v][4] >= min_words]
print("gold set (high, en/ru, >=%d words): %d videos, %d words" % (min_words, len(gold), sum(meta[v][4] for v in gold)))
json.dump(gold, open("gold_ids.json", "w"))
