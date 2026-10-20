# WWDC25: Get to know the new design system | Apple

**Канал:** Apple Developer · 18 мин · субтитры: en (ручные) · https://youtu.be/DS2ildqCrB0

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. UI поддерживает, когда нужно, и не отвлекает, когда нет
`внимание · иерархия · body-doubling` · [06:20](https://youtu.be/DS2ildqCrB0?t=380)

**Мысль:** Функциональный слой парит над контентом, придавая структуру и ясность, не забирая фокус.

**Слова автора:**

> As apps become more immersive and content-focused, the UI should support interaction where needed, and remain unobtrusive when it’s not. Liquid Glass defines a new functional layer in the UI, floating above your content to bring structure and clarity, without ever stealing focus.

**Для Напарника:** Метафора присутствия кота: рядом, но не надзирает и не крадёт внимание во время Фокуса.


---

## 2. Затемнение для модальной задачи, разделение для параллельной
`иерархия · внимание · крафт` · [07:40](https://youtu.be/DS2ildqCrB0?t=460)

**Мысль:** Если задача прерывает основной поток, затемнение центрирует внимание; если идёт параллельно, достаточно естественного разделения без разрыва потока.

**Слова автора:**

> A dimming layer to signal modality when a sheet appears. When a task interrupts the main flow, pair Liquid Glass with a dimming layer to help center attention, making the sheet feel like a clear, purposeful space. On the other hand, when a task happens in parallel, Liquid Glass creates a natural separation to help keep things clear without breaking the flow.

**Для Напарника:** Шторки Фокуса: затемнять фон только при действительно прерывающем действии, остальное лёгким разделением.


---

## 3. Иерархия через раскладку и группировку, а не через декор
`иерархия · вкус · крафт` · [08:33](https://youtu.be/DS2ildqCrB0?t=513)

**Мысль:** Лишние фоны и рамки у кнопок для веса теперь не нужны; акцент создаётся расположением и группами.

**Слова автора:**

> First things first: if you’ve customized your bars, now’s the time to clean them up. We've all added extra backgrounds or borders to give buttons the right weight. This was common, and totally valid, for a long time. But with the new system appearance, we’re all relearning where emphasis comes from, making customizations like these unnecessary. Instead of relying on decoration, hierarchy should be expressed through layout and grouping.

**Для Напарника:** Убирать лишние рамки/фоны у кнопок Напарника; вес задавать размером, отступом и группировкой.


---

## 4. Переполненная панель: убрать лишнее, группировать по функции и частоте, главное отдельно
`иерархия · мобильный · крафт` · [09:19](https://youtu.be/DS2ildqCrB0?t=559)

**Мысль:** Второстепенные действия уходят в меню; кнопки группируются по смыслу и частоте; символы и текст не смешивать; главное действие отделено и подсвечено.

**Слова автора:**

> If your bar is feeling too crowded, use it as a cue to remove anything unnecessary and move secondary actions into a more menu to keep things clean and accessible. Group bar items by function and frequency. Buttons that perform related actions should generally go together. Just be sure to not group symbols with text, like “Select” and the share icon you see here, since it could be perceived as a single button. If you have a need for text buttons, allow them to sit on their own containers. A primary action, like Done, stays separate and appears tinted, often as a blue checkmark on iOS and iPadOS, or as a prominent text button on macOS, creating a clear focal point that’s easy to spot and interact with.

**Для Напарника:** Навигация и шапки Напарника: максимум одно подсвеченное главное действие, остальное группами или в меню.


---

## 5. Нет очевидного значка: лучше текстовая подпись
`иконки · микрокопирайтинг · доверие` · [15:12](https://youtu.be/DS2ildqCrB0?t=912)

**Мысль:** Карандаш может значить «аннотировать», галочка «подтвердить»; неоднозначные действия легко прочитать неверно; одинаковые символы повторять для узнаваемости.

**Слова автора:**

> Use the same symbols across devices to preserve meaning and build familiarity through repetition. However, not every action spells itself out. A pencil might suggest annotate, and a checkmark can look like confirm— making actions like Select or Edit easy to misread. When there’s no clear shorthand, a text label is always the better choice.

**Для Напарника:** Для неочевидных действий Напарника писать слово рядом с иконкой; иконки Play и ArrowRight различают контракт, но подпись обязательна.
