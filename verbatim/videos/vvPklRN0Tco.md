# The Easy Way to Pick UI Colors

**Канал:** Sajid · 9 мин · субтитры: en (авто YouTube) · https://youtu.be/vvPklRN0Tco

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Три группы цвета достаточно: нейтральные, бренд, семантические
`цвет · дизайн-система · процесс` · [00:12](https://youtu.be/vvPklRN0Tco?t=12)

**Мысль:** Сложность цвета в том, чтобы вовремя остановиться. Нейтральные для фона, текста и границ, основной для главных действий, семантические для состояний.

**Слова автора:**

> The tricky bit is knowing when to stop playing and just pick something that works. Here's what actually works. Neutral colors for background, text, borders, and a lot of other elements. the brand or primary color for main actions and to add a bit of character. And finally, maybe some semantic colors to communicate different states. These are all the colors you'll ever need to design apps and UIs.

**Для Напарника:** Ограничить палитру Напарника тремя группами, а новый цвет добавлять только при реальной смысловой необходимости.


---

## 2. HSL вместо hex: оттенки считаются изменением одного параметра
`цвет · крафт · дизайн-система` · [00:45](https://youtu.be/vvPklRN0Tco?t=45)

**Мысль:** Hex у трёх похожих серых выглядят непохоже, а в HSL оттенок, насыщенность и светлота понятны. Меняя только светлоту, получаешь гармоничные оттенки без угадывания.

**Слова автора:**

> To create shades, you need to pick the right color format. Most people are familiar with hex and RGB color values, but they are the worst when it comes to creating a color palette. Like these three shades of gray we have for our background colors. They look very similar visually, but the code doesn't. Now compare that with a more intuitive color format, and the code actually makes sense. You have hue or the actual color on the color wheel that goes from 0 to 360. Then the saturation, which goes from 0 to 100, controls the intensity of that color. In our case, we have set it to zero. That means no matter what color you choose for the hue, it's always going to be neutral. And finally, we use the lightness value to create a bunch of shades. Simple and easy math to create a harmonic palette without any guesswork.

**Для Напарника:** Оттенки неба по часам суток строить в oklch, меняя оттенок и насыщенность при фиксированной светлоте в коридоре 0.152–0.172.


---

## 3. Поверхности светлеют по важности; заголовок не 100% белый
`цвет · иерархия · доступность` · [01:53](https://youtu.be/vvPklRN0Tco?t=113)

**Мысль:** Чем светлее элемент, тем он ближе к пользователю, поэтому светлота резервируется для важного. Заголовкам чистая белизна даёт слишком резкий контраст, остальному тексту нужен приглушённый оттенок.

**Слова автора:**

> With hue and saturation both set to zero, we will start with 0% lightness for our base color. Then 5% for the next shade that can be used for cards and other surface elements, and finally 10% to highlight the most important or raised elements. The lighter elements appear on top and feel closer to the user. So obviously only use them for important stuff. Same thing with text. Keep a sharper and high contrast color for headings and important elements and use a slightly muted shade for the rest. Still legible, just not in your face all the time. That's why we don't use 100% lightness for the headings. It would look too harsh on the eyes.

**Для Напарника:** Текст на тёмном фоне Напарника делать не чисто белым, а чуть приглушённым, и поднимать светлоту поверхности только у важных карточек.


---

## 4. Светлая тема: вычесть светлоту из 100 и подправить глазами; имена токенов нейтральны
`цвет · дизайн-система · процесс` · [02:37](https://youtu.be/vvPklRN0Tco?t=157)

**Мысль:** Инверсия даёт стартовую точку, а глаз корректирует: свет обычно сверху, поэтому верхний элемент самый светлый. Токены лучше называть так, чтобы имя работало для обеих тем.

**Слова автора:**

> Start by subtracting the lightness value by 100. That'll give you a good starting point. Then we'll use our eyes and some common sense to adjust the values manually. For example, why does the top element have the darkest color? Light usually comes from the top, so it should be the lightest and the base color should be the darkest. That's why I name my background colors as BG dark or BG light. So BG dark will be the darkest and BG light will be the lightest shade, whether it's dark or light mode. But we can't do that with text colors. So use names that make sense for both cases.

**Для Напарника:** Токены дизайн-системы называть по роли, не по цвету, на случай светлой темы.


---

## 5. Градиент карточки и светлая верхняя граница имитируют свет сверху
`цвет · вкус · крафт` · [05:33](https://youtu.be/vvPklRN0Tco?t=333)

**Мысль:** Лёгкий градиент из фоновых цветов и более светлая верхняя граница создают ощущение света, падающего сверху, без лишнего декора.

**Слова автора:**

> The border should be clearly visible but not too distracting. Then create a simple gradient using our background colors. If it feels too distracting, we can tweak it a bit and reveal the full gradient on hover. This way, it looks shiny on top, like the light is coming from above. To really sell this effect, we can use a lighter color for the top border.

**Для Напарника:** Карточки поверх AppBackdrop могут получить тонкую светлую верхнюю кромку как отсылку к небу и свету очага.


---

## 6. Тень: смешивай тёмную короткую и светлую длинную
`крафт · вкус · иерархия` · [06:39](https://youtu.be/vvPklRN0Tco?t=399)

**Мысль:** Две тени разной длины и прозрачности выглядят реалистичнее одной, а прозрачность задаётся альфа-каналом.

**Слова автора:**

> And finally, let's add a nice shadow to create some depth because where there's light, there's a shadow. Shadows need some transparency, so you'll need to use an alpha value that goes from 0 to one. Always mix a darker and shorter shadow with a lighter and longer one to achieve a more realistic effect.

**Для Напарника:** Для поднятых карточек и модалок использовать двухслойную тень с низкой альфой.


---

## 7. OKLCH: светлота, хрома и оттенок; шаги выглядят естественнее, чем в HSL
`цвет · крафт · дизайн-система` · [07:45](https://youtu.be/vvPklRN0Tco?t=465)

**Мысль:** В UI хроме редко нужно больше 0.15–0.2. В HSL тёмные и светлые оттенки теряют насыщенность, в LCH и OKLCH приращения равномернее, и Tailwind v4 перешёл на OKLCH.

**Слова автора:**

> Just look at LCH. L and H are lightness and hue, which you already know from HSL. C stands for chroma, which is kind of like saturation, but instead of going from zero to 100, it goes from 0 to 4. And for UI work, you rarely need more than.15 or 2. As I said in the beginning, colors are one of those things where the more you learn, the more you realize how much you didn't know, and it gets complicated real fast. Hue is the same as before, 0 to 360. Chroma goes from 0 to 02 and lightness goes from 0 to 1. Actually, LCH is a color format on its own. OKLCH is the newer and better version of it. With the V4 update, Tailwind has also switched to OKLCH as the default color format. So, let's compare these three color formats and see how they differ. With HSL, the biggest issue is how it handles lightness. The dark and light shades lose all saturation. with LCH and OKLCH, the increments look way more natural.

**Для Напарника:** Подтверждает использование oklch для SKY: светлоту можно держать в коридоре, а оттенок и хрому менять независимо.
