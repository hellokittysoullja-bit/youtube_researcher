#!/bin/bash
# Установка окружения для ytr в облачной сессии Claude Code (можно вставить в Setup script окружения).
set -e
pip install -q -U "yt-dlp[default]" bgutil-ytdlp-pot-provider
# Генератор PO-токенов (обход бот-проверки YouTube для облачных IP), слушает 127.0.0.1:4416
if [ ! -d /opt/bgutil ]; then
  git clone -q --depth 1 https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git /opt/bgutil
  (cd /opt/bgutil/server && npm ci --silent && npx tsc)
fi
pgrep -f "bgutil/server/build/main.js" >/dev/null || (nohup node /opt/bgutil/server/build/main.js >/tmp/bgutil.log 2>&1 &)
