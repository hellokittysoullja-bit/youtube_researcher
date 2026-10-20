# Designing on expert mode

**Канал:** Dive Club 🤿 · 9 мин · субтитры: en (авто YouTube) · https://youtu.be/fJP4MKnx81s

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. На мобильном жесты и движение это сам дизайн, а не easing в конце
`мобильный · анимация · крафт` · [01:09](https://youtu.be/fJP4MKnx81s?t=69)

**Мысль:** Мультитач-жесты расширяют возможности, и интеракция определяет качество, а не добавляется финальным штрихом.

**Слова автора:**

> This becomes especially true when you're designing for mobile because touch gestures really raise the ceiling for interaction design just take it from Gavin Nelson who's designing the linear mobile app you don't have things like hover States but you do have things like multi-touch gestures on iOS for example it applies a unique set of constraints but it also like opens up a whole new world of possibilities and that's where a lot of I find nice interaction designed to come in on mobile all of a sudden the interactions aren't the easing curves that you're slapping on at the end of the process they're the design itself.

**Для Напарника:** Жесты (drag-to-reply, свайпы) проектировать как основу взаимодействия на 390px-вьюпорте, тестируя на реальном устройстве.


---

## 2. Приложение должно ощущаться «живым», а не торговым автоматом
`анимация · вкус · крафт` · [02:13](https://youtu.be/fJP4MKnx81s?t=133)

**Мысль:** Netflix сделал общий переход от арта к странице деталей, не прикручивая интеракции поверх готового дизайна; вкус теперь это ещё и внимание к тому, как приложение движется.

**Слова автора:**

> They wanted to figure out how can we make this app feel a little bit more alive and dynamic right versus kind of like a vending machine or something like that I think one of the first ones that we knew we wanted to do was that shared transition from the artwork to the detail page that's seemed kind of like a no-brainer right it's like okay we have this like beautiful artwork already we can make that detail page more immersive right it wasn't like we designed this new art direction for the homepage and then figured out like oh how do we like tack on interactions right we wanted the whole thing to feel very cohesive we talk a lot about improving your taste by paying attention to pixel level details and recreating the UI of your favorite apps but the thing that I'm paying attention to more and more is how apps move and the little details that make an interaction special.

**Для Напарника:** Переходы между Домом, Фокусом и Миром (общий AppBackdrop) должны быть связными, а не «тоже анимированными»; детали движения тренируют вкус.


---

## 3. Если движение ощущается неправильно, красивые статичные макеты не спасут
`анимация · крафт` · [04:03](https://youtu.be/fJP4MKnx81s?t=243)

**Мысль:** Для интерактивных продуктов поведение и есть дизайн; нельзя подделать ощущение.

**Слова автора:**

> In Amy's case the way that the split panel moves is the design I mean if it doesn't feel or behave in the right way then it doesn't matter how pretty the static mocks are it's like when Jam was talking about working on interactions for the iPad pointer you can't fake anything there right if you make something and for some reason it feels off or it feels bad the experience of using this product just now feels bad.


---

## 4. Прототип, неотличимый от прода, это универсальный язык обратной связи
`процесс · исследования` · [05:55](https://youtu.be/fJP4MKnx81s?t=355)

**Мысль:** Если интеракция ядро дизайна, проверять её нужно в фиделити продакшена: дать человеку выполнить реальную задачу и посмотреть, лёгко ли и сколько тапов.

**Слова автора:**

> The quality of what you're designing is dictated by the interaction itself you can't wait too long in the design process to make something that feels real at that point I might turn to prototyping to put together a very low Fidelity prototype that has kind of a higher Fidelity implementation of the interaction just to test it out and see like okay that doesn't work or it needs to change in this way make it as kind of indistinguishable from what I might see in production if it was built over an engineering cycle and the goal with that being is you can just hand that to someone and say what do you think of this does it work maybe there's a little context setting of like what the goal is of this like what you're trying to get done but you hand it to someone and you say like change the properties on this linear issue and that is a real life user test in a way like can they do it do they find it easy does it take them way too many Taps to do when you have that prototype that may be just entirely spaghetti code that's never actually going to ship in the background but it creates this very high fidelity thing that's indistinguishable from production that's like the universal language of getting feedback and just like testing your idea for real.

**Для Напарника:** Проверять Фокус на реальных данных и в живом рендере (CLAUDE.md §6), а не по макету.


---

## 5. Каждый слой абстракции даёт отговорку: чем ближе к реальному, тем больше ответственность
`процесс · крафт` · [08:10](https://youtu.be/fJP4MKnx81s?t=490)

**Мысль:** Чтобы иметь убеждённость в решении, нужно трогать и чувствовать дизайн; слои абстракции позволяют сбросить ответственность.

**Слова автора:**

> Designer is choosing between the best options of course you're going to rely on your gut and your intuition but you want to have conviction with whatever solution you're putting forward how can we get to that conviction if we don't even touch and feel our designs it's like a sculptor that spends all their time drawing a picture of the 3D sculpture and then spends the last 10% with their hands in the clay the more layers of abstraction that we add it increases our comfort zone because for every layer of abstraction is an excuse or a finger point to something else or someone else where I then don't have to take accountability the closer you get to the real thing also increases your level of accountability and responsibility.
