"""Перекачка роликов, у которых в базе субтитры не на языке автора (машинный перевод ar/hi/bn…)."""
import sys; sys.path.insert(0, ".")
import sqlite3, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import ytr
c = ytr.db()
ids = [r[0] for r in c.execute("select id from videos where substr(lang,1,2) not in ('en','ru')")]
print(len(ids), "to refetch", file=sys.stderr)
fixed, still = [], []
with ThreadPoolExecutor(4) as ex:
    futs = {ex.submit(ytr.transcribe, v, "en"): v for v in ids}
    for f in as_completed(futs):
        v = futs[f]; r = f.result()
        if "error" not in r and r["lang"][:2] in ("en", "ru"):
            ytr.save(c, r); fixed.append(v); print("fixed", v, r["lang"], r["words"], file=sys.stderr)
        else:
            still.append(v); print("still foreign", v, (r.get("lang") or r.get("error", ""))[:60], file=sys.stderr)
open("foreign_only.txt", "w").write("\n".join(still))
print(f"DONE fixed={len(fixed)} still_foreign={len(still)}", file=sys.stderr)
