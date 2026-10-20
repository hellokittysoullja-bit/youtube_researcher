# The secrets to good Pixel Art animation! (Animation tutorial)

**Канал:** Pixel Overload · 6 мин · субтитры: en (ручные) · https://youtu.be/J1sFBDQt8J0

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. 12 fps: скорость = пикселей между кадрами; кадр короче, чем кажется
`анимация · время · крафт` · [00:51](https://youtu.be/J1sFBDQt8J0?t=51)

**Мысль:** 12 кадров/с (анимация «на двойках») сочетает объём работы и плавность; скорость определяется смещением между кадрами, а кадр виден меньше, чем пока его рисуешь.

**Слова автора:**

> Standard television is around 24 frames a second. So one of the most common frame rates for animating pixel art is 12 frames a second. Which, you’ll notice, is half the speed of 24. People like to refer to animating on every second frame as ‘Animating on Twos’. For beginners, and even pros, I think 12 frames a second is a fantastic choice, because the more frames you have means more work, but less frames can be less smooth, and 12 frames a second walks that line perfectly. But how do we draw when we want to make these adjustments to every frame across this 12 fps animation? Well here’s the simple concept: the number of pixels moved between frames determines the speed. Cause, you know? Speed equals distance divided by time. Also be mindful of how long a frame will be displayed. It’s usually shorter than you think because you’ll spend longer looking at it while you draw. And for us on 12 fps, it’ll be a twelfth of a second.

**Для Напарника:** Для покадровых спрайтов кота и костра использовать 12 fps как рабочую частоту.


---

## 2. Планируй движение отдельно от эстетики: простые формы и скелет
`анимация · процесс · крафт` · [01:43](https://youtu.be/J1sFBDQt8J0?t=103)

**Мысль:** Анимация — это движение, а не свет и характер. Сначала упрощённые формы и цепочки точек для ткани, потом возвращаешь «кожу». Это даёт лучший результат вдвое быстрее.

**Слова автора:**

> It’s one of those things that no-one likes to do, but it really enables you to create much better animations in half the time. Don’t get me wrong, I never liked to plan out the movement for my animations, until I realised how useful it was. It’s so easy to get lost trying to create animations from a static sprite by shifting pieces around and playing with individual pixels. But this often results in an awkward animation. Animation isn’t about the lighting or the character. Animation is about movement. We need to separate the aesthetic of the static image from its movement and focus only on that movement. Once we have the really nice foundation of good movement, we can begin to put the ‘skin’ back on the character. Instead of investing time and energy into polishing every frame as we go, the best way is to simplify the subject into its most primitive shapes, and make these shapes move fluidly. For a humanoid character, that would be a different coloured shape for each limb. For fabric or cloth, create a chain of dots with delayed reactions to the movement of the dots above. Each segment reacts like links in a chain, but once you average out the movement with a curved line, it can be used for anything organic. So it’s kind of like drawing the skeleton of your character.

**Для Напарника:** Для анимации кота и пламени сначала делать грубые примитивы с правильным движением, затем детализировать.


---

## 3. Нарисуй линию траектории: тогда думаешь только о скорости
`анимация · процесс · крафт` · [02:48](https://youtu.be/J1sFBDQt8J0?t=168)

**Мысль:** Быстро набросанная линия пути убирает половину вопросов и спасает от переделки анимации с нуля.

**Слова автора:**

> Sometimes, you want an object to jump or fall. Probably one the most overused cliches of animation tutorials (besides the slime) is the bouncing ball. They always show a curved parabola to demonstrate the path of the ball. I never saw myself actually drawing this line for an animation, but it’s just one of those planning things that really helps improve the final product and, more importantly, ease the process. I would 100% recommend drawing a quick line for the path of your animation. Because then you only have to think about the object’s speed and not the path. I think I’ve said enough about planning. Yes, it can be a pain but it’s a much better alternative to having to start a high-fidelity animation all over again from scratch.

**Для Напарника:** Для полёта искр, прыжка кота или появления ориентира задавать путь заранее (SVG-path/motion-path), а динамику настраивать отдельно.


---

## 4. Смазывание, замах и вторичная анимация продают удар
`анимация · вкус · крафт` · [03:26](https://youtu.be/J1sFBDQt8J0?t=206)

**Мысль:** Меньше кадров для быстрого движения, смаз заменяет motion blur, замах перед резким движением и реакция окружения (причина и следствие) придают весомость.

**Слова автора:**

> Here are some quick tips to improve your actual animation and movement. Because I haven’t really talked about how to improve your motion yet. For a weapon attack, a common mistake is to depict every single frame. You can see as this axe is swung, there are five unique frames as it’s held at different angles. The point is, sometimes you want Impact. To make your movement nice and crunchy, don’t worry about drawing so many frames. Just do a couple. If something is moving that fast, it won’t be on-screen for very long. Of course, this can look choppy, so a remedy for fewer frames is a technique called smearing. Smearing acts like motion blur does in real footage by stretching the object into a blotch of colour that signifies direction. This shape tells us both the speed and the direction the subject is moving. Like a lot of things, smearing is good in moderation. Before a drastic movement, winding up or providing some anticipation frames can be a super nice touch. You can hold these frames for as long as you want. Something else that also sells impact is secondary animation. Secondary animation is where things in your world react to the primary movement. Think of it like cause and effect. If a heavy thing is dropped here, these lighter things might jump up because of it.

**Для Напарника:** Когда кот реагирует (находка, реплика), реакцию окружения (искры, листья, лёгкое сияние) запускать вторично; замах перед прыжком.


---

## 5. Ease in/out: сжимай расстояния в начале и конце движения
`анимация · время · крафт` · [04:36](https://youtu.be/J1sFBDQt8J0?t=276)

**Мысль:** Если убрать одну вещь из видео, то easing: малый шаг в начале и конце и большой в середине создают ускорение и замедление, которые выглядят живо.

**Слова автора:**

> If there’s one thing to take away from this video it would be easing in and out. To ease in and out, exponentially decrease the distance your sprite moves for the start and end of its movement. This will make it accelerate and decelerate, and therefore feel more lifelike. Like we said before, the commonl rule is that the distance between frames will determine the speed, so the way you arrange these distances will influence your object's acceleration. Compress your distances so it moves 1 or 2 pixels at the start and 8 or 9 in the middle.

**Для Напарника:** Все переходы Напарника: ease-in-out вместо linear, особенно для медленных циклов фона (7–23 с).


---

## 6. Овершут и преувеличение делают движение живым
`анимация · персонаж · вкус` · [05:49](https://youtu.be/J1sFBDQt8J0?t=349)

**Мысль:** Лёгкий перелёт позиции оживляет даже неодушевлённое; новички боятся больших движений, но крупное преувеличенное движение читается лучше, чем смещение на один пиксель.

**Слова автора:**

> Overshooting is when your subject goes just that little bit too far with their movement. It can help to make your subject more animated or lively. Nonetheless, a nice technique to have in your toolbox. And remember it can be used for animating inanimate objects. Another thing that I’ve seen beginners do, and something that I’ve done myself, is to restrict a character’s movement and to not go very big with the swings and walks. Always go for over-exaggerated, bigger movements. It takes time and planning, but it’s much better than a walk cycle with only a one-pixel shift in the legs.

**Для Напарника:** Пружинные переходы (spring с небольшим overshoot) для появления ориентира и реакции кота; движения заметны, но не резки.
