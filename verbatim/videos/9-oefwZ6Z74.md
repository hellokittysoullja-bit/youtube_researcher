# The 80% of UI Design - Typography

**Канал:** Sajid · 12 мин · субтитры: en (авто YouTube) · https://youtu.be/9-oefwZ6Z74

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Типографика это 20% работы, дающие 80% результата
`типографика · иерархия` · [00:00](https://youtu.be/9-oefwZ6Z74?t=0)

**Мысль:** Если убрать стили шрифта, пропадают выбранный пункт и точка фокуса, и экран превращается в набор текста.

**Слова автора:**

> Most of the uis are just text and buttons with some icons to help users take necessary actions so mastering typography is that 20% of the design that gives you the 80% of the results let's start by removing all the font styles from this very popular UI on the left sidebar we broke the selected tab that's definitely bad for user experience we have no idea where we are right now same thing for the buttons on top now coming to the feed itself there is no hierarchy and point of focus so it's tough to tell what we are looking at it's just a bunch of text.

**Для Напарника:** Прежде чем добавлять эффекты, проверить, что типографика различает выбранное, главное и второстепенное на каждом экране.


---

## 2. Группировать и разделять можно размером, цветом, расстоянием и весом
`иерархия · отступы · цвет` · [00:58](https://youtu.be/9-oefwZ6Z74?t=58)

**Мысль:** Разнос кружков не всегда ясен, а смещение второй группы вниз сразу даёт две группы. Закон близости работает для тех же целей, что размер и цвет, и результат стоит проверять на коллегах.

**Слова автора:**

> This whole thing looks like one single block of information like we are telling the user hey you better read this as well but we know that the title is connected to the thumbnail and users should look at these two together before moving on to the other elements in short we don't just want the title to stand out we also need it to stand on its own separate from this group to do that we need to understand how the human brain recognizes shapes and patterns what do you see here how can we separate them into two groups we could space them out like this but people might still get confused between one group of six circles or two groups of three circles so let's try size this is also confusing some might see this as three groups instead of the two we intended let's try color it's still not clear enough if it's three or two groups but if we just move the second group of bit down it becomes very clear that it's two groups instead of three you can validate this by showing it to your friends or colleagues now let's retrace our steps before we go back to fonts you are going to need size color and spacing to group or separate elements technically spacing falls under the law of proximity but it's used for the same purpose to group or separate elements.

**Для Напарника:** На Доме отделять реплику от её действий расстоянием и цветом, а не рамками.


---

## 3. Когда белое на чёрном уже максимум, выделяй приглушением остального (~60% светлоты)
`иерархия · цвет · доступность` · [02:38](https://youtu.be/9-oefwZ6Z74?t=158)

**Мысль:** Нельзя сделать контраст выше максимума, поэтому второстепенное затемняют. Около 60% светлоты текст остаётся читаемым, а заголовок выделяется.

**Слова автора:**

> We already have these three properties to emphasize and separate the title from this group all we need is color but which color white on black is already at the max contrast possible so to emphasize this we need to deemphasize that the easiest way to do that is by tweaking the lightness value and seeing what works best in our case 60% lightness is the sweet spot for keeping the text readable and still emphasizing the title.

**Для Напарника:** Второстепенные подписи на Фокусе приглушать, сверяя контраст с замеренными значениями (muted-foreground 6.63:1).


---

## 4. Самое важное с наибольшим контрастом, остальное приглушено светлотой
`цвет · иерархия` · [04:09](https://youtu.be/9-oefwZ6Z74?t=249)

**Мысль:** Во многих известных интерфейсах акцент строится на разнице светлоты, а не на новых цветах.

**Слова автора:**

> If we zoom out a bit we'll see this color trick being used everywhere the most important elements have the highest contrast and then to deemphasize other elements they just played with the lightness value.

**Для Напарника:** Выбранный таб в AppNav выделять светлотой и контрастом, а не отдельным цветом.


---

## 5. Разбор списка: размер и вес заголовка, приглушённый ник, кнопка в карточке, проверка в исходном размере
`иерархия · типографика · процесс` · [07:00](https://youtu.be/9-oefwZ6Z74?t=420)

**Мысль:** Крупный жирный заголовок, более тёмный и мелкий ник и лёгкая кнопка создают иерархию. Нужно проверять результат в реальном размере, не только при увеличении.

**Слова автора:**

> Firstly there is no hierarchy everything just looks like a blob of text secondly this button needs to stand out let's zoom in some size and weight to emphasize the title then a darker color and smaller size to deemphasize the username a lighter color to highlight the button but the button doesn't look quite right here let's move it to the right and wrap everything inside a card it's looking much better now the button still looks a bit bulky though let's reduce the font size to match the username it looks good but remember we're zoomed in we need to check if it works at the original size the username might be hard to read it could use some weight and so could the button.

**Для Напарника:** Всегда сверять типографику на реальном вьюпорте 390px, а не только в увеличении.


---

## 6. Базовый размер 14/16px и шкала от него: иерархия вес и цвет, а не размер
`типографика · иерархия · дизайн-система` · [07:55](https://youtu.be/9-oefwZ6Z74?t=475)

**Мысль:** Почти весь интерфейс может быть одного размера, различаясь весом и цветом. Шкала задаётся базой и шагами на два пикселя вверх или вниз.

**Слова автора:**

> These are all the font sizes you need to design 99% of apps and uis and if you want just these three combined with weight and color are enough to build an entire UI how many font sizes do you see here these all have the same font size of 16 pixels except for this one the impact of weight and color on font size is pretty wild so you don't need many sizes to create hierarchy combining size weight and color can do the trick I'm not saying you should create a typ scale like this but this won't help you much either you'll probably need something more like this yep that's it everything you see is 14 pixels except for the title and the two headings it's the same on this video page everything is 14 pixels except for the title and the channel name for your project just pick a base font size either 14 or 16 pixels regular weight and 100% lightness I'll get to light mode in a minute but let's finish this first once you've picked your base font try designing everything with that size and when you absolutely need to go two pixels up or down from there that's it that's your typ scale.

**Для Напарника:** Принять базу 16px и ограничить шкалу Напарника несколькими шагами, различая элементы весом и светлотой.


---

## 7. rem для доступности; line-height работает как отступ; код по документу, стиль по визуалу
`типографика · доступность · дизайн-система` · [09:24](https://youtu.be/9-oefwZ6Z74?t=564)

**Мысль:** rem позволяет менять размер шрифта, а интерлиньяж берёт на себя нижний отступ заголовка. H1 в разных местах могут выглядеть по-разному, ведь стиль подчиняется визуальной иерархии.

**Слова автора:**

> First convert the pixel unit to a rem value we want our apt to follow accessibility guidelines so users should be able to adjust the font size if they need to secondly this m value is very important remember this Gap this is crucial for the title to stand out and stand alone in most cases we don't need to manually add a gap or margin the line height takes care of it automatically acting as the margin bottom for text elements so your Global variables might look something like this and that's it this is all you need to build a top tier UI but keep in mind not all H1 elements will share the same font style code for document hierarchy but style for visual hierarchy you might think this is the obvious solution but it should actually look something like this use your common sense to judge what the user will focus on.

**Для Напарника:** Размеры шрифта задавать в rem и задавать интерлиньяж так, чтобы не добавлять ручные margin к заголовкам.


---

## 8. Размер относителен соседям; динамические числа тоже проектируй
`типографика · иерархия · процесс` · [10:32](https://youtu.be/9-oefwZ6Z74?t=632)

**Мысль:** Элементы конкурируют за внимание, и жирный крупный шрифт бывает слишком резким, тогда снижают вес. Нужно учитывать динамические значения, не только визуальную иерархию.

**Слова автора:**

> Font size is a relative unit meaning it depends on its neighboring elements right now both are competing for attention let's try a bigger font size and see if that works big bold fonts can often be too harsh on the eyes so let's bring the weight down and see if that works it looks good but this is a dynamic number so we need to account for that as well don't just design for visual hierarchy design for functionality too.

**Для Напарника:** Таймер сессии должен корректно выглядеть и при двузначных, и при однозначных минутах, не прыгая шириной.
