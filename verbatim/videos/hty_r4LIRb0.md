# Here's What Makes Incremental Games FUN!

**Канал:** Developing Ideal Idle Incremental Game · 10 мин · субтитры: en (авто YouTube) · https://youtu.be/hty_r4LIRb0

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Качели доходов и затрат: линейный рост против экспоненциальной цены
`игровой-дизайн · награды · дофамин` · [03:08](https://youtu.be/hty_r4LIRb0?t=188)

**Мысль:** Каждый генератор даёт линейный прирост, а стоит на 10% дороже предыдущего, поэтому ожидание растёт от секунд до недель и игрок упирается в стену.

**Слова автора:**

> The vast majority of idle incremental games are just a seesaw between profits and costs this means that with every next generator you buy your profits grow linearly while your costs grow exponentially to make this clearer let's take a look at the formulas I'm using for a do game average generator you buy will increase your dock production by two ducks per second this means that 10 generators will produce 20 ducks per second and a 100 generators will produce 200 docks per second that's what linear growth is however the cost of each subsequent generator will be 10% higher than previous one given this exponential growth the cost of the 10 generator will be 24 docks and the 100s one will cost more than 100,000 ducks that escalated quickly now what do these numbers really mean let's say you already have nine generators producing 18 docks per second it will only take you two seconds to purchase your 10 generator but you would need to wait more than 10 minutes to progress from 99 to 100 generators and if you've already purchased 199 generators it would take more than 50 days to buy the 200 one which would cost more than two billion docks That's The Power of exponential growth so at the earlier stages of the game your production will exceed costs but the more generators you buy the higher the price of the next one becomes until eventually the waiting time for the next generators becomes prohibitive and you hit the wall.

**Для Напарника:** Для кривой роста острова избегать стен, из-за которых человек чувствует «застрял»; кривая должна оставаться посильной.


---

## 2. Веселье — в изобретательных способах пробить стену
`игровой-дизайн · мотивация` · [04:50](https://youtu.be/hty_r4LIRb0?t=290)

**Мысль:** Вся вовлечённость инкрементальной игры рождается из разных способов преодоления стены; автор считает двух базовых способов достаточно для хорошей игры.

**Слова автора:**

> Remember the one and only mechanic that makes incremental games fun I mentioned about well in my opinion all the enjoyment and engagement of idle inal game stems from its ability to offer creative ways to overcome this wall potentially there are tens or even hundreds approaches to it covering them all would definitely be beyond the scope of this video however there are two basic and essential ones that without exaggeration are used in every incremental game I ever played and I firmly believe that using just these two are sufficient to create a reasonably engaging game.

**Для Напарника:** Если рост замедляется, давать человеку интересный выбор (новое существо, новый способ), а не просто больше ожидания.


---

## 3. Новые типы генераторов: дорогие, но выгоднее из-за экспоненты
`игровой-дизайн · награды · игровой-дизайн` · [05:36](https://youtu.be/hty_r4LIRb0?t=336)

**Мысль:** Второй тип генератора стоит дороже, но из-за экспоненциальной цены первого оказывается выгоднее; число типов выбирает дизайнер.

**Слова автора:**

> So once we hit the wall and the speed of our game slows down what can be done to speed it up the most obvious and widely used solution is to create another type of generator whose price would be much higher but whose production is also greater in our case we create a second type of generator which will cost one 1,000 ducks and will produce 100 Ducks per second at first glance it might seem that this generator is less preferable because its production rate compared to its price is lower however due to the exponential nature of price growth in fact this second type of generator produces more ducks and costs less let me show you an example you will spend more than 11,000 ducks to buy 50 generators of the first type which produce 100 Ducks per second this same production will cost you only 1,000 Ducks if you buy the generator of the second type now it will cost you almost 1 and a half million ducks to purchase 100 generators of the first type producing 200 Ducks per second but you can reach that same level of production by buying just two generators of the second type for 2,100 Ducks I hope that makes sense at the same time doesn't really matter how much more appealing the second type of generator is because sooner or later it will also become irrelevant only the game designer decides how many types of generators there will be in the game for the Duck game I limited myself for three types of generators the last one produces 5,000 ducks per second and it cost starts from 100,000 ducks in my main game project get a little gold there are 15 types of generators ranging from fan to a white hole.

**Для Напарника:** Вводить для острова новые типы построек с разной ролью и выгодой, а не только больше одного и того же.


---

## 4. Престиж: сброс прогресса в обмен на постоянный бонус
`игровой-дизайн · удержание · награды` · [07:46](https://youtu.be/hty_r4LIRb0?t=466)

**Мысль:** Престиж-механика позволяет сбросить прогресс ради постоянного бонуса и решить, ждать ли ради большего бонуса.

**Слова автора:**

> Well the second approach to Breaking the wall is the well-known Prestige mechanic again if you play it incremental games before you almost suddenly come across the concept of prestige Mechanic In A not it's a mechanic that allows you to reset the progress in the game in exchange for some permanent boost that allows you to progress faster next time for our Duck game Let's implement the most basic Prestige mechanic first we should add the variable to keep track of all ducks produced during the game now once the number of ducks reaches 1 million will'll show a button offering to reset the progress and obtain a 100% boost to all duck production we can either Prestige now or wait longer to collect more ducks and increase our potential bonus each subsequent step require 1 million more Ducks than previous one and we'll add another 100% to the bonus so to reach 200% bonus we need to collect a total of 3 million docks and to reach 300% bonus we need to collect 6 million Ducks.

**Для Напарника:** Не применимо: сброс прогресса противоречит принципу «ничего не отнимать»; допустима только добровольная смена острова (сезон) без потери накопленного.


---

## 5. Оффлайн-доход: прогресс идёт, пока тебя нет
`удержание · привычки · СДВГ` · [08:58](https://youtu.be/hty_r4LIRb0?t=538)

**Мысль:** Сохраняется время выхода, а при возвращении секунды умножаются на скорость производства, так игра награждает за возвращение.

**Слова автора:**

> Another important aspect of virtually every incremental game is offline earnings so let's add them to the DU game the simpler the game the easier is to add the offline earnings mechanic in our case it will be a breeze we just save the time when the player close the game and count how many seconds they were offline once they start the game again then we can multiply these seconds by the duck production value and receive the amount of ducks produced when the player was offline.

**Для Напарника:** Остров продолжает «жить» между сессиями (небо меняется, существо у очага), и возвращение встречает приятным сюрпризом без вины.
