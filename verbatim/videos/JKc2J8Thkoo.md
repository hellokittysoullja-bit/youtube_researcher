# Inside Stripe’s Design Team: Moving Fast Without Sacrificing Quality

**Канал:** Designer Fund · 10 мин · субтитры: en (авто YouTube) · https://youtu.be/JKc2J8Thkoo

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Садовник: вкус и редактура важны, когда ИИ ускоряет выпуск
`процесс · вкус · ИИ` · [01:10](https://youtu.be/JKc2J8Thkoo?t=70)

**Мысль:** ИИ позволяет всем делать прототипы, дерево растёт буйно; нужен человек со вкусом и точкой зрения, который «обрезает», а планку качества удерживает система.

**Слова автора:**

> And so I kind of picture this tree that's kind of growing wildly and then you know somebody with a taste, a vision, a point of view can kind of help to shape that into something that feels coherent. And so the role of a gardener or somebody pruning the mass that starts to come is going to be really important. >> You know, we don't want to let the quality bar slip just because we're shipping more and faster. We still care about sentence case and end dashes and Oxford commas. We still want to have that stripe quality. It just became a question of designing a system to enable that at this newer scale.

**Для Напарника:** Когда ИИ генерирует реплики и шаги для Напарника, нужен слой редактуры и правил тона, чтобы качество и тёплый голос не размывались.


---

## 2. Живой интерактивный прототип понятнее статичного макета
`процесс · исследования · крафт` · [04:39](https://youtu.be/JKc2J8Thkoo?t=279)

**Мысль:** Пользователь может почувствовать компоненты в рабочем прототипе, статичный мок трудно оценить.

**Слова автора:**

> So you can imagine putting this in front of a user is a much more rich experience because they can actually feel the different components of it versus a static screen or mock which is much harder to sort of grasp.

**Для Напарника:** Новые механики Напарника (реакции кота, рост острова) прототипировать в движении, статичные мокапы не показывают динамику.


---

## 3. Dante: контроль качества текстов на масштабе через ИИ
`процесс · тексты · ИИ` · [04:49](https://youtu.be/JKc2J8Thkoo?t=289)

**Мысль:** Скорость выпуска превысила способность контент-дизайнеров проверять строки, поэтому сделали ассистента, встроенного в Slack, GitHub и CLI и обученного на стиле компании.

**Слова автора:**

> One of the tools that we created internally is called Dante and that came out of the need to solve a problem about quality at scale. The content design team was seeing the company and our scale and the speed of which we were moving was just like far exceeding their ability to do you know reviews and you know make sure all the words were checked and that we were only you know following the right thing. Chris within the content design team partnered with engine and PM to work on a tool that could then be integrated in Slack in GitHub in the CLI so that when people are building experiences we are along the way helping them make sure that they're making the right choices and following the right styles and that the content that's going to be in our product is a content that we're proud of and really fits the end all.

**Для Напарника:** Автоматическая проверка текстов Напарника на соответствие тону (без стыда, тёпло) перед выпуском, например линтер строк.
