# Pixel Art Class - Simple Character Idle Animation

**Канал:** AdamCYounis · 17 мин · субтитры: en (авто YouTube) · https://youtu.be/vs-ierVdE7I

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Idle: не переанимируй; редкие выразительные движения раз в ~5 секунд
`анимация · маскот · персонаж · время` · [02:58](https://youtu.be/vs-ierVdE7I?t=178)

**Мысль:** Мелкая анимация ощущается тяжёлой: даже один пиксель вверх-вниз при 64 px может выглядеть как одышка. Выразительные движения (перенос веса, поворот) разреживай раз в несколько секунд; характер задаёт амплитуду.

**Слова автора:**

> Now that's not to say that you can't have more advanced idle animations one of the things that I've been going for in my game is I've been looking to have animations that move between states so a character like shifting their weight or turning and looking somewhere else these are more expressive movements that you can kind of stagger out once every 5 seconds or so that feel natural without trying to make the character look like they're constantly heaving for air and that's a risk in general with characters you know at 64 pixels or smaller you know even one pixel up and down can feel like a lot so if your game's trying to go for something more natural it can be a risk to over animate something that should be very simple especially if it's not in the character's nature to breed that way so this character she's quite stoic she's she's quite seasoned and so I want her to seem calm.

**Для Напарника:** Кот-напарник: спокойный idle с редкими жестами раз в ~5-20 с, амплитуда малая; не мельтешить рядом с работой пользователя (метафора присутствия, не надзора).


---

## 2. Дыхание в два состояния: сдвиг верхней части на 1 пиксель, 10-12 кадров
`анимация · маскот · время · крафт` · [04:49](https://youtu.be/vs-ierVdE7I?t=289)

**Мысль:** Простой idle строится из вдоха и выдоха: верх тела над бёдрами сдвигается на 1 пиксель, большинство кадров — удержание, а переход растягивают на несколько кадров для медленного вдоха.

**Слова автора:**

> Let's say we want this to be just a simple Idol we're going between two major sort of points exhale inhale I'm going to take all of the stuff that's above the hips and I'm going to shift it down one pixel so these are my two you know States I suppose and I'm going to give 10 frames for this like most of this stuff is like a holding so we can do it this way and I do prefer to do it this way just in case I want to do some more subtle sub pixel animations during these pauses right like if you look at this we've got one up and one down over five frames so the approaches we can take is we can try to modulate those slowly over the course so it's a slow exhale slow inhale over 10 frames or we can do like two or three frames either side so it's like inhale over three frames exhale over three frames and everything in the middle can just be kind of like either like repeated frames or you can even extend the duration of these frames now for my game I don't have any way of interpreting these durations so for me I'd have to then go into the engine and duplicate the frames or tolerate them being duplicated here I'm going to try to like just keep it really simple and a little bit of waste of data it's not a big issue I might even go to 12 frames actually.

**Для Напарника:** Дыхание кота: медленный цикл (4-7 с) с сдвигом на 1-2 px/scale 1-2%, большая часть цикла в удержании.


---

## 3. Сглаживай переходы: от центра к конечностям, промежуточный тон
`анимация · крафт · вкус` · [06:21](https://youtu.be/vs-ierVdE7I?t=381)

**Мысль:** Чтобы дыхание не дёргалось, начинай с груди и распространяй к краям; промежуточные серые пиксели делают переход мягким вместо резкого скачка всего сразу.

**Слова автора:**

> What I want to do is take this transition point and kind of smoothing it out a little bit in order to make this feel subtle right now it feels quite jarring because everything moves at once but I think what I can do is start with the core elements first and then animate kind of like extending outwards to the extremities so we can start with the chest and we can start bringing down parts of this so we could take maybe this part here and start descending that and start just smoothing a lot of this out and I might even bring some of this up and then feather out this so it's more of a sub pixel drop okay so this middle tone it's almost like the white is moving from white to gray to black or to the darker gray over three frames and it makes it feel a lot less a lot less jarring and we might even keep one of these here so it's this again feels like a transition because it's like three pixels moving to one pixel moving to no pixels on this line which also feels like a transition.

**Для Напарника:** Для SVG-кота анимировать части со сдвигом по фазе (корпус, затем хвост/уши), а не единым transform; мягкий opacity-переход.


---

## 4. Вторичное движение с задержкой и мягкая посадка в покой
`анимация · маскот · крафт · вкус` · [10:07](https://youtu.be/vs-ierVdE7I?t=607)

**Мысль:** Руки и волосы реагируют позже тела, а почти конечный кадр делают близким к финальному, чтобы не двигаться равномерно: «почти готово, потом готово» читается как отдых.

**Слова автора:**

> I want to do a little more secondary motion so when we start to shift down here what I'm going to do is have the hands respond a little bit later so I'm going to instead of dropping them down I'm going to move them out and let's have that happen a little further up and I want that to be a little more like delayed I want that to take a few more frames so we're just going to see what we can get away with here so then on this Frame we're going to include a little bit more transition maybe even flare this out slightly more just to give us a little more something and the same for the arms maybe we could even slightly shift some of this shoulder pad stuff around and I think this Frame it should be like as close as we can get it to the SEC to the last frame cuz I don't want it to feel like we're moving evenly I want it to feel like we're moving so it's like out almost finished and then finished so this here is probably a little too high cramp this down a little so it's like just getting it as close as we can to that last frame I think that makes it feel more of like a more of like a rest.

**Для Напарника:** Задержка и мягкая посадка на ease-out для реакций кота и искр костра: быстро вышел, плавно осел.


---

## 5. Силуэт неподвижен, дыхание лёгкое
`анимация · маскот · вкус` · [14:30](https://youtu.be/vs-ierVdE7I?t=870)

**Мысль:** Не двигай ноги ради реализма: сохрани силуэт и сдвинь только тень, потому что дыхание не должно быть тяжёлым.

**Слова автора:**

> With the legs I mean technically like you know we could make the knees bend a little bit here or there I'm more inclined to just shift this Shadow just a little bit keep the silhouette exactly as it is for the legs because I really don't want the breathing to be too heavy.

**Для Напарника:** Не двигать основу кота при idle, чтобы не отвлекать от текста и задачи пользователя.


---

## 6. Idle как удержание + периодический «вдох» по таймеру
`анимация · маскот · время · крафт` · [16:09](https://youtu.be/vs-ierVdE7I?t=969)

**Мысль:** Одно-кадровый idle держат произвольное время (1-2 с), затем проигрывают короткую анимацию дыхания и возвращаются, поэтому жизнь не повторяется механически.

**Слова автора:**

> Frame one and then call this a new tag idle and now we can sit here and then we can play this and then we can sit back here again for as long as we want and we can have the character breathe you know periodically or whatever we want to do in the script my animation system allows me to play a onef frame animation for as long as I want so I could say hold this for 2 seconds or hold this for 1 second and then play a breathe and then go back to the start and do the same thing again so in my engine I could do it this way.

**Для Напарника:** Реализация кота: статичный кадр, и через случайные интервалы короткие жесты (моргание, вдох); без жёсткого цикла.
