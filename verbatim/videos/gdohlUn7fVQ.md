# FIX Color Contrast – Accessibility in Web & UI Design

**Канал:** Pimp my Type · 10 мин · субтитры: en (ручные) · https://youtu.be/gdohlUn7fVQ

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Пороги контраста WCAG: 4.5:1, 3:1 для крупного и жирного
`доступность · цвет · типографика` · [02:48](https://youtu.be/gdohlUn7fVQ?t=168)

**Мысль:** Обычный текст не ниже 4.5:1, крупный (от 24px) и жирный (от 19px) — 3:1; значения считаются в пикселях.

**Слова автора:**

> Your text needs to have a minimum contrast of 4.5 to 1 for normal text, 3 to 1 for text larger than 24 pixels and 3 to 1 for bold text larger than 19 pixels. Don't get confused by the WCAG, when you look it up there it says points but you'll have to calculate this in pixels which is the thing we love on the web. Fairly easy to understand and you can use a Figma plugin or other extensions or your dev tools to check if your contrast ratio is met.

**Для Напарника:** Проверка muted-foreground (6.63:1) и мелких подписей на фоне; держать запас над 4.5:1.


---

## 2. Границы интерактивного элемента нужны, иначе кнопка выглядит текстом
`доступность · иерархия · цвет` · [04:04](https://youtu.be/gdohlUn7fVQ?t=244)

**Мысль:** Помимо текста, сам контрол должен контрастировать с фоном минимум 3:1, иначе пользователь не отличит кнопку от обычного текста.

**Слова автора:**

> Whenever there's interactive control, you're gonna need to clearly show the boundary of that control. Otherwise people won't see the background of the button. They just see the text. That way they might not know if that's a button or just plain text.

**Для Напарника:** Чипы длительности и вторичные кнопки на тёмном фоне: тонкая обводка или заливка с контрастом ≥3:1.


---

## 3. Три способа сделать контрол различимым: рамка, иконка, подчёркивание
`доступность · крафт · иконки` · [05:07](https://youtu.be/gdohlUn7fVQ?t=307)

**Мысль:** Рамка цветом текста (ghost-кнопка) решает проблему; иконка и подчёркивание дополнительные сигналы, но рамка показывает, куда нажимать.

**Слова автора:**

> The simplest way of doing this is by adding a border around it. I prefer using the text color so it will become a ghost button. But you can use whatever color you like as long as it has a 3 to 1 contrast ratio at least. Now thinking about this again, color contrast is very relevant for people that have a visual impairment or a certain degree of blindness and that's the hard part here to us as designers because it's not either fully sighted everything's working fine or and because this is hard to mention there are these guidelines to have a minimum standard that will work for more people with a slight impairment. Basically everything that has a lower than 3 to 1 contrast ratio you treat that as the background color and if you have the border around it's much clearer for people who can't distinguish colors as exactly as most people can. Another approach would be leaving the background as it is but adding an icon. Working, but it comes with a little disadvantage in usability. So showing that boundary would be more helpful, allow people to know where to click, like they don't have to click exactly. This problem remains when we underline the text, but this also would pass. because it adds an additional signifier that this is an interactive component.

**Для Напарника:** Вторичные действия в Напарнике (Повторить, Следующий шаг): обводка плюс иконка Play/ArrowRight.
