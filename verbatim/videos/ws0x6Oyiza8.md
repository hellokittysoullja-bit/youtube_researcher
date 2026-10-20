# Make Any Game Feel AMAZING: 7 Juice Tricks from "Juice It or Lose It" (JavaScript Tutorial)

**Канал:** Back To Code · 11 мин · субтитры: en (авто YouTube) · https://youtu.be/ws0x6Oyiza8

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Juice - слой обратной связи: подтверждает каждое действие
`крафт · анимация · доверие · вкус` · [01:19](https://youtu.be/ws0x6Oyiza8?t=79)

**Мысль:** Juice - это не новые механики, уровни или арт, а отклик на ввод; игра подтверждает каждое действие, и игрок чувствует себя услышанным.

**Слова автора:**

> So, what exactly is Juice? Steve Swing's book, Game Field, defines game feel as realtime control of virtual objects in a simulated space with interactions emphasized by polish. Juice is that polish. It's the feedback layer. Everything the game does to answer the player. When you press a button, something should react clearly and generously. Notice what juice is not. It's not new mechanics, not new levels, and not better art. It's the response. A juicy game confirms every action so the player always feels heard.

**Для Напарника:** Каждое касание в Напарнике получает ясный, щедрый, но тихий отклик.


---

## 2. Вспышка показывает, где произошло событие: дешёвая обратная связь, которую чувствуют сразу
`анимация · крафт · вкус` · [02:56](https://youtu.be/ws0x6Oyiza8?t=176)

**Мысль:** Короткая вспышка объекта указывает, где произошло столкновение; такая обратная связь недорога, и игроки чувствуют её, даже не умея объяснить.

**Слова автора:**

> Nothing about the gameplay changed, but the right side already reads better. The flash is doing real work. It tells your eyes exactly where the collision happened, a split second after it happened. That's feedback. The talk's point is that feedback like this is cheap to add and players feel it instantly, even if they could never tell you why.

**Для Напарника:** Короткое мягкое подсвечивание затронутого элемента (шаг, постройка) вместо анимации экрана.


---

## 3. Кривая плавности задаёт характер: линейная механична, эластичная желейна
`анимация · вкус · крафт · маскот` · [03:21](https://youtu.be/ws0x6Oyiza8?t=201)

**Мысль:** При той же длительности и концах кривая меняет личность: линейная как робот, ease-out мягче, elastic с перелётом как желе. Каскад с задержкой по ряду и колонке.

**Слова автора:**

> Things popping into place, they move there over time. The magic is in the easing function, a curve that maps time from zero to one into a feeling. Here we use an elastic ease, the same family Robert Penner made famous. Each brick gets a small delay based on its row and column. So the wall cascades in. And when the ball hits anything, every brick bumps a little bigger, then settles back. Let's reset the level and see it. Same tween, three different easing curves. Linear first. It moves, but it feels mechanical like a robot. Now an ease out cubic, which starts fast and slows down gently. smoother, more natural, and now elastic. It overshoots and wobbles into place like the bricks are made of jelly. Same duration, same start, same end. The curve alone changes the personality of the whole game.

**Для Напарника:** Подбирать easing под характер Напарника (ease-out, лёгкое перерегулирование для радости), использовать каскад для появления элементов.


---

## 4. Squash and stretch: растяжение читается как скорость, сплющивание как вес
`анимация · маскот · крафт` · [04:15](https://youtu.be/ws0x6Oyiza8?t=255)

**Мысль:** Добавление растяжения и сплющивания превращает твёрдый камень в мягкое живое существо без других изменений; площадь сохраняют, добавляют пружинку при ударе.

**Слова автора:**

> Idea three, squash and stretch. Borrowed straight from classic animation, a fastmoving ball stretches along its direction of travel and squashes when it slows. We measure the speed, rotate to face the velocity, and scale one axis up and the other down so the area stays the same. Then we add a tiny spring. On every hit, the ball wobbles and the paddle squashes like it absorbed the impact. Now drag the stretch amount up and watch the ball go from a rigid to something rubbery. Side by side, on the left, the ball is a perfect circle always. On the right, it leans into its motion. Your brain reads stretch as speed and squash as weight. The book game feel by Steve Swink tells a story about the game to blob. Adding squash and stretch to a ball made it go from feeling like solid stone to feeling soft and alive with no other change.

**Для Напарника:** Для лёгких касаний и реакций (не трогая MascotSvg): небольшая упругость при появлении элементов острова.


---

## 5. Тряска пропорциональна силе удара, пауза ощущается, а не видна
`анимация · хаптика · крафт · вкус` · [05:20](https://youtu.be/ws0x6Oyiza8?t=320)

**Мысль:** Использовать trauma в квадрате, чтобы малые удары почти не двигали, а большие били; микропауза в 50 мс чувствуется. Слишком сильная тряска тошнотворна, хорошая ощущается больше, чем видна.

**Слова автора:**

> The famous one, screen shake. Instead of a fixed shake, we use a trauma value. A trick from Squirrel Eisera's camera talk at GDC. Each hit adds trauma and trauma slowly drains away. The shake offset is trauma squared times a strength. So small hits barely move and big hits really kick. We also add hit stop from Jan William Nijman's talk the art of screen shake. Freeze the game for 50 milliseconds on every brick. You don't see the pause, you feel the impact. Now compare. The left side hits bricks politely. The right side hits them like it means it. Let's turn the strength right up. That's too much and it's honestly a little nauseating. Now back down to about 10. Both talks make the same point here. Screen shake is powerful, so use it with care and keep it short. A good shake is felt more than it's seen.

**Для Напарника:** Принцип для хаптики и эффектов: масштаб отклика пропорционален значимости события, короткий и умеренный.


---

## 6. Разрушение вместо исчезновения: у каждого удара есть начало, середина и конец
`анимация · игровой-дизайн · крафт` · [07:14](https://youtu.be/ws0x6Oyiza8?t=434)

**Мысль:** Падающие, вращающиеся и затемнённые кирпичи делают удар тяжёлым и дают маленькую историю; затемнение сохраняет читаемость.

**Слова автора:**

> A brick that gets hit simply vanishes. The talk went through several versions. Fade it out, make it fall, let the ball push it, make it spin, and finally make it darker so it doesn't blend with the live bricks. We'll do all of that in a few lines. When a brick breaks, we push a copy into a falling list, carrying some of the ball's velocity in a random spin. Gravity takes it from there. Compare the two. On the left, bricks just blink out of existence. On the right, every brick tumbles away, spinning, pushed in the direction it was hit. It makes the ball feel heavy, and it gives every hit a little story with a beginning, a middle, and an end. The darker color matters, too. It keeps the falling pieces readable, so you never confuse them with bricks that are still in play.

**Для Напарника:** Завершённый шаг может не просто исчезать, а с мягким уходом/превращением во что-то (искра -> часть острова).


---

## 7. Дай объекту лицо: глаза следят за мячом, и ты за него болеешь
`персонаж · маскот · вкус · анимация` · [08:11](https://youtu.be/ws0x6Oyiza8?t=491)

**Мысль:** Два зрачка, следящие за мячом, и улыбка после удара превращают платформу в персонажа, за которого начинаешь болеть.

**Слова автора:**

> Give the paddle a face. Two eyes whose pupils follow the ball and a mouth that grins after every hit. It sounds silly, but suddenly the paddle is a character and you start rooting for it.

**Для Напарника:** Подтверждает ценность кота-присутствия: его взгляд, следящий за действиями пользователя, создаёт эмпатию.


---

## 8. Эффекты работают в наслоении, но избыток прячет важное: дозируй и дай reduced motion
`анимация · доступность · крафт · вкус` · [09:39](https://youtu.be/ws0x6Oyiza8?t=579)

**Мысль:** Ни один слой сам по себе не драматичен, их сумма превращает прототип в игру; при слишком большом juice важное теряется, нужен вариант без движения.

**Слова автора:**

> No single step is dramatic on its own. It's the stacking that turns a prototype into something you want to keep playing. One last trick, a single juice dial that scales every effect at once. At zero, we're back to a clean, colorful game with no feedback at all. At 1.5, it's chaos with particles everywhere and the screen jumping around. A research survey on game field points out exactly this risk. Too much juice can hide what actually matters in the game, so tune it and give players a reduced motion option.

**Для Напарника:** Поддержка prefers-reduced-motion для анимаций острова и ограничение числа слоёв эффекта на финале.
