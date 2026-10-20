# Juice it or lose it - a talk by Martin Jonasson & Petri Purho

**Канал:** grapefrukt · 15 мин · субтитры: en (ручные) · https://youtu.be/Fy0aCDmgnxg

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Сочность: максимум отклика на минимум ввода
`анимация · дофамин · крафт` · [00:35](https://youtu.be/Fy0aCDmgnxg?t=35)

**Мысль:** «Сочная» игра отвечает на каждое действие каскадом реакций; сок бывает визуальный, звуковой или в неожиданных текстовых ответах. Авторы утверждают, что он улучшает игру всегда.

**Слова автора:**

> In videogames, juicy things are things that wobble, squirt, bounce around or make cute noises. Sort of a catch-all phrase for things that make the game feel good to interact with. The term juicy comes from this classic Gamasutra article called 'How to prototype a game in under 7 days'. And they say this: a juicy game feels alive and responds to everything you do, tons of cascading action and response for minimal user input, and juice is typically visual or auditory, but it doesn't really need to be: Emily Short mentions on her blog that interactive fiction, which is a text-based game, they can't really do wiggles and squirts much, but they have their own kind of juice: the fun and, sort of unexpected responses you get when you try something in the game that you're not supposed to do. And that's pretty much what juice is about, it's about maximum output for minimum input. - So why juiciness? I recently had the "pleasure" of giving feedback on some student games, and what I noticed was that almost all of them lacked juiciness. That made me realize how important juiciness actually is to a game. Because game design is quite hard and it's impossible to give broad statements that are true for everything. But adding juiciness to your game makes your game better 100% of the time, guaranteed.

**Для Напарника:** Каждый тап в Напарнике (старт сессии, отметка шага) должен вызывать тёплый многослойный отклик кота и острова, при этом без шума ради шума.


---

## 2. Простейший ease-out: двигайся на 10% к цели каждый кадр
`анимация · крафт` · [03:59](https://youtu.be/Fy0aCDmgnxg?t=239)

**Мысль:** Приём, когда значение каждый кадр приближается на долю расстояния: сначала быстро, потом замедляется. Очень просто реализуется и выглядит плавно.

**Слова автора:**

> Basically we're moving x (whatever value that is) 10% of the way we need to go. So at first, it will go fast and then as it approaches its target it will slow down. Looks very nice, very easy to implement, like this, have it run every frame: you're good.

**Для Напарника:** Использовать такой приём для плавных движений кота, счётчиков и появления элементов острова.


---

## 3. Easing с перелётом, масштаб, вращение и случайная задержка
`анимация · крафт · дофамин` · [04:33](https://youtu.be/Fy0aCDmgnxg?t=273)

**Мысль:** Заменив линейное появление блоков на замедление, перелёт цели и отскок, а также добавив случайную задержку, игра выглядит дороже без изменения логики.

**Слова автора:**

> And now we can use these mystical equations here, so instead of using the linear one, which is just falling in, we can use this sort of slowdown type equation. Look at it. It's slowing down slightly. We can do better, though. We can go slightly past our target using a different equation. Look at that! Very luxurious! And there's also crazy equations. You're laughing. This is serious stuff. And the bouncing equation, this is a crazy one: look at it! Amazing. And we can also tween other properties, not just position. We can tween rotation, we can tween scaling. Let's try that. See what happens. Very nice. You see, it's getting somewhere. And the best thing we can do is add a little bit of delay, a random delay to everything. Looks like this. Look at that! Same thing: we're not changing the game at all.

**Для Напарника:** Появление новых построек острова и карточек награды делать с лёгким перелётом и разной задержкой, а не линейным fade.


---

## 4. Сжатие и растяжение: реакция объектов на каждое событие
`анимация · крафт · дофамин` · [05:34](https://youtu.be/Fy0aCDmgnxg?t=334)

**Мысль:** Масштаб при ударе, поворот по направлению, растяжение по скорости, белая вспышка и покачивание линий делают предметы живыми, хотя логика не меняется.

**Слова автора:**

> So, unlike easing and tweening, squeezing and stretching isn't an actual programming term that you can Google, but this is this a term we came up with for a bunch of different effects that you can add your game to make things way better. Some of these are done with tweening and easing, or most of these are done with tweening and easing. So we're gonna start out with making the paddle respond a bit. So, instead of... This isn't actually even using any kind of easing, it's using the offset of the mouse pointer and where the paddle is to figure out the scale of x and y. It's a very simple effect to implement. The next thing we're gonna do is we're going to add some extra scaling to the ball. So when the ball hits something, it's gonna scale up to bigger, and it's gonna go smaller with an easing equation and that looks kind of nice and adds a bit of feel to the ball hitting things. Then we're gonna make the ball rotate. So it's gonna rotate in the direction that it's going. We're gonna animate this rotation for a very small subtle effect that's almost impossible to see. We're gonna make also the ball stretch a bit. It's stretching based on its velocity. This looks way better if you have gravity, but it's okay with this. It also looks better if it's actually a ball shape. We're gonna animate the stretching down, so whenever the ball hits something, it's gonna wobble for a bit. And for the last thing, we're gonna add color to the ball, So the ball will get white every time it hits something, and then it's gonna scale back to its normal. So it already feels way better to move, bounce the ball around. But this isn't juicy enough, so we're gonna add some tweening to all of the blocks when something is hit. So when the ball hits something, there's a small scaling effect on all the blocks, which is done with tweening. It's a very simple effect to add. And the last thing we're gonna add: bouncy line. So whenever the ball hits the line, the lines are gonna bounce a bit. Making things feel so much nicer to play around with.

**Для Напарника:** Мягкая реакция кота и предметов острова на события (сквиш при тапе, короткая вспышка) вместо статичных картинок; оставлять медленной и диегетичной.


---

## 5. Звук — самый выгодный способ усилить ощущение
`звук · дофамин · крафт` · [07:38](https://youtu.be/Fy0aCDmgnxg?t=458)

**Мысль:** Тот же демо-анимационный ролик с добавленным звуком выглядит как столкновение вместо прохождения насквозь; звуковые эффекты и музыка превращают демо в настоящую игру.

**Слова автора:**

> Next up is probably one of the most important parts you can add, like this is the most cost-effective thing you can add to a game to make it juicier, which is sound. Unfortunately, an extremely often ignored part of game development. This is a simple Demo we ripped off from the Steve Swink book 'Game Feel'. So there are two balls/circles that pass through each other. This is without sound. We're gonna add sound to this, and... You can see, hopefully, the difference. So you can see now they seem to bounce off from each other instead of passing through. And this is the same animation with the only exception of adding sound effect to it. So now we're gonna add some sound effects to our game. - Sound effects. - Yes! Remove everything else, enable sound effects. So we're gonna first bounce off the walls, so it's just going to be a small sound when... So much better. Add sound for blocks. - Sound effects, thanks to Niklas. - Is he here? Are you here? - Yeaaaah! - Yeaaaah! Oh come on! Give me more than one! Add the paddle effect. And lastly, very important, the music by Niklas. Actually even though the game doesn't have anything else except sound effects, now it feels almost like a real game instead of a crappy demo.

**Для Напарника:** Расставить тихие звуки на события (старт, завершение шага, находка) с хаптикой: самый дешёвый способ сделать Напарника «ощутимым».


---

## 6. Частицы и слои простых эффектов складываются в красоту
`анимация · дофамин · крафт` · [09:37](https://youtu.be/Fy0aCDmgnxg?t=577)

**Мысль:** Дым, падение блоков, толчок, вращение и затемнение по одному просты, а вместе дают богатство. Предупреждение: не застревать на создании собственного движка частиц.

**Слова автора:**

> There's this saying, like you can't ever have too many particles in your game, and, again, you can't make broad sweeping statements, but it's 100% true. Let's add some particles. We're gonna start with the classic smoke, the ball hits something, we put a little puff of smoke in there. And you can use whatever particle engine you can find. It's kind of a trap for programmers, these particle engines, because you get stuck making one, and you're making it the very best one and then you never use it... But it was fun making... So, don't do that. Just find something that's already made, use it. - Do it. It's like the simplest thing you can program. - Don't listen to him! Don't listen to him! So we've got smoke in the game, like smoke coming off the ball. We can do better, we can do better. We want to make something with the blocks. So we want to make them sort of disappear. This isn't technically a particle effect. This is tweening. But if you can manage to hit a block you can see it's slowly going away. We can do better. We can do better, way better. So let's make them fall away when you hit them. Look at that. This is falling off the screen. We can do even better. Let's have some more stuff. Let's add... Let's make the ball sort of push the block. Look at that. And why not make it spin while we're at it. And now you can tell, like it's hard to see... the block falling off is blending with the other ones, so let's make it darker. These are all simple things, like, stacking together to make something beautiful.

**Для Напарника:** Для финала сессии собрать эффект из нескольких простых слоёв (искры, свечение, движение), а не одной сложной анимации.


---

## 7. Тряска экрана — мощный, но опасный эффект
`анимация · крафт` · [11:59](https://youtu.be/Fy0aCDmgnxg?t=719)

**Мысль:** Простая тряска при ударе превращает объект из обычного в значимый; авторы просят осторожности, так как эффект сильный.

**Слова автора:**

> Now we're going to move on to one of the more powerful effects and I want you to be careful with this when you try it at home because it's... It's powerful! So would you bring out the screen shake, Petri? This really, for effort, this is one of the best ones. So when the ball hits something, we shake everything a little bit. And the ball went from being, like, a stupid tennis ball to a motherfucking comet, or something.

**Для Напарника:** Не применимо: резкая тряска противоречит спокойному тону и риску перегрузки при СДВГ; допустима лишь едва заметная реакция на редкие находки.


---

## 8. Добавь глаза: личность за копейки
`маскот · персонаж · крафт` · [12:56](https://youtu.be/Fy0aCDmgnxg?t=776)

**Мысль:** Глаза, которые моргают, следят за мячом, улыбаются и грустят, дают огромную личность при минимальных затратах на код и графику.

**Слова автора:**

> It's not exactly an effect, but it's a thing. You add eyes to anything you have. So we're adding these small eyes to the paddle. Which is, like, so little programming effort and art effort. The animation is just disabling the eyes for a while, and it looks like it's blinking. We can animate the eyes a little bit more, so we can make it look towards the ball as it's going. It's a nice little thing. We're also gonna add a smile to it. So it's got a small mouth there. And it smiles when it hits the ball. It's just scaling that y value of it. If you can get the ball to go further away, you can see it frowns in horror. And the effort of this, like, how much personality it adds, it's insane.

**Для Напарника:** Подтверждает ставку на кота: взгляд на задачу, моргание, лёгкая улыбка при успехе дают присутствие дешевле любого нового контента.
