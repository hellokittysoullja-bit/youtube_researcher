# Every UI/UX Concept Explained in Under 10 Minutes

**Канал:** Kole Jain · 9 мин · субтитры: en (авто YouTube) · https://youtu.be/EcbgbKtOELY

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Сигнифаеры: интерфейс сам объясняет, как им пользоваться
`иерархия · онбординг · крафт` · [00:00](https://youtu.be/EcbgbKtOELY?t=0)

**Мысль:** Контейнер, выделение активного и серый неактивный текст объясняют работу без инструкции. Состояния нажатия, подсветки и подсказки сообщают, что элемент умеет.

**Слова автора:**

> This one's easiest to explain with an example first. If I have three text and icon pairs, but I put a container around drinks and food, you know that they're related and dessert is not. Then, if I put a container around drinks, you know that it's selected and you can toggle over to food. If I gray this text out, you know that it's inactive and clicking it probably won't do anything. See how you just knew all of that? I didn't need to write instructions on how it worked because the UI was signifying how things worked. Good UI has many signifiers, like a button press state, highlights on active nav items, hover states, or even tooltips to tell the user what a UI affords or what it can do.

**Для Напарника:** Чипы длительности и кнопки на Фокусе должны сами показывать выбранное и неактивное состояние, без пояснительных надписей.


---

## 2. Иерархия создаётся контрастом размера, позиции и цвета
`иерархия · типографика · цвет` · [00:47](https://youtu.be/EcbgbKtOELY?t=47)

**Мысль:** Самое важное крупно и вверху, второстепенное мельче и ниже, а акцентный элемент отличается цветом. Именно разница между большим и малым создаёт иерархию.

**Слова автора:**

> Now, take a look at this card. It displays all of the information in a logical, repeatable format, but it looks like a spreadsheet, not a design. So, let's give it some hierarchy, which is pretty intuitive. We have size, position, and color to use to our advantage. Starting from the top, an image always adds a great pop of color and makes scanning super easy, just like Uber. If in this case the item is the most important, we want that large and bold and at the top because otherwise it'll blend in with something like the time and date, which can be below and much smaller. And it's this contrast, the difference between small and big or colorful and not, that actually creates the hierarchy. It's also why price should be at the top, right aligned, and blue. It's different than the rest, which draws the eye to it. The location should be smaller and below like this.

**Для Напарника:** В reward-карточке и карточках шагов выделять одну главную строку размером и позицией, остальное делать меньше и тише.


---

## 3. Сетка лишь ориентир; важнее белое пространство и группировка
`сетка · отступы · иерархия` · [02:05](https://youtu.be/EcbgbKtOELY?t=125)

**Мысль:** Не всё должно ложиться в 12 колонок, а кратность 4 нужна, чтобы значения делились пополам и давали согласованность. Группировка близких элементов тоже форма иерархии.

**Слова автора:**

> Now, some people have this misconception that all of your content needs to align to a 12-column grid and be exactly eight pixels apart. But, these are just guidelines. For example, this design doesn't line up with any of the columns and that's not uncommon, especially for custom landing pages. But, for highly structured pages like galleries, blogs, or any repeating content, they can actually be useful for responsiveness by giving guidelines for responsive behavior on tablet with eight columns and mobile with four. But, much more important than using excessive grids and layouts is white space, letting things breathe. For example, in a simple section like this, the large text would have a font size and line height like this and the subtext would have a font size and line height like so. Buttons would be similar and optionally a top announcement bar like this. Then, simply 32 pixels between every item, but you can also group elements that just go together like the announcement and text or the text and subtext, which is just another form of visual hierarchy. And this is where we see the four-point grid system actually come into play. Everything is a multiple, not because it inherently looks better, but because you can always split things in half,.

**Для Напарника:** Использовать шаг 4/8 пикселей и группировать связанные элементы, а между блоками оставлять воздух, особенно на Доме.


---

## 4. Один шрифт и приём: letter-spacing −2…−3%, line-height 110–120% для заголовков
`типографика · крафт · вкус` · [03:10](https://youtu.be/EcbgbKtOELY?t=190)

**Мысль:** Дизайн в основном текст, и одного гротеска достаточно. Подтянутый трекинг и межстрочный интервал крупного текста мгновенно делают его профессиональнее.

**Слова автора:**

> Typography is really interesting because design is mostly just text. And for picking a font, I can almost unilaterally say you'll never need more than one for any design. So, find a nice sans serif font like the ones on screen and stick to it. Over the last seven years of designing, I've rarely used any fonts other than what's on screen and this shouldn't be where you're spending tons of time. I'm also not a big fan of calling any design skill a hack, but this one kind of is. This design looks okay right now, but our header text feels a little too loose. If you tighten up the letter spacing on this by about -2% to -3% and drop the line height to about 110% to 120%, it instantly makes any larger text look super pro real fast.

**Для Напарника:** Крупные заголовки на лендинге и Фокусе подтянуть: tracking около -0.02em и line-height 1.1–1.2.


---

## 5. Не больше шести размеров шрифта; в плотных экранах диапазон меньше
`типографика · иерархия` · [04:06](https://youtu.be/EcbgbKtOELY?t=246)

**Мысль:** Для лендингов диапазон размеров большой, для дашбордов он сжимается (обычно до 24px) из-за плотности информации.

**Слова автора:**

> Text sizes can vary wildly. For landing pages and websites, you generally don't want more than six font sizes, which can have a really large range. For things like dashboards, that range shrinks dramatically to where you don't normally have text sizes larger than 24 pixels because of the increase in information density.

**Для Напарника:** Ограничить шкалу типографики Напарника шестью размерами и не раздувать размеры на плотных экранах вроде Мира.


---

## 6. Один основной цвет и семантические цвета с назначением
`цвет · дизайн-система · доверие` · [05:01](https://youtu.be/EcbgbKtOELY?t=301)

**Мысль:** От бренд-цвета берутся светлые фоны и тёмный текст. Семантические цвета (синий доверие, красный опасность, жёлтый предупреждение, зелёный успех) несут смысл, а не украшение.

**Слова автора:**

> Starting with one primary color. Generally, this is your brand color. Then, you can lighten it for a good background or darken it for text colors. Both good ways to incorporate subtle color and make an otherwise drab design look much more interesting. And with all of that, we're already halfway to a color ramp, which is what large companies use to build out chips, states, charts, and really anything else. But, I also think it's important as a beginner to let the color find you. Like an announcement bar to grab attention or a focus state on an input or the green new chip on a link. These are all semantic colors, which are colors that have meaning and provide signifiers to the user. Blue for trust, red for danger or urgency, yellow for warning, and green for success. Make sure you use color for purpose, not just for decoration.

**Для Напарника:** Тёплый акцент как единственный основной цвет; красный опасности использовать минимально, чтобы не вызывать стыд и тревогу.


---

## 7. Тёмная тема: глубину даёт более светлая карточка, а не тень
`цвет · тёмная-тема · иерархия` · [05:44](https://youtu.be/EcbgbKtOELY?t=344)

**Мысль:** В тёмном режиме тени не работают, поэтому карточка светлее фона, границы слабее, а чипы приглушены по насыщенности и яркости. Фон может быть не только серым, но и глубоким фиолетовым или зелёным.

**Слова автора:**

> Now, designing in dark mode presents some pretty interesting challenges for us. First, this card is using a light border, which creates a bit too much contrast. So, we'll lower that down. In dark mode, we don't have shadows like light mode, so to create depth, we need to have a lighter card than the background. So, I'll make that adjustment. This chip is also far too bright, so we can dim down the saturation and brightness and flip that for the text to create some hierarchy. There's also a ton of flexibility for deep purples, reds, or greens,.

**Для Напарника:** Для карточек над AppBackdrop поднимать светлоту карточки на малый шаг и приглушать границы, не меняя коридор фона.


---

## 8. Тени: меньше непрозрачности, больше блюра; тень не должна бросаться в глаза
`крафт · вкус · иерархия` · [06:16](https://youtu.be/EcbgbKtOELY?t=376)

**Мысль:** Карточкам нужна слабая тень, а попапам сильнее. Если тень видна первой, она использована неверно.

**Слова автора:**

> But, speaking of depth, shadows are a fantastic tool to use on light mode. This shadow, along with most, is too strong. So, reducing the opacity and dialing up the blur helps a lot. The strength you'll need depends on the foreground and background, but cards require less while content that sits above other content like popovers will need stronger shadows. We can even use these techniques with inner and outer shadows to create effects like raised tactile buttons. Just remember, if the shadow is the first thing you notice on a design, you're not using it right.

**Для Напарника:** Для всплывающих элементов использовать мягкие широкие тени низкой непрозрачности, чтобы они не конфликтовали с живым фоном.


---

## 9. Размер иконки равен line-height текста; padding кнопки по ширине вдвое больше высоты
`иконки · отступы · крафт` · [06:52](https://youtu.be/EcbgbKtOELY?t=412)

**Мысль:** Иконки обычно слишком крупны, поэтому их сверяют с высотой строки. Для кнопок с иконкой или без работает правило ширина примерно вдвое больше высоты.

**Слова автора:**

> Most icons are generally too large, so the trick is to get the line height of your font, in this case 24 pixels, and make the icons the same size and then tighten up the text. Sidebar links like this are actually just buttons without a background until you hover, which are often called ghost buttons. And if we isolate one and center it, we've got a perfect standalone button. These are super common when you have a primary and secondary CTA side by side. And a good guideline for padding on these is to double the height for the width.

**Для Напарника:** Иконки Play и ArrowRight в кнопках шага сделать размером в line-height подписи.


---

## 10. Каждое действие получает отклик: состояния кнопок и полей
`микрокопирайтинг · доверие · анимация` · [07:25](https://youtu.be/EcbgbKtOELY?t=445)

**Мысль:** У кнопки минимум default, hover, pressed и disabled, а у поля ввода focus, error и warning. Также нужны спиннеры загрузки и сообщения об успехе.

**Слова автора:**

> A good rule of design is when a user does anything, there should be a response. For example, every button needs at least four states: default, hovered, active or pressed, and disabled. Sometimes you'll need a loading state, too, with a spinner. Inputs are even more critical. You'll need a focus state when the user clicks in, error states with red borders and messages when something's wrong, and sometimes even warning states for optional issues. And this applies everywhere. Loading spinners when data is fetching, success messages when an action completes, even micro animations on scroll or swipe. Every interaction needs a response.

**Для Напарника:** Ответы на ошибку и успех оформлять голосом напарника инлайн, не toast; состояния pressed и disabled для кнопок обязательны.


---

## 11. Микро-взаимодействие подтверждает действие, от практичного до игривого
`анимация · награды · микрокопирайтинг` · [08:09](https://youtu.be/EcbgbKtOELY?t=489)

**Мысль:** Hover и клик по копированию без подтверждения оставляют сомнение, а выезжающий чип подтверждает действие.

**Слова автора:**

> Micro interactions are a form of feedback, but they step things up a notch. For example, this copy button has states and feedback when we hover and click, but we still don't know that we've copied anything. Instead, if we have this chip slide up, that's a micro interaction that confirms our action. And these can range from highly practical to much more fun and playful.

**Для Напарника:** Подтверждения в Напарнике давать кошачьим жестом или репликой рядом с элементом, а не уведомлением.


---

## 12. Оверлей текста на картинке: линейный градиент вместо сплошной заливки
`крафт · типографика · доступность` · [08:30](https://youtu.be/EcbgbKtOELY?t=510)

**Мысль:** Сплошной оверлей портит картинку, градиент плавно переходит в читаемый фон под текстом, а прогрессивный блюр добавляет современности.

**Слова автора:**

> Finally, overlays are really important because if you screw them up, you're going to ruin the image and the text, too. In this case, we can't leave it as is, so we could add in a full-screen overlay, but it doesn't do the image justice. So, instead, add in a linear gradient that'll display the image then smoothly converge into a text-readable background. Or, if we're going for extra fancy, we can add in a progressive blur on top of the gradient for an even more modern look.

**Для Напарника:** Скрим под сноской над грядой ориентиров делать градиентом, согласуя с отступом pb-[32vh], а не фиксированной высотой.
