# Conversation Design Tips & Voice UX Design Conventions

**Канал:** Chatbots Life · 11 мин · субтитры: en (авто YouTube) · https://youtu.be/YjQutdrPXWU

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Смолтолк как мост от лёгкого к глубокому, обратно к главному
`чат · маскот · онбординг` · [00:11](https://youtu.be/YjQutdrPXWU?t=11)

**Мысль:** Как и у людей, разговор идёт от поверхностного к глубокому; бот должен поддержать «привет/помощь/меню» и мягко вернуть в основную пользу.

**Слова автора:**

> A lot of bots don't have any small talk in them and they even fail at you know things like high or help or menu so make sure that your bot could definitely handle these basic you know these very basic requests from your users so it should at the very minimum be able to have some sort of small conversation and then be able to help your users or have a way of guiding them through small talk and small talk is very important because what the way small talk works in conversational design and in bots is almost the same way it works with real people and real conversations and that is that people will talk about you know they'll have small talk and then that small talk will give us something to that we have in common or something that we could latch on to and then we'll you know we'll go down that path and have a deeper conversation so you go typically you know like a pool you go from shallow to deep and so your bot needs to be able to do the same thing it needs to be able to have some small talk and then the small talk could act as a guide to get the people or your user right back into the main things and the main ways your bot could help them.

**Для Напарника:** Напарник отвечает на «привет» и пустые реплики тёплой мелочью, затем мягко предлагает один следующий шаг (Фокус).


---

## 2. Сбои бота — данные о желаниях людей; у каждого шага свой запасной ответ
`чат · ИИ · доверие · стыд` · [02:44](https://youtu.be/YjQutdrPXWU?t=164)

**Мысль:** Непонятый запрос показывает, чего хотят люди. Универсальный «я не понял, вот меню» подрывает доверие и откатывает к началу; нужен fallback внутри контекста (как «нет овсяного молока» на слоте молока).

**Слова автора:**

> And that is failure okay bots kind of like two people that don't know each other very well they have a high failure in terms of conversing while in the first go around and overall that's not a bad thing it's actually a really good thing because with your bots failing that means that users are telling you about what they want but your bot wasn't able to handle that but you have this all this information about what users want and you can take that information and you could use it to make your bot better and to give people what they want you might discover things because of those interactions that you would have never been able to discover with the static app or website for example if let's say you're 1 800 flowers and you're talking to your customers your bots conversing and let's say the customers are always asking about a certain type of flour you never carry well now you know that they want this flower right before you had no idea that they wanted this flower you there was no possible way for you to know just by then visiting your website or ordering flowers or through you know any mobile app or something like that but now since they're telling your bot your bot knows all this data's in there that they want xyz flower the other thing is you can think of failure in different ways so one way of failing is that the bot just outright doesn't understand something right and if it doesn't understand something as a designer you can create a safety net and we call that a fallback so a bot doesn't understand something it would say something like oh i'm sorry i don't understand that but i could help you with a option a b c or d i can help you with your order i can help you with customer service i can help you with sales you know whatever those options are this would be kind of like a universal failure mechanism no matter where they are and about or what the floor context is this can kind of act as a safety net the problem with this sort of wide safety net is that it's not very it's not very effective and it doesn't and it diminishes trust it's kind of like if you and i are having a conversation and i was helping you do something like i was taking your order and then let's say you're at my coffee shop i'm taking your order and then i ask you what type of milk you want and you tell me that you want oat milk and i don't have oat milk and no and i never thought that i would ever need oat milk and my brain freezes up and we have to start the transaction all over again right so we what we don't want is to have a situation where users requests for something that the bot doesn't have or can't provide or your business doesn't offer and then for the person to have to restart the whole process or be taken back to some sort of root main menu where they have to like okay where do i go from here i have to restart the entire process and all of us have had this experience especially with like calling a 1-800 number where you're on hold and then you're put back to the root menu and then you just have to wait for longer it's a very frustrating process so the solution for that is dedicated fallbacks so each of your each of your contextual flows needs to have its own dedicated fallback so if someone if you're already further down you've already 90 ordered your coffee now you're asking for oat milk the bhakti oh i'm sorry i don't know what that is or i can't help you with that did you want some other type of milk because it's on that milk slot it's asking for milk and now it just knows that it doesn't have the answer to that specific thing.

**Для Напарника:** В чек-ине и дроблении при непонятном ответе кот переспрашивает именно этот слот («не знаю такого — выберем из этих?»), не сбрасывая человека на главный экран.


---

## 3. Люди скользят глазами: короткие предложения и визуальные слова
`тексты · микрокопирайтинг · СДВГ · внимание` · [08:06](https://youtu.be/YjQutdrPXWU?t=486)

**Мысль:** Тексты бота почти не читают, их просматривают и отвлекаются; короткие предложения и конкретные визуальные слова (стена, а не «личность») снимают когнитивную нагрузку.

**Слова автора:**

> Remember to be really simple like believe it or not most people are not going to read those texts that your bot sends them what they're going to do is they're going to skim them they're just going to look at it and just get distracted and do something else so you want to make sure that the words and the sentences are small you want to have short sentences in like four letter words and then the other thing is that you want those words to be really visual so if you think about the way trump talks he talks in this way it's like a fourth grade level of difficulty so there is no cognitive load on the on the user it's really easy and you look at you know what he tweets for example or what about texts it you it should be almost impossible for the person not to read it you know like and then you want to use words like wall instead of words like personality because a word like wall is very visual it's four letters it's like you see the word wall written and here we'll do it right here and it's almost impossible for you not to read it like you recognize it right away you know it's like seeing a tree you know where's personality it you know you can't even like describe or draw personality very quickly it takes you a little bit more to like think about what the context and what the meaning of the sentence is.

**Для Напарника:** Реплики напарника: 1–2 коротких предложения, конкретные образы (костёр, остров, шаг) вместо абстракций.


---

## 4. Говори о выгоде выгоды и учитывай эмоцию человека
`тексты · мотивация · чат` · [09:36](https://youtu.be/YjQutdrPXWU?t=576)

**Мысль:** Плащ покупают ради сухости; каждое взаимодействие вызывает мысль и чувство, и эмпатия к ним позволяет предсказать следующий шаг.

**Слова автора:**

> Your bot should focus not on features but on the benefit of the benefit right like the example with the raincoat is an example of the person trying to find out what the weather is that's the benefit of the benefit of that in the context of that question and if they decide to buy a raincoat they're buying it not because they want to own a raincoat but because it's raining outside and it's and they're not gonna get wet so it's gonna keep them dry right so that you know that's why like you know people in alaska aren't buying bikinis right you need it's it's you need to focus on the benefit of the benefit when it comes to your to your bot and then last but not least is you have to consider the emotion of your user so every interaction that a person has with your bot is going to do some sort of thoughts and feelings within that person so as you're designing your bot you need to have empathy and put yourself in that user shoes and see what those thoughts corresponding thoughts and feelings you're going to be like and when you do that then you can better predict what they're most likely to say or do next.

**Для Напарника:** Предлагая сессию, говорить не «запусти таймер», а о выгоде («пять минут рядом — и сдвинется»); тон подбирать под эмоцию чек-ина.
