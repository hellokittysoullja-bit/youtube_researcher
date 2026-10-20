# How we animate the Duolingo world - The innovative tech behind our characters

**Канал:** Duolingo · 9 мин · субтитры: en (ручные) · https://youtu.be/fgOqvyPif3g

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Анимация универсальна: взгляд и мимика говорят без слов
`анимация · персонаж · маскот` · [01:42](https://youtu.be/fgOqvyPif3g?t=102)

**Мысль:** Язык тела персонажа передаёт эмоции и намерения вне языка; взгляд направляет внимание, выражение показывает успех или замешательство.

**Слова автора:**

> And the reason for this is simple, animation is universal. It has this unique ability to transcend language barriers, which allows us to connect with our learners on a deeper and more intuitive level. For example, the use of body language in animation offers a universal method for expressing emotions and intentions that can be easily understood by individuals from any linguistic background. One character's gaze can direct attention or express interest, while another character's expression can express success or confusion. It is a fundamental human language that resonates with anyone around the world.

**Для Напарника:** Кот-напарник: направлять внимание взглядом и мимикой (expression-based MascotSvg) вместо текстовых пояснений.


---

## 2. Ограниченный набор ассетов, комбинируемых в безлимит вариантов
`анимация · крафт · персонаж` · [04:11](https://youtu.be/fgOqvyPif3g?t=251)

**Мысль:** Мало анимационных ассетов + интерактивная сборка дают практически неограниченные комбинации в одном компактном файле.

**Слова автора:**

> Rive helps take a limited number of animation assets and allows us to mix and match them into a variety of ways to create a virtually unlimited number of combinations. It allows us to streamline the animation process while also making a single compact animation file that can be used for multiple unique purposes.

**Для Напарника:** Для маскота делать модульные состояния (выражение, поза) и комбинировать, а не рисовать отдельный ролик под каждую реплику.


---

## 3. Две независимые системы (рот и персонаж) оживляют героя
`анимация · персонаж · маскот` · [05:19](https://youtu.be/fgOqvyPif3g?t=319)

**Мысль:** Рот и реакция персонажа (idle → верно/неверно) работают параллельно и не ломают друг друга; цель, чтобы персонаж ощущался внимательным напарником по учёбе, а не картинкой под звук.

**Слова автора:**

> To overcome this challenge, we used Rive to develop two systems. The first system was just for the mouths, which would be programmatically called and can be called in any order that you'd like. Then the second system was the actual character animation, which would be from an idle state would be triggered to go into an incorrect or correct state based on if you got it right or wrong. We were then able to run these two systems at the same time which allowed for independent movement of the mouth without actually affecting the character animation. Now one might be wondering, why would you do this? Who cares? What is the point of putting so much effort and energy into something as small as minuscule mouth movements? Well, for starters, we thought that it would help to make the characters feel more alive. Like that they were talking to you, as an attentive study buddy, instead of just a character with audio playing over them as they moved. Additionally, we thought it would help to provide some visual reinforcement of the spoken content, which is pretty important when you're learning a language.

**Для Напарника:** Развести слои маскота: дыхание/присутствие отдельно от реакций на события, чтобы реакции не прерывали «сидение рядом».
