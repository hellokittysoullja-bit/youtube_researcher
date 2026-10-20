# Designing Voice user interfaces to boost customer experiences | Founder Fridays - June 2022

**Канал:** Google for Developers · 10 мин · субтитры: en (авто YouTube) · https://youtu.be/PT3lFf_wi7U

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Пауза и недосказанность несут смысл, а машина видит только слова
`чат · ИИ · внимание` · [02:33](https://youtu.be/PT3lFf_wi7U?t=153)

**Мысль:** Живой диалог держится на взгляде, паузе, интонации; у компьютера есть только текст. Поэтому в чате неоднозначность и молчание нужно проектировать явно.

**Слова автора:**

> So there's really a lot going on here even though it's a very simple transaction there's eye gaze there's body language there's pausing there's intonation all these things we use when we communicate and we do it every day without even thinking about it but a computer finds this very difficult the computer just has the words so you have to cram a lot of information into kind of a small signal so imagine that you said to me do you want coffee and I said coffee will keep me awake do I want coffee or not well it depends right if you ask me in the morning and I have a big day ahead of me it's probably a yes coffee will I really want some coffee to keep me awake but if it's late I'm about to go to bed probably means no now this is another thing this kind of ambiguity and language that humans do every day without even really thinking about it but it's very hard for computers what if I said to you can I get a ride tomorrow morning and a very small amount of time passed without you speaking let's say almost a second well even though you haven't said anything you've already told me something important which is you probably can't or won't be able to give me a ride so even though it's your turn to talk I'll probably jump in and say oh you're probably too busy how about Friday here's an example where important information is being communicated just in silence.

**Для Напарника:** В чате напарника не требовать развёрнутого ответа: давать короткие варианты-чипы и считать молчание нормой (без «ты не ответил»).


---

## 2. Проектируй чат по реальным разговорам, а не по воображаемым
`чат · исследования · процесс` · [04:36](https://youtu.be/PT3lFf_wi7U?t=276)

**Мысль:** Люди из колл-центра и живых диалогов знают, о чём клиенты спрашивают и как формулируют. Это источник реальных реплик вместо придуманных.

**Слова автора:**

> First off lean on real world conversations what do I mean by that if your business has a call center with human agents or agents who do online chat talk to them they are a wealth of information they're the ones who are actually interacting with your customers they know what kind of things they want to talk about and they know how they ask for them now if you don't have that think about where in the world those real life conversations are happening that are related to what you're trying to do for example if you're making an app that books restaurant reservations talk to the people at restaurants who answer the phone or maybe you have a health care app talk to the nurses the doctors the people who would be having those conversations with people.

**Для Напарника:** Реплики напарника писать от реальных фраз людей с СДВГ (из отзывов, интервью), а не от «правильных» формулировок.


---

## 3. Направленные вопросы вместо «чем помочь?», старт с малого, запасной выход
`чат · ИИ · доверие · этика` · [05:33](https://youtu.be/PT3lFf_wi7U?t=333)

**Мысль:** Открытый вопрос не говорит, что бот умеет; FAQ придуманы под ответы, а не под реальные вопросы; начинать нужно с одной рутинной задачи; при фрустрации человеку нужен выход к живому.

**Слова автора:**

> In the beginning especially steer clear of open-ended questions in high-stakes situations so an example of an open-ended question is how can I help you that seems like a really standard thing for a chatbot to ask right but it usually can have users run into a lot of trouble because it doesn't really tell them anything about what your chatbot can do so they don't know what they can say or what they can't say so it's better to have directed questions that are a little more specific in those situations and high-stakes situations I mean things like highly emotional things like if you have a very unhappy Customer because their product arrived broken or if you have a health care situation where you have to deliver upsetting Health news don't Outsource those to a bot that's where your humans really need to be available sometimes I'll see companies say oh the first thing we'll do is voiceify our FAQ it seems pretty straightforward it's already in a question and answer set up but FAQs are often artificially constructed you have information you want to communicate to customers and so you come up with a question to match the answer which as it turns out is often not the way that people will actually ask for that information so you might have a beautiful q a experience but nobody asks the questions that you think they were going to start small don't think you need to you know create all of your content all of your functionality via this chatbot or voice experience right from the start pick something small manageable maybe routine like an intake form or information that people often ask about like the return policy start there get it right and then expand let your customers have an escape hatch if they are frustrated in their chat experience let them go to a human and if you don't have a human what else do you have do you have a support email address otherwise because there are going to be times when your chat bot can't help them and you don't want to leave them frustrated.

**Для Напарника:** Первая реплика напарника на Доме — конкретный выбор из 2–3 шагов, а не «как дела?». При сбое AI — тёплая запасная кнопка (вручную) вместо тупика.


---

## 4. Sample dialogues: прочитай диалог вслух с партнёром
`процесс · чат · тексты` · [08:05](https://youtu.be/PT3lFf_wi7U?t=485)

**Мысль:** Дешёвые черновые диалоги, прочитанные вслух, вскрывают массу проблем ещё до кода.

**Слова автора:**

> Do a lot of prototyping early and often you don't have to get fancy those things I did at the beginning with the tuna salad conversations those are called sample dialogues and that's how we begin any design experience we just start writing those and read them out loud hopefully you have a partner you can read with and it won't just be like I did reading to myself but you'd be amazed at how many problems you can find just by doing these simple sample dialogue readings and they're low-cost low Fidelity and you can work out a lot of things early.

**Для Напарника:** Любую новую цепочку реплик напарника сначала прогонять как сценарий вслух, проверяя тон и длину.


---

## 5. Проектируй под то, как люди говорят на самом деле
`исследования · чат · процесс` · [09:10](https://youtu.be/PT3lFf_wi7U?t=550)

**Мысль:** Пользователи говорят неожиданно; принять это и итерировать — путь к успешному диалогу.

**Слова автора:**

> If you only remember one thing from this whole talk this is the slide design for how people actually talk not how you want them to talk and what I mean by that is you may create what you think is a beautiful design and you put it out in the world and then you watch people interact with it and then you just start cringing because they're saying all these things that you're like but they shouldn't say that I never expected that but that's how it is people talk in a lot of different ways they're going to say things you don't expect and that's okay and if you can accept that and understand that you're going to iterate on your design and make it better then you're on your way to making really successful conversational experiences.

**Для Напарника:** Логировать (локально/с согласия) нераспознанные ответы в чек-инах и дописывать ветки реплик напарника.
