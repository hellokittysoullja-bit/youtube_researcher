# WWDC25: Design foundations from idea to interface | Apple

**Канал:** Apple Developer · 19 мин · субтитры: en (ручные) · https://youtu.be/dGcqqA3Sl-o

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Три вопроса экрана: где я, что могу, куда дальше
`иерархия · онбординг · крафт` · [01:48](https://youtu.be/dGcqqA3Sl-o?t=108)

**Мысль:** Ясность экрана проверяется тремя вопросами; если ответ очевиден без усилий, приложение ощущается приглашающим и плавным.

**Слова автора:**

> When I look at an app, I want to find clarity — this makes the experience inviting and helps me use it confidently. That starts with knowing where I am. The app should make that clear right away — so I’m not left wondering where I am or how I got there. The next question is: “What can I do?” I shouldn’t have to guess — actions should be clear and easy to understand. And finally, I ask: “Where can I go from here?” A clear sense of next steps keeps the flow going and helps me avoid hesitation or second-guessing. When those questions are easy to answer, the app feels inviting and fluid.

**Для Напарника:** Проверять каждый экран Напарника (Дом, Фокус, Мир): заголовок/контекст, главное действие и следующий шаг видны сразу.


---

## 2. Каждая лишняя вкладка = ещё одно решение; действия не в таб-баре
`иерархия · мобильный · крафт` · [05:22](https://youtu.be/dGcqqA3Sl-o?t=322)

**Мысль:** Лишние табы заставляют принимать решения и усложняют вид приложения; табы для навигации, действия размещаются внутри экрана.

**Слова автора:**

> Simplifying it matters because each extra tab means one more decision for people to make and might present the app as much more complex that what it really is. So I pause and ask: What’s truly essential? What deserves a tab? One example of what doesn't? Crates. It’s just a screen to group Records. So I merge them. No need for both. Then there’s Add, it’s here in the tab bar because it’s the primary action of the app. But I start wondering — is this the best place for it? When I’m not sure when or how to properly use a component, I always go back to the Human Interface Guidelines. And sure enough: tabs are for navigation, not for taking action. So I’ll move Add inside Records where someone is most likely to use it.

**Для Напарника:** Держать AppNav минимальным (Дом/Фокус/Мир), не выносить действия вроде «начать» в таб-бар.


---

## 3. Progressive disclosure: показывать только необходимое
`иерархия · внимание · крафт` · [08:52](https://youtu.be/dGcqqA3Sl-o?t=532)

**Мысль:** Показывается лишь нужное для старта, остальное раскрывается по касанию в момент релевантности.

**Слова автора:**

> So what if now I show only a few groups, and let people uncover more as they go? That concept is called progressive disclosure. It’s about showing only what’s necessary upfront — just enough to help people get started then revealing more as they interact. You’ll see it anywhere an interface begins simple and gradually offers more detail or advanced options. So the rest of the content, is not missing, it’s just behind a tap on the disclosure control next to the title, waiting for the moment it becomes relevant.

**Для Напарника:** На Доме и Фокусе скрывать вторичное (длительность, очередь шагов) за раскрытием, не вываливать всё сразу.


---

## 4. Тест прищуривания: визуальный якорь размером и контрастом
`иерархия · цвет · вкус` · [13:55](https://youtu.be/dGcqqA3Sl-o?t=835)

**Мысль:** Прищурившись видно, куда идёт взгляд; главное нужно сделать крупнее или контрастнее, чтобы оно заметилось первым.

**Слова автора:**

> When I squint, my eyes go straight down to the first collection, because it’s visually heavier and colorful. Missing half of the content, and sense of place. What’s missing here is visual hierarchy. It’s about guiding the eye through the screen, so it notices the different design elements in order of importance. To improve it, I’m going to turn this suggestion into a visual anchor by making what’s most important larger or higher in contrast, so it naturally draws attention first.

**Для Напарника:** Проверять Дом и Фокус прищуриванием: главный CTA/таймер должен быть единственным якорем.


---

## 5. Текст на изображении: мягкая подложка (градиент/блюр)
`типографика · доступность · цвет` · [15:20](https://youtu.be/dGcqqA3Sl-o?t=920)

**Мысль:** Поверх пёстрого фона читаемость первична; лёгкий градиент или блюр за текстом решает проблему без разрушения дизайна.

**Слова автора:**

> But when text overlays an image, legibility can quickly become a problem especially with busy or high-contrast visuals. In those cases, clarity has to come first. One simple way to fix this is by adding a subtle background behind the text like a gradient or blur. It improves readability, while adding some dimension without disrupting the design.

**Для Напарника:** Подтверждает скрим под сноской над грядой в AppBackdrop; опираться на структурный отступ pb-[32vh], скрим вторичен.


---

## 6. Когерентный визуальный стиль: 4 цвета и пара простых правил
`вкус · цвет · дизайн-система` · [16:09](https://youtu.be/dGcqqA3Sl-o?t=969)

**Мысль:** Разнородные изображения рушат целостность; ограниченная палитра, несколько форм и правила их смешения дают единый узнаваемый стиль.

**Слова автора:**

> But not every image seems to work. They are all very different — in color, style. I start to see that what I really need is a cohesive visual style. To get there, I’m choosing a color palette and setting some simple rules to use it. Hopefully, this will establish a consistent aesthetic and evoke the right feeling. I choose four colors, a few retro shapes and then I mix and match. For those groups that show a title, I went with a bolder, expanded font, so they look different from text in the list. I really like how this is looking, I think these choices sharpen the app’s personality and make it easier to stay consistent as it grows.

**Для Напарника:** Держать иллюстрации Мира и маскота в единой палитре; новые ориентиры острова рисовать по тем же правилам.


---

## 7. Семантические цвета: имя по назначению, не по виду
`цвет · доступность · дизайн-система` · [16:55](https://youtu.be/dGcqqA3Sl-o?t=1015)

**Мысль:** Цвета, названные по роли, автоматически адаптируются к контрасту, режимам и окружению; акцентный цвет надо использовать аккуратно.

**Слова автора:**

> But those already have color, just not the kind I pick from a palette. They’re not black or purple they have names like label or secondarySystemBackground. These are semantic colors, and are named after their purpose, not their appearance — because they’re dynamic. They automatically change according to contrast settings, screen environments and modes like dark and light. I can use an accent color here and there — on buttons, controls, maybe to show what’s selected. But I have to be careful it doesn’t get in the way of dynamic changes, overall legibility, or people’s comfort. So I’d say that for anything dynamic, this is basically my color palette of system colors. They’re also part of the Apple Design Resources, and they give me a flexible set of options to build visual hierarchy that seamlessly adapt to people’s preferred appearance, without extra work.

**Для Напарника:** Токены цвета Напарника держать семантическими (muted-foreground и т.д.) и не сдвигать коридор светлоты 0.152–0.172.
