# You'll Regret NOT Using The 8pt Grid in Figma (UI/UX Beginner Tutorial)

**Канал:** Tim Gabe · 7 мин · субтитры: en (авто YouTube) · https://youtu.be/ohF93_k3IMk

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Зачем сетка 4/8: убирает случайность и упрощает общение с разработчиком
`сетка · отступы · процесс` · [00:22](https://youtu.be/ohF93_k3IMk?t=22)

**Мысль:** Фиксированный набор чисел исключает 52 здесь и 47 там, а любое значение вне шкалы сразу заметно и дизайнеру, и разработчику.

**Слова автора:**

> The eight point or four point grid system is basically just you as a designer adhering to heights widths sizes that are divisible by eight or four in most cases and we'll get to some cases where you don't want to do it so that means that you'll use pixel sizes like 4 8 12 16 24 32 40 48 all the way up to whatever number you feel is needed for your designs and what this does for you it just creates consistency so it eliminates randomness and creates consistency so you can be sure that your designs are all going to look very consistent because you have a consistent sizing system you don't have to worry that oh wait a second did i use 52 here and 47 there and then 31 here no you know that maybe for most buttons i'm using 40 48 and 64. for most paddings it's 32 or 24. it's much easier to stay consistent and eliminate randomness and the second thing and the last thing for why we use it is for communication so if you're working with developers you're working with designers in your design files knowing that we just need to remember the numbers four and eight is gonna help a lot so if a developer sees in your design file that wait a second this is 51 pixels and we're using numbers divisible by 4 and 8. something is wrong here then they might address that and come back to you and talk to you about it the same with designers they're gonna see that something is wrong here and they're also gonna know that when we're designing our paddings it's not gonna be some random number i know that it's either 24 or 32. and it reduces the amount of choices you have and the amount of possibilities for error so great for communication.

**Для Напарника:** Использовать шкалу 4/8/12/16/24/32 в Tailwind и сверять скриншоты на странные значения.


---

## 2. Шаг 4 для мелких связанных вещей (иконка у ссылки), 8 для крупных
`сетка · отступы · иконки` · [02:29](https://youtu.be/ohF93_k3IMk?t=149)

**Мысль:** Иконка на расстоянии 8 от ссылки выглядит отдельной, на расстоянии 4 частью компонента. Точность выбирается по масштабу.

**Слова автора:**

> Now when do we use four versus eight and it all depends on what level of precision you need.

**Для Напарника:** Иконки в кнопках Play/ArrowRight держать на 4px от текста, чтобы читались как часть одной кнопки.


---

## 3. Сетка 4/8 не для ширин контейнеров и высот: мастер это отступы и padding
`сетка · отступы · мобильный` · [04:33](https://youtu.be/ohF93_k3IMk?t=273)

**Мысль:** Динамическая ширина карточки (350.5) и высота (195) не обязаны делиться на 4, главное, чтобы margin и padding были кратны.

**Слова автора:**

> But there are places where we don't use it like for container woods so when it comes to web development and design we're creating things within containers and the biggest container the master container of them all the container for your whole page is usually based on a number so 1140 pixels for example is a very common container width with that we have a column system that we adhere to so column systems are based on containers and the width of the content within will be dynamic now when it comes to columns i have a video on that you can check it here where i go into detail about these things but just know that the widths for your things so for example let's look at the card here again so this card when we shrink it needs to be dynamic it needs to follow how the page kind of shrinks now that makes it impossible for us to use an point or four point grid system because then we set this fixed number and that's not gonna work so if we look at this width here it's 350.5 which is not divisible by four or eight if we would then use the eight or four point grid to create the width or to set the width of this card layout then you can see how it breaks our column layout which is not what we want when it comes to web development this also is true for most container heights so if we look at this once again like i showed you before we have margins that adhere to this eight point or four point grid system and we have paddings that also adheres to it the result of this is of course that the full height of this card is not necessarily gonna adhere to the 8.4 point grid in this case it's 195 which means that it's not divisible by four or eight and that's okay because we're focusing on having the margins and the paddings as the masters here.

**Для Напарника:** Не пытаться подгонять ширину карточек под сетку на разных вьюпортах, держать кратными только отступы.


---

## 4. Когда можно нарушить сетку: мелкий текст с иконкой, но лучше менять размер иконки
`сетка · иконки · крафт` · [06:40](https://youtu.be/ohF93_k3IMk?t=400)

**Мысль:** Шесть пикселей иногда выглядят идеально, но надёжнее подогнать размер иконки и сохранить шаблон.

**Слова автора:**

> When do we break the rules first of all we should aim to not do it but sometimes you might need to one case where i usually end up being in this situation where i might need to break the rules is when i'm handling small text sizes with icons so in this example here you have a four pixel spacing we have a six pixel spacing and we have an eight pixel spacing the four pixel spacing seems a bit tight and the eight pixel one seems a bit too separated and six pixel feels like just the right kind of balance but once again even though like this looks a bit better if we can change the size of the icon or do anything else then actually breaking our pattern of 8 pixels or 4 pixels that's the best way to go because in the end more simplicity equals a happy design life.

**Для Напарника:** Сначала менять размер иконки или текста, и только потом вводить исключение из шкалы.
