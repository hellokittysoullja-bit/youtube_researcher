# WWDC25: Meet Liquid Glass | Apple

**Канал:** Apple Developer · 19 мин · субтитры: en (ручные) · https://youtu.be/IrGYUq1mklk

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. В покое тихо, оживает при касании
`анимация · иерархия · внимание` · [04:04](https://youtu.be/IrGYUq1mklk?t=244)

**Мысль:** Элемент временно «поднимается» при взаимодействии; состояние покоя остаётся визуально спокойным, а жизнь проявляется на касание.

**Слова автора:**

> Elements can even lift up into Liquid Glass temporarily, such as when you interact with a component. This lets the resting state stay visually quiet, while it comes to life on touch. This works great for things like controls, where the transparent liquid lens can be seen through to precisely observe the value underneath it.

**Для Напарника:** Диегетичность: UI Напарника спокоен, реакции только на события и касания, не пульсирует просто так (§3).


---

## 2. Эффект только для навигационного слоя; никакого «стекла на стекле»
`иерархия · вкус · крафт` · [13:04](https://youtu.be/IrGYUq1mklk?t=784)

**Мысль:** Применение эффекта везде конкурирует с остальными элементами и путает иерархию; стопка слоёв выглядит перегруженной, верхним элементам нужны заливки и прозрачность.

**Слова автора:**

> You may be tempted to use Liquid Glass everywhere but it is best reserved for the navigation layer that floats above the content of your app. Consider this tableview: making it Liquid Glass would make it compete with other elements and muddy the hierarchy. So keep it in the content layer instead to ensure clarity Similarly, always avoid glass on glass Stacking Liquid Glass elements on top of each other can quickly make the interface feel cluttered and confusing. When placing elements on top of Liquid Glass, avoid applying the material to both layers. Instead, use fills, transparency, and vibrancy for the top elements to make them feel like a thin overlay that is part of the material.

**Для Напарника:** Не накладывать свечение/размытие на свечение; блюр и glow ограничивать одним слоем (навбар/скрим).


---

## 3. Акцентный цвет только для главного; если всё выделено, ничего не выделяется
`цвет · иерархия · вкус` · [17:21](https://youtu.be/IrGYUq1mklk?t=1041)

**Мысль:** Тонировка нужна для основных действий; при выделении всех элементов ничто не выделяется и возникает путаница; цвет добавляют в слое контента.

**Слова автора:**

> Tinting should only be used to bring emphasis to primary elements and actions in the UI. First, lets look at an example of what not to do. Avoid tinting all your elements. When every element is tinted, nothing stands out, and it can be confusing. If you want to imbue color into your app, do it in the content layer instead.

**Для Напарника:** Один акцентный CTA на экран Напарника (эффект Фон Ресторфф); остальное в приглушённых тонах.


---

## 4. В стационарном состоянии не пересекать контент и слой управления
`иерархия · крафт · доступность` · [17:45](https://youtu.be/IrGYUq1mklk?t=1065)

**Мысль:** При запуске приложения избегать пересечений контента с плавающим слоем; сдвигать или масштабировать контент для разделения.

**Слова автора:**

> The content layer is also key to avoiding any unwanted visual noise. In steady states, such as when an app first launches, avoid intersections between content and Liquid Glass. Instead, reposition or scale the content to maintain separation.

**Для Напарника:** Это ровно баг §5.2: сноска не должна пересекаться с грядой ориентиров; решается структурным отступом, а не скримом.


---

## 5. Пониженная прозрачность, повышенный контраст, снижение движения
`доступность · анимация · крафт` · [18:08](https://youtu.be/IrGYUq1mklk?t=1088)

**Мысль:** Системные настройки модифицируют материал: frostier при reduced transparency, чёрно-белые элементы с рамкой при increased contrast, меньше интенсивности и без упругих эффектов при reduced motion.

**Слова автора:**

> There are also several accessibility features that Liquid Glass offers to suit all kinds of people and needs. These act as modifiers on the material that change certain layers of Liquid Glass, without sacrificing its magic. For instance, Reduced Transparency, makes Liquid Glass frostier and obscures more of the content behind it. Increased contrast, makes elements predominantly black or white and highlights them with a contrasting border and Reduced Motion decreases the intensity of some effects and disables any elastic properties for the material. These are available automatically whenever you use the new material. So whenever these settings are turned on at a system-level, Liquid Glass elements will get them across the board.

**Для Напарника:** Учесть prefers-reduced-motion для AppBackdrop, авроры и роста острова; для СДВГ с сенсорной чувствительностью это особенно важно.
