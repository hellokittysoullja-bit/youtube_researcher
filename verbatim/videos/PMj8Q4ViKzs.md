# What are loops in game design? - Loops - Game Design Theory

**Канал:** Game Design with Michael · 9 мин · субтитры: en (ручные) · https://youtu.be/PMj8Q4ViKzs

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Сессия может длиться секунды: цикл сведён до базовой механики
`игровой-дизайн · удержание · время` · [00:54](https://youtu.be/PMj8Q4ViKzs?t=54)

**Мысль:** В строительных играх сессия: открыть, собрать ресурсы, закрыть. Цикл «собрать, выбрать, поставить в очередь, уйти и вернуться по готовности».

**Слова автора:**

> Base building is an interesting genre as a play session may involve opening the game collecting resources and then immediately closing the game, with such a session lasting as short as a few seconds. That is because base building games along with many mobile titles have distilled the game design concept of loops down to being the base mechanic of the game. Collect resources, look at what to build next, queue it to build, leave and come back when the building has completed.

**Для Напарника:** Допустить микросессии в Напарнике (открыл, увидел рост острова, ушёл) как полноценную ценность.


---

## 2. Цикл Дэна Кука: ментальная модель, действие, правила, обратная связь
`игровой-дизайн · исследования · процесс` · [01:30](https://youtu.be/PMj8Q4ViKzs?t=90)

**Мысль:** Мозг использует ментальную модель, чтобы выбрать действие, система применяет правила и возвращает обратную связь, которую игрок встраивает в модель.

**Слова автора:**

> Loops are a concept that can be found in the interaction design and learning fields. When the brain is interacting with something there is a process that it goes through in order to adapt to its surroundings. There are several different versions of this loop so we will be using the one proposed by Daniel Cooke of Spry Fox. The process looks like this. We start at the top where we have a store of information the brain already has. This is called the mental model. At the start of the game this is likely going to be pretty empty, although it may have common things like genre constants to draw upon. An example of a genre constant might be most first-person shooters have very similar controls. The brain uses this information to devise an action that may have an effect on the current situation and then it acts. The action in the case of a game is received by the system and run through the rules. This is the part where the game takes the action the player has taken and reacts to it with an output. This output is then fed back to the player as a response to what has happened after their action, also known as feedback. The player then receives this information, interprets it by referencing it with their current understanding and tries to fit the new feedback into their mental model. The process then repeats.

**Для Напарника:** Моделировать каждое взаимодействие Напарника как такой цикл и проверять, что игрок получает понятный отклик на своё действие.


---

## 3. Циклы бывают разного размера: быстрые и медленные
`игровой-дизайн · внимание` · [05:09](https://youtu.be/PMj8Q4ViKzs?t=309)

**Мысль:** Игры состоят из быстрых частых и медленных редких циклов; быстрый: «могу ли я нажать кнопку», медленнее: освоение комбинации.

**Слова автора:**

> Right, so even though that section of play was only something like 20 seconds it can be seen how the player will go through this loop of coming up with an idea, acting on it, waiting for the game to process that action and give them feedback and then applying this new information to their mental model. That was also a good example to show how loops come in different sizes. Games are made up of all sized loops. Again using terminology from Daniel cook games can have fast frequent loops, all the way out to slow infrequent loops. So a fast look might be can I press the button? Yes. I can cool add that I can stand on buttons to my mental model. A slightly slower loop is that if I mix dash with running at the right time, I can make it through the door.

**Для Напарника:** Разделить циклы Напарника по длине: тап и отклик (секунды), сессия (минуты), рост острова (дни).


---

## 4. Линия восприятия: без обратной связи цикл ломается
`игровой-дизайн · анимация · доступность` · [06:42](https://youtu.be/PMj8Q4ViKzs?t=402)

**Мысль:** Игрок видит только то, что над линией восприятия. В Hidden Folks игроки не знали, что объекты сдвигаются, и разработчик добавил покачивание объекта, замыкающее цикл.

**Слова автора:**

> As a last little piece of the model I'm going to add this line. This is what I'm going to call the perception line. Everything above the perception line is available information to the player, everything below the perception line is hidden. So from the player's perspective they don't understand what the system is doing, they just take actions and are waiting for feedback to see if their actions did anything. So if something isn't working in your game you can break the mechanic down into its loot components. Does the loop look like this? If you miss the feedback step the game might be processing the players actions but the player doesn't know whether the game is doing anything or not. Hidden folks is a game that works similar to Where's Wally books. In a GDC talk, the developer of hidden folks spoke about players not realizing you could slide things out of the way to find characters. This is because there wasn't any feedback for the user to interpret. The solution the developer implemented to fix this was if a player tapped on an object that could slide but then didn't slide it, the object would wiggle. This wiggle completes the loop by providing feedback for an action which allows the player to adjust their mental model.

**Для Напарника:** Любое нажатие в Напарнике должно давать видимый отклик (покачивание, изменение), иначе человек не понимает, сработало ли действие.


---

## 5. Ведение за руку не строит ментальную модель
`онбординг · игровой-дизайн · исследования` · [08:28](https://youtu.be/PMj8Q4ViKzs?t=508)

**Мысль:** В FFXV: A New Empire игрок получил подсказки следовать за рукой и повторять «квест, улучшение», но не понял, как системы связаны; ментальная модель не сформировалась.

**Слова автора:**

> Another way to use loops is to assess whether your feedback is being interpreted into the mental model of the player correctly. This is some footage from Final Fantasy XV:A New Empire, the mobile game. It at first looks very similar to Clash of Clans. The way I ended up playing this game was that instead of the feedback telling me this building does this, information which I should add to my mental model to make informed decisions in the future. I found myself just following the hand around for half an hour without being taught very much about the game and how the system's interconnect. Once the game stopped hand-holding me my mental model didn't say this is what I should do next because it will help my empire, it was press quest. Upgrade building, repeat. At one point I trained a soldier from the training grounds. By the end I still had no idea what the purpose of that action was. My interpretation of the feedback didn't translate into helpful information in my mental model.

**Для Напарника:** Онбординг Напарника должен объяснять, зачем действие и что оно даёт острову, а не просто вести за руку.
