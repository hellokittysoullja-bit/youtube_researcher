# 9 || Accessibility in UI/UX design for beginners || English

**Канал:** Dezinx by Kirtanya · 13 мин · субтитры: en (авто YouTube) · https://youtu.be/J38z28N7MoU

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Ограничение бывает постоянным, временным и ситуативным
`доступность · мобильный · СДВГ` · [00:22](https://youtu.be/J38z28N7MoU?t=22)

**Мысль:** Три вида: постоянное (одна рука), временное (травма), ситуативное (в руках вещи). Проектировать надо под все три, а не только под диагноз.

**Слова автора:**

> Now accessibility simply means designing for people who have some special need like they might be having some physical disability or mental disability or they might be in a special situation or they have some special requirements because disability is not permanent like we have three kind of disability permanent temporary and situational you can see the example of this thing you can take the screenshot of this thing like if you take the example of touch imagine if a person who have only one hand so he will use any app or website with only one hand or in any situation if you got injured then in that case also the user can use only one hand or you might be carrying something in your hand so in these three conditions the person is disabled either temporary permanently or situationally so you have to design your app according to these things.

**Для Напарника:** Напарник для людей с СДВГ: учитывать ситуативную невнимательность (шум, спешка, одна рука); крупные цели нажатия, минимум ввода текста.


---

## 2. Не полагаться только на цвет: добавлять иконку к состоянию
`доступность · иконки · цвет` · [01:59](https://youtu.be/J38z28N7MoU?t=119)

**Мысль:** Для дальтоников и просто для быстрого сканирования иконка рядом с ошибкой или статусом сообщает смысл быстрее и надёжнее, чем один цвет.

**Слова автора:**

> Now next thing we have is the using icons not just colors now icons will be very helpful for the people who have some kind of color blindness like if you just look at this example in this the person cannot see colors he will see only dragon white things here she has to read that text to understand that this is the error but if you add a icon it will be easy for the user to understand that there is something wrong and he need to pay attention it will be easy for the user to scan and this will also help normal users to scan the app ation better because majority of the time we scan a app or website to understand the content if you add a icon it will be very helpful for the user to understand that there is something wrong or any other kind of thing.

**Для Напарника:** Состояния в Напарнике (ошибка сети, сохранено) подавать не цветом, а иконкой плюс репликой кота, не toast.


---

## 3. Межстрочный интервал 130–150% (в пикселях), не больше
`типографика · доступность · отступы` · [07:39](https://youtu.be/J38z28N7MoU?t=459)

**Мысль:** Auto line height у шрифтов слишком плотный; 130–150% читается лучше, но выше 150% абзац распадается на отдельные строки.

**Слова автора:**

> Second thing is you should always increase the line height if you just select this paragraph and if you click here on this line height option by default it's set to Auto and every font has different line height like in this case we have 16 if you just click on it will show you the line height and every font has different line height let me choose another font like this font has line height of 17 pixel so you have to change the line height of the font you are using to make it more readable let me undo it and choose Roboto now the line height we should use it's around 130% to 150% that's a good line height and you should also not increase it too much because that way it will be very difficult to scan or read any paragraph like if you just type 150 here percent also then it will change the line height to 150% for 14 pixels font size now what it's doing it's calculating 15% of 14 now to calculate the 150% of 14 you can either use a calculator or you can do basic Madden figma just click here and select all and delete simply press 1.5 because we want 150% so we will type 1.5 if you want 125% you have to type 1.25 and simply multiply it by pressing shift 8 for the star symbol you can see that we have a star symbol and then press 14 then it will show you the line height is 21 pixels and you should always give your line height in pixels because if you use percentage and design for lineer like if I typed 150% here it will create some problem in development so it's always a good idea to use pixels you have to do this thing for every font like if the font size was 16 pixels so I will simply change the line height simply go here type 1.5 if I'm using 150% and type 60 then the line height will be 24 pixels and you can choose any line height between 130% to 150% don't go beyond that because that will be too much and let me show you like if I increase the line height paragraph will not look like a paragraph it will looks like they are individual lines so it's not a good idea to go beyond 150% let me undo it and if you want to go below 130% you can go up to 125% or 120% depending upon your font but you should always increase the line height of your paragraph to make it more readable.

**Для Напарника:** Чат-пузыри и подписи в Напарнике: line-height около 1.4–1.5 для основного текста; проверить в chat-bubble.tsx.


---

## 4. Минимальные размеры шрифта: абзац 14px, мелкий текст 12px
`типографика · доступность · мобильный` · [09:31](https://youtu.be/J38z28N7MoU?t=571)

**Мысль:** Для мобильного абзац не меньше 14px, самый мелкий текст 12px (10px не рекомендуется), для десктопа абзац от 16px.

**Слова автора:**

> The minimum font size for paragraph is 14 pixels you should not go below 14 pixels because that will be very hard to read on screen and for desktop version at 16 pixel you should avoid using paragraphs below 16% for the desktop version of the website like the PC version of the website the paragraph font size should be minimum 16 pixels okay and the smallest size of font you should use in your design is 12 pixels for mobile design like the application design or the mobile version of any website and for paragraph it's 14 pixels and for other small text you can use 12 pixels although in some cases you can use 10 pixels but it's not recommended you should try to stick to 12 pixels and for PC it's 14 pixel you should not go below 14 pixels for any kind of text make note of this thing otherwise you might forget what I just said.

**Для Напарника:** Сноски и подписи на Фокусе и Доме: не опускаться ниже 12px, основной текст реплик ≥14–16px.


---

## 5. Двусмысленные кнопки: «Отмена» vs «Не отменять»
`микрокопирайтинг · тексты · доступность` · [10:47](https://youtu.be/J38z28N7MoU?t=647)

**Мысль:** В диалоге «Вы уверены, что хотите отменить?» кнопки «Да» и «Отмена» путают: непонятно, что отменяется. Подпись должна называть действие.

**Слова автора:**

> Now ux copy is not exactly in accessibility design but it's very important that you should keep your ux copy very simple now ux copy is the written text on the UI we have like yes cancel or this heading or this paragraph This is a ux copy this is the written content of all the app or website now if you just look at this example if are you sure you want to cancel the transaction now we have two options C yes and cancel now this is very confusing that like the cancel button will cancel the transaction or this will cancel the action so it's always a good idea to give simple or understandable ux copy because majority of the people are not that much smarter you should always try to keep the ux copy as simple as possible now to fix this thing what you can do is you can simply change the ux copy you can change the label to cancel and don't cancel now it's very clear you can also change it to cancel transaction that will be more easy but this will also work fine.

**Для Напарника:** Подтверждения в Фокусе (прервать сессию?): называть действие прямо в голосе кота, например «Закончить сейчас» и «Остаться со мной».


---

## 6. Зона касания минимум 48x48px и зазор 8px
`доступность · мобильный · отступы` · [11:34](https://youtu.be/J38z28N7MoU?t=694)

**Мысль:** Палец примерно 48px; у людей с дрожью рук или в тряске метро мелкая цель недостижима. Увеличивать зону можно невидимым контейнером вокруг кнопки.

**Слова автора:**

> Next thing we have is the touch area like if you just look at this text I have to tap exactly on this text like the height is 20 pixels only then the button will work but if you just look at this example like I have enclosed that thing in a container or other frame its touch area is 48x 48 pixels now it's touch area height is 48x 54 pixels now the minimum touch area is 48x 48 pixels because our thumb size is also similar although you can easily touch elements have smaller size than 48 pixels but there are some situations or some kind of disability in which it will be difficult to touch a smaller element like if you are in a very crowded place and if you're not able to use your phone properly your phone is shaking then you will not be able to touch that thing properly or if any person has some kind of disability and it's shaking very much then it will not be able to touch it properly and it has to pinpoint on that thing to touch that thing so it's always a good idea to increase the touch area and to increase the touch area you don't have to do anything you have to tell your developer to increase the touch area you can only give extra spacing in your design to increase the touch area like in this case I have enclosed that thing inside a frame you can see that thing in a layers panel like this is the button like this is the text button and I haven't closed that thing inside a container or a frame so developer will assign a touch action to this whole container instead of this button and it will be easy for the user to touch it and the minimum gap between two elements which are clickable it's 8 pixels it always recommended although you can reduce this Gap to zero but you should be very smart when you are doing this.

**Для Напарника:** Чипы длительности и кнопки Фокуса: hit-area ≥48px, зазор между соседними ≥8px.
