# Очередь агентов (лимит 20 одновременно)

Состояние на 2026-10-20 ~09:50 UTC. Сбор завершён: 1381 ролик (60 основных запросов + 12 доборных).
Заметки готовы по всем 37 основным пачкам.

## В работе (возобновлены после лимита)
- справочники: motion-interaction, behavioral-design, attention-neuro, mobile-systems, conversion-landing
- конспекты (дописываются): onboarding_01..03, behavioral-design_01..03, conversion-landing_01..03, podcasts-masters_01..06

## Ждут запуска (объём урезан по просьбе владельца: «если уже достаточно — не надо слишком много»)
- [ ] ТОЛЬКО notes company-teardowns-extra_01..03 (без конспектов)
- [ ] synth podcasts-masters (notes _01.._06 готовы)
- [ ] synth company-teardowns (notes _01.._04 + extra _01.._03)

## Отменено
- conspect company-teardowns_01..04, conspect attention-neuro_01..04 — знания уже в notes
- перекачка ~95 роликов с неверным языком субтитров — аналитики прочитали по смыслу
- [ ] SKILL.md + references → Напарник .claude/skills/uiux-knowledge (PR, по разрешению)
- [ ] push в youtube_researcher после каждой волны

## Находки для продукта (вне задачи, предложить отдельно)
- iOS: navigator.vibrate не работает → хаптики на iPhone нет; обход через <input type="switch"> (iOS 18+), риск что Apple закроет; проверить, работает ли программный клик вне жеста (hapticReward идёт из setTimeout 850мс)
- ПРОВЕРЕНО: hapticLandmark/hapticRare нигде не вызываются; reveal-island.tsx:78 всегда hapticReward() — редкая находка неотличима на ощупь
- ПРОВЕРЕНО: hapticStart на отправку реплики/тап по чипу (companion-chat.tsx:645,799) — хаптика на тап, против CLAUDE.md §4
- hapticDone одинаков для конца сессии и «скопировано» (chat-bubble.tsx:148); hapticThreshold один для пикера и порога жеста; нет выключателя вибрации
- лендинг: <title>/OG («не даст тебе слиться» — звучит как надзор) расходится с H1 («Начать — самое трудное. Я прихожу первым»); соцдоказательства нет — честный вариант: живой фрагмент продукта, потом одна реальная цифра
- спор: данные behavioral-design в пользу более короткого старта новичку, чем дефолт «25 мин рекомендуем»
- промпты api/companion|breakdown|session-voice: рецепт против дрейфа (бриф+non-goals, плохо/хорошо/идеально, самопроверка) — podcasts-masters
- drag-to-reply: обнаруживаемость жеста (ux-principles_03, JFirvnAVmtc)
- Tiimo (App of the Year 2025) — ближайший аналог, разобрать (zNU6DHHlq6U)
