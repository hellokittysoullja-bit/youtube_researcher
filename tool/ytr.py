#!/usr/bin/env python3
"""ytr — YouTube-исследователь: поиск роликов по теме, полные транскрипты, база SQLite с полнотекстовым поиском.

Обход бот-проверки облачных IP: метаданные берём клиентом android_vr (он проходит без cookies),
а сами субтитры скачиваем напрямую по ссылке timedtext из ответа.

  ytr.py collect "тема" [--n 100] [--lang ru] [--workers 6]   найти и сохранить
  ytr.py add URL_or_ID [...]                                  добавить конкретные ролики
  ytr.py grep "запрос" [--limit 20]                            полнотекстовый поиск по всем транскриптам
  ytr.py show ID                                               полный транскрипт
  ytr.py list [--topic T]                                      что есть в базе
  ytr.py stats
  ytr.py export --topic T OUT.md                               все транскрипты темы одним файлом
"""
import argparse, json, os, random, sqlite3, sys, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import yt_dlp

DB = os.environ.get("YTR_DB", os.path.join(os.path.dirname(os.path.abspath(__file__)), "ytr.sqlite"))

SCHEMA = """
CREATE TABLE IF NOT EXISTS videos(
  id TEXT PRIMARY KEY, title TEXT, channel TEXT, duration INT, upload_date TEXT, views INT,
  lang TEXT, caption_kind TEXT, words INT, transcript TEXT, segments TEXT, description TEXT,
  fetched_at TEXT);
CREATE TABLE IF NOT EXISTS topics(topic TEXT, video_id TEXT, rank INT, PRIMARY KEY(topic, video_id));
CREATE TABLE IF NOT EXISTS failures(video_id TEXT PRIMARY KEY, reason TEXT, at TEXT);
CREATE VIRTUAL TABLE IF NOT EXISTS fts USING fts5(id UNINDEXED, title, transcript, tokenize='unicode61');
"""


def db():
    c = sqlite3.connect(DB, timeout=60)
    c.executescript(SCHEMA)
    return c


class _Mute:
    def debug(self, m): pass
    warning = info = error = debug


# mweb + PO-токены (bgutil-сервер на :4416) проходят даже когда IP в бот-блоке; android_vr — запасной
CLIENTS = [["mweb"], ["android_vr"]]
KEY_FILE = os.path.join(os.path.dirname(DB), "..", ".yt_api_key")


def ydl(client=("mweb",), **extra):
    opts = {"quiet": True, "no_warnings": True, "skip_download": True, "logger": _Mute(),
            "js_runtimes": {"node": {}}, "extractor_args": {"youtube": {"player_client": list(client)}}}
    opts.update(extra)
    return yt_dlp.YoutubeDL(opts)


def api_key():
    k = os.environ.get("YT_API_KEY")
    if not k and os.path.exists(KEY_FILE):
        k = open(KEY_FILE).read().strip()
    return k


def search(query, n, lang="ru", order="relevance", min_minutes=0):
    """YouTube Data API (100 ед. квоты за страницу из 50; лимит 10 000/день), без ключа — поиск yt-dlp."""
    key = api_key()
    if not key:
        with ydl(extract_flat=True) as y:
            r = y.extract_info(f"ytsearch{n}:{query}", download=False)
        return [e["id"] for e in r.get("entries", []) if e and e.get("id")]
    ids, token = [], None
    dur = {"medium": "medium", "long": "long"}.get("long" if min_minutes >= 20 else "medium" if min_minutes >= 4 else "")
    while len(ids) < n:
        q = {"part": "id", "type": "video", "maxResults": min(50, n - len(ids)), "q": query, "key": key,
             "relevanceLanguage": lang, "order": order}
        if dur:
            q["videoDuration"] = dur
        if token:
            q["pageToken"] = token
        d = fetch_json("https://www.googleapis.com/youtube/v3/search?" + urllib.parse.urlencode(q))
        ids += [i["id"]["videoId"] for i in d.get("items", [])]
        token = d.get("nextPageToken")
        if not token:
            break
    return ids


def pick_track(info, pref):
    """Ручные субтитры на языке оригинала > авто-оригинал (*-orig) > предпочитаемый язык > любой."""
    subs, auto = info.get("subtitles") or {}, info.get("automatic_captions") or {}
    # у роликов с дубляжом несколько дорожек *-orig (по одной на аудио) — язык оригинала берём из метаданных
    orig = [k[:-5] for k in auto if k.endswith("-orig")]
    meta = info.get("language")
    olang = next((o for o in orig if meta and (o == meta or o.split("-")[0] == meta.split("-")[0])), None) \
        or meta or (orig[0] if len(orig) == 1 else pref)
    order = [(subs, olang, "manual"), (subs, (meta or olang).split("-")[0], "manual"), (auto, f"{olang}-orig", "auto"),
             (subs, pref, "manual"),
             (auto, f"{pref}-orig", "auto"), (auto, olang, "auto")]
    order += [(subs, k, "manual") for k in subs if k != "live_chat"]
    for src, key, kind in order:
        for f in src.get(key) or []:
            if f.get("ext") == "json3":
                return key.replace("-orig", ""), kind, f["url"]
    return None


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=40).read())


def transcribe(vid, pref="ru", tries=6):
    last = None
    for a in range(tries):
        try:
            with ydl(CLIENTS[a % len(CLIENTS)]) as y:
                info = y.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
            tr = pick_track(info, pref)
            if not tr:
                return {"id": vid, "error": "no captions"}
            lang, kind, url = tr
            j = fetch_json(url)
            segs = []
            for e in j.get("events", []):
                t = "".join(s.get("utf8", "") for s in e.get("segs", []) or []).replace("\n", " ").strip()
                if t:
                    segs.append([round(e.get("tStartMs", 0) / 1000, 1), t])
            text = " ".join(s[1] for s in segs)
            return {"id": vid, "title": info.get("title"), "channel": info.get("channel") or info.get("uploader"),
                    "duration": info.get("duration"), "upload_date": info.get("upload_date"),
                    "views": info.get("view_count"), "lang": lang, "caption_kind": kind,
                    "words": len(text.split()), "transcript": text, "segments": json.dumps(segs, ensure_ascii=False),
                    "description": info.get("description")}
        except Exception as e:  # бот-проверка срабатывает эпизодически — повтор с отступом
            last = str(e)[:200]
            time.sleep(2 ** a + random.random() * 2)
    return {"id": vid, "error": last}


def save(c, r, topic=None, rank=None):
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if "error" in r:
        c.execute("INSERT OR REPLACE INTO failures VALUES(?,?,?)", (r["id"], r["error"], now))
    else:
        cols = ["id", "title", "channel", "duration", "upload_date", "views", "lang", "caption_kind",
                "words", "transcript", "segments", "description"]
        c.execute(f"INSERT OR REPLACE INTO videos({','.join(cols)},fetched_at) VALUES({','.join('?'*(len(cols)+1))})",
                  [r[k] for k in cols] + [now])
        c.execute("DELETE FROM fts WHERE id=?", (r["id"],))
        c.execute("INSERT INTO fts VALUES(?,?,?)", (r["id"], r["title"], r["transcript"]))
        c.execute("DELETE FROM failures WHERE video_id=?", (r["id"],))
    if topic:
        c.execute("INSERT OR IGNORE INTO topics VALUES(?,?,?)", (topic, r["id"], rank))
    c.commit()


def run(ids, topic, lang, workers):
    c = db()
    have = {row[0] for row in c.execute("SELECT id FROM videos")}
    todo = [(i, v) for i, v in enumerate(ids) if v not in have]
    for i, v in enumerate(ids):
        if v in have and topic:
            c.execute("INSERT OR IGNORE INTO topics VALUES(?,?,?)", (topic, v, i))
    c.commit()
    print(f"{len(ids)} роликов, уже в базе {len(ids) - len(todo)}, качаю {len(todo)}", file=sys.stderr)
    ok = fail = words = 0
    with ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(transcribe, v, lang): (i, v) for i, v in todo}
        for f in as_completed(futs):
            i, v = futs[f]
            r = f.result()
            save(c, r, topic, i)
            if "error" in r:
                fail += 1
                print(f"  ✗ {v}: {r['error'][:90]}", file=sys.stderr)
            else:
                ok += 1
                words += r["words"]
                print(f"  ✓ [{ok + fail}/{len(todo)}] {r['words']:>6} сл  {r['title'][:70]}", file=sys.stderr)
    print(f"готово: {ok} ок, {fail} без транскрипта, {words} слов", file=sys.stderr)


def main():
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest="cmd", required=True)
    a = s.add_parser("collect"); a.add_argument("query", nargs="+"); a.add_argument("--n", type=int, default=50)
    a.add_argument("--lang", default="ru"); a.add_argument("--workers", type=int, default=4); a.add_argument("--topic")
    a.add_argument("--order", default="relevance", help="relevance|viewCount|date|rating")
    a.add_argument("--min-minutes", type=int, default=0, help="4 = только средние+, 20 = только длинные")
    a = s.add_parser("add"); a.add_argument("ids", nargs="+"); a.add_argument("--topic"); a.add_argument("--lang", default="ru")
    a.add_argument("--workers", type=int, default=6)
    a = s.add_parser("grep"); a.add_argument("q"); a.add_argument("--limit", type=int, default=20)
    a = s.add_parser("show"); a.add_argument("id"); a.add_argument("--ts", action="store_true")
    a = s.add_parser("list"); a.add_argument("--topic")
    s.add_parser("stats")
    a = s.add_parser("export"); a.add_argument("--topic", required=True); a.add_argument("out")
    o = p.parse_args()

    if o.cmd == "collect":
        ids, seen = [], set()
        for q in o.query:  # несколько формулировок = шире охват темы
            for v in search(q, o.n, o.lang, o.order, o.min_minutes):
                if v not in seen:
                    seen.add(v); ids.append(v)
        run(ids, o.topic or o.query[0], o.lang, o.workers)
    elif o.cmd == "add":
        ids = [x.split("v=")[-1].split("&")[0].split("/")[-1] for x in o.ids]
        run(ids, o.topic, o.lang, o.workers)
    elif o.cmd == "grep":
        for vid, title, snip in db().execute(
                "SELECT id,title,snippet(fts,2,'«','»','…',24) FROM fts WHERE fts MATCH ? ORDER BY rank LIMIT ?",
                (o.q, o.limit)):
            print(f"{vid}  {title}\n   {snip}\n")
    elif o.cmd == "show":
        r = db().execute("SELECT title,channel,duration,transcript,segments FROM videos WHERE id=?", (o.id,)).fetchone()
        if not r:
            sys.exit("нет в базе")
        print(f"# {r[0]}\n{r[1]} · {r[2]//60} мин · https://youtu.be/{o.id}\n")
        if o.ts:
            for t, x in json.loads(r[4]):
                print(f"[{int(t)//60:02d}:{int(t)%60:02d}] {x}")
        else:
            print(r[3])
    elif o.cmd == "list":
        q = "SELECT v.id,v.words,v.lang,v.title FROM videos v"
        args = ()
        if o.topic:
            q += " JOIN topics t ON t.video_id=v.id WHERE t.topic=? ORDER BY t.rank"; args = (o.topic,)
        for row in db().execute(q, args):
            print(f"{row[0]}  {row[1]:>6} сл  {row[2]}  {row[3]}")
    elif o.cmd == "stats":
        c = db()
        n, w, d = c.execute("SELECT count(*),coalesce(sum(words),0),coalesce(sum(duration),0) FROM videos").fetchone()
        print(f"роликов: {n}, слов: {w}, часов видео: {d/3600:.1f}, неудач: {c.execute('SELECT count(*) FROM failures').fetchone()[0]}")
        for t, k in c.execute("SELECT topic,count(*) FROM topics GROUP BY topic"):
            print(f"  {k:>4}  {t}")
    elif o.cmd == "export":
        with open(o.out, "w") as f:
            for vid, title, ch, tr in db().execute(
                    "SELECT v.id,v.title,v.channel,v.transcript FROM videos v JOIN topics t ON t.video_id=v.id "
                    "WHERE t.topic=? ORDER BY t.rank", (o.topic,)):
                f.write(f"## {title}\n{ch} · https://youtu.be/{vid}\n\n{tr}\n\n")
        print(o.out)


if __name__ == "__main__":
    main()
