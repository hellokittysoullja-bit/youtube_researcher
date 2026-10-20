"""Полные транскрипты (только язык автора en/ru) + каталог с оценкой ценности. export_kb.py DB OUT_DIR"""
import glob, json, os, re, sqlite3, sys
db, out = sys.argv[1], sys.argv[2]
c = sqlite3.connect(db)
val = {}
for f in glob.glob("conspects/*.md"):
    for p in re.split(r"\n(?=## )", open(f).read()):
        m = re.search(r"`([\w-]{11})`", p[:400]); v = re.search(r"\*\*Ценность:\*\*\s*([а-яё/ ]+)", p[:900], re.I)
        if m and v: val[m.group(1)] = v.group(1).strip().lower()
for f in glob.glob("notes/*.md"):
    for m in re.finditer(r"([\w-]{11})[^\n]{0,260}?ценност[а-яё]*:?\s*(высок|средн|низк|мусор)", open(f).read().split("## Знания")[0], re.I):
        val.setdefault(m.group(1), m.group(2).lower())
have = {os.path.basename(p)[:-3] for p in glob.glob("kb/videos/*.md")}
os.makedirs(out, exist_ok=True)
idx = open(os.path.join(out, "index.tsv"), "w")
idx.write("id\ttopic\ttitle\tchannel\tminutes\tviews\tlang\twords\tvalue\thas_insights\n")
n = skipped = 0
for vid, title, ch, dur, views, lang, words, segs in c.execute("select id,title,channel,duration,views,lang,words,segments from videos order by id"):
    if lang[:2] not in ("en", "ru"):
        skipped += 1; continue
    t = c.execute("select topic from topics where video_id=? order by rowid limit 1", (vid,)).fetchone()
    topic = t[0] if t else "misc"
    os.makedirs(os.path.join(out, topic), exist_ok=True)
    with open(os.path.join(out, topic, f"{vid}.md"), "w") as f:
        f.write(f"# {title}\n{ch} · {(dur or 0)//60} мин · {views} просмотров · {lang} · https://youtu.be/{vid}\n")
        last = -99
        for s, x in json.loads(segs):
            if s - last >= 30: f.write(f"\n\n[{int(s)//60:02d}:{int(s)%60:02d}] "); last = s
            f.write(x + " ")
        f.write("\n")
    idx.write("\t".join(str(x).replace("\t", " ") for x in (vid, topic, title, ch, (dur or 0)//60, views, lang, words, val.get(vid, "?"), "yes" if vid in have else "")) + "\n")
    n += 1
print("transcripts written:", n, " skipped (not author's language):", skipped)
