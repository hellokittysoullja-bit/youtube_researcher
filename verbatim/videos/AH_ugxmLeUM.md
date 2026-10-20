# 7 UI/UX mistakes that SCREAM you’re a beginner

**Канал:** Kole Jain · 7 мин · субтитры: en (авто YouTube) · https://youtu.be/AH_ugxmLeUM

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Пропуски в пользовательском потоке: поиск, пропуск, скрытые состояния
`процесс · онбординг · крафт` · [00:23](https://youtu.be/AH_ugxmLeUM?t=23)

**Мысль:** Экран выбора аллергий без поиска и без «пропустить» упускает случаи. Наброски на бумаге ловят дыры, а чаще всего забывают навигацию, скрытые состояния и динамику.

**Слова автора:**

> Number one, user flow. Let's start with something that quietly ruins your UX, user flow. Here's our allergy screen with six preset options, but no search bar if someone's allergic to something else. We also don't have a skip button either. What if the user doesn't have any allergies? These are things you will miss if you don't plan out your flow, but users, they'll feel it instantly. So, even something as simple as sketching boxes on paper helps you catch major gaps early on. And it's not just all about big stuff. Little touches like a filter icon on the search bar or a save button up top go a long way. The most commonly missed elements, navigation links, hidden states, and dynamic interactions like button hovers or micro interactions.

**Для Напарника:** В онбординге Напарника у каждого вопроса должен быть мягкий пропуск («потом»), чтобы никого не загонять.


---

## 2. Перебор эффектов: меняй цвет тени и блюр, градиент без разброса оттенков
`вкус · цвет · крафт` · [01:06](https://youtu.be/AH_ugxmLeUM?t=66)

**Мысль:** Градиенты из разных цветов не работают, градиент допустим только в вариациях одного. Тень лучше смягчать цветом и блюром, и чаще меньше шума значит лучше.

**Слова автора:**

> Early on, I was addicted to visual effects. Shadows, glows, gradients, you name it. But the truth, overusing them can make your designs feel cluttered and amateur. Let's start with the gradient here. It's blue and green, and it's just not working. If you really need a gradient, stick to variations of the same color, like a darker or lighter green. But honestly, this would look way cleaner with no gradient at all. And that's usually the case. Now, let's talk drop shadows for a second. These Figma defaults are way too harsh. Instead of just lowering opacity, I change the entire shadow color, usually to a light gray, and increase the blur significantly. Or once again, remove the shadow completely. Because most of the time, less visual noise equals a better design.

**Для Напарника:** Свечения и тени на острове использовать только там, где есть смысловая привязка, как требует §10 CLAUDE.md.


---

## 3. Новички упаковывают слишком плотно; на мобильном нужно больше воздуха
`отступы · мобильный · сетка` · [01:51](https://youtu.be/AH_ugxmLeUM?t=111)

**Мысль:** Сетки и auto layout задают порядок, вертикальный отступ группирует элементы, а на мобильном его нужно больше, чем кажется.

**Слова автора:**

> Most beginner UIs are packed way too tight, like my old app design. So, I'll use two tools here, grids and auto layout to make it so much better. First, we'll set up a three column grid for this screen and two column grid here with these measurements. Now, just align elements to the grid as closely as possible. If something needs to break the grid slightly, like these elements, just leave it as is if it still feels balanced. Next, for stack content like this, increase the vertical spacing to let things breathe and group naturally, especially on mobile screens, you'll need more space than you think.

**Для Напарника:** Проверить отступы на 390px по Дому и Фокусу, особенно между репликами и формами.


---

## 4. Консистентность: единый радиус, одинаковые кнопки, стили и переменные
`дизайн-система · крафт · процесс` · [02:47](https://youtu.be/AH_ugxmLeUM?t=167)

**Мысль:** Разные радиусы и одинаковые по смыслу, но по-разному оформленные кнопки выглядят любительски. Помогают стили цвета, переменные размеров и компоненты.

**Слова автора:**

> This one kills me since it's just so easy to fix. You'll notice throughout our design, we have all sorts of different corner radiuses and components like this back and skip button that are exactly the same but designed differently, which just makes the design feel amateur. Instead, let's make a few changes. First, we'll make the two search bars identical other than the prompting text. We'll set the corner radius of all smaller components to be 10 pixels. This is an important one that most designers miss. And of course, we'll update the skip button and back button to match in size, corner radius, and style. Being consistent means using styles for colors, variables for measurements, and components for UI elements to really bring your design together.

**Для Напарника:** Единые радиусы и размеры кнопок «Назад»/«Пропустить» во всех экранах; токены вместо магических чисел.


---

## 5. Иконки: нужны на карточках, один набор, подписи для неочевидных
`иконки · дизайн-система · онбординг` · [03:41](https://youtu.be/AH_ugxmLeUM?t=221)

**Мысль:** Без иконок приходится читать больше. Несоответствие заливки и линий видно сразу, а разные стили допустимы лишь в визуально разделённых зонах.

**Слова автора:**

> First of all, we have no icons on these cards here, which forces users to read more and slows down the browsing process. Let's add in some good icons and replace the save text. Then up above, we have icons, but they're mismatched in fill, line width, and style. We can fix this by using the same library of icons like flat icons. On their website, select interface icons and then sort by stroke, width, and corner to get some consistent results. Make sure when you download to grab SVG for the best results. If you want to choose a Figma plugin instead, I like feather icons and phosphor icons. Finally, we have a fair amount of icons down here without labels. If the icons are wellknown enough, like the house, bookmark, and user, then you don't need to have anything, but for these two, a tool tip pop-up could make the onboarding process much smoother. Just try not to have bizarre icons everywhere. Finally, this is a very pro tip, but interestingly, it is okay to have different styles of icons in the same design, but only if they're visually separate. For example, these navbar icons are slightly different than the food icons, and those are different than our recipe icons, but it all works together since they're in separate areas of our design and used for different things.

**Для Напарника:** Один набор иконок, подпись или подсказка только для неочевидных иконок в AppNav; известные (дом) без подписи.


---

## 6. Лишние элементы: убирай стрелки там, где работает жест
`иерархия · крафт` · [04:57](https://youtu.be/AH_ugxmLeUM?t=297)

**Мысль:** Стрелка при возможности свайпа и обводки без необходимости только визуальный шум.

**Слова автора:**

> Having redundant elements is actually a really common mistake, especially as the trend of having stuff everywhere takes over. Looking at this screen, we can get rid of this arrow since we'll be able to swipe on mobile. And same idea down below. We can also get rid of this arrow since it's really just visual clutter and dim down the color of the button.

**Для Напарника:** Убрать декоративные стрелки там, где работает drag-to-reply и свайп, оставив действие очевидным без украшения.


---

## 7. Интерактивный отклик: серая кнопка при нажатии и метка нового
`анимация · доверие · микрокопирайтинг` · [05:32](https://youtu.be/AH_ugxmLeUM?t=332)

**Мысль:** Если следующий экран грузится дольше мгновения, кажется, что клика не было. Серое состояние и красная точка у вкладки подтверждают действие.

**Слова автора:**

> Now let's cover the underuse of different interactive effects. For example, if we're navigating through our flow, but it takes a split second longer for the next screen to load, it looks like we haven't even clicked on the button at all. But if we make it grayed out when we click on it, we've added some interaction and it shows the user that the next screen is coming. Even better, we could add a loading wheel if it's really taking a long time. Another good example is clicking on this save icon. Filling it in is a great first step, but we could also add a red dot to our save tab. So, when we click on the icon, we get it filled in and it's clear to the user that there's a new recipe added to the save tab.

**Для Напарника:** После нажатия «Начать» кнопка сразу меняется, а в AppNav новый ориентир отмечается мягкой точкой вместо уведомления.


---

## 8. Графики не надо переоформлять: ось и читаемые столбцы важнее эстетики
`иерархия · доступность · крафт` · [06:27](https://youtu.be/AH_ugxmLeUM?t=387)

**Мысль:** Закруглённые столбцы без оси и 16 столбцов на 7 дней нечитаемы, а простой график даёт больше пользы.

**Слова автора:**

> Charts are so often messed up by overdesigning the thing that I thought I should make a point to mention it. I have two charts here. Which one do you think I got from Dribble? The one on the right. Yes. And it's basically impossible to read without any vertical axis. And even if we had a vertical axis, it's hard to tell where the bar ends with a rounded top. And then there are 16 bars here, but only 7 days of the week. Why would you do that? Whereas the one on the left is simple, definitely less aesthetic, but conveys so much more useful information to the user.

**Для Напарника:** Если в Мире появится статистика недели, делать её простой и честной, с понятной осью.
