# How I make UI color palettes

**Канал:** UX Tools · 8 мин · субтитры: en (ручные) · https://youtu.be/yYwEnLYT55c

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Три категории цвета в UI: бренд, поддерживающие, нейтральные
`цвет · дизайн-система` · [00:12](https://youtu.be/yYwEnLYT55c?t=12)

**Мысль:** Бренд даёт ощущение продукта, поддерживающие цвета несут статусы, а большая часть интерфейса состоит из нейтральных. Синий Facebook делает приложение «синим», хотя оно почти серое.

**Слова автора:**

> Almost all UI color palettes have just three categories of colors brand colors supporting colors and neutrals brand colors come from the business you'll have one maybe two brand colors that you'll be working with and you'll kind of use them throughout the UI as splashes of color and it will determine what the feel of the site is a good example of this is Facebook's blue which makes their app feel blue even though it's mostly Grace you'll use brand colors on things like buttons links navigation and icons supporting colors are used throughout the interface in key places where you need to draw attention or communicate something to the user using Color these will be used less often than brand colors you'll only see them in certain places like error messages or confirmations or informational dialogues most of your app is going to be made up of colors from the neutrals category because almost everything in a UI is some form of gray think text backgrounds border colors and secondary buttons.

**Для Напарника:** В дизайн-системе Напарника держать тёплый акцент редким, а основную поверхность строить на нейтральных ночных тонах.


---

## 2. Для палитры используй HSB, а не hex или RGB
`цвет · крафт · процесс` · [02:36](https://youtu.be/yYwEnLYT55c?t=156)

**Мысль:** HSB даёт понятный контроль над оттенком, насыщенностью и яркостью, а значит, палитру проще строить систематически.

**Слова автора:**

> Most design programs will default to using hex values for colors but when making a color palette you should use HSB instead of hex or RGB the H in HSB stands for Hue which is the color it's a number from 1 to 365 which makes sense because it goes all the way around the color wheel s stands for saturation which is how intense the color is on a scale from 0 to 100 and b stands for brightness which means how much black or white you're adding to the color again on a scale from zero to a hundred HSB will give us much finer control over our colors in a more understandable way.

**Для Напарника:** Палитру ориентиров и неба в oklch строить так же систематически: менять один параметр за раз.


---

## 3. Четыре статусных цвета, держащихся рядом с базовым по S и B
`цвет · дизайн-система · доверие` · [03:22](https://youtu.be/yYwEnLYT55c?t=202)

**Мысль:** Успех, предупреждение, опасность и информация должны быть в пределах 5–10 единиц насыщенности и яркости от базового цвета, иначе UI выглядит разорванным.

**Слова автора:**

> I like to have at least the following four colors in a UI green for Success messages or other positive confirmations orange or yellow for warnings red for dangerous situations like a form error and blue for neutral informational messages supporting colors need to feel like they go along with your brand color a really simple example of this is if your brand color is really saturated and your supporting colors are really desaturated the UI might end up feeling a little odd or disconnected to avoid this just pay attention to your HSB numbers make sure saturation and brightness stay close to your base color I like to keep it within 5 or 10 away then you can adjust the Hue however you want.

**Для Напарника:** Статусные оттенки в голосе напарника (ошибки, подтверждения) делать мягкими и родственными основному тёплому цвету, без кричащего красного. Toast не применимо.


---

## 4. Шкала из 9 оттенков 100–900 по диагонали палитры
`цвет · дизайн-система · процесс` · [04:21](https://youtu.be/yYwEnLYT55c?t=261)

**Мысль:** Берётся базовый цвет как 500, самый тёмный и самый светлый края, затем серединные точки по дуге от верхнего левого до нижнего правого угла пикера. Тёмный оттенок идёт на текст, светлый на тонированный фон.

**Слова автора:**

> Our colors are going to be used in all kinds of different places throughout the UI so we're going to need more than just a dark medium and light we'll probably want five to ten Shades so here's the process I like to follow layout nine blocks nine is a good number because it's easy to divide up as you'll see in a minute label them 100 to 900 and we use hundreds like this in part two allow us to easily add half steps later if we want but the color you've already chosen in the middle spot at 500 so let's start with our brand purple now we're going to start picking Shades but here is the trick for finding them imagine a line that starts at the top left corner of the Color Picker and goes to the bottom right corner passing through your base color the secret is to pick your Shades along this Arc the first Shades we're going to be picking are the lightest and darkest Shades out at the ends if you need a starting point try a dark shade around 90 to 100 saturation and 20 to 30 brightness and a light shade around 5 to 10 saturation and 95 to 100 brightness but also think about where it's going to be used the darkest shade of a color is usually used for text and your lightest shade will probably be used for a tinted background an alert component is a good example that combines both of these use cases so it can be a great place to pick these colors now we have two gaps let's pick the colors right in the middle of the gaps at 300 and 700 our lightest shade is here on the Color Picker and our 500 shade is here so let's pick this middle point between them on the arc for 300 and we'll do the same for 700.

**Для Напарника:** Построить для акцента Напарника шкалу 100–900 и фиксировать её токенами в дизайн-системе, а не подбирать оттенки на глаз.


---

## 5. Проверка шкал прищуриванием: одинаковый диапазон светлоты
`цвет · процесс · крафт` · [06:29](https://youtu.be/yYwEnLYT55c?t=389)

**Мысль:** Если шкалы разных цветов не совпадают по диапазону света, при замене 200 жёлтого на 200 синего интерфейс выглядит несвязным.

**Слова автора:**

> The fifth and final step is to test them out to see if we need to make any tweaks something I like to do is put all the scales in a row and then squint my eyes or blur the layers to make sure each scale has the same range going from light to dark you can see in this palette that we're making that the line is a little squiggly it's not really even and that means that when we swap out colors in the UI like for example switching out a background from yellow 200 to a blue 200 it won't look cohesive.

**Для Напарника:** Прищуриванием или блюром проверять, что оттенки неба по часам суток остаются в одном коридоре светлоты.


---

## 6. Правь существующие оттенки, не плоди новые; максимум 10
`цвет · доступность · крафт` · [07:21](https://youtu.be/yYwEnLYT55c?t=441)

**Мысль:** Инструменты нужны для доступности, но глаз тоже проверяет, например, неоновость зелёного. Избыток оттенков делает выбор мучительным.

**Слова автора:**

> Use tools especially for things like accessibility but also trust your eyes for example I'm noticing that our green feels a little too saturated almost neon compared to our other colors so I'm going to bring down the saturation a bit on that scale in the future don't be afraid to keep iterating just try to avoid adding too many new shades if you can help it tweak what you have instead of creating a ton of new shades you don't want to be deciding between 70 different options try to stick to a maximum of 10 Shades.

**Для Напарника:** Ограничить число цветовых токенов и при правках подкручивать имеющиеся, а не добавлять новые.
