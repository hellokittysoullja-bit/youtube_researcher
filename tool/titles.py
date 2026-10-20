"""Список роликов темы (id | название | канал | минут | начало описания) для предфильтра по релевантности."""
import sqlite3, sys
c = sqlite3.connect("ytr.sqlite")
for vid, t, ch, d, desc in c.execute("""SELECT v.id,v.title,v.channel,v.duration,v.description FROM videos v
    WHERE (SELECT t2.topic FROM topics t2 WHERE t2.video_id=v.id ORDER BY t2.rowid LIMIT 1)=? AND v.words>=300""", (sys.argv[1],)):
    print(f"{vid} | {t} | {ch} | {(d or 0)//60}m | {(desc or '').replace(chr(10),' ')[:140]}")
