# The Perfect Spacing Framework in UI Design | Figma Tutorial

**Канал:** Mizko · 8 мин · субтитры: en (авто YouTube) · https://youtu.be/Al1xsdol4Pk

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Правило четырёх: любой отступ кратен 4
`сетка · отступы · дизайн-система` · [00:33](https://youtu.be/Al1xsdol4Pk?t=33)

**Мысль:** Единый шаг даёт согласованность, масштабируемость и понятность для разработчиков.

**Слова автора:**

> Whenever you are creating space between any element it should be divisible by four so with my eyes closed I am going to recite to you the four point grid system so it's either going to be four eight sixteen sorry take that back 12 16 20 24 28 32 36 40 44 48 52 56 60 and just increments of four.

**Для Напарника:** Все отступы Tailwind в Напарнике держать кратными 4px (шаг 1 = 4px) и не вводить произвольных значений.


---

## 2. Внутренний отступ меньше внешнего: близость группирует
`отступы · сетка · иерархия` · [01:58](https://youtu.be/Al1xsdol4Pk?t=118)

**Мысль:** Если контейнер имеет поле 16px, элементы внутри должны быть ближе друг к другу, иначе группа не читается; выглядит лучше 8 или 4, чем 16.

**Слова автора:**

> Because if you go ahead and look at the proximity of this design this entire box on the outside we have created spacing for 16 pixels right so it's divisible by 4 so on the left and right in the top and bottom you can see that there is 16 pixels so any elements on the inside it has to have less spacing than the container element okay so once you go to let's just make it 16 it looks a little bit weird because we've created the bounding space of this container to be 16 already so for the elements inside it has to feel closer together to feel like they are a relevant group so if we use 12 looks a little bit better if we use eight looks even better and let's just take a look at four might even look the best so as you can see utilizing the four point grid system first keeps all your measurements very consistent it's scalable and it's easy for developers to actually understand.

**Для Напарника:** Внутри карточек Напарника ставить интервал между элементами меньше внешних полей карточки.


---

## 3. Иди от широкого к узкому: чем глубже вложенность, тем меньше шаг
`отступы · сетка · процесс` · [05:19](https://youtu.be/Al1xsdol4Pk?t=319)

**Мысль:** Каждый уровень вложенности использует меньший отступ, чем родительский, например 32, затем 24, затем 20.

**Слова автора:**

> So we go from 32 down to 24 and then if we go even a level deeper you should be able to see that inside the input we have spacings of 20. so once again starting with a broad measurement going down further and always keeping it divisible by four is going to help you create really consistent UI designs.

**Для Напарника:** Заложить в дизайн-систему лестницу отступов по уровню вложенности (экран, карточка, элемент).


---

## 4. Нарушение правила оправдано: больше воздуха между несвязанными блоками
`отступы · иерархия · сетка` · [06:13](https://youtu.be/Al1xsdol4Pk?t=373)

**Мысль:** 40px между секциями сайдбара сообщает, что блоки не связаны, тогда как внутри блока 12 и 8 показывают родство. Отступ работает как язык связей.

**Слова автора:**

> But remember because we are working within this container we are now trying to create separation right we are actually not trying to make all these elements feel like they are in one group we are actually trying to tell visually communicate visually that this sidebar is all relevant to each other but all these blocks these separate blocks as you can see in here they are not relevant to each other so that's why we are actually creating more space in between okay but then when we've got a little bit deeper into each block as you can see over here we went from 20 on the left and right to 12 between the title and the import and then as you can see over here we have 12 and then if I double click onto the title the title only has eight so we started off at 20 then we went into 12 then we went into eight and that is how you create systematic spacing between all your designs.

**Для Напарника:** На Фокусе между разными зонами (шаг, длительность, старт) давать больший зазор, чем внутри каждой зоны.
