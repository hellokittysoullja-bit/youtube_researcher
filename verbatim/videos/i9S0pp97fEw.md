# How Duolingo Built a $1B App Empire (And You Can Too)

**Канал:** Anything  · 13 мин · субтитры: en (авто YouTube) · https://youtu.be/i9S0pp97fEw

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Личность маскота работает, когда аутентична продукту
`маскот · персонаж · удержание` · [02:56](https://youtu.be/i9S0pp97fEw?t=176)

**Мысль:** Сова Duo действительно «пилит» тебя уроками в продукте, а соцсети лишь усиливают эту уже существующую личность; без цепочек согласования.

**Слова автора:**

> Ones get five. Duolingo gets 11. Their social team treats Duo like an internet creator. Absurdist humor, trend jacking, breaking the fourth wall. Once a week, the team scrolls trending audio, picks ideas, and shoots. No approval chains, no corporate review boards. It works because the personality is authentic to the product. The owl actually does nag you to do your lessons. The social media just turns that up to 11.

**Для Напарника:** Голос кота в соцсетях и в приложении должен идти из реального поведения продукта (присутствие рядом), но без «нытья» и давления.


---

## 2. CURR: удержание текущих пользователей весомее привлечения
`метрики · удержание · процесс` · [04:27](https://youtu.be/i9S0pp97fEw?t=267)

**Мысль:** Метрика вероятности вернуться на следующей неделе у стабильно активных оказалась в 5 раз влиятельнее следующей по важности; фокус сместился на удержание.

**Слова автора:**

> Around 2018, their growth team developed the CUR framework, current user retention rate. It measures how likely a consistently engaged user is to come back next week. When they ran sensitivity analysis on what drives daily active users, CUR had five times the impact of the second best metric. That insight changed their entire strategy. They stopped obsessing over acquiring new users and started obsessing over keeping the ones they had.

**Для Напарника:** Для Напарника главная метрика: возвращается ли человек на следующей неделе, а не число установок.


---

## 3. Стрики и неприятие потери: данные Duolingo
`стрики · удержание · мотивация` · [05:22](https://youtu.be/i9S0pp97fEw?t=322)

**Мысль:** 7-дневная серия даёт в 3,6 раза больше вероятности остаться; заморозки, амулеты защищают серию; рычаг это неприятие потери, оно мотивирует сильнее награды.

**Слова автора:**

> Streaks are the foundation, consecutive days of completing at least one lesson. Their data shows users who maintain a 7-day streak are 3.6 times more likely to stay engaged over long term. Over 6 million users have active streaks of 7 days or more. The longest active streak is over 4,100 days. Someone has completed a lesson every single day for more than 11 years. They've built an economy around protecting your streak. Streak freezes cover a missed day. Weekend amulets protect weekends. Streak wagers let you bet gems on maintaining your streak. The lever is loss aversion. Losing a 200-day streak feels devastating. That's way more motivating than getting a reward.

**Для Напарника:** Не применимо в лоб: страх потери серии противоречит тону без стыда. Берём идею защиты (прощение пропуска), но не угрозу.


---

## 4. Уведомления как bandit-алгоритм: шаблоны как руки автомата
`уведомления · ИИ · удержание` · [06:43](https://youtu.be/i9S0pp97fEw?t=403)

**Мысль:** Каждый шаблон рассматривается как рука бандита; алгоритм подбирает лучшее сообщение для пользователя, учитывает усталость от новизны; результат +72% уроков.

**Слова автора:**

> And push notifications. Duolingo's are famous for being passive-aggressive. Things like, "These reminders don't seem to be working, so I'll stop sending them." But behind the humor is serious engineering. They published an academic paper on their notification system. They used a sleeping recovering bandit algorithm. Each notification template is treated like a slot machine arm. The algorithm learns which message works best for each user, accounts for novelty fatigue, and handles conditional availability. They trained it by sending 200 million notifications over 34 days. Users with optimized notifications completed 72% more lessons and maintain streaks 124% longer.

**Для Напарника:** Ротация нескольких тёплых шаблонов напоминаний с учётом усталости; тон без пассивной агрессии.


---

## 5. Стрик меряет «пришёл», а не мастерство; нужна защита от срыва
`стрики · привычки · СДВГ` · [10:16](https://youtu.be/i9S0pp97fEw?t=616)

**Мысль:** Измерять появление, а не результат, делает ежедневное участие достижимым; но нужны механики защиты, чтобы один занятой день не убил серию и не заставил бросить.

**Слова автора:**

> Because a streak redefines progress. Instead of measuring mastery, which is slow and discouraging, a streak measures showing up. That shift makes daily engagement feel achievable. If your app has any daily use case, fitness, journaling, learning, habit tracking, meditation, build a streak mechanic. But a simple day counter isn't enough. You need protection mechanics so users don't lose a 60-day streak to a busy Tuesday and quit forever.

**Для Напарника:** Метрика «пришёл посидеть с котом» вместо результата; пропуск не обнуляет остров, а прощается.


---

## 6. Пуши как продукт: 3-5 шаблонов, ротация, метрика возврата
`уведомления · микрокопирайтинг · удержание` · [11:00](https://youtu.be/i9S0pp97fEw?t=660)

**Мысль:** Не одно сообщение всем; ротировать шаблоны, мерить, какие приводят к завершённой сессии, а не просто открытию; тестировать время отправки.

**Слова автора:**

> Number two, treat push notifications as a product, not just a channel. Most apps send the same notification to everyone at the same time. Start with three to five different templates and rotate them. Track which ones bring users back to a completed session, not just which ones get opened. Test different send times. Optimal timing varies by user. And rotate your copy to avoid fatigue. Add personality. Duolingo's passive-aggressive owl isn't just funny, it's a retention mechanic.

**Для Напарника:** Мерить напоминания по завершённой сессии, а не по открытию; добавить личность кота.


---

## 7. Хороший бесплатный продукт; платно только комфорт
`цены · конверсия · этика` · [11:32](https://youtu.be/i9S0pp97fEw?t=692)

**Мысль:** Бесплатная часть должна быть настоящим продуктом, который рекомендуют; платными делают точки трения и удобство, а не само обучение.

**Слова автора:**

> Number three, your free tier has to be genuinely good, not a crippled demo, not a 7-day trial, a real product someone would recommend without ever paying you. That's what drives 80% organic acquisition. Then identify friction points, moments of waiting, limits, small annoyances, and make those upgrade triggers. Duolingo doesn't gate lessons behind a paywall, they gate comfort. Hearts create friction when you make mistakes. Ads interrupt flow. The actual learning is always free.

**Для Напарника:** Ядро Напарника (Фокус, остров) бесплатно полноценно; платить можно за украшения/комфорт, не за доступ к фокусу.
