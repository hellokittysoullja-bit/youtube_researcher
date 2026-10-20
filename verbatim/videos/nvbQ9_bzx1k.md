# How to MAKE YOUR GAME LOOK GOOD!

**Канал:** Brackeys · 13 мин · субтитры: en (ручные) · https://youtu.be/nvbQ9_bzx1k

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Фокальный элемент: контраст должен быть у одного, а не у всех
`иерархия · внимание · цвет · крафт` · [03:21](https://youtu.be/nvbQ9_bzx1k?t=201)

**Мысль:** Если контраст, насыщенность и размер применены ко всему, ничего не выделяется. Приглушив окружение, автор сразу делает героя точкой притяжения взгляда.

**Слова автора:**

> So at this point, it's a good idea to ask ourselves which part of the scene is most important and should be the thing the player sees first. In this case, I would probably say the player character. So let's try making that a focal element. Now there's a few ways of making something a focal element. Some direct influences of focus are high contrast, saturation, size and movement. This of course only works if one of few elements have these. At the moment, there is a lot of contrast in the scene, but it applies to everything. So nothing really stands out. Let's fix that. I will go ahead and make the environment, the coins and the bug stack, to tone down the overall contrast of the scene. And just like that, it looks a lot better and your eye is immediately drawn towards the player. And make him a bit bigger to emphasise the effect even more,.

**Для Напарника:** На экране Фокуса один главный элемент (таймер/кот) должен быть самым контрастным, а остальное приглушено.


---

## 2. Свет ведёт игрока, а движение показывает, что объект интерактивен
`внимание · анимация · иерархия · игровой-дизайн` · [05:00](https://youtu.be/nvbQ9_bzx1k?t=300)

**Мысль:** Игроки идут к свету, а на статичной сцене любое медленное движение сразу маркирует интерактивные предметы. Свет рассказывает маленькую историю о том, откуда он падает.

**Слова автора:**

> Let's try adding some lighting to the scene. I find that when working with lighting, it helps if I think of it like I'm creating a narrative. In this case, we could imagine that we just wandered into this cave, and now some light is spilling in from the entrance. So I'll add light that shines some light from the entrance onto the box. But the scene still feels a bit unbalanced. There's a lot going on the left side with the contrast and lighting. So I'll add a dim light on the right to balance things out a bit. This also guides the player towards the exit of the level. And this is definitely a key takeaway. Players always go towards the light. Of course, right now the coins are looking a bit off. At first glance, you might not even realise that there are coins you can pick up. So let's fix that. As I mentioned earlier, movement has a huge influence on focus, especially when everything else is static like in the scene. So I've gone ahead and made this little script that makes the coins float up and down. And just like that, they clearly stand out as something you can interact with.

**Для Напарника:** На острове и у костра в AppBackdrop интерактивные находки можно мягко подсвечивать и слегка покачивать (медленно, по правилам диегетичности), чтобы они читались как «можно взять».


---

## 3. Гармонии цвета: аналоговая, монохром, триада, комплементарная
`цвет · вкус` · [06:50](https://youtu.be/nvbQ9_bzx1k?t=410)

**Мысль:** Аналоговые цвета безопасны для глаз, монохром спокоен, но тогда форма и движение несут больше работы. Комплементарные цвета дают контраст, и если использовать их поровну, получается неприятная картинка.

**Слова автора:**

> Using this colour harmony ensures a common palette that is easy on the eyes. I've tried a few combinations using this, but I don't really think it fit. Next up is monochromatic. This works quite well for a minimalistic game like mine. This also creates a calm image, which means that when using this, other factors such as shape and movement becomes much more important in order to balance the image. As you can see, this works pretty well, but I want more colours, which leads us to the next one, triad. Here you get three colours that are equally distance on the wheel. This creates a strong and colourful image. It can be a bit hard to control but when it works, it really works. Complimentary is the most commonly used because it works so well. As the name suggests, the colours complement each other because they are on opposite sides of the colour wheel more simultaneously bringing a lot of contrast to the image. However, using the two colours equally, often creates an unpleasant image with too much contrast. So choose one and use the other sparingly.

**Для Напарника:** Для неба и очага в AppBackdrop держать один доминирующий оттенок, а комплементарный (тёплый огонь на холодном фоне) использовать только как акцент.


---

## 4. Лёгкая виньетка и оживление персонажа улучшают ощущение без изменений механики
`анимация · крафт · вкус · маскот` · [08:45](https://youtu.be/nvbQ9_bzx1k?t=525)

**Мысль:** Незаметная виньетка собирает картинку, лёгкий наклон героя по направлению движения делает его живым. Игра ощущается более плавной, хотя управление не менялось.

**Слова автора:**

> First I'll add a vignette post processing effect to darken the edges of the screen. This is subtle enough that most people won't notice but it really helps tie everything together. Of course if you want to learn more about post-processing which can be a huge step in making a game look good, we've created an entire video, on all the effects in the new post-processing stack. As always, link for that in the description. Also add some lights to the coins to make them glow a bit. Again, really subtle but very effective. And I think the character movement is looking a bit stiff compared to the floaty coins. So I'll add some animation to him as well. I've made a little script that makes the player body lean towards the direction of movement. It's very simple, but it really helps the character feel more alive. Also add a simple jumping animation. And just like that, our character looks much better and somehow feels smoother to control even though we didn't change the movement at all.

**Для Напарника:** Кот-напарник в MascotSvg может едва заметно «подаваться» к действию пользователя (наклон к полю ввода), но без правок общего компонента ради одного экрана.


---

## 5. Контровой свет противоположного оттенка отделяет объекты от фона
`цвет · вкус · крафт` · [10:24](https://youtu.be/nvbQ9_bzx1k?t=624)

**Мысль:** Тени уходят в фон, если нет противоположного света. Холодная подсветка сзади против тёплого основного света возвращает форму.

**Слова автора:**

> In general, if we want to add drama to a scene, show more shadows. Now the parts that are in the sun look great, but everything in the shadow just kind of fades into the background. A great trick to counteract this is to use a rim or backlight coming from the opposite direction of our main light source. In our case, the sun. So I'll add another light with a more blue or purple tint to make our environment pop against the background.

**Для Напарника:** Силуэты ориентиров острова на тёмном фоне можно отделять тонкой холодной кромкой, не меняя светлоту фона из коридора 0.152–0.172.
