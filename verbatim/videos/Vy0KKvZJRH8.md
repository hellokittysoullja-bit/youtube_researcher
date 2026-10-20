# Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)

**Канал:** Kole Jain · 9 мин · субтитры: en (авто YouTube) · https://youtu.be/Vy0KKvZJRH8

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Оптимистичный UI: считаем успех, пока фон завершает
`доверие · микрокопирайтинг · крафт` · [01:59](https://youtu.be/Vy0KKvZJRH8?t=119)

**Мысль:** Приложение показывает результат сразу, предполагая успех (как Apple Mail убирает письмо в корзину до удаления на сервере), что делает отклик мгновенным.

**Слова автора:**

> Examples of optimistic UI since we're processing and saving the image in the background, but we just assume that it will succeed, which is why we're optimistic. Apple Mail and many other applications follow this pattern, moving the email to trash before it's actually deleted off the server.

**Для Напарника:** Шаг, отмеченный выполненным, сразу отражается на острове, а синхронизация идёт в фоне (всё в localStorage).


---

## 2. Пустое состояние и поэтапное раскрытие: показывай только нужное сейчас
`онбординг · иерархия · стыд · доступность` · [03:27](https://youtu.be/Vy0KKvZJRH8?t=207)

**Мысль:** Пока нет данных, фильтры и компоненты скрыты; данные показываются по клику. Вопрос: какой минимум интерфейса позволяет контенту сиять.

**Слова автора:**

> Just like when you get a clear empty state when you have no notes, we'll have a simple empty state inviting the user to start saving inspiration. This is a form of progressive disclosure, only showing the user what they need to see in that moment. All of the filters and other components are hidden because they simply aren't useful until the user starts saving inspiration. Another good example of this is when we do have images only showing all of the data when the user actually clicks on the image. So before adding colors or effects, ask yourself this. What is the minimum UI needed to really let that content shine?

**Для Напарника:** Пустой остров и пустой план: «Плана нет, и это ноль», приглашение начать; остальное раскрывается по мере появления данных.


---

## 3. Тёмную и светлую темы не делай точными инверсиями
`цвет · дизайн-система · вкус` · [05:05](https://youtu.be/Vy0KKvZJRH8?t=305)

**Мысль:** В тёмной теме нужны более различающиеся цвета; прямая инверсия даёт слишком высокий контраст в светлой. Темы должны ощущаться разными, но согласованными.

**Слова автора:**

> Directly inverting the colors looks okay. This is because dark mode requires colors that are more different from each other than light mode. Since there's less light and less differentiation when we directly invert to light mode, the contrast is much higher and it doesn't look stellar. If we collapse the colors to be more similar, it looks a lot more refined. Design light and dark mode not as exact opposites. They should feel different but consistent.

**Для Напарника:** Для Напарника актуален принцип разной насыщенности и оттенка при одинаковой светлоте фона; полной инверсии не делать.


---

## 4. Без видимого изменения человек решает, что что-то сломалось
`анимация · доверие · микрокопирайтинг` · [06:44](https://youtu.be/Vy0KKvZJRH8?t=404)

**Мысль:** Визуальная обратная связь на действие так же важна, как сама функция; микроанимации или смена состояния нужны, чтобы подтвердить выполнение.

**Слова автора:**

> The point is they're important, but arguably just as important is the visual feedback from it. If you don't see a change, you assume that something went wrong. That's why micro animations, or at least a state change, are instrumental.

**Для Напарника:** Любое нажатие (старт, шаг, чек-ин) должно давать видимое изменение, подтверждение в голосе кота, а не toast.
