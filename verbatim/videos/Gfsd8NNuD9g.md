# Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)

**Канал:** Kole Jain · 7 мин · субтитры: en (авто YouTube) · https://youtu.be/Gfsd8NNuD9g

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Нижняя панель: 3–5 пунктов, цель касания больше 44px
`мобильный · доступность · иерархия` · [00:23](https://youtu.be/Gfsd8NNuD9g?t=23)

**Мысль:** На мобильном вместо сайдбара плавающий нижний бар, где пять ссылок это предел, а три-четыре идеал; это гарантирует цель больше 44 пикселей.

**Слова автора:**

> Obviously the navigation. Where we had an expansive sidebar, we now definitely do not. So, we have two options. If we can consolidate our sidebar links down to just a few key icons, we can go with a nice bottom bar, which nowadays is typically floating with the important action broken out just like this. Five links down here is pretty much the definite limit, and three or four is much more ideal. But, either way, this means that we'll always maintain over a 44-pixel target since people do have fat fingers.

**Для Напарника:** AppNav с тремя пунктами (Дом, Фокус, Мир) уже в идеале; проверить высоту цели касания не менее 44px.


---

## 2. На телефоне крупнее шрифт и выбор одного: один блок, одно направление
`мобильный · типографика · иерархия` · [01:37](https://youtu.be/Gfsd8NNuD9g?t=97)

**Мысль:** База шрифта iOS 17px против 13px у macOS, поэтому на малых экранах всё крупнее. Из набора десктопных блоков остаётся один, и секция течёт либо вертикально, либо горизонтально, но не в обе стороны.

**Слова автора:**

> Despite our screen getting much, much smaller, the type scale and spacing remains relatively similar to desktop, even getting a bit larger. iOS actually has a base font size of 17 pixels, while macOS has a base of only 13 pixels. So, more often than not, things actually get larger on these smaller screens. And it's a tough realization that on desktop, where you could have had an action bar, a gallery of recent notes, a full calendar, tasks, and a scratch pad, now you can pick one of those things. And because we have to pick just one, the way we start to lay out content starts to change a little. Dashboards and desktop designs can lay out content in two directions at the same time. What that means is this layout has two columns and three rows, obviously extending in both directions. However, on mobile, you can choose one direction to move in per section. Either you can stack each note vertically, or you can make it horizontal off the page, but of course, you can't have both like you reasonably could on desktop. This is a useful guideline when taking content from dashboards and making it mobile-optimized. And if you understand that concept, things really start to become a piece of cake.

**Для Напарника:** Не втискивать в Дом много блоков: на 390px показывать одну главную цель и один способ прокрутки в секции.


---

## 3. Карточки как основной блок; не вкладывай карточки друг в друга
`отступы · мобильный · иерархия` · [02:46](https://youtu.be/Gfsd8NNuD9g?t=166)

**Мысль:** Карточки группируют содержимое вместо пустого пространства, но двойная вложенность создаёт отступ на отступе и сжимает место. Часто группировку можно сделать пробелом.

**Слова автора:**

> There's really only four types of building blocks for an app. The biggest and most important are cards. Basically, everything on here is a card in some way or another because it allows us to flexibly group content in place of white space, which we don't typically have a lot of here. The others are text or links, of course, images, and inputs. And of course, any of those can be put into cards as well. One important note about cards is to try and avoid double-nesting them, kind of like this. It's not always avoidable, but it creates padding on padding, which really restricts the space you have and ends up cramping things. Often, you can group with white space instead of a container and somewhat alleviate this problem.

**Для Напарника:** Не класть карточки в карточки на Доме и Фокусе; группировать связанные кнопки расстоянием.


---

## 4. Один экран делает одно; контекстный выбор через bottom sheet
`мобильный · иерархия · СДВГ` · [03:29](https://youtu.be/Gfsd8NNuD9g?t=209)

**Мысль:** Настройки это только настройки, редактор это только редактор. Когда нужен выбор в контексте, нижняя шторка оставляет пользователя на месте.

**Слова автора:**

> One screen does one thing, and that's it. Obviously, the very notable exception is our home screen, but otherwise, the settings is just settings, and the notes editor is just a notes editor. We don't throw in clutter like recent notes or suggested templates at the top. Instead, whenever you need to add something new, don't reach for a different layout, reach for a different page altogether. Though, this example about templates brings up an interesting point about context. We're editing a note, so we don't want to be ripped away to a new page to select a template, but we don't have enough room on screen. This is where bottom sheets become super useful. This is a bottom sheet. You've probably seen it a bunch, and now we can simply add in a title, search bar, and a check and X, and all of our templates, too. These can be any height, but they keep the user in context and are easy to navigate with.

**Для Напарника:** Фокус остаётся экраном одной цели; выбор длительности и шагов можно вынести в нижнюю шторку, а не на отдельную страницу.


---

## 5. Свайпы можно использовать широко, если научить пользователя
`мобильный · онбординг · анимация` · [05:28](https://youtu.be/Gfsd8NNuD9g?t=328)

**Мысль:** Жесты в современных приложениях привычны, но на них можно опираться, только объяснив пользователю, как они работают.

**Слова автора:**

> Swipes are everywhere in modern mobile apps, so as long as you educate the user on how to use them, they can be relied on pretty.

**Для Напарника:** Для drag-to-reply в пузыре чата нужна мягкая подсказка при первом появлении, а не молчаливый жест.


---

## 6. Два типа пустых состояний: первый вход и отсутствие результатов поиска
`онбординг · микрокопирайтинг · мобильный · активация` · [06:22](https://youtu.be/Gfsd8NNuD9g?t=382)

**Мысль:** При первом входе внимание направляют на главное действие и короткий поповер, а при пустой выдаче дают картинку, признание ситуации, подсказки и действие выхода.

**Слова автора:**

> Finally, what we've designed here is an ideal state. The app is filled with content, but don't forget what the user sees the first time they log in when there is no content. We could have cards inviting user to start adding in events, tasks, and notes, but instead, let's draw attention to the plus button, which is our main action, and add in a full-screen empty state to simplify things. Then, we have a simple popover instructing them on how things actually work. But, there is also another type of empty state, which is when we search for a note, for example, and get no results. Instead of just an instruction, we should have some nice imagery, and we need to acknowledge that there are no notes matching the existing keywords, and then perhaps give them a few suggestions in case of a typo, and an action to exit the empty state.

**Для Напарника:** Пустой Дом и пустой остров должны указывать на одно действие (начать Фокус) тёплым голосом кота, без ощущения «пусто, значит провал».
