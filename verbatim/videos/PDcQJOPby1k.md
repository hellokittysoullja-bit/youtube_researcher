# 5 SaaS UI/UX mistakes that SCREAM you Vibe Code

**Канал:** Kole Jain · 6 мин · субтитры: en (авто YouTube) · https://youtu.be/PDcQJOPby1k

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Убрать эмодзи как иконки и не доверять ИИ выбор цветов
`вкус · иконки · цвет · ИИ` · [00:12](https://youtu.be/PDcQJOPby1k?t=12)

**Мысль:** Эмодзи выглядят непрофессионально, а ИИ выбирает яркие несочетающиеся цвета. Заменить на иконки интерфейсной библиотеки и вручную настроить фоны.

**Слова автора:**

> The first problem is pretty painfully obvious. Get rid of the emojis. Admittedly, some apps like Notion successfully use them, but if we take this card and just swap to some more professional icons, it already starts looking better. I like phosphor icons, but Lucide or any other interface icon libraries work well, too. Along those same lines, never let an AI choose any of your colors. They always go for bright colors that don't really work well together.

**Для Напарника:** В ИИ-сгенерированных репликах и интерфейсе не использовать эмодзи вместо иконок; цвета брать только из токенов.


---

## 2. Не отдавай ИИ раскладку: дублирование блоков и лишние ссылки
`ИИ · иерархия · процесс` · [01:09](https://youtu.be/PDcQJOPby1k?t=69)

**Мысль:** ИИ дублирует одни и те же KPI на разных экранах и перегружает сайдбар второстепенными ссылками. Пользователь ищет данные там, где они логично должны быть.

**Слова автора:**

> These four KPIs at the top show up not once, not twice, but three times in a small app. Bringing me to my next point. Never let an AI choose your layout either. Starting with the sidebar, if I'm in custom domains or teams, the amount of clicks and links doesn't really matter to me. If I need that information, I'll visit the dashboard or the analytics tab, which we definitely need to add. We'll align this to the left and tighten up the spacing, too.

**Для Напарника:** Не повторять один и тот же счётчик (число сессий) на Доме, Фокусе и Мире без причины.


---

## 3. Разгрузка перегруженных карточек: меню действий, иконки вместо чипов
`иерархия · крафт · ИИ` · [01:41](https://youtu.be/PDcQJOPby1k?t=101)

**Мысль:** Кнопки сворачиваются в меню, чипы заменяются иконками, ключевые данные выравниваются по краям.

**Слова автора:**

> Gradient profile circles with letters in them. So, let's swap this for an account card. And with that, we can get rid of these links and tuck them into a popover on click and collapse settings and billing and usage together. And finally for these cards, they're feeling a little busy. Let's collapse these buttons into a triple dot menu. Move the date to the center. Collapse these chips to just icons. And move clicks to the right.

**Для Напарника:** Карточки шагов и reward держать лёгкими: главное действие видно, второстепенные уходят в меню.


---

## 4. Тарифы: меньше планов, крупная цена, показать скидку и что даёт следующий план
`цены · иерархия · конверсия` · [03:53](https://youtu.be/PDcQJOPby1k?t=233)

**Мысль:** Пять планов слишком много, название тарифа не важно, а цена в месяц важна. Реальную скидку и дополнительные возможности нужно показывать явно.

**Слова автора:**

> Also, having five plans is really not ideal. Hobby probably makes the most sense to drop, but at least one of them needs to go. The hierarchy isn't bad, but I think we can tune it up a little with that extra width we have. Let's drop some of the unnecessary elements and adjust the colors. Drop the size of the name since no one cares about that. Increase the size of the cost per month since people do care about that. Business has become enterprise since if you need 50,000 links per month, you probably need more. Showing the actual discount the user is getting is very important. And also showing them what the next plan includes that the current plan doesn't have.

**Для Напарника:** Если появятся тарифы, оставить 2–3 плана, цену сделать крупной и не давить скидкой, соблюдая принцип без стыда.


---

## 5. Лендинг теряет клиентов без графики; он про презентацию, а не про сложность
`лендинг · конверсия · доверие` · [05:42](https://youtu.be/PDcQJOPby1k?t=342)

**Мысль:** Стандарт качества SaaS-лендингов формирует доверие подсознательно, а скриншоты настоящих экранов и лёгкий скос карточек поднимают страницу.

**Слова автора:**

> There's definitely a standard of quality on SAS landing pages that establishes trust, even subconsciously. Applying some of the color and layout principles we talked about helps, but what we really need are some graphics. Even adding something as stupid simple as link cards with some skew really starts to elevate the page. And instead of these lameass icons, we can use a slightly edited image of the analytics page we designed or same idea with password protection. Landing pages aren't about complexity, they're about presentation. And generally, the better the presentation, the better the conversion.

**Для Напарника:** На лендинге Напарника показывать реальный остров и экран Фокуса в настоящих кадрах вместо абстрактных иконок.
