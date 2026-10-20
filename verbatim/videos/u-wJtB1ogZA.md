# Your App Passed the Accessibility Audit. It's Still a Nightmare to Use.

**Канал:** Moriel Schottlender · 14 мин · субтитры: en (авто YouTube) · https://youtu.be/u-wJtB1ogZA

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Compliance theater: WCAG — пол, а не потолок
`доступность · процесс · вкус` · [02:00](https://youtu.be/u-wJtB1ogZA?t=120)

**Мысль:** Аудит ловит alt-тексты и контраст, но не отвечает, может ли реальный человек с реальной целью пользоваться продуктом.

**Слова автора:**

> The audit passes. Every checkbox is ticked. The accessibility report comes back green, and everyone breathes a sigh of relief and moves on. And the site is still functionally a cognitive obstacle course. This is what I'd call compliance theater. You've satisfied the standard, and the standard was never designed to be the ceiling. It was designed to be the floor. We've just been treating it as if it's the whole building, you know, with a pool and a sauna. WCAG is great at catching things like, "Is there an alt text on this image? Does this button have a label? Is the color contrast sufficient?" These are necessary questions, but they don't ask, "Can a real human with a real goal under real conditions actually use this thing?".

**Для Напарника:** Контраст 6.63:1 — минимум; сверять Напарник на реальных сценариях и реалистичных данных (§5.2 CLAUDE.md).


---

## 2. Нейроотличные пользователи — канарейки в шахте продукта
`доступность · СДВГ · исследования` · [02:56](https://youtu.be/u-wJtB1ogZA?t=176)

**Мысль:** Они первыми и сильнее всех упираются в то, что потом раздражает всех; это сигнал, а не краевой случай.

**Слова автора:**

> And here's where it gets interesting because the users who feel that gap first, the ones who hit the wall before anyone else does, are neurodivergent users. People with ADHD, dyslexia, anxiety, cognitive difference of all kinds. As I've talked about in previous videos, these users are the canaries in your app's mine. They're not the edge case to accommodate after the fact. They're the signal. They experienced first and most intensely what eventually frustrates everyone.

**Для Напарника:** Дизайн Напарника под самый перегруженный мозг даст преимущество всем пользователям.


---

## 3. Бесконечная лента повышает метрики, но отнимает цель пользователя
`этика · тёмные-паттерны · внимание · метрики` · [03:53](https://youtu.be/u-wJtB1ogZA?t=233)

**Мысль:** Бесконечный скролл специально прерывает цель более стимулирующим контентом; внимание потреблено, ничего не отдано.

**Слова автора:**

> So, let's talk about what actually drains that cognitive budget. Because it's usually not just one big thing. It's a hundred of small decisions, each one individually defensible, that adds up to an experience that quietly exhausts you. Take infinite scroll. There's a reason it became the default pattern for feeds and timelines and social media. It works in the sense that it keeps people on the page longer. Engagement goes up. Session duration goes up. The metrics look great. But here's what's actually happening. You came to the site to do something specific. You had a goal. And the infinite scroll is specifically designed to interrupt that goal with something more immediately stimulating. That's not a distraction. That's a design pattern that consumed your attention and handed you nothing in return.

**Для Напарника:** Не вводить бесконечные ленты и «ещё одну сессию»; финал сессии имеет конец.


---

## 4. Модное название функции — налог на перевод в голове каждый раз
`микрокопирайтинг · иерархия · тексты` · [04:39](https://youtu.be/u-wJtB1ogZA?t=279)

**Мысль:** «Пространства» значат «папки»: каждое обращение требует мини-перевода; без метафоры и онбординга это чистая нагрузка.

**Слова автора:**

> Now, let's talk about naming. There was a period of time, roughly 2015 to 2020, though some of this still very much alive, where every product started naming its features with words that sounded modern and brandable and meant essentially nothing. Spaces, flows, canvas, hubs, streams. Now, to be fair, I don't think smart naming is inherently bad. A good brand name can be memorable, distinctive, even useful. But here's the thing, a clever name adds cognitive overhead. Every time you encounter spaces in an interface, your brain has to perform a small translation. Spaces means folder in this app. That's not free. It's a small tax paid every single time by every single user. And if your clever name doesn't come with a clear tagline, consistent metaphor, or solid onboarding, if you just named it and moved on, you've added overhead without providing any offset.

**Для Напарника:** Названия экранов должны сказать, что это (Дом, Фокус, Мир) — не абстрактные «потоки»; метафоры диегетичны и сразу понятны.


---

## 5. Трение невидимо в аналитике: человек уходит в другую вкладку или к ИИ
`метрики · исследования · удержание` · [06:13](https://youtu.be/u-wJtB1ogZA?t=373)

**Мысль:** Порог терпения пересечён — пользователь не жалуется, а уходит; bounce rate и scroll depth не показывают намерение и фрустрацию.

**Слова автора:**

> And this is where it stops being just a UX problem. Because every one of these friction points, the scroll that takes over, the menu that tells you nothing, the name that requires translation, has a threshold. And when a user hits that threshold, they don't file a complaint. They don't leave a review. They just open a new tab. They ask an AI agent. They get an answer in 11 seconds. They never come back. The product never knew they were there, and it definitely doesn't know they left. That's the thing about this kind of friction. It's invisible to your analytics. Bounce rate, session duration, scroll depth, none of those metrics capture the intent that walked in and the frustration that walked out. The user who routed around you to a competitor or to an AI doesn't show up as a lost customer. They just quietly disappear.

**Для Напарника:** Измерять успех Напарника через завершённые шаги и опрос людей, а не по времени на экране; слушать живые отзывы.


---

## 6. Дизайн для выносливости против дизайна для самостоятельности: 2–3 настройки, что реально важны
`доступность · мобильный · дизайн-система · вкус` · [07:19](https://youtu.be/u-wJtB1ogZA?t=439)

**Мысль:** Вместо «терпи» дать контролы над сенсорной средой: низкая анимация, плотность, сниженный контраст; но не 40 тумблеров.

**Слова автора:**

> The difference between designing for endurance and designing for agency. Endurance design says, "Here's the experience. Hold on. You'll get through it." But agency design says, "Here are the controls. You're in charge of your own experience." The most visible version of this is dark mode. Dark mode is awesome. Dark mode is a genuine improvement for a lot of users, but dark mode is also the beginning of the conversation, not the end. The fuller version of this is giving users meaningful controls over their sensory environment. Low motion modes for users who experience vestibular issues or are simply distracted by animation. Density controls because not everyone wants the same amount of information on the screen at once. Reduced contrast options, not just high contrast because some users find high contrast harder to read, not easier. Now, I'm not saying every product needs to ship 40 preference toggles. That's its own kind of cognitive overhead. The question is, where does a small amount of user control make a disproportionately large difference? That's UX research question, not a checklist question. Talk to your users, run tests, find the two or three settings that actually matter on how people use your specific product.

**Для Напарника:** Режим «меньше движения» для анимаций AppBackdrop и выбор плотности; 2–3 настройки, найденные на практике.


---

## 7. Выходы «не сейчас»: отложить без потери контекста
`онбординг · этика · стыд · доступность` · [08:38](https://youtu.be/u-wJtB1ogZA?t=518)

**Мысль:** Запрос разрешений до контента, мастер на 12 шагов, тур без повторного доступа — «сейчас или никогда»; нужен выбор отложить, и это удерживает.

**Слова автора:**

> Something I think about a lot, which I call exit ramps. Here's a pattern. A user hits an onboarding flow, a permission request, a multi-step model. They're not ready to deal with it right now. Maybe they came in to do something specific and this appeared in the way. What they need is a clear not now, a way to defer, to skip, to pause, and to come back later without losing their context or starting from scratch. Now, sometimes the flow genuinely needs information before it can proceed. That's fair. A payment form needs payment details. A shipping address field isn't optional. That's fine. That's not what we're talking about. We're talking about the notification permission request that fires before the user has seen a single piece of content. The 12-step profile wizard that blocks access to the product they just signed up for. The onboarding tour you can't skip because someone's completion metric depends on it, and if you do manage to dismiss it, it's gone forever. There's no way to revisit it when you actually need it. That's not a not now, it's just now or never. The goal isn't to never ask users for anything, it's to ask at the right moment, make skipping or deferring feel like a valid choice, and not assume that every user processes information the same way, or wants to do everything in the same order. Exit ramps aren't about letting users abandon your product, they're about giving them enough control to stay on their own terms.

**Для Напарника:** Чек-ины и вопросы (имя, вечерний) всегда с «не сейчас», который не наказывается и возвращается позже; один вопрос за визит.


---

## 8. Inclusive by default: сначала наименьшее лишнее трение, сложность — когда заслужила место
`доступность · процесс · вкус` · [11:23](https://youtu.be/u-wJtB1ogZA?t=683)

**Мысль:** Это не про самого ограниченного пользователя, а про решения: меню «возвраты», скролл туда, куда указал, понятное имя, выход, которые принимались иначе ради эстетики и метрик.

**Слова автора:**

> It doesn't mean designing for the most constrained possible user and calling it done. It means making the design decision that creates the least unnecessary friction first and then adding complexity only when it genuinely earns its place. The menu that says returns instead of connect, the scroll that goes where you point it, the name that tells you what the thing does even if it also has a clever brand name next to it, the exit ramp that's actually there. None of these are heroic accessibility work. They're just decisions. Decisions that got made the other way for reasons that usually had more to do with aesthetics or engagement metrics or what the design portfolio would look like.

**Для Напарника:** Принцип приёмки любой правки: убирает ли она лишнее трение; красота не должна его увеличивать.


---

## 9. Адаптивный ИИ поверх плохой основы — умная ловушка
`ИИ · доступность · доверие · этика` · [12:08](https://youtu.be/u-wJtB1ogZA?t=728)

**Мысль:** Интерфейс, самовольно упрощающий себя, убирает нужное и лишает контроля; основа должна быть правильной.

**Слова автора:**

> Now, there's a version of the future where AI-driven adaptive interfaces adjust complexity in real time based on your cognitive state. That might be interesting. I'm definitely watching for that. But, I want to be honest, that future, if it comes, is going to be built on top of the same design decisions we're making right now. A well-designed adaptive interface on top of a scroll-jacked, jargon-named, exit-ramp-free product is just a smarter trap. The foundation has to be right first. >> I've detected elevated cognitive load. I'm going to simplify your experience. >> Oh. Okay, thank you. >> I've removed the advanced settings panel. >> I was in the advanced settings panel. >> I've also condensed the navigation to three core options. >> The thing I need is not in those three options. >> For your comfort, I've reduced the number of visible items by 40%. >> I just want to find >> Interface optimized. Enjoy your simplified experience. >> I don't even know what I wanted to do anymore.

**Для Напарника:** Напарник не должен сам убирать функции «ради вашего комфорта»; предлагать, а не навязывать, давать вернуть.
