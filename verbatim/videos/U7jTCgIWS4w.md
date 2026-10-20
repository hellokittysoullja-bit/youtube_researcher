# The INSANE Gap Between Average and World-Class UX/UI Design

**Канал:** uxpeak · 15 мин · субтитры: en (авто YouTube) · https://youtu.be/U7jTCgIWS4w

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Экран джуниора: мелкие фото, миф «всё above the fold», нет иерархии, две формы
`иерархия · дизайн-система · типографика · вкус` · [00:34](https://youtu.be/U7jTCgIWS4w?t=34)

**Мысль:** Фото 56 px показывают, что в миске что-то есть, но не вызывают аппетит; «втиснуть как можно больше выше сгиба» устарело, потому что все скроллят. Нет иерархии (13 px против 11.5 px, всё серым) и смешаны два языка форм (углы 4 px против кругов).

**Слова автора:**

> So, let's start with C. The screen a junior would design. There is one decision here they got right and four places where it goes wrong. The right one is the photos. They showed you the food instead of the restaurant's logo. A logo tells you who is selling. A photo tells you what you are eating and that is what you came for. Then the size. Those photos are 56 pixels. An image in a list can identify or it can create appetite. An appetite takes real space. At 56 pixels, you can see there's a bowl of something, but it doesn't make you want to eat it. And why is it so small? Because six restaurants fit above the fold at that size. Juniors and marketers usually want as much as they can get above the fold. That is the first mistake, and it's still being taught as a good thing. Everybody scrolls now. What matters is whether the first thing somebody sees is worth continuing for, not how much you fit before the cut. We cover this in much more detail in our UX Peak Plus platform because there is more nuance to it. Second mistake, filters and sort are hidden inside two drop-downs with 17 options behind them you would never know about. Third, the card has no hierarchy. The name is 13 pixels. Everything under it is 11.5, all on one gray line at the same size and color. If you cannot say which element somebody should read first, they will not be able to either. And fourth, every corner here is four pixels while the category images are circles. Two different shape languages on the same screen.

**Для Напарника:** Главная картинка (кот, остров) должна быть достаточно большой, чтобы вызывать эмоцию; один визуальный приоритет на экран; единый язык скруглений во всём /app.


---

## 2. Мид: иерархия важнее всего остального — название выше, остальное отступает
`иерархия · дизайн-система · отступы · сетка` · [02:04](https://youtu.be/U7jTCgIWS4w?t=124)

**Мысль:** Увеличенные фото, единые скругления, лучше отступы и цвет; но главное — иерархия: название выходит вперёд, остальное затихает, так список можно сканировать, а не читать. Фильтры видимы.

**Слова автора:**

> Same six restaurants and four things change. The photos change from a square to a rectangle, get three times wider, and become the biggest thing on the card. The corners are rounder now, and the same rounding runs across the whole screen. The screen is more polished all around. The spacing is better. There's more white space and the colors are handled with more care. And there is hierarchy which matters more than any of it. The name steps up. The rating takes the star and the weight. And everything else drops back. That is what lets you scan a list instead of reading it. And the filters are visible. Eight ships sitting on the screen tapable. What the junior buried is now something you can find.

**Для Напарника:** На Доме: один главный элемент, остальные приглушены (depth-fade). Спрятанное в меню перенести на поверхность, если часто нужно.


---

## 3. Сеньор: кастомные иконки вместо конкурирующих фото, счётчик результатов, выбор вида
`иерархия · иконки · игровой-дизайн · вкус` · [02:37](https://youtu.be/U7jTCgIWS4w?t=157)

**Мысль:** Собственный набор иконок даёт личность и убирает конкуренцию между изображениями; показ количества результатов помогает понять объём; когда нет верного значения по умолчанию для всех, дайте пользователю выбор раскладки.

**Слова автора:**

> Then D, the senior. The photos get even bigger as they go full width and take over the card. The category row stops being photos and becomes a custom icon set. That does two things. It gives the app a personality that the stock photos do not. And it stops six food photos competing with the six food photos directly underneath them, so the actual meals stand out more. The quick filters are still here. And next to them, there is now a filter button that you can tap on and see more filter options that you can apply. With the sort button sitting beside it, that's exactly where Zomato, Swiggy, and Global put theirs. And there is account now 640 places. You know how much you are looking through, which changes how you approach it. And then the layout switch, cards, or a compact list. Big photos make you want food. A list lets you compare quickly. And some people might prefer the second one. So instead of choosing for everybody, the senior lets you choose. When there is no correct default for everybody, give people the control,.

**Для Напарника:** Мир/остров: декоративные элементы не должны конкурировать с главным. Когда у выбора нет универсального дефолта (плотность присутствия кота) — оставлять человеку управление.


---

## 4. Стафф: плейсхолдер говорит, что искать, персональная метка «лучшее совпадение», детали вне фото
`микрокопирайтинг · иерархия · дизайн-система · ИИ` · [03:45](https://youtu.be/U7jTCgIWS4w?t=225)

**Мысль:** Подсказка в поиске называет, что можно искать; метка на основе знания о пользователе; текст вынесен с фото, чтобы карточка выглядела одинаково при любой загруженной картинке.

**Слова автора:**

> Which leaves B, the staff screen, which takes all of that further. The search placeholder says what you can actually search for, places, dishes, or cuisines. The icons and their backgrounds are cleaner and quieter, so the row stays out of the way of the food. The top card carries a best match label based on what we know about the user. and the main one, the name and the numbers come off the photo, which means the card looks the same whatever the restaurant uploads as its photo. Uber Eats builds its cards the same way. Photo on top and the details underneath.

**Для Напарника:** Плейсхолдер ввода шага в Фокусе называет примеры («Помыть две тарелки»); текст не кладём поверх изображения, чтобы контраст не зависел от картинки.


---

## 5. Требования нестрогие: фильтр помогает человеку выяснить, чего он хочет
`иерархия · исследования · процесс · игровой-дизайн` · [05:25](https://youtu.be/U7jTCgIWS4w?t=325)

**Мысль:** Люди готовы смягчить бюджет или число комнат, если это даёт лучшие варианты; задача фильтра не в скрытии несовпадающего, а в помощи сузить огромный набор, пока человек ещё определяется.

**Слова автора:**

> Sounds pretty simple, but this is where filters get interesting because those requirements usually aren't as fixed as they sound. Maybe you want three bedrooms, but if that leaves you with almost nothing, you'd probably consider two. Maybe you have a budget in mind. But if another 50,000 suddenly gives you much better options, you might be willing to stretch it. So the job of a filter isn't just to ask the user for a bunch of values and hide everything that doesn't match. It has to help them narrow down a huge set of options while they're still figuring out what they actually want. And this problem is everywhere. Shopping, flights, jobs, food delivery. You start with hundreds of thousands of options and somehow the interface has to help you get down to the few that are actually worth your time. That's what makes filters surprisingly difficult to design.

**Для Напарника:** Принцип выбора для Напарника: помогать выбрать задачу и длительность через рекомендуемый дефолт и подсказки, а не заставлять сразу назвать точное значение.


---

## 6. Простота «одной страницы на фильтр» перекладывает работу: 7 тапов и ни одного обратного сигнала
`иерархия · онбординг · крафт · доверие` · [08:09](https://youtu.be/U7jTCgIWS4w?t=489)

**Мысль:** Разные страницы для каждой настройки скрывают связанные решения, прячут результаты и не говорят, сколько будет совпадений. Выглядеть простым не равно облегчать решение.

**Слова автора:**

> Version A looks clean, but most of that simplicity comes from moving the work somewhere else. The junior designer is trying to keep things simple and clean. Instead of putting every control on one screen, each filter gets its own page. So, you have price, bedrooms, bathrooms, and home type, and you deal with them one at a time. At first, that seems like a pretty sensible way to reduce clutter. But once you actually use it, you start to see the problem. Let's say I want at least three bedrooms. I tap bedrooms, choose three, then go back. Now I want two bathrooms. I open bathrooms, choose two, and go back again. Then I finally tap show homes. That's seven taps just to set two basic filters. But the taps aren't really the biggest problem. The bigger problem is what happens every time you move to another page. When I'm choosing bathrooms, I can't see the bedroom choice I just made. I can't see my price range either. So, I'm making each decision separately, even though those decisions are actually connected. Maybe I want three bedrooms, but if that gives me almost nothing, I'd happily take two. Maybe another 50,000 suddenly opens up much better homes. That's the kind of trade-off you want to understand while you're filtering, not after you've finished. And the full page approach makes that harder, too. As soon as I open the filter, the homes I was just looking at disappear completely. There's also no feedback on the main action. The button just says show homes. I could have 41 matches. I could have four. I could have none. I only find out after I tap it. So, the junior designer has focused on making the interface feel simple by showing us less at once. But there's an important difference between making the interface look simpler and making the decision easier.

**Для Напарника:** Не дробить связанный выбор на отдельные экраны. Настройка сессии (шаг, длительность) на одном экране с видимым результатом.


---

## 7. Лист поверх результатов, слайдер + ввод, кнопка «Показать 41 дом»
`иерархия · микрокопирайтинг · мобильный · игровой-дизайн` · [09:49](https://youtu.be/U7jTCgIWS4w?t=589)

**Мысль:** Всё решение возвращено в одно место; слайдер для быстрого исследования диапазона и ручной ввод для точности; степперы медленны, когда число известно; кнопка действия сообщает результат заранее.

**Слова автора:**

> Version B fixes the biggest problem with version A. It brings the decisions back together. The filter no longer takes over the whole screen. Instead, it opens as a sheet over the results. So, you still have some sense of the page you came from and what you're filtering. And instead of hiding bedrooms and bathrooms on separate pages, everything now lives in one scroll. That makes it much easier to balance the choices against each other. Maybe I start with three bedrooms, then adjust the budget, or I drop to two bedrooms and see whether that gives me much better options. Price is also easier to adjust. Instead of relying only on manual inputs, we now have a slider. A slider is useful when you want to quickly move through a range and get roughly where you want to be without having to type a new number every time. And if you already know your exact budget, the manual inputs are still there, so you get both quick exploration with the slider and precision when you need it. There's one choice I wouldn't make, though. Bedrooms and bathrooms use steppers. Plus and minus works well when you're nudging a number you already have, like the quantity in your basket or the temperature on a thermostat. But if I already know I want three bedrooms, making me tap my way up to three is slower and it hides the other options from me. And finally, the button is much more useful. Instead of just saying show homes, it tells me exactly what my current filters will return. Show 41 homes. So before I apply anything, I already know whether I've narrowed the search too much or not enough.

**Для Напарника:** Кнопка «Начать» может говорить, что произойдёт («Начать на 25 минут»); для длительности — чипы с видимыми вариантами, а не степпер +/-.


---

## 8. Гистограмма за слайдером: контрол показывает рынок, а не только просит цифру
`иерархия · метрики · игровой-дизайн · вкус` · [11:15](https://youtu.be/U7jTCgIWS4w?t=675)

**Мысль:** Распределение цен позволяет увидеть, где сосредоточено большинство вариантов и что даст небольшое увеличение бюджета: решение принимается осознанно.

**Слова автора:**

> Version C goes beyond making the filter easier to use. It starts helping you make the decision. The first thing you'll notice is the price filter. We still have the slider and manual inputs from the mid version, but now there's also a histogram behind the slider. That histogram shows the distribution of the available homes across different prices. So before $700,000 and $750,000 were just two numbers on a range. Now I can actually see whether most homes are clustered around that price, whether I'm already near the edge of the market, or whether stretching my budget a little would suddenly open up a lot more options. So instead of blindly moving the slider and waiting to see what happens, I can understand the market while I'm adjusting it. The control isn't just asking me for a price anymore. It's showing me what's actually available, so I can make a more informed trade-off.

**Для Напарника:** Идея для статистики Мира: вместо одной цифры показывать контекст (как выглядит неделя, где пик), чтобы человек видел собственный ритм без оценки.


---

## 9. Видимые варианты вместо степперов; «3+» совпадает с мышлением человека
`иерархия · микрокопирайтинг · дизайн-система · мобильный` · [12:11](https://youtu.be/U7jTCgIWS4w?t=731)

**Мысль:** Все значения видны сразу и доступны одним тапом; «3+» отражает то, что человек думает («минимум три»), и не отсекает варианты с четырьмя.

**Слова автора:**

> The steppers are gone, and now all the options are visible at once. So, if I want three bedrooms, I can just tap three plus instead of tapping my way up to it. And the plus is important. We said at the beginning that we want at least three bedrooms, so choosing three shouldn't accidentally remove every four-bedroom home from the results. If I really do want exactly three, I can still choose that separately. That's a small detail, but it matches the way people actually think about this kind of search.

**Для Напарника:** Чипы длительности (15/25/45) видимы сразу, без степпера. Подписи варианта формулировать так, как человек думает о задаче.


---

## 10. D: контекст и пересчёт под человека, счётчик результатов у каждого варианта до выбора
`иерархия · ИИ · микрокопирайтинг · игровой-дизайн` · [12:55](https://youtu.be/U7jTCgIWS4w?t=775)

**Мысль:** Интерфейс показывает медиану, долю подходящего и переводит понятные человеку величины (депозит и ежемесячный платёж) в нужный параметр; у каждого варианта сразу видна цена выбора, без цикла «выбери — посмотри — вернись».

**Слова автора:**

> Version D doesn't just show you the market. It starts connecting that market to your search and your own budget. You can see that immediately in the price section. We still have the histogram from the senior version, but now there's even more context around it. If I've selected three plus bedrooms, I can see that I'm looking at 3 plusbedroom homes, their median price, and on the right that 459 out of 1,557 homes currently fit my filters. So, I'm not looking at price in isolation anymore. I can immediately understand how much of the market actually fits what I'm looking for. And then there's the bigger change underneath. Because when someone asks, "What's your maximum price?" You might not actually know. What you may know is, "I have $65,000 for a deposit, and I'd be comfortable spending around $5,000 a month." So, instead of forcing me to somehow turn those numbers into a house price myself, the product does that work for me. I enter my deposit, my comfortable monthly payment, and the interest rate, and it works out roughly what price I can shop at. Then, it places that limit directly onto the histogram. Now I can see the market, the homes that match my filters and where my own budget cuts through all of it in the same place. That's much more useful than asking the user to guess a maximum price and then discover later whether it was realistic. Then we get to bedrooms and bathrooms. And there's another important change here. Each option now shows how many homes I'd get before I choose it. Maybe three bedrooms leaves me with 459 homes, while four leaves me with 229. So I can see what making the filter stricter will cost me before I make the decision. Instead of choose something, see what happened, go back, try something else, the interface gives me that information upfront.

**Для Напарника:** Дробление задачи: показывать «что будет» до выбора (например, «3 шага, около 10 минут»). Просить в терминах, понятных человеку, а не заставлять пересчитывать.


---

## 11. Цена информации: решить, что помогает решению, а что только шум
`иерархия · вкус · внимание · СДВГ` · [14:56](https://youtu.be/U7jTCgIWS4w?t=896)

**Мысль:** Каждая добавленная информация делает интерфейс занятнее, поэтому нужен критерий: помогает ли она принять решение.

**Слова автора:**

> The trade-off is that all this extra content makes the interface busier. So, the challenge is knowing what information genuinely helps the decision and what just adds noise.

**Для Напарника:** Критерий для любого нового элемента на Доме/Фокусе: помогает ли он сделать следующий шаг прямо сейчас. Если нет, не добавлять (Hick's Law).
