# Why the 60-30-10 Rule is RUINING Your UI Designs

**Канал:** Kole Jain · 6 мин · субтитры: en (авто YouTube) · https://youtu.be/66oOi9OLMCw

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. В продукте 60-30-10 не работает: нейтральный фундамент из слоёв
`цвет · дизайн-система · иерархия` · [00:10](https://youtu.be/66oOi9OLMCw?t=10)

**Мысль:** Vercel примерно 90% чёрный, 8% белый, 2% красный. Для продукта нужно четыре слоя фона, 1–2 обводки и три варианта текста.

**Слова автора:**

> Product design, things change. Take versel. It's like 90% black, 8% white, and 2% red, which sometimes isn't even there. In this video, I'm going to walk you through the four layers of color theory for product design, so by the end, you can create rich, interactive designs without any guesswork. Layer number one is our neutral foundation. So, let's talk backgrounds first. Linear uses 99% white. Notion is 100%. Versella is 98%. There is some variance, but nothing to say you can't use pure white. Now, for a landing page, 3 to five neutrals works great. But for a product design, you'll generally want four layers of backgrounds, at least one stroke, often two, and then about three text variants.

**Для Напарника:** Заложить в токены Напарника 4 слоя фона, 1–2 границы и 3 оттенка текста, а акцент оставить редким.


---

## 2. Цифры светлых тем: рамка ~85% белого, текст 11–20% белого, подтекст 30–40%; важнее кнопка, тем темнее
`цвет · иерархия · дизайн-система` · [00:53](https://youtu.be/66oOi9OLMCw?t=53)

**Мысль:** Боковая панель чуть темнее фона, чистый белый уместен для карточек, тонкая чёрная рамка плоха, лучше около 85% белого. Чем важнее кнопка, тем она темнее.

**Слова автора:**

> So, how do we choose all these colors? Let's start with the frame of your web app. This is a slightly darker anchor. For example, Mercury adds 2% blue to their sidebar. Because it's a pretty large element, it only needs to be very slightly darker, especially on light mode. As we add content to the dashboard, it's important to know that light mode is very flexible because we can have a dark background with lighter cards like Verscell or a light background with darker cards like Notion or monochromatic layers like Superbase. Darker cards are often the same color as your sidebar. And lighter cards can be pure white, which is a good reason not to have pure white as your background. Now, if I have cards on this background, it looks very washed out. It's only slightly better if I add a subtle drop shadow. You might reach for a thin black border. Don't. Instead, use roughly 85% white to define the edge, but not overpower it. Another great rule is the more important a button is, the darker it is. That goes for ghost buttons all the way to black buttons with white text. and everything else within that range. Though most multi-purpose buttons sit around 90 to 95% white. Finally, text. The darkest colors are reserved for important headings, but even those are still about 11% white. The majority of your text should fall around 15 to 20% white and subtext around 30 to 40%.

**Для Напарника:** Цифры можно инвертировать для тёмной темы Напарника, сверяя с замеренным контрастом.


---

## 3. Акцент как шкала: основной 500–600, hover 700, ссылка 400–500
`цвет · дизайн-система` · [02:11](https://youtu.be/66oOi9OLMCw?t=131)

**Мысль:** Акцентный цвет проектируется как шкала от светлого до тёмного, а не как одно значение, и роли состояний привязываются к ступеням.

**Слова автора:**

> Don't think of your color as a single color. Rather, think of it as a scale from the lightest version of it to the darkest. You'll really only use the 500 or 600 as your main color, but a hover would step up to a 700, and a link might be 400 or 500.

**Для Напарника:** Описать акцент Напарника ступенями и привязать hover/pressed к соседним ступеням шкалы.


---

## 4. Тёмная тема: удвой дистанцию между слоями; поднятое становится светлее
`цвет · тёмная-тема · иерархия` · [03:29](https://youtu.be/66oOi9OLMCw?t=209)

**Мысль:** Тёмные цвета похожи друг на друга, поэтому между слоями нужно 4–6% вместо 2%. Поверхности светлеют по мере подъёма, поэтому поднятая карточка получает светлый цвет или границу.

**Слова автора:**

> Dark colors look more similar, so they require more distance to look as different as lighter colors. That's a bit of a mouthful, but if you just reflect your light palette, the background elements will lose all of their distinction. So, a good rule of thumb is double the distance. Most of our light colors have distances of about 2% white between them. So, on dark mode, we'll want four to 6% between those colors. Stretching out our color palette with that rule results in actually a pretty reasonable design. Now for the main color, once again, we can break out the color ramp to choose a 300 or 400 as our primary brand color on dark mode with hover being a 400 or 500. You'll also need to dim the text and brighten any borders. And if you stare at this screen all day, you'll definitely start to notice the difference. Now, where light mode was more flexible, dark mode is not. Surfaces always get lighter as they elevate. So any raised cards need to have a lighter color or just a border like the search bar.

**Для Напарника:** Для слоёв над AppBackdrop использовать шаг светлоты побольше, но не выходя из коридора 0.152–0.172 для самого фона.


---

## 5. Семантические цвета нарушают систему ради смысла; деструктив это красный
`цвет · доверие · этика` · [04:33](https://youtu.be/66oOi9OLMCw?t=273)

**Мысль:** Даже у чёрно-белого бренда статусы билдов различаются цветом. Делать деструктивное действие не красным это ошибка дизайна.

**Слова автора:**

> Colors convey meaning, and because of that, we have to break the system that we've built. Versel understands this. So, even with a brand color of black and white, you can tell which builds are successful, failed, or in progress. Even if your brand color is purple, it's pretty much a design sin to make destructive actions anything other than red.

**Для Напарника:** Применять с оговоркой: красный для сброса данных, а не для обычных промахов, чтобы сохранить отсутствие стыда.


---

## 6. OKLCH даёт одинаковую воспринимаемую яркость у разных оттенков
`цвет · крафт · дизайн-система` · [05:07](https://youtu.be/66oOi9OLMCw?t=307)

**Мысль:** Зелёный кажется неоновее синего, и OKLCH с фиксированными светлотой и хромой позволяет получить спектр одного тона.

**Слова автора:**

> Ever notice how bright green seems so much more neon than bright blue? There's a whole bunch of very interesting science behind that which I won't get into today. But we need some way to get the same tone of color across the entire spectrum. And the solution is the OKLCH palette, which depends on human perception of color. Meaning, we can get the same perceived brightness across different colors.

**Для Напарника:** Цвета ориентиров острова задавать в oklch с одинаковой светлотой, чтобы ни один не выпирал.


---

## 7. Тематизация: сдвиг светлоты и хромы нейтралей в OKLCH и смена оттенка
`цвет · дизайн-система · процесс` · [05:31](https://youtu.be/66oOi9OLMCw?t=331)

**Мысль:** Для каждого нейтрала немного опускают светлоту и поднимают хрому, затем меняют оттенок и получают согласованную тему.

**Слова автора:**

> Last but not least, layer four, theming. If you want to convert any of your designs into a color themed version, it's actually a lot easier than you think. You could take all of your neutrals and guess, but this is where the okay LCH color system becomes super useful. For every neutral you have, plug in the hex value and drop the lightness by 003 and increase the chroma by 0.02. And then just adjust the hue to get any themed output. This means you can theme any design to red, green, blue. bang on the money every single time.

**Для Напарника:** Часовые SKY-палитры можно получать из нейтралей смещением оттенка и хромы при фиксированной светлоте.
