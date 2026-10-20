"""Дословная выжимка по диапазонам: LLM выбирает только [t0,t1] и метки, текст берёт скрипт из транскрипта.
   Галлюцинации исключены по построению. Из текста убираются только слова-паразиты um/uh."""
import json, re, sqlite3, sys
FILLERS = {"um", "uh", "umm", "uhh", "erm"}
def raw(vid, t0, t1, db="ytr.sqlite"):
    segs = json.loads(sqlite3.connect(db).execute("select segments from videos where id=?", (vid,)).fetchone()[0])
    words = " ".join(x[1] for x in segs if t0 <= x[0] < t1).split()
    return " ".join(w for w in words if re.sub(r"\W", "", w.lower()) not in FILLERS)
# ошибки автосубтитров в названиях: поправка допускается, но всегда перечисляется в шапке файла
ASR_FIX = {"tick tock": "tiktok"}
def norm(s):
    s = s.lower()
    for bad, good in ASR_FIX.items(): s = s.replace(bad, good)
    return [w.strip("'") for w in re.sub(r"[^\w\s']", " ", s).split() if w.strip("'") and w.strip("'") not in FILLERS]
if __name__ == "__main__":
    vid = sys.argv[1]
    for rng in sys.argv[2:]:
        a, b = map(int, rng.split("-")); print(f"### {a}-{b}\n{raw(vid, a, b)}\n")
