# Accessible Web Design: What Is It & How To Do It

**Канал:** Flux Academy · 16 мин · субтитры: en (авто YouTube) · https://youtu.be/-ao_Kc_8rpE

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Дизайнеры работают на хороших экранах и делают иерархию серыми оттенками и мелким шрифтом
`доступность · цвет · типографика · иерархия` · [04:11](https://youtu.be/-ao_Kc_8rpE?t=251)

**Мысль:** Люди с плохим зрением или на слабых экранах не могут читать низкоконтрастный и мелкий текст; как в упаковке лекарств, должен быть минимум сочетания цвета и размера.

**Слова автора:**

> So the first concept is color contrast and text size and the idea here is that as I said some people may be old people or maybe people that have some in parodies can't see as good and maybe you know we're designers will usually work maybe on a Mac or on a fancy on a fancy display that shows color really nice and so we like to create hierarchies with like let's say some kind of a shade of grey or something but for people who can't see super well or have an amazing display like we have that makes reading really a tough job sometimes to the point of impossible the same size the same thing goes for text size we as designers we like to make things fancy and leave a lot of kind of like white space and stuff like that by using tiny fonts but we have to consider that for a lot of people using these type of super small fonts makes it hard to impossible to read so just like that in packaging design when somebody is you know designing and medication and they put this tiny little paper there's actually laws that says the font size can't be lower than something because people old people need to be able to read this the same thing goes with web site guidelines your font can't be below some combination of color and size to make sure that it will be seen.

**Для Напарника:** Подтверждает требование контраста muted-foreground и минимального размера шрифта; иерархию строить размером и весом, а не только серым оттенком.


---

## 2. Не полагаться только на цвет для различия состояний
`доступность · цвет · иерархия` · [06:14](https://youtu.be/-ao_Kc_8rpE?t=374)

**Мысль:** Люди с дальтонизмом не отличат жёлтую и оранжевую метки; статус нужно дублировать текстом или формой.

**Слова автора:**

> Now one more thing that you should when you're designing take in mind is that you don't want to use color alone to make kind of difference differentiations bright because some people are color blind and they might not see the difference so let me give you an example so let's say here if you look at the right we have two types of card and one of them is labeled with a yellow and one is labeled with an orange but somebody that has colorblindness might not actually see that they are different and if your imagine that you're designing some kind of maybe a task management or something like that and you want to show a status of a project if you're gonna be only relying on color then somebody that's looking at it might not even see that there's a difference or urgency or something like that so make sure that when you're designing you add something else to this besides color for example if you look at the example on the right I've added for example team egg and Team B so it's not only relying on color obviously for those of us who can see well we're gonna be able to make decisions or understand very quickly because of the help of color but color is not the only way.

**Для Напарника:** Статусы шагов и чек-ина обозначать иконкой или словом, а не только оттенком.


---

## 3. Проектируй состояние фокуса для клавиатуры, а не только hover
`доступность · крафт · мобильный` · [07:22](https://youtu.be/-ao_Kc_8rpE?t=442)

**Мысль:** Дизайнеры любят hover, но забывают focus state для тех, кто ходит по сайту через Tab; его не рисуют, потому что сами им не пользуются.

**Слова автора:**

> One more thing that you should care about is focus States so we as designers obviously we like to focus a lot on hover States and you know what happens when people move and hover with the mouse over something create fancy interactions but we a lot of times forget about the focus state so focus States basically is for people who use the keyboard to navigate websites and stuff like that so they might click the tab and then they kind of the selected link is going to be somehow selected right and we need to show how that looks like so this state is called focus State and a lot of designers don't even bother designing it or telling the developers that they should implement this because again this is not something that's visible or used by them and so they forget about it so make sure that you also design for the focus State for people who are using tab to select and then navigate through the websites.

**Для Напарника:** Заметные focus-кольца на кнопках, чипах длительности и полях в /app для клавиатурных и скринридерных пользователей.


---

## 4. Плейсхолдер не заменяет label: скринридер читает именно label
`доступность · микрокопирайтинг · крафт` · [08:26](https://youtu.be/-ao_Kc_8rpE?t=506)

**Мысль:** Минималистичные формы без подписей над полем делают поле непонятным для людей со скринридерами.

**Слова автора:**

> All right one more thing is labels so these days a lot of kind of trendy or this kind of design that you might see on dribble or stuff like that when people are designing forms it's very kind of minimalistic right so it's like the example on the left they're not even using a label for the form and by label is what you see on the right when you have kind of tax that is above the form field so a lot of times people would just use what's called the placeholder text inside the label to specify what this label is for so again like the example on the left you can see that the full name is actually not a label it's what's called a placeholder text now the problem with this is as I've mentioned some people use tools that read the websites to them and when there is no label they're not gonna be able to know what this form field is just because the website readers actually read the labels of the form so you have to have kind of a label for the form just build it this way otherwise they won't be able to know what's this form is for and won't be able to fill it up.

**Для Напарника:** Форма имени и чек-ина на Доме и поле шага на Фокусе: настоящий (хотя бы визуально скрытый) label, а не только placeholder.
