# A Lesson in How Inconsistent UI Kills the First Experience | App Breakdown #88

**Канал:** App Breakdown · 13 мин · субтитры: en (авто YouTube) · https://youtu.be/hgpk0ejGs-E

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Подтверждение почты в онбординге убивает первый опыт
`онбординг · активация · доверие` · [01:25](https://youtu.be/hgpk0ejGs-E?t=85)

**Мысль:** Заставлять уходить из приложения в почту до первой ценности — устаревшая практика; есть десятки лучших способов.

**Слова автора:**

> Verify your email. Okay, this is the first time since like 2016 that I've seen an onboarding that makes me go to my email. This is terrible. I'm just going to hit skip. Never do this, okay? There are 20 different ways to do onboarding that are better than this.

**Для Напарника:** Не требовать подтверждения почты или аккаунта до первой сессии.


---

## 2. Длинную анимацию можно показывать, но нужно дать пропустить; триггер — тройной тап
`анимация · онбординг · доступность · крафт` · [04:24](https://youtu.be/hgpk0ejGs-E?t=264)

**Мысль:** Автор определял, что человек тапает по экрану три-четыре раза подряд, и без кнопки «пропустить» просто пропускал анимацию. Нетерпение пользователя — сигнал.

**Слова автора:**

> And this animation is taking forever. I am triple tapping and quadruple tapping here to speed it up. So that's one actually pro tip for you is if you want to do a long animation or show a long video to a user, that's totally fine. There's a lot of places where there's valuable, but if they want to skip, they should be able to skip. And one little trick I've used before is not including any skip button or but detecting if users triple or quadruple tap and skipping them in that case.

**Для Напарника:** Хореография RevealIsland и starting→running: тап по экрану во время анимации должен ускорять или завершать её, без отдельной кнопки пропуска.


---

## 3. Hold-to-commit: удержание усиливает ощущение намерения; без хаптики и ясности портит
`хаптика · микровзаимодействия · запуск-задачи · мотивация` · [04:58](https://youtu.be/hgpk0ejGs-E?t=298)

**Мысль:** Подпись или удержание делает обязательство тяжелее и значимее обычного тапа, но здесь исполнение плохое: мелкий текст, непонятно, что удерживать, нет хаптики.

**Слова автора:**

> And now we have a hold to commit. Now the hold to commit in this case it's not done in the proper way like the letters are tiny and it's not clear that I'm supposed to hold this, but holding to commit or signing to commit generally is a good way to make a user feel a heavier intention towards what they're about to do. Like it the some significance behind a regular tap.

**Для Напарника:** Кандидат на ритуал старта сессии: удержание кнопки «Начать» с нарастающей хаптикой (hapticStart на событие старта). Не применимо для частых действий: только для значимого старта, и без шкалы давления.


---

## 4. Дизайн строит доверие: нечёткий UX — отказ давать разрешения
`доверие · онбординг · дизайн-система · вкус` · [07:30](https://youtu.be/hgpk0ejGs-E?t=450)

**Мысль:** Автор нажимает «не разрешать» календарь и будильники, потому что приложение не вызвало доверия; при аккуратном проведении через всё он бы согласился.

**Слова автора:**

> I know you're probably watching this video and thinking, "Why are you pressing not allow if you're supposed to test the app?" But the reality is that from what I've seen in the app this far, I do not trust it. And I am not going to give my calendar and my alarms and all of these things to an app that I don't trust cuz design is also about building trust in the user. If this was a sleek app, if they had guided me through everything, if I had known what's going on, I would have given these permissions, no problem. But like this, I will not do it.

**Для Напарника:** Разрешения (уведомления, звук) запрашивать только после того, как продукт уже понравился, и объяснять зачем голосом кота. Качество визуала и согласованности напрямую влияет на готовность дать доступ.


---

## 5. Главная кнопка всегда в одном месте
`иерархия · онбординг · дизайн-система · мобильный` · [08:28](https://youtu.be/hgpk0ejGs-E?t=508)

**Мысль:** Когда CTA прыгает с экрана на экран, нарушается моторная память и растёт когнитивная нагрузка.

**Слова автора:**

> Notice how the CTAs moved from the middle of the screen to the bottom and then other screens are in different places. Try to always keep the CTA in the same place.

**Для Напарника:** В Фокусе и онбординге главный CTA в одной зоне у большого пальца (нижняя треть), на одинаковой высоте на всех шагах.


---

## 6. Скриншоты в магазине обещают одно, а внутри хаос: несогласованный UI
`доверие · онбординг · дизайн-система · лендинг` · [09:02](https://youtu.be/hgpk0ejGs-E?t=542)

**Мысль:** Скриншоты магазина красивы, но приложение внутри выглядит как 25 разных приложений; резкая смена стиля путает и рвёт доверие.

**Слова автора:**

> Okay, to be honest, this might be one of the most confused states I've been while recording one of these videos. And again, the UI looks completely different now. Okay. Guys, if I had known that the app was going to turn out like this, I would have not recorded it. But it's a good example of how App Store screenshots can trick you into downloading an app and then there being something completely different there. So, do not sleep on your screenshots.

**Для Напарника:** Единый визуальный язык /, /app, /app/session, /app/world через общий AppBackdrop; лендинг не должен обещать то, чего нет внутри.


---

## 7. Лавина всплывающих подсказок: «просто дай мне увидеть приложение»
`онбординг · внимание · СДВГ · доступность` · [10:06](https://youtu.be/hgpk0ejGs-E?t=606)

**Мысль:** Много подсказок, всплывающих отовсюду, перегружают и вызывают желание уйти. Прогрессивное раскрытие без объяснения зачем — тоже шум.

**Слова автора:**

> And I'm actually going to stop. Like, I've been shown so many pop-ups. I just want to be on the home screen and it's just stuff appearing everywhere. It's just from here, from there. Like, what is happening? Just let me see the app for myself.

**Для Напарника:** Никаких туров и всплывашек в Напарнике (и никаких toast): одна тёплая реплика за визит, остальное человек открывает сам.


---

## 8. Пульсирует, но не нажимается: ложный сигнал аффорданса
`анимация · иерархия · доверие · крафт` · [11:02](https://youtu.be/hgpk0ejGs-E?t=662)

**Мысль:** Анимация подсказывает «нажми», а ничего не происходит — это ломает доверие к интерфейсу.

**Слова автора:**

> If I tap that, nothing happens. So, this looks like the most tappable thing ever and it's pulsing, but it's not tappable.

**Для Напарника:** Подтверждает диегетичность из CLAUDE.md: пульсировать/двигаться должно только то, что реально интерактивно или реально живёт в сцене. Проверить, что декоративные движения не выглядят кнопками.


---

## 9. Не толкать пользователя к новому, пока он просто наслаждается приложением
`внимание · онбординг · удержание · тёмные-паттерны` · [11:55](https://youtu.be/hgpk0ejGs-E?t=715)

**Мысль:** Постоянные анимации, апселлы и подсказки в момент, когда человек просто пользуется продуктом, раздражают и мешают.

**Слова автора:**

> They keep showing me animations. They're just showing me things. Now they're upselling me on the widget, like I'm just trying to enjoy the app. Stop pushing your users to see things when you're just trying to enjoy the app.

**Для Напарника:** В Доме и Фокусе никаких апселлов и новых предложений во время сессии; награды и предложения только в моменты после завершения, один вопрос за визит.
