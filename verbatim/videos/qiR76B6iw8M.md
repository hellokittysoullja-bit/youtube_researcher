# Designing for AI: From Features to Systems. Rethinking UX in the Age of Agents

**Канал:** Belfast Design · 19 мин · субтитры: en (авто YouTube) · https://youtu.be/qiR76B6iw8M

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Решение хорошо ровно настолько, насколько точна проблема
`процесс · исследования · вкус` · [02:02](https://youtu.be/qiR76B6iw8M?t=122)

**Мысль:** Мы одержимы решениями и мало думаем о корневой причине; решение — всего лишь идея, чтобы узнать больше о проблеме.

**Слова автора:**

> Because when I hear people talk about UX design, they'll often describe things like would be cool if we had a feature that and then they go on and describe a solution. And a solution is only as good as the accuracy and the specificity, can't really say that, of the problem that it's solving. And we tend to only think about solutions. in fact, I would say we obsess over solutions. Everybody thinks that their idea is the best idea and no one's ever thought of that before. and we spend considerably less time thinking about the root cause of any problem. And solutions are good if they're treated as just ideas to learn more about the problem. And a solution can be very dangerous if it just if people just go with it and don't, you know, think of what the potential impact is of that thing.

**Для Напарника:** Перед новой механикой Напарника формулировать проблему человека с СДВГ, а не «добавим фичу».


---

## 2. Промпт: описывай проблему, желаемый результат и измерение, а не решение
`ИИ · процесс` · [04:34](https://youtu.be/qiR76B6iw8M?t=274)

**Мысль:** GenAI работает лучше с контекстом; вместо готовых решений ему стоит дать проблему и критерии успеха.

**Слова автора:**

> And basically you've described absolutely no context to something that is a genai tool. And genai works best when you give it context. so this will not provide a good solution. what will provide a better solution is if you describe the problem, the ideal outcomes and how to measure it. and try to avoid giving genai tools solutions because they are better at coming up with it.

**Для Напарника:** Промпты api/breakdown и api/companion строить из контекста человека (время суток, состояние, желаемый результат), а не жёстких инструкций.


---

## 3. Зачем, когда, где, кто — контекст, без которого ИИ даёт «ровно что просили»
`ИИ · исследования · процесс` · [07:15](https://youtu.be/qiR76B6iw8M?t=435)

**Мысль:** Мы привыкли описывать как и что, но не зачем, когда, где и кто. Полный контекст — путь к полезному результату.

**Слова автора:**

> Features and this is a big trap. because people tend to not move beyond thinking of things as features. and that's because we're addicted to explaining the how and the what. And not really the why, the when, the where, or the who. and by the way, the why is the problem. The when is how frequently that thing happens. So does it happen every day? Does it happen in the morning? Does it happen at night? does it happen only monthly? Whatever it is, where is obvious could mean many things not it could be physically where or it could be virtually in what environment and who is obviously the different the user. and all of this is context. So if you can describe that when you're using genai that is that is how you'll get the best outcome. and AI is more efficient with coming up with the how and the what when with the caveat being that when you provide it with the full context. and the thing is as designers we've spent most of our time providing ourselves with context. So this should be a skill that should naturally come to designers better than engineers or other groups that haven't had to consider the context as much as designers have and UX researchers as well. so when you describe the how and the what and not the why, when, where, or who, AI will give you exactly what you asked for, which isn't always what you wanted.

**Для Напарника:** Передавать в API время суток, длительность, прошлые сессии и имя, чтобы реплики кота были к месту.


---

## 4. Восемь видов трения при проектировании ИИ: намерение, прозрачность, контроль, контекст, доверие, когнитивное, этическое, ответственность
`ИИ · доверие · этика` · [13:10](https://youtu.be/qiR76B6iw8M?t=790)

**Мысль:** Человеку непонятно, что просить, что агент делает, как остановить, почему показано это, можно ли верить, и откуда он знает мои данные.

**Слова автора:**

> So the next level is behavior and this is understanding how humans even saying humans is weird but anyway humans think decide and behave under friction which sound a little bit like obvious in UX but given that there's now all these new AI conventions we have to consider these things a wee bit differently there is intent friction so what did I even what do I even ask for how do I interact with this thing if it's agentic and then transparency friction which is particularly important in a gentic AI when like what did I just do if something's going off and doing something how do I even know what it's all what are all the tasks it's doing in the background control friction can I stop or correct it context why is it showing me this and then trust friction should I believe what it's showing me and cognitive this doesn't behave like tools I know and this is also going to be harder because you've got different models and different models act in different ways. So, not everything is going to act the same way that Chat GBT does. and you've got different like types of models that are good for specific things. I don't know if anyone here's used Nano Banana yet, but it's pretty fun. for images. and then ethical friction. So, why does why does it know that information? You know, people sometimes are a bit horrified whenever it can tell you. I think I asked Chad, what does it know about me? and it gave me my full address and I was like how do you know that? and I was like you put it in like 3 months ago and I was like okay. they asked me do you want me to forget about this and I was like yeah forget but forget. so yeah role of friction then who is responsible now? So again with a gentic AI when it when it evolves further you know at what point do we say that you know we as humans aren't responsible for what that thing just did. so these are kind of eight sort of different frictions that we have to be aware of when we're designing for AI.

**Для Напарника:** Чек-лист для реплик кота: объяснять, почему предлагает шаг, давать «отмена/другое», прозрачно говорить, что помнит и как это забыть.
