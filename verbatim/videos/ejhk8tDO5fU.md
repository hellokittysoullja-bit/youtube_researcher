# Design Systems at Scale // Episode 6: Maintaining and Evolving Your Design System

**Канал:** Dan Mall · 15 мин · субтитры: en (авто YouTube) · https://youtu.be/ejhk8tDO5fU

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Принципы нужны для выбора между двумя разумными путями
`процесс · дизайн-система · вкус` · [00:59](https://youtu.be/ejhk8tDO5fU?t=59)

**Мысль:** Принцип вроде «чисто и просто» бесполезен: никто не хочет грязно. Хороший принцип помогает на развилке, где разумный человек может пойти в обе стороны.

**Слова автора:**

> The importance of design principles is to actually help people make a decision when there are two viable paths so design principle like clean and simple is probably not going to be very useful because no one wants messy and complicated as their as their byword instead we want to sort of have some principles that help to make decisions when you're at a fork in the road where a reasonable person could go in one direction or another so design principles become these things that are rallying cries in a sense or reminders of what is in our path and help us to make decisions when there are competing directions that we might go in.

**Для Напарника:** CLAUDE.md уже так работает (тёплый тон, диегетичность, медленность): формулировать принципы как правила выбора, а не лозунги.


---

## 2. У бота есть личность: зафиксируй тон, фразы подтверждений, точку зрения
`тексты · маскот · чат · ИИ` · [13:20](https://youtu.be/ejhk8tDO5fU?t=800)

**Мысль:** Для голосового или чат-интерфейса записывают личность: типовые фразы для подтверждений, тон (яркая личность или нейтральный помощник). У компании должна быть позиция.

**Слова автора:**

> So for a speech interface you may have a bot or an interface that has a certain personality and that's something that should be recorded with common phrases for example for how you do confirmations and different language around that you could even have sort of some things like alexa has which are called speech-icons but a bing believe it or not alexa knows how to say and so you can sort of build in these sort of flourishes as a set of as a libraries in the same way that we have icons that we have in a system you can have things like speech icons as a collection all this is to say that for every different channel that you use there are likely to be guidelines and conventions that you want your designers and developers to use and as much as possible get that as close to the code so here is actually the code snippet that you use for that speech icon in your speech interface for example a design system consists of more than just a ui kit and a pattern library and a code library it's also all of the different ways that you communicate and interact with customers so it can include things like a writing style guide or voice and tone if you think about voice and tone that's also especially important as we have this emerging future of speech assistants and bots what is the tone of your bot how does it talk should it have a big personality or should it be sort of a neutral assistant all these things are things that as an industry we're starting to figure out but your company needs a point of view and the design system should have that point of view too.

**Для Напарника:** Голос кота в Напарнике (api/companion, api/session-voice): вести словарь типовых реплик подтверждений и ошибок в характере, без toast.
