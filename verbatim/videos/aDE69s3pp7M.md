# Core Game Loops

**Канал:** Timothy Cain · 13 мин · субтитры: en (авто YouTube) · https://youtu.be/aDE69s3pp7M

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Core loop: самые частые повторяющиеся действия большинства
`игровой-дизайн · процесс` · [01:17](https://youtu.be/aDE69s3pp7M?t=77)

**Мысль:** Core loop — набор действий, которым большинство игроков занимается большую часть времени.

**Слова автора:**

> The core game Loop is the set of actions in a game that most players will spend most of their time doing you can think of it as what are the most frequent and repeated actions that players take in your game.

**Для Напарника:** Чётко определить core loop Напарника (выбрать шаг, запустить Фокус, получить отклик) и вкладывать главное внимание в него.


---

## 2. Как определить core loop: час игры, демо, стример
`игровой-дизайн · исследования · процесс` · [05:24](https://youtu.be/aDE69s3pp7M?t=324)

**Мысль:** Достаточно часа игры или просмотра стримера, чтобы увидеть, что человек делает чаще всего; у игр без чёткого core loop человек не понимает, что происходит. Демо и vertical slice должны показывать core loop, а не просто красивую картинку.

**Слова автора:**

> Don't have to play an entire game from start to finish to know what its core game Loop is you usually you can pick up a game play it for an hour and you can probably pretty accurately Define its core game Loop if it's a good game and this is what why some games fail I think is because they don't have a well defined core game Loop and you can play for an hour and you're like I still don't know what's going on alternatively you could just play a demo the whole point of a demo is to express the core game Loop by the way if you're if you're making a vertical slice you should also be thinking core game Loop because that's what you're trying to express not just here's a visual example of the game but I've got enough of the core game Loop in there that you understand what the game's going to be like when you play it's not enough vertical slices you just it's not enough for them just to be pretty they have to instantiate the core game Loop a lot of times I've noticed that if you just watch a streamer play the game that's enough for you to figure out the core game Loop they just watch them for an hour and you see what they're doing over and over and over again are they jumping are they sneaking around are they hacking terminals what seems to be the thing that they do the most that's the core game Loop.

**Для Напарника:** Проверка Напарника: за час наблюдения за новым пользователем должно быть очевидно, что он делает чаще всего, и это должно быть приятно.


---

## 3. Core loop и дизайн-столпы — разные вещи
`процесс · игровой-дизайн · крафт` · [06:38](https://youtu.be/aDE69s3pp7M?t=398)

**Мысль:** Столпы объясняют, как каждая фича служит замыслу; core loop — те из фич, которые игроки используют чаще всего. Core loop должен касаться всех столпов, остальные фичи могут их не затрагивать.

**Слова автора:**

> Let me make a big distinguish here between core game loops and design pillars I have a whole video on design pillars and I'll link it below they are not the same thing the design pillars are there to explain how every feature that you've selected to be in the game serves those pillars but a core game Loop is you saying okay of all those features that we've put in the game that serve the design pillars these are the ones I expect most of the players to experience most of the time and there's difference there because you may have things that you put in like let's say you put in reactivity that's something I love putting in my game my games reactivity might be a design pillar which means when you put in features your you're going to always ask the question of how does the player what the player does when they interact with this feature come back to them how are they being told hey here's how good you're doing with this thing the core game Loop would be those features that the player does a lot you would expect all of them to have large amounts of reactivity because if this is what the player is doing most of the time it better be supporting that design pillar of reactivity because I've talked about you can occasionally have a feature that doesn't support all the design pillars like you may put something in that's if humor is one of your design pillars you may have something in the game that's not that funny as long as overall the game is funny but for your core game Loop it should probably touch on all your pillars because it's these features are what your the player is doing a lot it should it should re it should have a basis in those design pillars.

**Для Напарника:** Ввести столпы Напарника (тепло, без стыда, дофамин) и проверять, что core loop затрагивает каждый из них.


---

## 4. Core loop задаёт приоритеты, расписание и оптимизацию
`процесс · метрики · крафт` · [08:32](https://youtu.be/aDE69s3pp7M?t=512)

**Мысль:** Он подсказывает, что делать в первую очередь, что можно выбросить при нехватке времени и где искать баги: частые пути важнее редких.

**Слова автора:**

> Your core game Loop tells your entire team what to focus on because here are the features of this big design document here are the features that are the most important to get correct to get in early to get them correct it will help you it will help the production staff decide what to prioritize because when there are features that have to be done you're like well these are part of the core game Loop they have to be done you could have a fun it's like side quests if you have to drop a side quest because you run out of time that's okay because it's not part of the main story your features help you schedule in the same way this is a great feature it's fun but is it part of the core game Loop and if it's not it can go you may not want it to go but it can go similarly when you get to the end of the game this tells you where to spend a lot of your time optimizing because if core game Loop features like I said it's where most players spend most of their time you want that to be optimized you want a smooth UI experience you want a good frame rate you want to make sure that there are no bugs in that core game Loop because that's what most of your players are going to spend most of their time doing if there's a you know an occasional bug that occurs from some obscure thing that the player can maybe do like maybe if they craft one item at a particular table and give it to a particular NPC and it causes that NPC to go in a bad State you want to fix that but if you had to prioritize that bug against oh yeah if you ever shoot a gun at an NPC that has more than five hit points sometimes the game crashes fix that.

**Для Напарника:** Приоритизировать полировку и баги Дома и Фокуса (основные пути), а не редких экранов.


---

## 5. Core loop как аргумент против лишних фич и монетизации
`процесс · этика · метрики` · [10:36](https://youtu.be/aDE69s3pp7M?t=636)

**Мысль:** Когда издатель просит микротранзакции, можно ответить, что в core loop для них нет места; фичи вне core loop легко отложить.

**Слова автора:**

> There's another reason for you to make sure the core game Loop is defined early because you want Publishers or whoever's giving you money to see that core game Loop it is a great way to provide context for answers to your questions when they have questions about it so if for example you have a publisher going well we really like microtransactions a great way to respond to that if you don't want them is like we don't see a role for microtransactions in this game's core game Loop and the reason that's a nice way of phrasing it is either they have to figure out how microtransactions would fit in that core game Loop which they're probably not going to be able to do or they're going to have to ask you to change the core game Loop which you your response would be that's the core game Loop so you want me to change the entire game so we're going to throw away this we're going to throw away these things and because if microtransactions are part of the core game loop we're going to redesign it is a nice defense against some of the things that Publishers will ask you to add but you because if it's not part of the core game Loop you're like I don't see a lot of players doing this and I certainly don't see a lot of players doing this a lot you can often get features suggested features either deprioritized or not considered altogether.

**Для Напарника:** Использовать core loop Напарника как фильтр против запросов вроде стриков, лидербордов, магазинов и тёмных паттернов.


---

## 6. Чем больше core loop, тем больше расписание и команда
`процесс · крафт` · [11:52](https://youtu.be/aDE69s3pp7M?t=712)

**Мысль:** Большая вариативность режимов (боевой, диалог, стелс) множит работу; рекомендация держать core loop максимально сфокусированным.

**Слова автора:**

> One last thing about core game Loop and I'm saying this from experience the bigger your core game Loop the longer it takes you to write it down the more features that are part of it the harder that game Loop will be to implement I say this from experience because when I make games that I say I want people to be able to play them all these different ways I want them to talk through it and fight through it and stealth through it and go through primarily with companion support that just added a lot of work and time to your schedule because if that's the core game Loop that you expect most of the players to be doing it's got to be good and of course like I've always said that then translates a big core game Loop will translate into a big schedule which will translate into a big team and a lot of money so it's in your best interest to try to get your core game loop as laser focused as possible but understand that some games will have big core game Loops it's just always in your best interest it's in your best interest it's in your team's best interest for knowing what they should work on and it's in the Publishers best interest for knowing what game they're buying and how you're going to respond to suggestions to change it's in everybody's best interest to get that core game Loop defined as early and as specifically as you can.

**Для Напарника:** Держать core loop Напарника узким: один основной путь вместо множества режимов.
