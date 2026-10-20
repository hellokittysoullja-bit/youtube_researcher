# Tokyo iOS 2024 - Crafting Delight - My process of creating delightful interactions in iOS

**Канал:** Tim Oliver · 13 мин · субтитры: en (авто YouTube) · https://youtu.be/eKl1JDfMsg4

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Кастомный переход прячет загрузку и даёт ориентацию
`анимация · крафт · запуск-задачи` · [03:03](https://youtu.be/eKl1JDfMsg4?t=183)

**Мысль:** Анимация открытия связывает прошлый экран с текущим (wayfinding) и маскирует фоновую работу, так что пользователь думает, что всё мгновенно.

**Слова автора:**

> Lot of extra work and the answer is why bother? Which is a legitimate question especially when you're on tight deadlines and there's a lot of good reasons. One of them in this case is like wavefinding. connecting the previous screen to the to the current screen with a very obvious transition and when you exit out you also see where you went. You've got very good trans like very good context about what just happened in the app. Another one is this actually lets you hide some background details. Like instead of showing a loading spinner because opening a comic book takes a lot of effort, right? You got to open the zip file which is you know decode the zip file and then actually access the data inside it. Work out which does the page need to get extract that and then once you've extracted it convert it from a JPEG to raw pixel data. There's a non-trivial amount of effort that goes into taking a zip file and having it a presentable comic book. And so the idea is by playing this animation I can do all this stuff in the background and play a canned animation and the user thinks it was instantaneous whereas it's actually a loading screen.

**Для Напарника:** Анимация перехода в Фокус (starting→running) может скрывать подготовку и одновременно служить ритуалом начала; не растягивать её сверх нескольких секунд.


---

## 2. Craft: мелкие устранённые шероховатости превращают рабочее приложение в приятное
`крафт · вкус · анимация · хаптика` · [03:58](https://youtu.be/eKl1JDfMsg4?t=238)

**Мысль:** Прерываемые анимации, плавный скролл, хаптика и визуальный отклик на тап по отдельности незаметны, но в сумме дают ощущение «не знаю почему, но приятно».

**Слова автора:**

> Now this is called craft. And the idea of craft is it's basically trying to go through your app and finding everything that feels a bit jank and stuff that could be a little bit better for the user. This is like things like UX enhancements or performance enhancements. things like creating contextual animations, things like making sure scrolling is really smooth and locked at like 60 or 120. Making sure that when you tap buttons, you get like haptic feedback or visual feedback. Things like if you've got animations like in that case, you could tap the edge of the screen and an animation would play. Making sure that you can continue tapping that and it will keep going. Like sometimes the screen will be disabled while an animation is playing and users will feel that. So things like interruptible animations. But the idea is basically if you do all this kind of things, you go through and you like find these UX inconsistencies and go through, you can take a functional app and turn that into a delightful app. It's the kind of thing where users will be like, I don't know why, but this app feels really nice. Like these are all tiny little issues on their own that add up to a good app experience.

**Для Напарника:** Чек-лист полировки Дома и Фокуса: прерываемые анимации (не блокировать экран во время анимации), отклик на каждый тап, стабильный fps на слабых телефонах.


---

## 3. Прототипируй: вынеси идею из головы в руки как можно быстрее
`процесс · крафт` · [05:58](https://youtu.be/eKl1JDfMsg4?t=358)

**Мысль:** Как приложение ощущается, понятно только когда держишь его в руках; даже слайды Keynote или рисунок на бумаге быстрее проверяют идею, чем код вслепую.

**Слова автора:**

> Called prototyping. Fake it till you make it. And the idea that Apple promotes this concept a lot where it's like you don't know how an app will feel until you actually hold it in your hands and play with it. So you can try and imagine it as best as you can, but it really helps to have it in your hands and play with it. So do whatever you can to get what's in your head into the real world as quickly as possible so you can play with it and see if it actually works. that could be like make the app in Keynote or just do what like you know or just write on draw it on a piece of paper. just try and get it out of your head and on into reality and then see if it actually works in reality like you were picturing it in your head. So the CDR is like get as go as quickly as you can to kind try and create the thing you're picturing to see if it's actually feasible.

**Для Напарника:** Перед сложной анимацией (рост ориентира, финальная хореография) собрать грубый прототип и посмотреть на реальном телефоне, как рекомендует §6 CLAUDE.md.


---

## 4. Затемнение и блик добавляют глубину простому переходу
`анимация · крафт · вкус` · [09:09](https://youtu.be/eKl1JDfMsg4?t=549)

**Мысль:** Переход выглядел «мутным» без разделения слоёв; добавили затемняющий слой и градиентный блик, имитирующий свет, и получили 3D-ощущение.

**Слова автора:**

> Because there's no separation between the front and the back. And like normally when a book starts to close, you'd imagine there's like some light involved. The background would get a bit dark as like shadows start to happen and stuff. So, what we can do is we can add a black dimming view that fades in as the book closes and we get a bit more 3D depth now as it kind of closes.

**Для Напарника:** В RevealIsland и появлении ориентиров на гряде добавлять мягкое затенение и свет слоёв вместо плоского масштабирования, не выходя за коридор светлоты фона (§3).


---

## 5. Полируй то, что пользователь видит десятки раз за сессию
`крафт · метрики · вкус` · [11:38](https://youtu.be/eKl1JDfMsg4?t=698)

**Мысль:** Анимацию, которую человек увидит множество раз за каждый заход, стоит оттачивать; в настройках это не имеет смысла.

**Слова автора:**

> Amount of effort for ostensibly it's a very simple thing but when you're working on an app where the concept is reading in comic books. This is sort of interaction users will see maybe dozens of times every session. So, it's the kind of thing that if you spend a bit of time here polishing the core part of the app as opposed to, you know, this would make no sense if you did it in the settings screen and things like that. The idea is this is where you can add to the experience of the app.

**Для Напарника:** Приоритет полировки: старт сессии, финал и чат на Доме, а не редкие экраны вроде формы имени.
