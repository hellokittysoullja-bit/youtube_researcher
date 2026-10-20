# How to do Basic Animation from a beginner to a beginner

**Канал:** Bluebiscuits · 16 мин · субтитры: en (авто YouTube) · https://youtu.be/Al_k9hmd4ws

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. В анимации цель — движение, а не идеальный кадр
`анимация · крафт · процесс` · [00:57](https://youtu.be/Al_k9hmd4ws?t=57)

**Мысль:** Анимация это другой способ видеть искусство: простые формы, без идеальных кадров, главное — чтобы двигалось.

**Слова автора:**

> The first thing you have to do is let go of what you know about drawing like illustrations. Animation is a whole other way of seeing art. Try not to follow the rules you'd use for an illustration. Don't think about making every single frame look perfect or adding maximum exaggeration and shedding. It's literally about making it as easy as possible with the simplest shapes. Movement is the goal, not the masterpiece.

**Для Напарника:** При анимации кота и острова начинать с простых форм и ритма; не полировать статичные кадры, пока движение не ощущается живым.


---

## 2. Планируй по ключевым кадрам: старт и конец, потом промежуточные
`анимация · крафт · процесс` · [02:47](https://youtu.be/Al_k9hmd4ws?t=167)

**Мысль:** Сначала фиксируешь начальную и конечную позу, затем добавляешь промежуточные кадры, которые делают движение плавным. Можно взять лишь один кадр рядом со стартом и один рядом с концом.

**Слова автора:**

> The simplest way to plan is by focusing on the start frame and the end frame. This is the main movement you want your character or object to be in. Get those two perfect and then you add the in-betweens to smooth everything out. This makes it much easier to plan out. My animations will look something like this. start and end frame planned out and then I go in and add the inbetweens. The in-betweens are the frames that allow the animation to actually move. So, it will look a bit choppy and then it won't. I'm pretty lazy, so I usually just do one frame like slightly off the start and then closer to the end frame. I don't really do the ones in the middle cuz I think this works just fine.

**Для Напарника:** Анимации кота (проснулся, подпрыгнул) задавать двумя позами, а плавность добавлять easing-ом в CSS/Framer Motion, а не набором промежуточных кадров.


---

## 3. Подсчёт кадров: смешивай удержания 2-3-4 для ease in/out
`анимация · время · крафт` · [03:31](https://youtu.be/Al_k9hmd4ws?t=211)

**Мысль:** Анимация на единицах плавна, но дорога; на двойках она равномерна. Смешивание двоек, троек и четвёрок по таймлайну даёт быстро-медленно-быстро, то есть замедление в начале и конце.

**Слова автора:**

> Frame counting. So, how many like of these like frames that you see here or in between each drawing? Apparently, it's very important. I didn't even know this was a thing when I first started, but it makes a huge difference. My animation before was very choppy and I couldn't figure out why, but frame counting makes it run a lot smoother. You've probably seen this little graph that animators use and this is basically how they count frames. So the frames will be very close at the start and then very close at the end. It's basically how they do it. Counting also has to do with the frame rate. So you've probably seen like 24 frames per second, 12 frames per second. This is this is what this means. So you can animate on ones which means every frame you're adding an animation cell which it look really smooth but it's also really time consuming. You can animate on twos. This means that every drawing is held for two frames. So drawing frame drawing frame drawing frame. This makes the movement a lot smoother and uniform and it's the most popular one that people use. You can also do on threes and then on fours. but the further you go like the more choppier it gets. Now that you understand counting, you're supposed to mix them in between a single like timeline. So you can go twos, threes, fours, twos. So that would look something like this. I've held on the two frames, then I did a three frame, four frame, and then two frames. And if I play it, it's going to go fast, slow, fast. like the movement will be it will ease in and ease out.

**Для Напарника:** Для анимаций Напарника использовать ease-in-out, а не linear; движение с ускорением и замедлением выглядит живым.


---

## 4. Учись, разбирая чужую анимацию покадрово и считая кадры
`анимация · крафт · процесс · исследования` · [05:21](https://youtu.be/Al_k9hmd4ws?t=321)

**Мысль:** Замедление работ мастеров и подсчёт использованных кадров быстро объясняет, как строить тайминг.

**Слова автора:**

> What really helped me grasp when to use it is to go frame by frame on animations I like and then count the frames that this animator has used. It's completely unlock something in my brain and really helps me like visualize what I'm supposed to be doing. I slowed down Minbits animations on YouTube. They're really cool and she uses like really fastpaced animations. I highly recommend trying this. If you're using YouTube, you can use the comma and the dot key to go frame by frame on a video. H and then you can count. I know counting isn't that interesting, but it's very important.

**Для Напарника:** Перед созданием анимации кота замедлять эталонные анимации (нужный характер) и считать мс фаз, чтобы переносить в тайминги.


---

## 5. Круговые траектории и сжатие/растяжение
`анимация · вкус · крафт` · [06:26](https://youtu.be/Al_k9hmd4ws?t=386)

**Мысль:** Движущиеся части выглядят естественнее по кривой, а не по прямой. Падает — сплющивается, взлетает — растягивается; преувеличение приятно глазу.

**Слова автора:**

> Animators really love their circles. Parts that will move look more natural and animated if they follow a circular movement. The path of the object flows should not be a straight line, but should always be curved in a way. I don't know, it just looks nice. I saw a lot of animators do this, so this is what I picked up from them. So, everything in a circle. I normally just have the frames loosely follow circle. I don't normally like plan out the circle too much. just as long as there's like a slight movement. This is where the liquify tool comes in handy. Again, when anything is moving, you want to overexaggerate it to make it look pleasing to the eye. These in between frames should be squished and stretched. So, if something is falling down, squish it. If it's taking off, stretch it. When it lands, you can stretch it as well. I just use the liquify tool to do this because I am lazy. It looks cool. And there's probably some logic behind it, but I haven't really figured it out. It just kind of works.

**Для Напарника:** Движения кота и частиц у костра по дугам, лёгкий squash & stretch на прыжках; не прямые линейные перемещения.


---

## 6. Покой, замах назад и отскок: дешёвые приёмы оживления
`анимация · маскот · персонаж · крафт` · [07:35](https://youtu.be/Al_k9hmd4ws?t=455)

**Мысль:** После движения держи позу 1-2 кадра для покоя; перед движением чуть оттяни персонажа назад (anticipation); перед финальной позой добавь небольшой подскок. Это делает персонаж живым.

**Слова автора:**

> After you're done a movement, add one or two frames where the character or object is in the same position to allow it to rest. I do this on ones or twos behind the last frame of the animation. I don't know why this works, but it just looks so much cooler. you're supposed to redraw it, but I just use the liquify tool to scooch it up just even slightly. So then that's the rest. But redrawing the frame again looks way cooler. This is the same trick. At the start of something moving, I will pull it back in the opposite direction of the actual movement. Just like one single frame, count it a one or two, ever so slightly squish it and then allow it to play. It does like this little like pull back and release. I don't know. It looks cool. The simple little bounce. This is the same principle as the squish and stretch. I think a lot of people do this cuz it's like the easiest way to make a character like lively. For a small movement in the frames just before the final position, I shift the object up a little bit so it like bounces. It will look like the character is bouncing or reacting. It's cool for when you're changing an expression or making a small movement or having the character make a sound.

**Для Напарника:** Для реакций кота: короткий замах перед прыжком, лёгкий отскок при смене выражения или реплике.


---

## 7. Самое полезное: замедлять и изучать чужие работы и просто начать
`процесс · крафт` · [09:01](https://youtu.be/Al_k9hmd4ws?t=541)

**Мысль:** Изучение работ других плюс практика сняли страх перед анимацией; после старта оказалось не так страшно.

**Слова автора:**

> Think slowing down and studying other people's work has helped the most along with just practicing because once I got started, I realized it wasn't as scary as I thought it was.

**Для Напарника:** Принцип запуска применим и к пользователю: страшно только до первого шага; формулировать первый шаг очень маленьким.
