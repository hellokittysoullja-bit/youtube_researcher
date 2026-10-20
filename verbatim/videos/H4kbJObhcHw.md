# How Games Use Feedback Loops

**Канал:** Game Maker's Toolkit · 13 мин · субтитры: en (ручные) · https://youtu.be/H4kbJObhcHw

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Положительные и отрицательные петли: успех усиливает успех, а Mario Kart выравнивает
`игровой-дизайн · метрики · геймификация` · [00:27](https://youtu.be/H4kbJObhcHw?t=27)

**Мысль:** Положительные петли компаундируют победы и поражения; отрицательные гасят изменения и держат равновесие.

**Слова автора:**

> Feedback loops are systems where the output is fed back into the system as an input. And when it comes to game design, this typically means that a player’s success or failure impacts the likelihood of future successes and failures. And feedback loops come in two delicious flavours - positive feedback loops, and negative feedback loops. Let’s start with positive loops. These reinforce successes with more successes, and compound failures with more failures, and I think a good example of the first one is the kill streak system in the Call of Duty games, especially the earlier titles like Modern Warfare. In those games, getting a handful of kills in a single life grants you special “kill streak” bonuses, which might mean putting enemy locations on your radar, or allowing you to call in an airstrike or an attack helicopter. Which ultimately means that those who are already doing well by racking up kills, are rewarded with the tools to do even better. This can have something of a snowball effect - a sort of “rich get richer” type outcome where successes are compounded. But, of course, positive feedback loops can also be about how losses lead to further losses. Like in chess, where losing a piece from the board means that you now have fewer tactical options which could lead to even more losses down the line. On the opposite side of the coin are negative feedback loops, which balance out successes and failures. And there’s one example everyone always uses when talking about this stuff - but that’s just because it’s the perfect one. it’s the item distribution in Mario Kart. So, players who manage to get to the front of the pack will find themselves getting rather weak items like green shells and banana peels. But those who are at the back of the crowd are handed really powerful weaponry like the bullet bill, the golden mushroom, and - of course - the infamous blue shell which specifically targets the person in first place. So winners are punished, and losers are rewarded. If positive feedback loops work to compound changes in a game state, negative feedback loops strive to always counteract those changes and keep things in equilibrium.

**Для Напарника:** Для Напарника важно: неудачный день не должен запускать «спираль смерти»; ставим мягкие компенсирующие петли.


---

## 2. В Pyre проигрыш всё равно даёт опыт, нет перманентных потерь: ошибка — кочка, не точка невозврата
`игровой-дизайн · стыд · СДВГ · удержание` · [06:44](https://youtu.be/H4kbJObhcHw?t=404)

**Мысль:** Положительная петля без компенсатора ведёт к спирали неудач; парой с отрицательной петлёй (опыт за поражение, нет permadeath) игра остаётся в зоне вызова.

**Слова автора:**

> But Pyre counteracts this issue, by pairing those positive feedback loops - with negative feedback loops. So, yes, losing matches sucks but - here’s loop number one - you still receive some experience points for failing. Meaning that you’re not punished too much for messing up. Also, unlike XCOM, there’s no permadeath so you’re not massively screwed for future matches. And then on the other side of things, counteracting the issue of overpowered troops, there’s the liberation system. You see, Pyre is set in a sort of grim purgatory called the Downside - and the entire point of the game is to win these special liberation rites - because the prize is that the team’s leader gets to leave the Downside, have their crimes forgotten, and return to the Commonwealth. And in the game, this means that at various intervals throughout the adventure, you permanently send away your most powerful soldiers, because you can only liberate those who are of a high enough rank So I guess Pyre does have permadeath... but it’s a good thing. And all this means that the resulting experience - at least for me - is that the game is always a close and interesting challenge. Mistakes became a road bump on the way to the conclusion, not a tipping point that could send me into an inescapable death spiral.

**Для Напарника:** Ключевой принцип проекта: сессия, которую бросили или недоделали, всё равно что-то даёт (опыт, тёплая реплика), а не обнуляет прогресс.


---

## 3. Скрытые отрицательные петли дают противоречивые сигналы (скрытая сложность)
`игровой-дизайн · этика · доверие` · [08:16](https://youtu.be/H4kbJObhcHw?t=496)

**Мысль:** Если сообщить, что игра облегчается при ошибках, игроки специально ошибаются; наказание за успех противоречит поощрению.

**Слова автора:**

> One big issue with negative feedback loops is that they can send mixed signals. As we talked about in this episode, games are carefully designed to entice and encourage players towards a certain way of playing - so punishing someone for successfully playing the game completely goes against those encouragements. This is one reason why is was so important for Capcom to never reveal that Resident Evil 4 was using a dynamic difficulty system - ultimately, a negative feedback loop. Telling players that the game will get harder if they’re doing well, or easier if they’re struggling, is effectively telling good players to make mistakes.

**Для Напарника:** Не делать адаптивную сложность, которая карает за успех; награда за прогресс должна быть понятной.


---

## 4. Развяжи награду за мастерство и прогрессию: лучшим игрокам — бонус-уровни, а не больше денег
`игровой-дизайн · награды · этика` · [11:43](https://youtu.be/H4kbJObhcHw?t=703)

**Мысль:** Награда, которая даёт сильным больше ресурсов, оставляет слабых без нужного; поэтому награду за успех сделать содержательной, а не механической выгодой.

**Слова автора:**

> But sometimes it’s best to remove a feedback loop altogether. In Devil May Cry, getting a high score at the end of a level will grant a player more red orbs which are used to buy better weapons and health potions. This is a positive feedback loop that has the unfortunate effect of giving the best players a helping hand that they really don’t need, and means struggling players won’t have enough cash to get the items they require. It can be a good idea to simply decouple rewards for doing well, from the progression of the game. Donkey Kong has these challenging-to-collect KONG letters but grabbing them all doesn’t earn you coins or extra lives or anything like that: instead, you get extra difficult bonus levels, which is a suitable reward for players who are already proving themselves to be good at the game.

**Для Напарника:** Награды за длинные/сложные сессии — косметика и редкие находки, а не ускоритель роста острова.
