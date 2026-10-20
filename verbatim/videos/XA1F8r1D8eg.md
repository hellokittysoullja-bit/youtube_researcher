# Game Loops: Designing the Heartbeat of your Game

**Канал:** Vertical Nice: Game Design with Chillen · 13 мин · субтитры: en (авто YouTube) · https://youtu.be/XA1F8r1D8eg

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Игра - решение задач; удовольствие во многом от обучения
`игровой-дизайн · мотивация · нейро` · [00:33](https://youtu.be/XA1F8r1D8eg?t=33)

**Мысль:** Игра ставит цель и инструменты, учит ими пользоваться; радость игр - это радость обучения.

**Слова автора:**

> A game is a problem-solving activity entered with a playful attitude when we play games the game presents us with a goal and some tools and then it tries to teach us how to use those tools to get what we want it's not far-fetched to say that a lot of the fun of games is really the fun of learning.

**Для Напарника:** Фокус как маленькая задача: цель, инструмент (таймер, шаг) и ощущение, что научился делать.


---

## 2. Новичок без ментальной модели путается, если игра не говорит, что верно
`онбординг · доступность · игровой-дизайн` · [03:15](https://youtu.be/XA1F8r1D8eg?t=195)

**Мысль:** Интуиция строится на прежнем опыте, а человек без игрового опыта дольше начинает и иначе трактует взаимодействия.

**Слова автора:**

> Intuition for games is because we come in with an existing mental model we've played similar games we've interacted with similar things in the real world so we have a set of expectations and we're able to make predictions about how these things will work in this new game in rasputin's video what games are like for someone who doesn't play games we see what actually happens when somebody who doesn't have that mental database built up tries to learn about the game and it takes longer to get started interacting with things in the way that the designer intended and they interpret interactions differently than any veteran player would if a player hasn't played similar games it's much easier for them to get confused when the game doesn't adequately tell them what's right and wrong remember this is our world and we're asking them to learn the rules of it.

**Для Напарника:** Онбординг Напарника не должен предполагать игровую грамотность: явные подсказки, что нажать и что произойдёт.


---

## 3. Без обратной связи нет обучения: ответы без оценки бесполезны
`доверие · игровой-дизайн · микрокопирайтинг` · [04:10](https://youtu.be/XA1F8r1D8eg?t=250)

**Мысль:** Тесты без проверки не дают знать, правильно ли ты отвечал; обратная связь нужна, чтобы обновлять ментальную модель.

**Слова автора:**

> Now imagine taking a math class in university and every week you're taught new material each element building up one after another each week you take a quiz and answer a bunch of questions but that quiz is never graded you don't know which answers are right or wrong at the end of the year after taking tons of quizzes without getting any feedback how well do you think you'll score on a test this is a crucial step in the analysis part of the scientific method feedback we perform a test so that we get a result so that we can know if we were right or wrong and we use that feedback to inform future experiments in games like in science if we want a better mental model we need to get good feedback.

**Для Напарника:** Каждое действие в приложении должно получать понятный отклик (в голосе напарника): сработало или нет.


---

## 4. Игровой цикл: ментальная модель, цель, действие, правила, обратная связь, обновление
`игровой-дизайн · мотивация · нейро · крафт` · [05:08](https://youtu.be/XA1F8r1D8eg?t=308)

**Мысль:** Игрок исходит из модели, ставит цель, выбирает действие, правила мира реагируют последовательно, обратная связь обновляет модель. Последовательность правил укрепляет уверенность в обучаемости мира.

**Слова автора:**

> Okay so what is the game loop then the game loop much like the loop involved with the scientific method is all about solving problems it's about learning skills it's about being presented with questions and doing your best with the tools provided to answer them sufficiently the idea of the game loop is very well described by spryfox co-founder dan cook's 2012 essay loops and arcs available on his lost guarded blog and also in his igda seattle talk game design theory i wish i knew we start with a mental model and what do we know about this game and things related to this game what goals do we have in mind in terms of the scientific method what's our question and what's our hypothesis maybe we're fighting a boss in a zelda game with a big yellow eye and based on our experience with previous zelda games we can predict that hitting the boss in the big yellow eye will deal the most damage maybe we're playing a puzzle game with ice cubes on an icy floor and we know from real life that ice is slippery and we might be able to push them around once we have a goal we instinctively predict which actions might be available to us and choose an action which we think is going to bring us closer to that goal no way nope okay victoria because this is our own world the next step is to have the rules of the game take place it's important for us as designers to consider this step because we're the ones designing the cause and effect of actions we want our actions to behave consistently to reinforce a strong mental model and boost the player's confidence that our game world really is learnable finally the all crucial feedback we give the player some kind of data that they can analyze and use to update their mental model this could be in the form of rewards like coins points or access to new areas or it could be in the form of evocative stimuli like animations or sound effects but of course this is a loop once we have our feedback this updates our mental model we have a better understanding of the game's rules and we can either try again at our goal or we can formulate a new goal and take actions towards that.

**Для Напарника:** Использовать цикл как чек-лист для Фокуса: цель ясна -> действие -> согласованная реакция кота/острова -> награда, обновляющая ожидания.


---

## 5. Линза петли: сигналы, обратная связь и количество вопросов к игроку
`процесс · исследования · игровой-дизайн · онбординг` · [10:20](https://youtu.be/XA1F8r1D8eg?t=620)

**Мысль:** Надо проверять, видны ли цели и действия, даёт ли петля обратную связь и не слишком ли много вопросов одновременно; плейтесты как учебные упражнения показывают, где петля ломается.

**Слова автора:**

> Well the loop asks us to look at what problems the player is solving how often and how exactly we're going about reinforcing them a key insight with the game loop is the importance of looking out for signs and feedback does our loop adequately signal available goals and actions and does it provide adequate feedback to teach the player more about the game rules after they take an action once we know the problems that are being solved and we've identified our loops we can start considering the player's questions while they engage in those loops how much health do i have left how does that enemy die which enemies should i hit first is the player asking interesting questions are we providing tools to answer those questions are we asking too many questions at once looking at the game as loops as cycles of learning and problem solving we can evaluate play tests as learning exercises and sort out where the loop is breaking for players.

**Для Напарника:** Проверять каждый экран: не задаём ли сразу много вопросов (принцип одного вопроса за визит).
