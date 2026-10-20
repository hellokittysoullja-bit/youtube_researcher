# Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing - Bala Ramdoss, Amazon Lens

**Канал:** AI Engineer · 14 мин · субтитры: en (авто YouTube) · https://youtu.be/maTp79FD9gI

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Ответ модели не равен интерфейсу: бронь за пару тапов вместо абзаца
`ИИ · чат · иерархия` · [00:01](https://youtu.be/maTp79FD9gI?t=1)

**Мысль:** Тот же ответ модели, показанный как дата, время и пара тапов, доводит до действия; текстовый ответ оставляет работу человеку.

**Слова автора:**

> I asked my AI assistant to help me reserve a table at a popular restaurant. Here's what it gave me. Now, it's not wrong. The phone number is there. The hours are right. It even knows the walk-in oyster bar at the front. The model did the real work, but look at the outcome. I have to do my research and work towards actually booking the table. Like, we've been here for a while. Now, imagine if you were to build something like this for your customers. What would you want it to do? Same answer, rendered like this instead. A date, a time, a couple of taps, and then you're done. The agentic product you're building already has all the tools to support your customer's needs. The only thing that you need to focus on is the layer between the model and something that a human can interact with.

**Для Напарника:** Ответы AI-дробления (api/breakdown) показывать карточками шагов с кнопкой «Начать», а не простынёй текста.


---

## 2. Модель выбирает из фиксированного меню компонентов и не изобретает новые
`ИИ · дизайн-система · процесс` · [07:31](https://youtu.be/maTp79FD9gI?t=451)

**Мысль:** Контракт задаёт блоки (текст и UI) и правила раскладки; модель только выбирает намерение из небольшого каталога — безопасно и предсказуемо.

**Слова автора:**

> This is usually the hard part of building the system. This is the model facing half of the contract. And you don't want the model to send back text. Like, you want it to stream blocks of UI components. a conversation block for what it says in text and a UI block for what it wants the client to render. The contract even encodes layout rules. In this example, one to three flights a swipable carousel. Four or more, a vertical list. The model picks the intent. And notice what the model never does. It never invents a component. It chooses from a fixed menu that you provide to it. Obviously, it won't be in the millions. It would be a handful.

**Для Напарника:** api/companion и api/breakdown возвращать типизированный JSON (реплика, шаги, тип карточки), а клиент рендерит родными компонентами Напарника.


---

## 3. Гонись за временем до первого фрагмента, а не за общей задержкой
`ИИ · анимация · метрики` · [09:11](https://youtu.be/maTp79FD9gI?t=551)

**Мысль:** Скелет, затем частичное наполнение, затем итог: ожидание 3–4 секунд переносимо. Метрика — когда пользователь увидел первое полезное; обычный спиннер для AI не годится.

**Слова автора:**

> Streaming helps here by not making the client wait for the whole response. It renders things in chunks at a time. Take a look at the illustrative example when you have to surface information one chunk at a time. First, you show a skeleton, then partially fill it, then complete it. It may take 3 to 4 seconds to get there, but the wait is bearable. That kind of changes what you measure for an app. Like you stop chasing the total latency, which we have done for over a decade. You start chasing time to first chunk. You know, the first useful thing that your user sees. For this reason, the traditional loading spinner won't work for AI features. Sometimes, you have to get creative and design your feature around it.

**Для Напарника:** Реплики напарника стримить и показывать сразу первый кусок; пока ждём AI-дробление, давать коту «задумчивое» выражение, а не спиннер.


---

## 4. Дай занять руки на время ожидания и показывай, что делает агент
`ИИ · доверие · внимание` · [10:19](https://youtu.be/maTp79FD9gI?t=619)

**Мысль:** Если рендер долгий, вовлекай пользователя; показывай, что агент делает — тогда 10 секунд ожидания терпимы и растёт доверие к результату. Мысль «думаю…» применять умеренно.

**Слова автора:**

> And when you know it's going to take time to render something, keep the user engaged. The Lens live allows the user to focus different things, tap on an object that they're interested in while they wait for the results. if you don't have the full screen in your control, you can show the thinking CX. But please use it sparingly. The overall AI users have moved out of the forgiving phase, and now they expect to know what is happening. Now that you have a way to stream back different states, you know how to show what your agent is doing. here's an example I copied from Gemini. When it starts to work on a task, it gives a glimpse into what the agent is doing. Even though it takes 10 seconds, I'm okay if I know what's happening and be able to trust the agent's final output.

**Для Напарника:** При дроблении задачи кот в характере сообщает, что делает («выделяю первый шаг»), без технических статусов и без toast.
