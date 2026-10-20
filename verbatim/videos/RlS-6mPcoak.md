# Simple 2D Idle Animation for your Character | Handdrawn | Beginner 2D Game Art

**Канал:** Nonsensical 2D · 18 мин · субтитры: en (авто YouTube) · https://youtu.be/RlS-6mPcoak

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Поза в покое объясняет характер персонажа
`маскот · персонаж · анимация` · [02:11](https://youtu.be/RlS-6mPcoak?t=131)

**Мысль:** Поза и силуэт в idle сообщают личность (сильный и гордый против сутулого), даже без слов.

**Слова автора:**

> One of the reasons why things such as posing is important is that it can help explain the character you're playing one of the best examples of this is guacamelee if we look at this pose not only is it a really strong and nice silhouette but it also tells the player what personality the character has he's sort of strong proud superhero character and we don't even need to look at another game to see why this can be valuable we can see here how much of a narrative difference it makes when we see the same character in a slump sort of fat pose and we can see lots of games where the pose and movement is heavily considered for narrative purposes.

**Для Напарника:** Поза кота в покое (расслабленная, тёплая, рядом) задаёт тон присутствия без надзора.


---

## 2. Больше движения = «игра» и активность; меньше = реализм и погружение
`анимация · внимание · мотивация` · [03:50](https://youtu.be/RlS-6mPcoak?t=230)

**Мысль:** Активная анимация заводит в режим действия, сдержанная создаёт атмосферу; непрофессионалы воспринимают много движения как «слишком игровое».

**Слова автора:**

> If we compare games such as Ghost Song and dead cells they're about equalism then but if we look at their animations we can see that the animation of ghost song is very timid and understated compared to dead cells and if you have great dead cells you know that there are many parts of it that incentivizes you to be active such as time Grooms you need to get to in under two minutes before they lock the animation really helps set you in that active mode compare that to Ghost Song which is exceedingly good at making you feel that you're exploring a desolate planet and that understated post really helps to sell that and I actually asked a few people I know who aren't into gaming to look at some of these animations to see what they thought the first thing one of them mentioned when she saw the animation of Wonder Boy was that she didn't like it because the amount of movement made it feel too much like a game it sort of reminded her of Flappy Birds and she compared it to the animation in Ghost Song her she felt reminded her more of a movie while I like both types of animations a lot I kind of agree with their assessment again with a lot of movement feels more like a game whereas less movement tends to feel more realistic and immersive.

**Для Напарника:** В Фокусе кот должен двигаться минимально (не провоцировать активность и не отвлекать), на Доме и в Мире можно чуть живее.


---

## 3. Даже дыхание можно сделать выразительным для характера
`маскот · анимация · персонаж` · [07:40](https://youtu.be/RlS-6mPcoak?t=460)

**Мысль:** Одно и то же дыхание: вздох с расправлением плеч у героя или с оседанием у неуверенного, так анимация несёт эмоцию.

**Слова автора:**

> We want the character to be sort of insecure and depressive so the perfect thing to do is to look at guacamelee and then do the opposite if we take a look at what that animation does it sort of goes to a straight posture when he breathes out but then when he breathes in goes in even greater superhero pose so what we're going to do for in secure mushroom is to start from a normal pose and then when the mushroom breathes out it slumps down even more so even though we're only doing a breathing animation we can still think about how we can use the animation to explain the personality of our character.

**Для Напарника:** Выдох кота как «вздох облегчения» после завершённой сессии; без стыда, тепло и мягко.


---

## 4. Лицо в idle лучше держать статичным, если тело дышит
`анимация · маскот · крафт` · [08:12](https://youtu.be/RlS-6mPcoak?t=492)

**Мысль:** Одновременное покачивание, улыбка и моргание каждые доли секунды выглядят неловко и снижают погружение. Автор считает лучше оставить лицо стабильным.

**Слова автора:**

> I will generally keep the face consistent throughout the entire animation we can see this in my current Running Animation these flaps swing back and forth but the face is static and we can see this in Hollow Knight as well my biggest reason for keeping the head and facial movement consistent throughout animation is that I generally feel that those types of Animation can reduce immersion if I were to sit up and bob up and down with each breath looks somewhat natural but if I were to bob up and down and smile and blink every 10th of a second it would feel kind of awkward and so in my opinion and hopefully yours too tends to be better and just keep it static and not open up for those type of awkward looks so what I'll do.

**Для Напарника:** Для кота: не накладывать частое моргание на дыхание; редкие выражения только по событиям (согласуется с контингентностью). Противоречит советам первого ролика про живое лицо, решать по контексту.


---

## 5. Начни с двух крайних поз, чтобы ограничить амплитуду
`анимация · крафт · процесс` · [09:08](https://youtu.be/RlS-6mPcoak?t=548)

**Мысль:** Две ключевые позы задают диапазон движения заранее, анимация живёт между ними.

**Слова автора:**

> The reason I start with the head is that it helps me figure out how much my character is going to move overall and it also helps me contain the animation so now I know that my animation is going to exist between these two frames and the jump is not going to be bigger or smaller than this.

**Для Напарника:** Для CSS-дыхания кота зафиксировать два состояния (scale/translate) и анимировать только между ними.


---

## 6. Минимум кадров и ping-pong вместо loop для idle
`анимация · крафт · процесс` · [10:46](https://youtu.be/RlS-6mPcoak?t=646)

**Мысль:** Добавлять кадры только до исчезновения рваности; ping-pong для idle вдвое сокращает работу, но не подходит для бега.

**Слова автора:**

> I don't generally care too much about whether I have 4 or 24 frames I tend to just add the least amount of frames I feel are necessary to get the animation the way I want it to be what this means is I'll slow it down to the type of speed I wanted to move and then I'll check if it's to jacket and if it's too Jagged then I'll add more frames when I'm shaking my animation I have it set to ping pong the animation so in most animation software you have it to try the ping pong or Loop what Ping Pong does is that it makes the animation play back and forth rather than repeat itself so the ping pong goes back and forth whereas the loop goes whoop and starts over Roop so we'll go to my last frame and then cycle all the way back to the start this kind of makes sense for an idle animation and makes it so that we only have to animate half as much.

**Для Напарника:** В CSS дыхание кота делать animation-direction: alternate с easing, а не два отдельных кейфрейма вверх и вниз.


---

## 7. Вторичные части (ткань, уши, хвост) идут с запаздыванием
`анимация · крафт · маскот` · [11:41](https://youtu.be/RlS-6mPcoak?t=701)

**Мысль:** Свободные части имеют инерцию и отстают от основного движения, поэтому их анимируют после основного и не синхронизируют.

**Слова автора:**

> When I have my main movement laid out I'll add the small Fabric and Flappy bits the reason I do them after my main movement is that these will generally be out of sync from my main animation which makes sense if you think about it they have some inertia and they aren't attached to me so when I move quickly it will take some time for it to catch up so it'll be easier to just think about and consider how these Flappy bits fly.

**Для Напарника:** Хвост и усы кота анимировать со сдвигом фазы относительно дыхания тела.


---

## 8. Наклон головы определяет настроение: вверх гордый, вниз робкий, без наклона наивный
`маскот · персонаж · анимация` · [13:50](https://youtu.be/RlS-6mPcoak?t=830)

**Мысль:** Лёгкое изменение угла головы меняет воспринимаемый характер персонажа.

**Слова автора:**

> So generally tilting the head up will make the character feel proud and stout and tilting it down we get this sort of Meek and depressed look if we just skip tilting it then I think we can make our character look a bit dumb but well meaning.

**Для Напарника:** Для выражений кота: лёгкий наклон головы набок как «слушаю тебя», без вниз-наклона, который читается как грусть или вина.


---

## 9. Лёгкая неидеальность читается как стиль, если выдерживать последовательно
`вкус · крафт · маскот` · [15:19](https://youtu.be/RlS-6mPcoak?t=919)

**Мысль:** Если всё чистое, любой недочёт выглядит ошибкой; если неидеальность везде, она воспринимается как намеренная.

**Слова автора:**

> Making everything too clean will tell the viewer that I want Merit to be clean and then every time something is left unpolished the viewer will see that as a mistake but if I just leaving small mistakes or a wavy line art constantly they'll see it and go well he obviously knows what he's doing so he wants it there it's intentional.

**Для Напарника:** Рукотворные неровности иллюстраций острова и кота допустимы, если выдержаны во всём продукте.


---

## 10. Дай работе отлежаться: дистанция показывает реальные проблемы
`процесс · крафт` · [17:06](https://youtu.be/RlS-6mPcoak?t=1026)

**Мысль:** Время вдали от проекта даёт перспективу, что действительно является проблемой; перфекционизм мешает закончить.

**Слова автора:**

> But the thing is I'm never fully happy with any of darts I do but after work done it then give it into a try I let it sit and then I come back to it in the future because time away from the project will give me perspective on whether it is an issue or not as an example when I made my staging scene I tried focusing on the core idea of where you might place your main background assets to maximize Paradox but then I completely overlooked working on the background so it looked really flat and empty but eventually this bugged me a lot so before I started my video on environment animations I went back into the scene and fixed it and we can see if I compared it to the difference it made and that tends to be the process I work through I don't like the idea of trying to perfect things because you would simply never get things done.

**Для Напарника:** Процессный совет: полировку экранов делать итерациями с паузой, а не доводить до идеала за раз.
