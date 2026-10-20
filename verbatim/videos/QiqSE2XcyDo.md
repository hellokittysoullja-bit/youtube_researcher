# The Most Popular UI/UX Animation Technique

**Канал:** DesignCourse · 13 мин · субтитры: en (авто YouTube) · https://youtu.be/QiqSE2XcyDo

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Mask-анимация: контейнер overflow hidden и сдвиг содержимого
`анимация · крафт` · [00:32](https://youtu.be/QiqSE2XcyDo?t=32)

**Мысль:** Родитель с overflow hidden скрывает элемент, сдвинутый transform translate; при появлении его возвращают на место — получается эффектное раскрытие.

**Слова автора:**

> This red outline here is basically its own div element its apparent element of this type element and this element will have an overflow of hidden and then we take whatever it is that we want to reveal and we give that a transform translate X or Translate Y property where it simply moves it out of view from the actual mask and so this is the whole idea.

**Для Напарника:** Реплики кота и заголовки Дома: раскрывать текст маской снизу, а не fade, для красивого появления (по событию).


---

## 2. Stagger: 1.4с, шаг 0.1с между строками, мягкий ease
`анимация · крафт · типографика` · [06:22](https://youtu.be/QiqSE2XcyDo?t=382)

**Мысль:** Задержка между строками (stagger 0.1) вместо ручных CSS-таймингов даёт приятную последовательную анимацию; слишком большой шаг (0.7) выглядит медленно.

**Слова автора:**

> Pieces of type essentially we're just defining a duration of 1.4 seconds we're seeing Y is zero which we're using the two method you can also use a from method and then a stagger of 0.1 between all of them which will create a stagger animation between each one of them and then just a custom easing of power two all right so we can make this a little bit more obvious about how stagger actually works by increasing this value just for demonstration purposes so if I change this from 0.1 to 0.7 and I go ahead back you can see how much slower each line is but you can see how much easier it makes your life because you don't have to rely on CSS to create all these specific timings animations manually all right so just revert that back to point one and it really just gives you a nice very nice sort of animation for your UI.

**Для Напарника:** Появление строк в reward-карточке и сводке: stagger около 0.1с, общая длительность около 1.4с, easing power2.


---

## 3. Анимация не должна заставлять ждать: шаг 0.01с на символ
`анимация · время · СДВГ` · [11:57](https://youtu.be/QiqSE2XcyDo?t=717)

**Мысль:** Слишком большой шаг stagger на символ растягивает появление и раздражает; 0.01с даёт гладкий эффект без ожидания.

**Слова автора:**

> Change this to 0.1 it's going to take a long time to go through each character but I'll show you just for demonstration purposes as you can see it's very slowly putting these all in and this would be bad you wouldn't want to make somebody sit there and wait that long so 0.01 I find works really well and it's a nice smooth animation.

**Для Напарника:** Печать реплик кота по символам или словам: общий ритм быстрый, чтобы человек с СДВГ не ждал текст.
