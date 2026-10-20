# How Claude Code’s lead designer builds with AI

**Канал:** Dive Club 🤿 · 12 мин · субтитры: en (авто YouTube) · https://youtu.be/hKeDfupbA4U

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Скилл-прототип: N вариантов, пусть ИИ выберет и обоснует
`процесс · ИИ · крафт` · [02:59](https://youtu.be/hKeDfupbA4U?t=179)

**Мысль:** Дизайнер Claude Code делает скилл, который генерирует пять вариантов фичи в HTML, сам выбирает лучший и объясняет почему, а результат приходит как PR со скриншотом или записью.

**Слова автора:**

> That's it. No design specs, no just like I want to add autocomplete, I want to see what it looks like. A few things I'm going to call out here that I think are important when you're prompting. The first is I built myself a slash prototype skill. I asked Claude to build this, you could build it in like 2 seconds. All it does is get Claude to generate n number of options, default to five, of a different implementation of a feature, generate an HTML file, preview it, and then iterate on it a few times and I can enter that n and I can enter what the feature is going to be. I did not write this. No one ever writes their skills by hand anymore. If anyone tells you they do, they're lying. Everyone just prompts them. and then a few things I will add in here is I always ask Claude to pick an option for me first. I think it's actually fun to see what Claude comes up with. So, historically, I used to be like, oh, like prototype and then I'll choose. Now I'm like, oh, prototype and then you should choose what you're going to do and then tell me why. And then I say another one is like feel free to research online. Now, if I were doing this in my production code base, I'd say like please look at Slack, Google Docs, any discussions, and like BigQuery, like look at all these sources and figure out which is the best one. But given that this is an open-source repo, online research is fine. And then, you know, implement the best option, verify, get the styles to match. really important one, put up a PR with a screenshot. Claude is actually really good at this, and I actually don't review the outputs anymore of Claude in the transcript. I'm typically reviewing a PR that Claude put up that has a recording of the feature that implemented.

**Для Напарника:** Для разработки Напарника: просить ИИ выдавать несколько вариантов экрана или микрокопирайта и выбирать с обоснованием, но финальное решение за владельцем продукта.


---

## 2. ИИ пока плох в дизайне: человек остаётся в цикле ремесла
`процесс · ИИ · вкус` · [05:44](https://youtu.be/hKeDfupbA4U?t=344)

**Мысль:** Автор считает, что LLM ещё не умеют проектировать хорошо, поэтому решение о том, что попадает в продукт, должен принимать человек.

**Слова автора:**

> So, the first is that Claude, tragically, and most LLMs are not good at design yet. So, what this means is that you should still very much be in the loop for the craft and the decision-making. It doesn't mean this is going to be holding true forever, but a lot of my workflows revolve around the idea that I still need to be the one making a decision about what actually goes into the product.

**Для Напарника:** Правило работы над Напарником: ИИ предлагает, но визуальные и тональные решения проверяются на реальном рендере (см. методологию в CLAUDE.md §6).


---

## 3. Если все могут выпускать, не всё должно выпускаться
`процесс · крафт` · [06:47](https://youtu.be/hKeDfupbA4U?t=407)

**Мысль:** Когда доступ к коду открыт всем, нужны системы масштабирования качества; автор отправляет сотни мелких полировочных правок и сводит их в один PR.

**Слова автора:**

> And then the third one, which I don't think is controversial for this room, but has definitely been one that has been an uphill battle a lot of places, is just because everyone can ship doesn't mean not everything should ship. And that's a pretty important distinction that we need to start making as we're adding more features and as everyone has the ability to access code and like push to production, we need better systems that scale. And so, some ways that we're fighting this internally today is I actually use Claude in the web. Does everyone have this internally at their teams or companies? you might have it with your own internal infrastructure, but I have like Claude in the cloud or Claude in the web is a service that we offer and I use it as a way to send like hundreds of tiny little polish fixes all the time that I find in the app. They're not worth spinning up a new session for, they're not worth dedicated time. I just have all of these going and I would say, sometimes I get complaints from the engineers that there's too many of them. So, every now and then I'll ask Claude to squash them all into one PR for me. And sometimes they just got auto approved because they're tiny CSS changes and no one really needs to review them. So, I would say like this is a really great way to maintain crafting quality in your products and it's something that you can do on the side as Claude is working.

**Для Напарника:** Копить мелкие правки полировки и сдавать одним PR, а не дробить на множество; соответствует практике ветки и squash-merge проекта.


---

## 4. Автоматизация на несколько шагов вперёд, даже если пока сыро
`процесс · ИИ` · [10:01](https://youtu.be/hKeDfupbA4U?t=601)

**Мысль:** Рутина проверяет, участвовал ли дизайнер в фронтенд-изменениях, и готовит адверсариальный дизайн-PR; автор отключил рассылки, потому что модель плоха в дизайне, но держит процесс готовым к следующей модели.

**Слова автора:**

> I have a Claude code routine, which is a scheduled task if you use Claude code work. And what this does is it scrapes all of our repositories for any front-end changes that anyone has implemented. It will check if a designer was involved in it by going through Slack, Google Meet transcripts, like Google Docs, like any kind of data that it has access to. If a designer was not involved in it, it will flag that it shipped without a designer or not. >> >> If it shipped without a designer, it will come up with an adversarial or it'll review the design and then it will typically come up with an adversarial design in a PR already drafted, DM it to the engineer who shipped that feature, and then ask them to work with the designer on that feature. I tested this a few times and I had to turn off the DMing cuz Claude was actually really bad at design, unfortunately. And I We did have to like it's And like that goes back to my first one, like Claude is not good at design yet, but I think this is the level of automation that you have to be thinking, like not just the first step, but like the next step, the next step, the next step after that. Like you want to be pushing it so far that it's like building the actual end product.
