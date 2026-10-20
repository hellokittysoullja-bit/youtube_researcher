# WWDC23: Design and build apps for watchOS 10 | Apple

**Канал:** Apple Developer · 19 мин · субтитры: en (ручные) · https://youtu.be/BPJZ6A_brSw

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. «Момент часов»: сузь опыт до того, что важно в эту секунду
`внимание · мобильный · крафт · СДВГ` · [01:17](https://youtu.be/BPJZ6A_brSw?t=77)

**Мысль:** Дизайнер Apple советует спросить: что самое релевантное, если у человека есть всего десять секунд внимания. Опыт сужается до одного момента.

**Слова автора:**

> The first thing you’ll want to think about when designing for Apple Watch is “What is the most relevant information or experience my app can offer to people in the moment?” Let’s look at the Weather app as an example. Because Apple Watch is a timekeeping device best suited for quick and focused interactions, the first thing you’ll see when opening the app is your local weather for today. With a simple rotation of the digital crown, you’ll get local weather for the rest of the day, and then for the rest of the week. And if I’m looking for the weather in New York, for example, my list of cities is just a single tap away from any of these detail views. Weather achieves what I like to think of as an “Apple Watch Moment.” When you’re designing your app, try to narrow the focus of the experience to just what’s relevant at the time the wearer raises their wrist. Watch experiences should be highly specialized for brief interactions. If you had ten seconds of someone’s attention, which information would you surface?

**Для Напарника:** Дом и Фокус: на входе показывать одну самую релевантную вещь (следующий шаг или таймер), а не меню из десятка опций.


---

## 2. Короткие взаимодействия: данные сначала, остальное — анимацией
`внимание · иерархия · мобильный` · [02:54](https://youtu.be/BPJZ6A_brSw?t=174)

**Мысль:** Когда внимания мало, нужно быть лаконичным: простые экраны, одна фокусная вьюха вместо широкого опыта.

**Слова автора:**

> Brief interactions are one of the things that I love about designing for Apple Watch. When you only get a few seconds of people's attention, you need to be concise, like how News focuses the experience on just today's headlines. And Heart Rate displays finite data first, so it can devote most of the view to a full screen animation. And Activity simplifies a broad experience into single focused views. So when designing your app, keep it brief and keep it focused.

**Для Напарника:** Экран Фокус: крупно одна цифра таймера и кот, без вторичных панелей.


---

## 3. Сразу в деталь по намерению пользователя, без заголовка
`онбординг · активация · иерархия` · [06:18](https://youtu.be/BPJZ6A_brSw?t=378)

**Мысль:** Приложение открывается сразу на нужном экране, выбранном по месту, давности, частоте; экран настолько очевиден, что заголовок не нужен.

**Слова автора:**

> Navigation Split View is a perfect option if you have a source list, like a list of cities in Weather or a list of stocks and detailed views of the items in that source list. Land people directly in the detail view when they launch your app. Use location, recency, frequency, or some other indication of user intent to inform which detail to surface first. Strive to make your detail view so unmistakable at a glance that it doesn’t need a title.

**Для Напарника:** Дом: открываться на продолжении (незавершённый шаг из очереди) вместо общего списка; применимо к saveStepQueue.


---

## 4. Цвет всего экрана как состояние: идёт отсчёт — тёмный, готово — яркий
`цвет · время · анимация` · [15:41](https://youtu.be/BPJZ6A_brSw?t=941)

**Мысль:** Полноэкранный цвет сообщает тон и смену состояния без текста: в таймере чёрный фон на отсчёте и яркий оранжевый по завершении.

**Слова автора:**

> Another great use of full screen color is to set tone, like this calming blue background in Sleep. You can use color to convey information at a glance, like in World Clock where we use solar gradients to show the time of day. You can also use full screen color to convey a state change. In Timers, the background is black when the timer is counting down, and then, bright orange declares that my egg timer is done.

**Для Напарника:** Фокус: смена оттенка фона при done вместо уведомления, но в коридоре светлоты 0.152–0.172 (только оттенок/насыщенность).
