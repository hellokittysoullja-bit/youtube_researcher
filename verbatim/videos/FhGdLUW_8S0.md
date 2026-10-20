# 8 Point Grid system - Improve your UI designs (Figma file included)

**Канал:** UX Tshili · 9 мин · субтитры: en (авто YouTube) · https://youtu.be/FhGdLUW_8S0

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Джуниоры гадают размеры; осознанность каждого размера отличает профессионала
`сетка · процесс · крафт` · [00:22](https://youtu.be/FhGdLUW_8S0?t=22)

**Мысль:** Сетка из 8 точек даёт единую структуру и сохраняет вид после передачи разработчикам.

**Слова автора:**

> I have realized that there is a common theme in people who are more Junior by just getting started in their design career they are not using grids everyone is just guessing they're spacing the size of the elements and the text that every size has to be intentional and this is where the eight point grid system comes in the a point grid is a layout system used in UI design to create consistent visual structure and hierarchy for your designs this ensures that your work is consistent and aligned use the eight point grid system as a guideline to determine the size of elements on your screen and the spacing between them grids allow you to achieve better looking designs faster and they also ensure that your designs will look as polished once you've handed them over to.

**Для Напарника:** Каждое число отступа в компоненте Напарника должно иметь обоснование в шкале.


---

## 2. Типографика кратна 8 от 16, минимум 12; на 10px проваливается доступность
`типографика · доступность · сетка` · [01:21](https://youtu.be/FhGdLUW_8S0?t=81)

**Мысль:** Размеры меньше 12 становятся нечитаемыми и не проходят требования доступности.

**Слова автора:**

> Even with your typography it should ideally be multiples of eight from 16 upwards if you need a smaller size then you can go down to like 12 which is a multiple of four so it kind of still works but you shouldn't really go any lower than that when you get to like 10 this text becomes very small and then that's where you start to not pass accessibility.

**Для Напарника:** Не использовать размеры мельче 12px; текст сноски на Фокусе не опускать ниже 12px.


---

## 3. Параметры сетки: мобильный 4 колонки, поле 16, желоб 8; десктоп 12 колонок, поле 32, желоб 16
`сетка · мобильный · отступы` · [02:20](https://youtu.be/FhGdLUW_8S0?t=140)

**Мысль:** Конкретные цифры сетки по устройствам: планшет 8 колонок с теми же полями, что у десктопа.

**Слова автора:**

> And we want four columns and then we want the margin which is the outside of 16 and the gutter which is the inner swim Lane of eight so that is your grid setup in Mobile so now let's do the same for desktop let's change that to columns in desktop we have 12 columns we can put a margin of 32 on the outside and the gutters of 16 and for tablet eight columns and similar margins to desktop 32.

**Для Напарника:** Использовать поле 16px на мобильном и 32px на десктопе в layout app/app/layout.tsx.


---

## 4. Title case и выравнивание влево читаются легче, чем капс и центр
`типографика · доступность` · [06:25](https://youtu.be/FhGdLUW_8S0?t=385)

**Мысль:** Капслок и центрирование замедляют чтение.

**Слова автора:**

> I don't think there was a need for them to be uppercase and I left aligned everything it's easier to read than Center alignment.

**Для Напарника:** Заголовки и реплики напарника выравнивать влево и не набирать капсом, кроме коротких лейблов.


---

## 5. Главный цвет зарезервирован для CTA; проверяй экраны вместе, а не по одному
`цвет · иерархия · процесс` · [06:46](https://youtu.be/FhGdLUW_8S0?t=406)

**Мысль:** Слишком много оранжевого размывает акцент, тогда как оставленный на кнопке действия он работает. Цветовая картина оценивается по связке экранов.

**Слова автора:**

> There is way too much orange on this page and it should be reserved for the most important areas which is the call to action button the add button and that's what I've done I created a color palette around the orange so I've got some harmonious colors here and the green which is a complementary color yes this page looks a bit more green however when we go into the other page where we've got the bigger orange buttons that's where you see more of the orange when you're designing it's not always screen by screen you're looking at how all the screens work together.

**Для Напарника:** Тёплый акцент только на кнопке старта и находках; проверять Дом, Фокус и Мир подряд.


---

## 6. Кнопки под большой палец, без вертикального текста, без конкурирующей вторичной кнопки
`мобильный · доступность · иерархия` · [08:18](https://youtu.be/FhGdLUW_8S0?t=498)

**Мысль:** Кнопки нужно делать крупнее для пальца. Яркая вторичная кнопка отвлекает от главной, поэтому её приглушают.

**Слова автора:**

> You think about if someone's thumb is hitting that you need a bit more space so I made the buttons bigger and on here we have got type on its side that is an absolute No-No there is no excuse for doing that so we made it fit under the image and it is gray button looks so bold that it's actually competing with the add a button for your attention.

**Для Напарника:** Вторичные действия на Фокусе (пропустить, назад) делать тише кнопки старта.
