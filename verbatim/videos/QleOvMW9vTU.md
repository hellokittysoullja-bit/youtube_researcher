# WWDC26: Create UI prototypes using agents in Xcode | Apple

**Канал:** Apple Developer · 18 мин · субтитры: en (ручные) · https://youtu.be/QleOvMW9vTU

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Размытый промпт даёт произвольный макет; задавай признаки, настроение и просись у агента несколько вариантов
`процесс · ИИ · крафт` · [03:04](https://youtu.be/QleOvMW9vTU?t=184)

**Мысль:** Расплывчатый запрос закрепляет случайную навигацию и угаданные функции, а потом изменения превращаются в раздутый интерфейс. Нужны конкретные функции, стилистические подсказки и множество вариантов на раннем этапе.

**Слова автора:**

> If you're like me, you just want to get started. With agents right in Xcode, you might be tempted to ask, "create a UI for managing a book club that meets regularly." This could generate an interesting result and quickly but the prompt is vague and it brings a few problems. The agent generated an arbitrary layout. While it might still work, it's one of many ways of organizing an app like this. And it also took a guess at the app features because it wasn't clearly defined in the prompt. Suppose we aren't interested in polling or a photo gallery, making it easy to get stuck or anchored on a flawed starting point. For example, we're now stuck with this arbitrary navigation element that might have made more sense with a different feature set. By the time we've gotten the interface to display the features we do want, it could present feature creep, looking clunky and inelegant. To avoid this, your prompts need to be much more specific. Take some time to think through the features and high-level points you want the app to have from the get-go. When it comes to your app and what problems you want it to solve, you likely have a better idea where to start than the agent does. Give stylistic cues. If you have an intuition about the mood or feeling you want your app to evoke, express those in the prompt. For example, for a book club, do you want to capture the warm atmosphere of a coffee shop and its color palette? Or do you want to highlight the feeling of paper and beautiful typography? Lastly, and most importantly, ask for multiple options. Early on is your best opportunity to evaluate and explore multiple and divergent directions.

**Для Напарника:** При работе ИИ-агентов над Напарником: давать явные функции и настроение (тёплый, прощающий) и просить 3-5 именованных вариантов для сравнения.


---

## 2. Наполнять прототип реалистичным контентом и краевыми случаями, а не заглушками
`процесс · ИИ · исследования` · [07:37](https://youtu.be/QleOvMW9vTU?t=457)

**Мысль:** Агент играет роль живого пользователя: правдоподобный контент, неограниченно растущие элементы, длинный ввод и пустые состояния. Данные лежат отдельным файлом, чтобы легко менять.

**Слова автора:**

> Early on in the development of your app, it's a great idea to let different people try it and give you feedback to guide your process of refinement. For some kinds of apps and interfaces though you still might be a ways off from having it in a state where people can try it with their own content. Fortunately, the agent can help play the role of somebody using your app so you can get an impression of what your app feels like when it's lived in Combined with images that you can bring in, an agent can get you from this kind of blank template, only loosely filled with content, to something rich, lived in, and closer to real use. Here are some prompting tips when working through how to make your app feel lived in. First, and this is a recurring theme, ask for not just one preview, but many previews. Second, stop and think through edge cases yourself. For example, in my app, how does the detail area look if no meeting has been scheduled yet? Try to be specific about what parts of the interface state should be iterated, minimizing the risk that the agent overlooks something. Make sure that there's enough context that the sample content is plausible for your app's audience. In this case, that means I need to make sure that the sample app content, such as the discussions, center around books. Pay attention to interface elements that can grow unbounded: the number of members in the club, the length of the message conversations, the number of previous books, and so on... It might also include things like long input. Is it appropriate for the text to truncate? Or to take multiple lines? If applicable, ask the coding agent to make sure that the example content it is authoring is reusable and readable in its own file so that you can go in and make changes if you need to.

**Для Напарника:** Совпадает с уроком проекта о реалистичных данных: тестировать остров на 9 ориентирах, а не на одном; хранить сид-данные отдельным файлом.


---

## 3. Находки на реальном контенте: пустые состояния, обрезка длинного текста, сокращение списка
`процесс · крафт · исследования` · [09:54](https://youtu.be/QleOvMW9vTU?t=594)

**Мысль:** На реальных данных вылезают отсутствующие пустые состояния, перекрытие обложки длинным текстом и слишком длинный лидерборд; решение: всегда показывать собственную позицию и раскрывать полный список.

**Слова автора:**

> Each variation gets its own tab, so I can quickly switch between them. In this example, I notice I don't have any real blank slate UI, no way of specifying a new book or even to manage my account. I address that by adding account management and call-to-action controls. In this variation, I noticed that really long next meeting descriptions might overrun the book cover. I address that by allowing truncation. In fact, I realize the title of the book is redundant with its cover, so I simplify it. Here I notice that the leaderboard, when there are too many participants, gets way too long, and it takes a long time to scroll to see the discussion. Instead, I can simply ensure that somebody can always see what their relative rank is, and with an expand control, see the full list.

**Для Напарника:** Дом и Мир: проверять пустые состояния (нет плана на сегодня) и длинные списки шагов; показывать только текущий шаг с раскрытием остальных.


---

## 4. Панель настройки анимации: разбить на фазы и дать общий словарь
`анимация · процесс · крафт` · [13:27](https://youtu.be/QleOvMW9vTU?t=807)

**Мысль:** Вместо правки констант в коде делают отдельную панель параметров; анимацию разбивают на фазы, это даёт общий словарь людям и агенту и позволяет настраивать каждую фазу изолированно.

**Слова автора:**

> This can work really well, but sometimes the constants I'm interested in live in different parts of the code, and the context switching can feel clunky. You might find it easier to create a custom UI whose job it is to help you tune those specific parameters that are relevant to your interface. Here's a simple interface to demonstrate this principle. Here I'm just tossing an interface element at a goal to understand the different spring properties at play for this kind of interaction. A menu button brings up a tuning panel that allows me to try different parameters. Here, Xcode can help you immensely. Instead of building the UI directly, enlist the agent to build a UI to display tunable parameters. When you ask the agent in Xcode for help with building a tuning panel for your UI, here are some best practices. Be as detailed as possible about what you want to iterate on. Are you exploring different animation styles or the specifics of spring curves? Does your animation feature multiple elements or does it feature a transition in which elements enter and leave your view hierarchy? To keep your tuning panel easy to understand, ask for the animation to be broken into phases. This also gives you and the agent a shared vocabulary about the specific parts of the animation.

**Для Напарника:** Для RevealIsland и островной анимации роста: описать фазы (проклюнулся, вырос, осел) и вынести тайминги в отладочную панель.


---

## 5. Сократить цикл обратной связи: делать панель настройки при выборе между параметрами
`процесс · анимация · крафт` · [17:09](https://youtu.be/QleOvMW9vTU?t=1029)

**Мысль:** Когда нужно выбирать между конфигурациями вида или параметрами анимации, панель настройки сокращает цикл и быстрее приводит к ощущению оптимума.

**Слова автора:**

> Let's look at it again. This is one of the most powerful flows in prototyping with coding agents in Xcode. Anytime you're trying to manage multiple configurations of a view or deciding between different animation or interaction parameters, make a tuning panel, shorten the feedback loop, and get to what feels optimal for your app.

**Для Напарника:** Инструмент разработки: тюнинг-панель для пружин и задержек пик-момента сессии.
