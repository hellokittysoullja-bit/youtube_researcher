"""Экспорт транскриптов из SQLite в transcripts/<topic>/<id>.md (+ index.tsv) — текстовая копия для git и grep."""
import json, os, sqlite3, sys
db, out = sys.argv[1], sys.argv[2]
c = sqlite3.connect(db)
idx = open(os.path.join(out, "index.tsv"), "w")
idx.write("id\ttopic\ttitle\tchannel\tminutes\tviews\tlang\twords\tupload_date\n")
for vid, title, ch, dur, views, lang, words, segs, up in c.execute(
        "SELECT id,title,channel,duration,views,lang,words,segments,upload_date FROM videos ORDER BY id"):
    t = c.execute("SELECT topic FROM topics WHERE video_id=? ORDER BY rowid LIMIT 1", (vid,)).fetchone()
    topic = t[0] if t else "misc"
    os.makedirs(os.path.join(out, topic), exist_ok=True)
    with open(os.path.join(out, topic, f"{vid}.md"), "w") as f:
        f.write(f"# {title}\n{ch} · {(dur or 0)//60} мин · {views} просмотров · {lang} · https://youtu.be/{vid}\n\n")
        last = -99
        for s, x in json.loads(segs):
            if s - last >= 30:
                f.write(f"\n\n[{int(s)//60:02d}:{int(s)%60:02d}] "); last = s
            f.write(x + " ")
        f.write("\n")
    idx.write("\t".join(str(v).replace("\t", " ") for v in (vid, topic, title, ch, (dur or 0)//60, views, lang, words, up)) + "\n")
