"""Нарезает транскрипты темы на пачки ~60k слов с таймкодами каждые ~30с — вход для агентов-аналитиков."""
import json, os, sqlite3, sys
db, topic, out = sys.argv[1], sys.argv[2], sys.argv[3]
LIMIT = int(sys.argv[4]) if len(sys.argv) > 4 else 60000
c = sqlite3.connect(db)
rows = c.execute("""SELECT v.id,v.title,v.channel,v.duration,v.views,v.lang,v.words,v.segments FROM videos v
  JOIN topics t ON t.video_id=v.id WHERE t.topic=? AND v.words>=300
  AND (SELECT t2.topic FROM topics t2 WHERE t2.video_id=v.id ORDER BY t2.rowid LIMIT 1)=?
  ORDER BY v.views DESC""", (topic, topic)).fetchall()
ex = set(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "excluded.txt")).read().split()) \
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "excluded.txt")) else set()
rows = [r for r in rows if r[0] not in ex]
os.makedirs(out, exist_ok=True)
chunks, cur, n = [], [], 0
for r in rows:
    if cur and n + r[6] > LIMIT:
        chunks.append(cur); cur, n = [], 0
    cur.append(r); n += r[6]
if cur: chunks.append(cur)
for k, ch in enumerate(chunks, 1):
    p = os.path.join(out, f"{topic}_{k:02d}.md")
    with open(p, "w") as f:
        for vid, title, chan, dur, views, lang, words, segs in ch:
            f.write(f"\n\n######## VIDEO {vid} | {title} | {chan} | {dur//60} min | {views} views | {lang}\n")
            last = -99
            for t, x in json.loads(segs):
                if t - last >= 30:
                    f.write(f"\n[{int(t)//60:02d}:{int(t)%60:02d}] "); last = t
                f.write(x + " ")
    print(p, len(ch), "videos", sum(r[6] for r in ch), "words")
