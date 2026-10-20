# My App Design Process: What Took Me 5 Years to Learn in 10 Minutes

**Канал:** Chris Raroque · 10 мин · субтитры: en (авто YouTube) · https://youtu.be/H0czeRyXPxA

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Тестируй UX на реальном устройстве и с реальными данными
`процесс · крафт · исследования` · [01:36](https://youtu.be/H0czeRyXPxA?t=96)

**Мысль:** Фигма показывает UI, но UX проверяется только на устройстве; красивые фейковые данные и картинки скрывают проблемы, которые вылезают на реальных данных.

**Слова автора:**

> The reason I want to test it on a real device is I want to test the ux or the user experience figma is great to be able to see the UI and see how it looks but I found if you really want to test the ux you need to do it on a real device so you can actually simulate what it's going to be like in the real world for users and I try really hard to test it with real data because sometimes fake data makes everything look really good there are so many designs that I've seen that look amazing because they have really good high quality imag or specific texts that just fit the screen and look really good but then in production with real data and lower quality images it just doesn't look as good so I try to test it with my own data or as real data as possible just so I can catch some ux problems that the really good fake data was hiding.

**Для Напарника:** Это ровно §5.2 CLAUDE.md: проверять Дом/Фокус/Мир на реалистичных данных (9 стартов, а не 1) на реальном вьюпорте.


---

## 2. Отбрасывать красивое, если оно не служит функции
`процесс · крафт · иерархия` · [04:18](https://youtu.be/H0czeRyXPxA?t=258)

**Мысль:** Карточка с глубиной не добавляла смысла (глубина должна выделять); группировка по типу ломала порядок релевантности. Скучный классический список дал лучший UX.

**Слова автора:**

> The first prototype was this concept where the results are inside of a card and the card looked really cool once I physically saw it here mocked up I realized it kind of added some unnecessary depth to the app usually depth is added to highlight or Elevate something for example if we added depth to the search bar it would make that more prominent in the UI but in this case the depth being added to the search results didn't really add anything in my opinion so I know we got this inspiration from this mockup from Airbnb but it makes a lot more sense for them because they have this map in the background so they kind of want to show this and let things float over it but since we just have a white screen in the back and we don't really have anything behind it felt a little bit unnecessary so we decided to not go with that option so another concept was grouping the results by type so if the matches are from the task title they'd be grouped here if they're from the notes they'll be grouped here that made a lot of sense and from a UI perspective it really did feel like this would make the design a little bit more clean but one of the issues with this when we thought about it a little more is the way that my backend and type sense which is the service I'm using for search they return the results and it's ranked by relevancy so the order actually matters if we group things I realize it would actually impact that order let me show you guys an example in the ungroup version it could appear as the second result however in the grouped version it appears as result number four so because there would be an actual impact on functionality tried not to go with the grouping option either and the last concept that we tried was a more traditional search list that you see in a bunch of different other apps it is a little bit more boring compared to the first two but I felt like it had the best ux out of all the three options.

**Для Напарника:** Перед добавлением глубины/свечения/группировки спрашивать, что это выделяет; привязка к принципу из §10 CLAUDE.md.


---

## 3. Если не добавляет опыта, вырезать; заменить значимым элементом
`процесс · иерархия · крафт` · [06:40](https://youtu.be/H0czeRyXPxA?t=400)

**Мысль:** Иконки типа совпадения игнорировались, их убрали ради снижения когнитивной нагрузки; чекбоксы выполнено/нет вернули воздух и неожиданно улучшили сканирование. Лишние индикаторы тоже вырезаны.

**Слова автора:**

> The next thing I noticed was the icons on the left side which indicated what type of match the result hads for example this one showed there's a match on the note there's a match on the subtask it was really good in theory but when I was using it didn't seem that helpful I was kind of just ignoring the icons every time I ran a search so we decided to cut it because my philosophy is if something isn't adding to the experience it's best to just remove it so it reduces cognitive load on the users but then removing it the design felt super text heavy and I really loved how in these mockups there are icons on the left because it does break up the text a little bit and make it a little bit more breathable so we did try to brainstorm something to replace those icons luckily we realized we forgot to add the complete and incomplete indicators on the task like the literal checkbox that shows that a task was complete maybe we can just put those there and when we tried that I actually feel like the ux improved a little bit because it made searching for incomplete task a little bit easier it's just easier to scan and see oh these ones are incomplete so that was an unintended side effect that came out of that where I feel like the ux actually improved for some reason we just didn't think about doing this in the original design so that was a pretty cool thing that happened so on that note of looking for things to cut and simplifying the UI I was trying to look for more things that weren't that necessary for me or I was ignoring and one of the things I noticed is there's a couple of indicators on the task that I didn't feel like were relevant during the search process one example is this indicator on the task shows how much time was spent on the task this is really relevant on certain screens like the task list screen as I was searching and I was trying to put myself in the user shoes I felt like that task indicator wasn't that relevant to the search so for now we cut all the indicators except for label subtask and Note and I feel like that would cover most of what people are going to be looking for when conducting a search if people ask to bring back the indicators I'll reconsider it but for now we cut it just to keep things simple.

**Для Напарника:** Аудит Дома и Фокуса: убрать декор, который пользователь игнорирует; вместо него использовать смысловые элементы (статус шага).


---

## 4. Подсветка совпадений: выбрали жёлтый фон по быстрому опросу
`иерархия · исследования · цвет` · [08:29](https://youtu.be/H0czeRyXPxA?t=509)

**Мысль:** Три варианта подсветки решили не гадать, а спросить аудиторию; победил жёлтый фон, вероятно из-за ассоциации с маркером и быстрого сканирования.

**Слова автора:**

> Thing I noticed was the highlighting was pretty good where it bolds the text and makes it The Color Purple which is the primary color of the app but I felt like it could be a little stronger and maybe there was a way to make this a little bit more scannable so I remember seeing this example on the mood board and I really liked how they do highlighting I felt like my eyes could more quickly scan for highlights in this version so we tried a couple variations of this here were two more variations we came up with between the three options we were really torn on which one to choose so decided to throw a quick poll on Twitter to see which one people preferred and I want you to pause the video and try to figure out which one you think won the poll so the one that won was the one with the yellow background I can't definitively say why that won the pull but I think people just associate yellow with highlighting so maybe it was a little bit easier to scan but regardless because people chose this and we were already 50/50 on this one we decided to roll with the yellow highlighting.

**Для Напарника:** Для спорных микрорешений делать быстрые опросы; но жёлтый фон на тёмном коридоре светлоты Напарника проверять на контраст.


---

## 5. Мелкие детали: высота поля, делители, хаптика, авто-клавиатура
`хаптика · крафт · запуск-задачи` · [09:21](https://youtu.be/H0czeRyXPxA?t=561)

**Мысль:** Итерация идёт в мелочах: оттенок разделителей, вибро при очистке и выборе, автооткрытие клавиатуры на экране поиска.

**Слова автора:**

> Was playing with the height and size of the search box trying to figure out what shade of gray the dividers between each of the results would be not covered in the figma but what haptics we should add here there's a little vibration or haptic when you clear the search box or when you click on a search result a little tweak where when the user navigates to the search page the keyboard automatically opens up.

**Для Напарника:** Автофокус допустим на Фокусе (одна цель входа) и не на Доме (§4); хаптику вешать на события, а не каждый тап.
