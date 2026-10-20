# Master the 3 Types of CRAZY Mobile UI Swipe Interactions

**Канал:** Kole Jain · 5 мин · субтитры: en (авто YouTube) · https://youtu.be/14h1VnkQvIc

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Почти никогда не линейный easing: кривая задаёт тон
`анимация · крафт · вкус` · [00:33](https://youtu.be/14h1VnkQvIc?t=33)

**Мысль:** В жизни вещи ускоряются и замедляются; кривая с упругостью делает жест живым и передаёт тон: чёткий, игривый или медленный и плавный.

**Слова автора:**

> Opening up the easing curve to give it some more bounce makes this feel much more natural, allowing the cards to carry more momentum. Easing and bounce are remarkably important to make lifelike interactions. Almost never do you want a linear ease. Things in real life speed up and slow down. And by playing with that curve, we transform animations. It also helps provide tone like snappy and performant, fun and springy, or slow and smooth.

**Для Напарника:** Подбор easing для острова и Фокуса под тёплый, медленный тон; линейное только для индикаторов времени.


---

## 2. Переход продолжает жест: контент следует направлению свайпа
`анимация · мобильный · крафт` · [03:19](https://youtu.be/14h1VnkQvIc?t=199)

**Мысль:** Фон и новый контент выезжают по направлению свайпа; изображение, увеличиваясь, становится героем нового экрана, создавая непрерывность.

**Слова автора:**

> Make the motion feel natural by following the direction of the swipe with a background and new content sliding up and in. This is a principle that we'll see in action in the next example, too. This is a simple onboarding flow, but instead of just a button to slide us over, we have a button that is clickable or swipeable. And by making the motion follow the direction of the swipe and then wrap around into the next slide, we make it super fluid. It might make more sense how this works if I zoom out and show you everything. We start with a circle that expands very large and move the content out. Then we swap the circles out and shrink that one back down and move the new content in. It's actually a pretty simple effect when you see it like this. Now, those are all well and good, but they're fairly complex, but even something similar like this is just so much better than sliding a new page in. This swipe creates continuity because we have this image actually zooming in to become the new hero image.

**Для Напарника:** Переходы между Домом, Фокусом и Миром: общий AppBackdrop уже даёт непрерывность; добавить сдвиг контента по направлению таб-перехода.


---

## 3. Слайдер подтверждения для необратимых действий
`мобильный · доверие · микрокопирайтинг` · [05:07](https://youtu.be/14h1VnkQvIc?t=307)

**Мысль:** Нажать кнопку случайно проще, чем провести слайдер через весь экран; для действий с высокой ценой ошибки жест надёжнее.

**Слова автора:**

> Another relatively common use of swipe gestures in real applications are confirmations. The email sender resend uses it to confirm sending an email since it's just much easier to accidentally click a button than it is to slide a slider all the way across the page. These are great for high impact or irreversible actions such as purchasing crypto in this example.

**Для Напарника:** Для редких необратимых действий (сброс острова) использовать «проведи, чтобы подтвердить»; на обычных шагах не применять, чтобы не добавлять трение.
