# I redesigned IRCTC App! - Product Design | Ansh Mehra

**Канал:** The Cutting Edge School · 13 мин · субтитры: en (авто YouTube) · https://youtu.be/2f57yfJPmQA

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Определи основное действие и отдай ему максимум места
`иерархия · внимание · крафт` · [01:43](https://youtu.be/2f57yfJPmQA?t=103)

**Мысль:** Когда на экране много элементов, глаз не знает, куда смотреть; нужно понять цель экрана и дать главному действию максимум площади, всё остальное по возможности вырезать.

**Слова автора:**

> Important thing here is to decide what is the primary action what is the common use case of this screen the most common use case is obviously to book a ticket when you're traveling there are two kinds of travel there's a one-way trip and there's a round trip and I have not used this mobile experience before so I'm still pretty confused as to how I can book just a round trip versus just a one-way trip secondly because there are so many items here so much Tech so many images my eyes don't really know where to look so I think the first principle here is to understand what is the core objective of the screen and then understand how can we give maximum real estate to that one primary action without adding elements that can distract you now in design there's a very basic principle that if you can get rid of something cut it away anything that comes on the screen should be absolutely necessary if you can cut away any word any single line of text that is recommended.

**Для Напарника:** Фокус: основное действие «начать» должно доминировать; вторичное убрать или раскрывать (progressive disclosure).


---

## 2. Референсы дают идеи, но решает контекст вашего пользователя
`исследования · процесс · вкус` · [03:29](https://youtu.be/2f57yfJPmQA?t=209)

**Мысль:** Чужие приложения улучшают визуал и генерируют идеи, но контекст персоны и своей задачи важнее копирования.

**Слова автора:**

> But to be honest when you're designing for your own brand or when you're designing for your own problem statements these things just help you get more ideas these things help you improve your visual design but overall you need to very careful that you're keeping in mind specific context of your user Persona specific context of your own problem statement.

**Для Напарника:** Референсы из других приложений фильтровать через контекст СДВГ: низкая энергия, нет стыда, одна цель.


---

## 3. Иерархия поля ввода: размер и цвет, мелкая подпись и крупное значение
`иерархия · типографика · цвет` · [04:26](https://youtu.be/2f57yfJPmQA?t=266)

**Мысль:** В поле ввода подпись («From») мелкая, значение («New Delhi») крупное; цвет и размер вместе строят иерархию.

**Слова автора:**

> A very core principle of creating components is visual hierarchy if I am making an input field I need to make sure that from is in a very small font and New Delhi is in a Big Font both the color and the size establish your hierarchy.

**Для Напарника:** В формах Дома/Фокуса (шаг, длительность) значение крупнее и контрастнее подписи.


---

## 4. Подпись под иконкой для новичка, иконка одна не объясняет
`онбординг · тексты · микрокопирайтинг` · [05:00](https://youtu.be/2f57yfJPmQA?t=300)

**Мысль:** Новичок не поймёт функцию по иконке и короткому названию; место под поясняющий подтекст снимает неопределённость.

**Слова автора:**

> A very big change was to make sure that instead of these icons I actually give space for a subtext because as a newcomer I would not even know what to expect under file TDR or I would not know what is change boarding because I am not a regular traveler so it's very important to have space for a subtext.

**Для Напарника:** Непонятные для новичка разделы Напарника сопровождать однострочным тёплым подтекстом.


---

## 5. Иконки и подписи не всегда нужны, если смысл очевиден
`иерархия · иконки · крафт` · [07:33](https://youtu.be/2f57yfJPmQA?t=453)

**Мысль:** Дата очевидно датой, ей не нужна иконка календаря; подпись нужна, когда непонятно, что за данные; иконки полезны в длинных списках.

**Слова автора:**

> You don't always need these icons if I remove Journey date if I remove this calendar icon your eyes will know that 12th June is the date itself you need labels when it is not very obvious what this data is for so if this wasn't 12 June 2023 if it was a normal text then I need a label because otherwise somebody would not even know what is this for is this from is this two is this your name is this your house address how would you know but when it comes to time and when it comes to date somebody can literally see and guess that this is a date so you don't need the label icons are usually helpful when you have a very long list but in this case even if you cut off these icons it would not affect the user experience overall.

**Для Напарника:** Убирать избыточные иконки на карточках Дома и Фокуса, оставлять там, где смысл неочевиден.


---

## 6. Слои поверхности: фон серый, карточка светлее, поле ввода серое
`иерархия · цвет · отступы` · [08:31](https://youtu.be/2f57yfJPmQA?t=511)

**Мысль:** Чем ближе к пользователю, тем светлее карточка; серое поле внутри белой карточки читается как «сюда можно вводить» по привычке из других приложений.

**Слова автора:**

> Towards the content and notice that in terms of hierarchy I have a gray surface on top of that you have a white card so as you move towards the screen the card should increase in lightness so all cards are in white so anything that you see in white is placed on that hierarchy and then the blue CTA is on top of that card but when it comes to the input field if you put something in Gray then it feels like you can fill something in it feels a layer under that white card so it's not like I made this into a gray and then the input feels white keeping it gray makes it feel like you can type in it now there is no explicit logic behind it's just that because we have been using so many apps this is the kind of behavior that we would expect when we're seeing something like this.

**Для Напарника:** Слои на светлоте: сохранять коридор 0.152–0.172 фона, вводить различие слоёв оттенком и насыщенностью, а не яркостью.


---

## 7. Высокий контраст на случай солнца и поцарапанного экрана
`доступность · цвет · мобильный` · [09:15](https://youtu.be/2f57yfJPmQA?t=555)

**Мысль:** Реальный контекст (вокзал, солнце, царапины) требует очень высокого контраста; доступность часть дизайна.

**Слова автора:**

> I've made sure that the contrast is extremely high because a lot of people might be using this on a scratched screen or a screen which is under sunlight or they might be using this right at the railway station itself so you need to be very careful about accessibility in general.

**Для Напарника:** Контраст Напарника измерен (muted-foreground 6.63:1); учитывать использование на улице при ярком свете.


---

## 8. Серая иконка рядом с текстом сигнализирует «кликабельно»
`иконки · доступность · иерархия` · [10:30](https://youtu.be/2f57yfJPmQA?t=630)

**Мысль:** Без значка строка воспринимается как простой список, а не как действие.

**Слова автора:**

> Next to the text so that you know that it is clickable otherwise if you don't put an icon people will not know that it is clickable they will think that it is simply a list.

**Для Напарника:** Тапабельные строки Дома/Мира снабжать намёком кликабельности (шеврон/иконка).
