# The Best AI Coding Tools for Designers

**Канал:** Dive Club 🤿 · 19 мин · субтитры: en (авто YouTube) · https://youtu.be/J08endIde9E

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Квадранты инструментов: размер задачи против того, что уже есть в проде
`процесс · ИИ` · [00:10](https://youtu.be/J08endIde9E?t=10)

**Мысль:** Автор выбирает инструмент по двум осям: размер работы и доля уже существующего материала; для неоформленных идей холст и текст лучше кода.

**Слова автора:**

> A mental model that I find very useful. So I'm going to share it with you today. These are the quadrants that exist inside of my brain. And the x-axis is the size of whatever I'm working on. Is it a quick P3 bug fix or are we going 0ero to one on some really big meaty ambiguous idea? And the yaxis is how much of the material that I'm going to work with already exists in production. Is this feature work that is starting from a blank slate or you know maybe we're just iterating on something that is already shipped. There's a lot of hype right now on Twitter about how the canvas is dead and everything has to exist in code. And honestly, I think it's kind of ridiculous. And yeah, not to overuse the double diamond metaphor, but I think there is merit to thinking of our work that way because a lot of times it's very unshaped. We have no idea what problem we're even solving or what way to approach it. And if that's the case, man, I love making a mess on a canvas. And I actually use a lot of writing. Like this is often what the initial stages of my design looks like. And you can see how ridiculous this is, right? Like I'm just not ready to start playing in code. I just want to get the general shape of an idea.


---

## 2. Ловушка: пересобирать прод внутри прототипного инструмента
`процесс · дизайн-система · ИИ` · [05:12](https://youtu.be/J08endIde9E?t=312)

**Мысль:** Дни, потраченные на доводку пикселей и интеракций вне дизайн-системы и без связи с продакшн-кодом, оказались пустой тратой; прототип должен быть маленьким и сфокусированным.

**Слова автора:**

> You're creating incredibly small focused prototypes. And the trap that you fall into is trying to rebuild production inside of an AI prototyping tool that doesn't sit on top of your production codebase. And I've totally been guilty of this. 6 months ago, I was spending days prototyping fully functional components inside of Lovable like this one. And they turned out kind of great actually. Like I was really happy with how this worked. There's no way that I have been able to do something like this inside of Figma because there's a bunch of different animations and anytime you're working inside of a textbased environment, like you kind of got to get into production code. So, all of this made a lot of sense to me, but I'm also self-aware enough to admit that I spent way too long sweating the details on all of these pixels and interactions and doing it in a way that wasn't built on top of my design system at all.

**Для Напарника:** Экспериментальные анимации острова и кота делать сразу в кодовой базе Next.js на токенах проекта, а не в отдельных прототипах.


---

## 3. Параллельные агенты спасают состояние потока
`внимание · процесс` · [07:13](https://youtu.be/J08endIde9E?t=433)

**Мысль:** Ожидание ответа каждые две минуты ломает поток; несколько изолированных рабочих пространств убирают стоп-старт.

**Слова автора:**

> And I freaking hate having to wait for Claude to reply every 2 minutes. So, the tool that has pretty much consumed the majority of my AI coding as of late is Conductor. It's an easy way to run multiple clawed codes in parallel, and each one is their own isolated workspace. So, I can work on multiple features at once, which kind of solves that flow state problem where I'm stopping and starting every single 2 minutes. Obviously, this is great for speed, but what I love again is that it helps me stay in a flow state because I don't have all of these little stop, start, stop, start where I'm waiting for Claude to process my request.

**Для Напарника:** Параллель с Фокусом: любые паузы ожидания (загрузка реплики напарника, дробление задачи) разрушают состояние потока, поэтому их нужно скрывать или сокращать.


---

## 4. Планирование с ИИ-CTO: фазы, параллельные ветки, оценка отчётов
`процесс · ИИ` · [16:21](https://youtu.be/J08endIde9E?t=981)

**Мысль:** Сначала долгий диалог, где ИИ задаёт вопросы и фиксирует контекст; затем план по фазам с учётом параллельной работы и цикл отчёт-оценка-следующий промпт.

**Слова автора:**

> CTO and help me create some of these initial project docs. The most important one is this development plan here. And I specifically asked Claude to break it up into phases and to think strategically about which work can happen in parallel so that I can use separate conductor work trees as well as separate conductor agents within an individual PR as effectively as possible. So you can see like this is phase one, the core data layer. And what I'm doing is I'm creating a new chat for each one of these phases. And then I actually have Claude write the prompts for conductor for me. So if I scroll all the way up here, these are separate conductor workree chats and then it's simultaneously writing the prompt for each one of them. I literally don't even read these. I kid you not. I just grab them and paste it into Conductor because I've already done all of the work up front in the planning phase. What I then do is tell Conductor that it has to report back to the CTO. And I take that report, I paste it back into Claude, and I ask it to evaluate the output, make sure everything looks good, and then it will create the prompt for the next step.
