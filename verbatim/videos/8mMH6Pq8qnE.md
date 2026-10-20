# How I Make Apps FEEL 10x Better (5 Design Secrets)

**Канал:** Chris Raroque · 11 мин · субтитры: en (авто YouTube) · https://youtu.be/8mMH6Pq8qnE

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Системные приложения статичны; движение отличает ваше приложение
`анимация · мобильный · крафт` · [00:35](https://youtu.be/8mMH6Pq8qnE?t=35)

**Мысль:** Apple не анимирует переключение табов из-за масштаба аудитории, но небольшому продукту можно добавить уместную анимацию. Страницы, выезжающие друг за другом, дают ощущение пространства.

**Слова автора:**

> Another way to add dimension to your app is to make it more interactive and just have a little bit more movement. Most apps are pretty static. When you're clicking on tabs in any of the default Apple apps, they kind of just appear instantly. There's no animation, probably for a good reason. They're serving a billion users. Maybe it's a motion sickness thing or an accessibility thing, but again, we're not Apple. So, what I like to do is try to add animation anywhere I feel is appropriate. So, for example, in my app Luna, I could have made it where when you're switching between the tabs, it just instantly appears like all of the default iOS apps, but instead, I decided to actually animate that page change.

**Для Напарника:** Переходы между Домом, Фокусом и Миром можно сделать мягким горизонтальным сдвигом, сохранив общий AppBackdrop неподвижным как мир вокруг.


---

## 2. Составная анимация действия: иконка превращается, фон расходится, текст затухает
`анимация · награды · крафт · вкус` · [01:18](https://youtu.be/8mMH6Pq8qnE?t=78)

**Мысль:** Кнопка отправки превращается в галочку, фон расширяется от микрофона, текст гаснет пружиной. Сотня таких мелочей складывается в ощущение премиальности.

**Слова автора:**

> Here's an even better example of where I went a little bit above and beyond on the interactions. So, I have this feature in Ellie where you can dictate tasks to the AI assistant that I built. So, something I spent a lot of time on was a custom animation sequence. When I slow it down, you can see a lot of things are happening here. The send button rotates into a check mark. The background expands from the microphone and the listening text fades with this kind of spring animation. And all of this stuff adds up to a really satisfying animation that I think adds a little bit more to the experience. This might seem small, but if you do this a 100 times throughout your app, it's going to add up to this very premium experience,.

**Для Напарника:** Старт сессии и подтверждение шага могут быть связной последовательностью (кнопка превращается в галочку, кот реагирует) вместо мгновенного переключения.


---

## 3. Сложную анимацию не заказывай одним промптом: разбей на подшаги
`процесс · анимация · крафт` · [02:01](https://youtu.be/8mMH6Pq8qnE?t=121)

**Мысль:** Если описать каждый под-эффект отдельно (стрелка превращается в галочку, фон расширяется, текст гаснет), ИИ исполняет это безупречно, а общий запрос даёт банальный результат.

**Слова автора:**

> Don't try to oneshot this and say, "Hey, can you go animate this for me?" Because it's not going to come up with anything this cool and complex. For this one, I had to break down all the sub animations that I wanted to happen. Can you make the arrow rotate into the check mark? Can you have that background expand from the microphone? Can you add some of this fade in fade out for the text? So, I broke down all the components I wanted to happen in the interaction and it just executed it for me flawlessly. Apple has a really good built-in API for animations and Claude Code and a lot of AI coding tools are very well trained on it. So, you can actually just tell it to do this stuff for you in plain English and it has a really high chance of doing it. But again, the trick is to not oneshot it and to instead break it down.

**Для Напарника:** При постановке задач ИИ на хореографию (RevealIsland) перечислять последовательность подшагов с таймингами.


---

## 4. Пустые состояния с иллюстрацией; один базовый маскот и бесконечные вариации
`маскот · персонаж · геймификация · вкус` · [02:45](https://youtu.be/8mMH6Pq8qnE?t=165)

**Мысль:** Вместо текста «ничего нет» маскот занимается делом (ищет, пьёт кофе, спит). От базового образа от художника можно генерировать множество вариаций, и это добавляет личность.

**Слова автора:**

> Tip number two is custom illustrations, especially for things like empty states. So, this is when your app has no data in it and it's just kind of an empty screen. A lot of apps just have a text that say there's no task for today or something like that. I want to go a step beyond that. Add custom illustrations or even animations to those empty states. This is something you can actually do with the AI tools on the market. So, in my case, for my app, Lily, which is a meeting assistant app, I have this ghost mascot. What's really cool with AI tools like chat GPT, you can actually take a base mascot like Lily, feed it into chat GPT, and with the right prompts, you can actually generate almost an infinite amount of variations of this mascot. I actually used it to generate the empty state for the search page. Now, instead of it just saying there's no meetings here, instead there's this illustration of Lily the Ghost searching for tasks. Or if there's an active meeting going on, I can have a custom illustration of Lily taking notes or sleeping or drinking coffee or walking my dog Luna. AI has really opened the door to make infinite illustrations and it does add a ton of personality and really makes your app stand out. My recommendation is to try to find some sort of artist or illustrator to make you a base illustration if you can. My case, I actually asked my girlfriend Cecilia to draw up some illustrations for me and now I have a base mascot to work off of and make an infinite amount of variations on. I really do recommend starting with custom illustrations because it does make it feel a lot more original. If you can't do that, you can use chatt to make these mascots for you. My advice is to be really creative when you do this. You're going to feed in reference images. Try to feed in a bunch of different reference images. That way, it just comes up with something a little bit more unique or really tweak the prompt and try to get creative to make it deviate from whatever references you're putting in. But again, if possible, I do recommend commissioning an artist or a graphic designer.

**Для Напарника:** Пустое состояние Дома и Мира («плана на сегодня нет — это ноль») показывать с котом, занятым делом, при этом не меняя общий MascotSvg ради одного экрана.


---

## 5. Хаптика разной силы: лёгкая для частых действий, плотнее для смены вкладок
`хаптика · мобильный · дофамин` · [04:56](https://youtu.be/8mMH6Pq8qnE?t=296)

**Мысль:** Автор ставит хаптику почти на каждый клик, меняя силу, и считает это затягивающим, как щелчок ручкой.

**Слова автора:**

> Is haptic feedback. This is when you click a button, you touch the app, and the phone kind of subtly vibrates and gives this physical feedback back to the user. This is something that adds a lot of depth and honestly just makes the app a lot more fun to tap for the user. Something I noticed is that Apple's default apps barely use haptics. To be fair, there probably is a reason they don't have haptics. They're designing for a billion users. Maybe it's a battery thing or an accessibility thing, but we're not Apple, so we can probably make choices that they can. So, in my budgeting app, Luna, almost every single button click has some sort of haptic feedback. Here's the key. Not all haptic feedback is equal or feels the same. You can actually control the strength of the vibration in the code. So for certain buttons, I add a lighter amount of haptic feedback. And for other buttons, I do a heavy amount of haptic feedback. When you're inputting a transaction where there's a lot of clicks, I really go light, but then when you're doing something like changing the tabs, it's a little bit heavier. I really wish I could convey what the haptics feel like in the video, but if you're curious, I'm not going to stop you from downloading the app to try it. Concern that I hear is that if you add a lot of haptic feedback, it's going to feel annoying. But I think when you do it correctly in the right places, it's actually very satisfying. I think there's just something addictive about physical feedback, kind of like clicking a pen, you just kind of want to tap around.

**Для Напарника:** Частично не применимо: CLAUDE.md требует хаптику на события мира, а не на каждый тап. Полезна только идея градации силы: лёгкая для выбора в пикере, плотнее для наград.


---

## 6. Стиль иконок меняет характер приложения: тонкие, заливка или сложные
`иконки · дизайн-система · вкус` · [06:54](https://youtu.be/8mMH6Pq8qnE?t=414)

**Мысль:** Переход с тонкой версии набора на толстую меняет ощущение таб-бара, а три типа иконок передают разные сообщения.

**Слова автора:**

> The first mistake that I see people making is picking the wrong icon style. Even with something like Hero icons, which all the icons look amazing. The style of icons really does make a difference. So, let's take a look at the tab bar in Luna, which is my budgeting app. I'm using the thin version of the icon pack here. You can see it looks very clean, very minimal. Watch what happens if I just switch to the thick versions of this. To some people, this might not be a big deal, but the differences in using the thin and the heavy versions actually really does change the entire feel of this tab bar, which then changes the feel of the app. So, depending on what kind of feeling you're going for, I think picking the right icon set makes a big difference. Usually, it boils down to are you going to pick icons with simple and minimal lines? Are you going to pick icons that are more filled and heavy, or are you going to pick icons that are very complicated and have many lines? All three of these do send a different message to the user. So, choosing is very important.

**Для Напарника:** Выбрать для AppNav один характер иконок (тонкие линии в тёплом, прощающем тоне) и закрепить его.


---

## 7. Смешение стилей ломает цельность; заливка у активной иконки добавляет глубину
`иконки · анимация · крафт` · [07:47](https://youtu.be/8mMH6Pq8qnE?t=467)

**Мысль:** Единый стиль даёт единство, а для активного состояния можно использовать тяжёлую заливную версию той же иконки вместо простой смены цвета.

**Слова автора:**

> Is a very common thing I see a lot of apps do is mixing and matching icon styles which really make the app feel less cohesive. So looking back at Luna's tab bar, it's again very clean minimal icons. Watch what happens when I swap two of the icons to a heavier version. It's not as uniform as the version where it was all minimal icons. So when you pick a style, making sure to stay consistent across really does make a big difference. But there is actually a time when you can use style. So here's another tip. it's to potentially use a different style to show different states. So, for example, in the tab bar, when I click something on Luna, it starts out as the thin version, but I actually use the heavier and filled out version of the icon when it's selected, which actually does make a big difference. So, here's what it looks like in the app now with the heavier version. And here's what it would have looked like if I didn't use that version and just highlighted it. It's really subtle, but I think it does add some depth. Apple doesn't even do stuff like this. Check out the phone app. When you click on the different tabs, they're using the exact same icon style, but just changing the color, which does work, but again is a little bit basic. Spending a little bit more details on what icon style you're going to use for the active and the non-active state, which icon pack are you using. All of this stuff adds up and it will make the app feel even better than the Apple default apps.

**Для Напарника:** В AppNav активный пункт показывать залитой версией иконки, а остальные оставить контурными.


---

## 8. Вкус растёт от постоянного воздействия хорошего дизайна
`вкус · процесс · исследования` · [09:01](https://youtu.be/8mMH6Pq8qnE?t=541)

**Мысль:** Подписка на дизайнеров и закладки того, что нравится, формируют вкус постепенно, не за один раз.

**Слова автора:**

> Up with these good designs? How do I just elevate the feeling of my app in general? and it is to expose yourself to really good design constantly because it's not a one-time thing. I really do think that it is a process to get better and elevate your taste. And I have two specific places that I go to do this. Number one is Twitter. There's a ton of really good talented designers on Twitter. So, I recommend just go finding them, following a bunch of designers, and then you'll just see a bunch of their stuff on your feed and bookmark everything that you like.

**Для Напарника:** Вести папку референсов (зрелые дорогие сайты, как разрешает §10 CLAUDE.md) для каждой полировки экрана.
