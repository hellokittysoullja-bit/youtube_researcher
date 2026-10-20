import json, sqlite3, sys, os
ids = json.load(open(sys.argv[1])); prefix = sys.argv[2]; LIMIT = 50000
done = set(l.split()[0] for l in open("hl_done.txt")) if os.path.exists("hl_done.txt") else set()
ids = [v for v in ids if v not in done]
c = sqlite3.connect("ytr.sqlite")
def topic(v):
    r = c.execute("select topic from topics where video_id=? order by rowid limit 1", (v,)).fetchone(); return r[0] if r else "misc"
rows = []
for v in ids:
    r = c.execute("select id,title,channel,duration,views,lang,words,segments from videos where id=?", (v,)).fetchone()
    if r: rows.append((topic(v), -(r[4] or 0), r))
rows.sort(key=lambda x: (x[0], x[1]))
os.makedirs("chunks_hl", exist_ok=True)
chunks, cur, n = [], [], 0
for _, _, r in rows:
    if cur and n + r[6] > LIMIT: chunks.append(cur); cur, n = [], 0
    cur.append(r); n += r[6]
if cur: chunks.append(cur)
for k, ch in enumerate(chunks, 1):
    p = f"chunks_hl/{prefix}_{k:02d}.md"
    with open(p, "w") as f:
        for vid, title, chan, dur, views, lang, words, segs in ch:
            f.write(f"\n\n######## VIDEO {vid} | {title} | {chan} | {dur//60} мин | {views} просм. | {lang}\n")
            last = -99
            for t, x in json.loads(segs):
                if t - last >= 10: f.write(f"\n[{int(t)//60:02d}:{int(t)%60:02d}] "); last = t
                f.write(x + " ")
    print(p, len(ch), "videos", sum(r[6] for r in ch), "words")
