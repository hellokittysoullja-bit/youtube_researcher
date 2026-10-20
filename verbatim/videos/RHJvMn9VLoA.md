# 7 mental models for designing AI products

**Канал:** Dive Club 🤿 · 13 мин · субтитры: en (авто YouTube) · https://youtu.be/RHJvMn9VLoA

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. ИИ-продукт это поле без карты: давать ровно столько путеводных нитей
`ИИ · чат · онбординг` · [01:43](https://youtu.be/RHJvMn9VLoA?t=103)

**Мысль:** Классический софт как метро с известными остановками, ИИ даёт бесконечные степени свободы, и это пугает; нужны подсказки, шаблоны, тропинки и мягкие барьеры, не сводящие всё к монорельсу.

**Слова автора:**

> Most existing software is something like being on a train or a Subway right there's a series of stops you can Define the journey ahead of time you could map the entire space you could say it's the New York City metro right it's like there are only 47 stops in this system I know how you get to each one right I think the current Paradigm is more like being dropped in the middle of a field with no map or Trails you can do anything just the number of degrees of freedom you have is almost literally infinite and that it's language based this is like both the astonishing power and opportunity of L it's also like pretty intimidating I think the challenge of a design team working in this space is to provide just enough wayfinding and Pathways that people feel comfortable but to not lock them into like a monor rail system and so there's existing patterns that work here you know suggestions templates you can give them guidance light guidance heavy guidance cow paths that maybe like guide them gently big roads with barriers where you're like you seem pretty stuck here we're going to like funnel you down this path so at least you get somewhere and then for the people who feel really comfortable there's always walking through the field in a direction that no one has asked you to go down.

**Для Напарника:** Чат Напарника: быстрые чипы-подсказки и мягкая очередь шагов для застрявших, но с возможностью написать что угодно (один вопрос за визит, CLAUDE.md §4).


---

## 2. В ИИ-продуктах дизайнер описывает намерение, а не макеты всех случаев
`ИИ · процесс` · [04:40](https://youtu.be/RHJvMn9VLoA?t=280)

**Мысль:** Нельзя нарисовать каждый исход; результат отображается в лучшей форме (график вместо текста), а дизайнер и инженеры собирают его в диалоге.

**Слова автора:**

> Designing products with infinite degrees of freedom kind of changes the way that software teams operate and also how we even think about design deliverables because we can't design every single outcome in figma it's literally impossible just take perplexity for example here's their head of design Henry giving us a little inside look no matter what the user wants to see we should represent that information in its most perfect form let's say I want to a stock price of Nvidia I could show you that in markdown with just text right I could bold the latest stock price and I could do a bullet list of the history but it would be a lot better if I showed you a graph that you could then interact with right that's like a much better representation of that information designers are thinking about this experience but they're not communicating it with mockups they're communicating it with guidance it becomes much more of a collaborative end to-end product crafting process rather than like design handoff to engineering because you cannot design all the cases just explain what the user is going to get and what the vision for the product experience is and then you and the engineers you build it together in a very collaborative conversational process.

**Для Напарника:** Для реплик напарника описывать желаемый опыт и тон в промптах, а не писать жёсткие шаблоны на каждый случай.


---

## 3. Промпт-дизайн как проектирование кухни для шефа-модели
`ИИ · процесс` · [06:20](https://youtu.be/RHJvMn9VLoA?t=380)

**Мысль:** Дизайнер расставляет в «кухне» нужные инструменты и информацию; итерации идут от того, что модели чего-то не хватило, как при анализе отвала в онбординге.

**Слова автора:**

> The term prompt engineering gets thrown around a lot I kind of think prompt design is more of an interesting term like I'm designing this kitchen and the model is the chef and I have to put the right things in the kitchen in the right place so that the model can make whatever the customer orders cuz we don't know what they're going to order and that's where a lot of the trial and error of like oh crap somebody came in and ordered this thing and we didn't have like a lemon peeler and so I need to like add a Lim and this a very abstract example A lot of times the iteration was just like the where s off the rails and being like Oh we need to like add this kind of tool or like oh we should add you know this pre-processing step in the pipeline so that we have this piece of information here that if we need it we have it's experienc design no different than thinking through why did this person fall off this onboarding flow.

**Для Напарника:** В /api/companion и /api/breakdown давать модели нужный контекст (час суток, очередь шагов, имя) и итерировать по реальным сбоям.


---

## 4. ИИ как новый материал: понимать его только игрой и поломкой
`ИИ · процесс · вкус` · [08:34](https://youtu.be/RHJvMn9VLoA?t=514)

**Мысль:** Как с деревом: пробуешь гнуть, греть паром и находишь границы; лучшие дизайнеры сохраняют игривость и экспериментируют до границ.

**Слова автора:**

> Almost like playing with the AI a bit which reminds me of another metaphor that Jason Yuen the co-founder of dot shared with me to understand the new material you have to play with it you have to take it out of the Play-Doh box and go like this you can't like draw a little picture and show your like Engineers like hey can you make the Play-Doh do that and they're like no but the Playdoh can do this The Playdoh can stretch have you considered that you know it's like you just have to play with it I think the best designers maintain a sense of play playfulness they like to play George kinberg hit on this idea too really stressing the importance of viewing AI as a new material that we get to design with I kind of look at it as this like alien space metal that has like crash landed on the planet and like it's a new material it's like a new thing that as designers we get to work with and the only way you really understand a material super well is by just experimenting with it and like trying stuff and just like continuing to like push the envelope of like what can this thing do you know like imagine if you had the first time you saw wood you're like what do I do with wood you know you would start trying things and you'd be like oh if I bend it this way it breaks but if I like heat it up with steam and bend it around this other thing I can make these like really cool curved edges you just have to go deep on these matal and just try a lot of stuff to see where they break and to see where they don't break.


---

## 5. Семистраничный промпт, 100 итераций ради простого чипа
`ИИ · микрокопирайтинг · процесс · крафт` · [10:11](https://youtu.be/RHJvMn9VLoA?t=611)

**Мысль:** Простая UI-фича с подсказками следующих шагов оказалась результатом сотен итераций промпта; промптинг теперь часть дизайна.

**Слова автора:**

> I have a fun story there so we were working on a feature that basically does this right like it looks at a chat it says here are three next steps we think you might want to do the designer working on it s in she brought it to crit she shows it's kind of like the UI the rectangles are like pretty straightforward it's little suggestion chips that appear underneath the chat she showed some examples you're like yeah that's pretty good like that makes sense those are good next steps we should think about you know when and how to roll this out and the crit was sort of tailing off just because it was good like there wasn't a lot to say and then someone was like can you show us the prompt that you used to ask this other instance of Claude to make the right suggestions and she brings up this seven page prompt with like all of these instructions and examples and little tweaks and like the art of prompting is like this Dark Art and she had just she had iterated I think she said like 75 or 100 there's like hundreds of iterations trying different combination of prompts looking at it seeing if it made sense all to get this thing that was just elegant and simple for a user and so this was another sort of like big Awakening moment for me switching into the AI world is prompting is part of the design process and designers need to know how to do it.

**Для Напарника:** Промпты Напарника (тёплый тон без стыда) заслуживают такой же итеративной доводки на реальных примерах, как и визуал.
