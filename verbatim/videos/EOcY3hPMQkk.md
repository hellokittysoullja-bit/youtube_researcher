# The 7 Color Mistakes that RUIN your UI Designs

**Канал:** Kole Jain · 7 мин · субтитры: en (авто YouTube) · https://youtu.be/EOcY3hPMQkk

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Меньше цвета: не всё должно быть разноцветным, иконкам цвет не нужен
`цвет · доступность · иерархия` · [00:11](https://youtu.be/EOcY3hPMQkk?t=11)

**Мысль:** Пять акцентных цветов на карточках конкурируют за внимание и проваливают WCAG. Иконки это узнаваемые символы, а цвет надо оставлять для статуса, например активной вкладки.

**Слова автора:**

> Less is almost always more with color. Not everything should be a different color like it is here. First, these cards are burning a hole in my eye, and they almost all fail the WCAG contrast checks, meaning we can't reasonably use them. I'm sure you've heard of the 603010 rule, meaning BY is 60% of our dominant neutral color, 30% secondary color, and 10% accent color. Lemon Squeezy is a good and very colorful example of this, with purple being 60%, yellow being the 30%, and white actually being the accent color in this section. Right now, we have at least five different accent colors on these cards, all competing for attention. If we swap the cards for our brand color, we somewhat hit the 603010 rule. But now, we have a different problem. The bright purple dominates the page for an element that really isn't that important and creates obvious accessibility issues. A good fix is to lighten it up so it draws less attention and swap the text to black. Next, let's focus on these icons down here. For the most part, icons need no color. Their job is to be recognizable symbols. Color should be reserved for communicating status, like highlighting this as an active tab.

**Для Напарника:** В AppNav цвет только у активного пункта, остальные иконки нейтральные.


---

## 2. Нейтральный баланс: фон тихий, лёгкий оттенок бренда вместо яркого фона
`цвет · тёмная-тема · вкус` · [01:31](https://youtu.be/EOcY3hPMQkk?t=91)

**Мысль:** Яркие фоны почти всегда плохо. Серый фон с каплей брендового оттенка (как у Headspace) добавляет цвет без перегруза.

**Слова автора:**

> It's called neutral balance. Backgrounds are the best place to start because they should remain in the background, and our sandy yellow gradient is not really doing that. Almost never will you want bright colors for your background. There are, of course, notable exceptions to every rule, but generally you want to start with a neutral gray background and a very light or white foreground. This is the same idea for a dark mode where the darker colors are in the background and slightly lighter colors make the foreground, but we can integrate a little more color into this by taking our neutral gray and adding a hint of purple to it. Headspace does this very thing where they take a tint of their bright orange and use it in the background on these cards to add a splash of color without overpowering the visuals.

**Для Напарника:** Фон Напарника держать нейтральным, а оттенок неба вносить через насыщенность в узком коридоре светлоты.


---

## 3. Адаптируй брендовый цвет: поверни по кругу, возьми комплементарный, затемни для контраста
`цвет · доступность · дизайн-система` · [02:27](https://youtu.be/EOcY3hPMQkk?t=147)

**Мысль:** Если бренд-цвет не проходит WCAG с белым текстом, его затемняют или берут комплементарный. Так делают Mailchimp и Airbnb.

**Слова автора:**

> A common challenge designers face is working with the brand colors that are provided. For example, with our brand colors, let's assume the brand guidelines look a little bit like this. The problem is we don't really have much else to work with. So in the storage bar we could change the opacity, but it feels a little bland. To spice it up, we can rotate our purple slightly on the color wheel to pick a blue and pinkish color. We can also choose a complimentary color across the color wheel, like a bright yellow. These colors all work well on our UI because they're analogous and complimentary colors. This strategy also works if you have a brand color like this orange that fails WCAG checks with white text. You can darken it up, which passes, or choose a complimentary blue, which also passes. A ton of brands actually follow this very idea. Take Mailchimp for example. They have bright yellow as their primary color, which is then used with a complimentary turquoise secondary, or Airbnb, who has a very bright pink and a much deeper pink to pair with it. The point is, don't be afraid to adapt brand colors in order to accommodate good design.

**Для Напарника:** Тёплый акцент Напарника проверять на контраст с текстом кнопки и при необходимости затемнять, а не снижать читаемость.


---

## 4. Серые вместо чистого чёрного и белого; тёмная тема это не инверсия светлой
`цвет · тёмная-тема · иерархия · доступность` · [04:05](https://youtu.be/EOcY3hPMQkk?t=245)

**Мысль:** Второстепенный текст светло-серый, в тёмной теме яркость серых снижают ради глаз, а чистый белый оставляют для главного. Границы и главные карточки в тёмной теме нужно осветлять сильнее, а акцент слегка десатурировать.

**Слова автора:**

> Using pure white and pure black is not bad. They're colors, so why not use them? But often there are just better options than black or white. And a lot of it boils down to hierarchy. For example, below the name of the file, we have the size and type of file. This isn't super important information, so we can use a dark gray instead. Same idea for the labels over here or for the borders we just added. Because the elements are well grouped, we can lighten it up, too. In fact, most of the text is light gray or dark purple, not even black. This is a similar idea for dark modes, but because of the distinct focus on eye strain, we can be even more aggressive with lowering the brightness of our grays. Reserving white only for the most important actions. Getting comfortable with using more gray and less black and white is really what differentiates mediocre designers from professional ones. Now, speaking of, dark mode is not just the inverse of light mode. If we were to inverse all the colors on our light mode, this is what we'd end up with. Not awful, but certainly not ideal. First, let's brighten up these borders and the main card since dark colors need to be more different than light colors to see the difference. Our text is all light purple because we're using a very dark purple instead of black on our light mode. Typically, light grays work best on dark mode to make it easier on the eyes than white. But from there, we'll brighten up some of the most important text like the logo and storage used to pure white. Finally, these colors are probably fine, but our logo should be desaturated a touch. So no, you shouldn't just inverse your colors from light to dark. Instead, a palette should be built with the goals of dark mode in mind.

**Для Напарника:** В тёмном интерфейсе чистый белый зарезервировать для самых важных элементов (таймер, главная кнопка), остальное светло-серое.


---

## 5. Деструктивное действие красное, даже если это не бренд-цвет
`цвет · доверие · этика` · [05:43](https://youtu.be/EOcY3hPMQkk?t=343)

**Мысль:** Бренд-цвет на кнопке удаления привлекает внимание и не показывает опасность, поэтому красный и зелёный есть даже в брендовых палитрах без этой роли.

**Слова автора:**

> Have the delete button have a purple background or a red background. The purple background is undeniably more on brand. However, that draws attention to the button and doesn't illustrate its destructive nature. Instead, we use red. And this is why red and green are often in a brand's color palette, even if they aren't a brand color. Because a pop-up like this just simply wouldn't fly from a usability point of view.

**Для Напарника:** Удаление данных (сброс острова) визуально отличать от обычных действий, но без пугающего тона, и подтверждать голосом напарника.


---

## 6. Состояния: hover светлее, pressed темнее, disabled десатурирован; на мобильном нажатие
`цвет · анимация · крафт` · [06:24](https://youtu.be/EOcY3hPMQkk?t=384)

**Мысль:** Нажатие чуть темнее серым создаёт ощущение, что давишь на поверхность; на мобильном hover нет.

**Слова автора:**

> For hover states, use a slightly lighter or brighter version of the base color. For an active or press state, use a slightly darker version. And then for a disabled state, just desaturate the color, assuming it's not already grayscale. But because we don't have hover effects on mobile, we usually just resort to click effects. For example, we don't need anything here. However, adding a slightly darker gray on press makes it feel like you're actually pressing into something.

**Для Напарника:** Для кнопок на Фокусе задать pressed-состояние чуть темнее/ниже, а disabled десатурированным.
