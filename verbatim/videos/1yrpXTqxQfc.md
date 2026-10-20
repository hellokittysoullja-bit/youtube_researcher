# Design Systems at Scale // Episode 5: Proven Strategies for Scaling Your Design System

**Канал:** Dan Mall · 14 мин · субтитры: en (авто YouTube) · https://youtu.be/1yrpXTqxQfc

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Дизайн-токены: переменные «субатомного» уровня
`дизайн-система · крафт · цвет` · [11:24](https://youtu.be/1yrpXTqxQfc?t=684)

**Мысль:** Токены (цвет бренда, радиус, шрифт) — свойства, не привязанные к реализации; из них собирается интерфейс, а менять их можно в одном месте.

**Слова автора:**

> Implementation agnostic design properties that might sound a little esoteric but that's what they are so any developer will know what a variable is right you say you know color brand red right so if you're a Target you have color brand red is Target red right or you might have a specific border radius value that you use for all of your digital products or you might have a specific font face you use for all of your products all of these design properties are what help build a brand these you could sort of refer to them as subatomic properties right these are the properties that ultimately make up your user interface.

**Для Напарника:** Вынести коридор светлоты 0.152–0.172 и шкалу SKY в токены/CSS-переменные, чтобы правка не ломала контраст.
