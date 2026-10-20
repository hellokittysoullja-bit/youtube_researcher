# How Video Game Economies are Designed

**Канал:** Game Maker's Toolkit · 16 мин · субтитры: en (ручные) · https://youtu.be/Zrf1cou_yVo

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Источники ресурсов (taps) направляют поведение игрока и задают ценность
`игровой-дизайн · геймификация · метрики` · [01:54](https://youtu.be/Zrf1cou_yVo?t=114)

**Мысль:** Куда и сколько падает ресурса — это стимул (лут с врагов, материалы по биомам) и регулятор редкости.

**Слова автора:**

> Taps generates new resources into the economy. That could be enemies who drop experience points when they die. A saw mill that harvests wood. A regenerating health bar. Or rocks that spit out iron ore. Some taps generate resources automatically, on a timer - others need to be mined manually, by the player. Now the thing about taps is that can be used to incentivise player behaviour. If you want players to fight monsters, then you can put loot drops on the enemies. If you want to push players to explore the world, then you might put unique crafting materials in every biome. And if you want players to punch demons in the face, then shower them with health points when they glory kill baddies. Also, just like a real tap… you can change the flow of resources. This will affect how scarce, and valuable, a resource is: from rare ammo drops in a survival horror game, to an abundance of munitions in a fast-paced shooter.

**Для Напарника:** Откуда на острове берутся элементы (сессии, находки) должно совпадать с нужным поведением: фокус, а не накликивание.


---

## 2. Положительная петля «повтори, стань сильнее» опасно затягивает и превращается в гринд
`игровой-дизайн · этика · удержание` · [06:23](https://youtu.be/Zrf1cou_yVo?t=383)

**Мысль:** Идле-игры строятся на петле, которая подкрепляет саму себя, и это эффективно, но порой вредно.

**Слова автора:**

> Idle games like Cookie Clicker, and roguelikes with permanent progression make players repeat the same, or very similar, content - but each time, with more power or efficiency than before. This creates a positive feedback loop - a system where the output is fed into the input, and then reinforces the output more strongly. And it can be very compelling - and dangerously addictive. But you know what else we might call repeating the same content to slowly amass power? Grinding. And that’s not always what we want.

**Для Напарника:** Не строить рост острова как гринд: ограничить накопление, чтобы мелкие сессии не копились ради очков.


---

## 3. Отрицательная петля: стоимость повышения растёт вместе с уровнем и убивает фарм
`игровой-дизайн · метрики · геймификация` · [09:03](https://youtu.be/Zrf1cou_yVo?t=543)

**Мысль:** В Elden Ring каждый следующий уровень требует всё больше рун, поэтому бить простых врагов неэффективно.

**Слова автора:**

> A system that works to balance itself to a status quo. In. Elden Ring, if you graph out the number of runes needed to unlock the next level, then you’ll see that it makes a sharp, upward curve where it costs more and more experience points to jump to the next level. So while you only need to dispatch about 10 guards in Limgrave to jump from level 9 to level 10, you’d need to kill hundreds of them to go from level 49 to 50. By changing the cost of the conversion in lock step with your level, Elden Ring makes killing the same simple enemies over and over again incredibly ineffective - massively discouraging this tactic. And so players are pushed to explore further afield, fight tougher monsters, and take bigger risks.

**Для Напарника:** Рост острова не должен быть линейно зависим от числа коротких сессий; ценить длину и регулярность разумно.
