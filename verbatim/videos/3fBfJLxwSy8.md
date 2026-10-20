# The Laws of UX for the AI Era – 19 Psychological Design Principles

**Канал:** Tech Forensics · 7 мин · субтитры: en (авто YouTube) · https://youtu.be/3fBfJLxwSy8

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Ожидание ответа ИИ съедает доверие за секунды
`время · доверие · ИИ` · [00:00](https://youtu.be/3fBfJLxwSy8?t=0)

**Мысль:** Пока крутится спиннер, мозг уже решает, что инструмент медленный, и точность итогового ответа не исправит первое впечатление.

**Слова автора:**

> Nothing happens on screen. The cursor blinks. You type the prompt 11 seconds ago. You're still waiting. Somewhere behind that spinner, a model is thinking, and you are just sitting there, hands off the keyboard, trust draining out of you 1 second at a time. You tell yourself it's fine. It's not fine. Your brain already decided this tool is slow, and no amount of accuracy in the final answer is going to undo that first impression.

**Для Напарника:** Реплика напарника (/api/companion, /api/breakdown) должна начинаться сразу: присутствие кота или тёплая промежуточная фраза вместо пустого ожидания.


---

## 2. Порог Доэрти 400 мс: отклик как продолжение мысли
`время · юзабилити · ИИ` · [01:28](https://youtu.be/3fBfJLxwSy8?t=88)

**Мысль:** Ответ быстрее 400 мс (против прежних 2000 мс) заставляет ощущать инструмент как расширение своего мышления; медленный воспринимается как недостойный доверия, даже если работает верно.

**Слова автора:**

> One number to sit with before we go further, 400 milliseconds. That's the exact threshold researchers set in 1982 for how fast a computer needs to respond before a human stops feeling in control of it. Most agentic coding tools blow past that number by a factor of 10 or more every single time you hit enter. Let's slow down and actually look at this. That 400 millisecond number comes from Walter Doherty and Arvin Kyra, published in an IBM Systems Journal paper. The previous industry standard for acceptable response time was 2,000 milliseconds. Doherty's research showed that once you cross under 400 milliseconds, something changes in how a person relates to the tool. It stops feeling like a program you're operating and starts feeling like an extension of your own thinking. Cross that threshold and productivity spikes. Miss it consistently and users describe the tool as sluggish, even when it's technically working correctly. Apply that to your daily coding agent. If it takes 8 seconds to return a suggestion, you're not in flow. You're in a waiting room and your brain treats every visit to that waiting room as evidence the tool can't be trusted.

**Для Напарника:** Отклик интерфейса меньше 400 мс; для долгих ИИ-запросов давать быстрый промежуточный сигнал.


---

## 3. Выбери умолчание и убери меню
`юзабилити · дефолты` · [03:08](https://youtu.be/3fBfJLxwSy8?t=188)

**Мысль:** Инструменты с одним умолчанием и спрятанным меню работают с законом Хика, а те, что показывают все варианты каждый раз, против него.

**Слова автора:**

> Then there's Hick's law from a 1952 study by William Hick and Ray Hyman. The more choices you present, the longer it takes someone to decide. Open any modern AI coding tool's model picker. 10 options. Fast model, smart model, reasoning model, cheap model, preview model. Every one of those choices adds real decision time before you've written a single line of code. The tools that let you pick a default and disappear the menu are working with the law. The ones that surface every option every time are working against it and they don't even know it.

**Для Напарника:** Не выводить все длительности и режимы сразу: умолчание 25 минут и раскрываемый выбор.


---

## 4. Чётко маркируй незавершённое, чтобы не терять место
`СДВГ · внимание · удержание` · [05:08](https://youtu.be/3fBfJLxwSy8?t=308)

**Мысль:** Незаконченные многошаговые задачи запоминаются лучше, и их явная пометка помогает ориентироваться в длинной сессии.

**Слова автора:**

> And the Zeigarnik effect, from Bluma Zeigarnik's research in the 1920s, found that people remember unfinished tasks far better than completed ones. Any agent that fails to clearly mark an incomplete multi-step task is throwing away a psychological hook that could keep you oriented across a long session.

**Для Напарника:** Показывать на экране Фокус, какой шаг из очереди текущий и что осталось, без давления.
