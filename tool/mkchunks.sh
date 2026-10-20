#!/bin/bash
# нарезка темы + слияние хвостовой мелкой пачки (<15k слов) в предыдущую
cd "$(dirname "$0")"
python3 -I chunk.py ytr.sqlite "$1" chunks 60000 > chunk_$1.txt
last=$(tail -1 chunk_$1.txt); n=$(wc -l < chunk_$1.txt)
w=$(echo "$last" | awk '{print $(NF-1)}'); f=$(echo "$last" | awk '{print $1}')
if [ "$n" -gt 1 ] && [ "$w" -lt 15000 ]; then prevf=$(sed -n "$((n-1))p" chunk_$1.txt | awk '{print $1}'); cat "$f" >> "$prevf"; rm "$f"; sed -i '$d' chunk_$1.txt; fi
cat chunk_$1.txt
