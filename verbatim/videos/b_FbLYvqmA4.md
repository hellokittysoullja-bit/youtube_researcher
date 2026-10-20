# 5 lessons for product designers — 🤿 Deep Dives season 2 takeaways

**Канал:** Dive Club 🤿 · 12 мин · субтитры: en (авто YouTube) · https://youtu.be/b_FbLYvqmA4

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Разделять примитивные и семантические переменные с первого дня
`дизайн-система · цвет · процесс` · [00:22](https://youtu.be/b_FbLYvqmA4?t=22)

**Мысль:** Смысловые токены (background primary, border subtle) отделяют от сырых цветов (blue 300), чтобы потом не делать огромный рефакторинг при втором бренде или продукте; в остальном система должна быть минимальной.

**Слова автора:**

> It's pretty easy to go overboard with variables in figma and that's why my default advice has been to build the smallest possible system and to not worry or spend too much time architecting for a future that you might not even know if it's going to happen or not but after talking with designer Advocate Louis oros I realized there's actually one exception to that rule even if you're not sure if you're going to have multiple brands or multiple products in the future it still makes sense to separate your primitive variables from your semantic variables and put them each in their own library from day one so in one file you'll have your color foundations these are your blue 300s your gray 400s and then in a separate file maybe it's your style guide you'll have your border subtle and your background primary and things like that it's not really that much more work than keeping these in the same file and just Des scoping your Primitives and this way you have a much more flexible foundation and you can make sure that you're not going to wake up one day a year from now or something like that and realize that you have this massive refactor on your hands.

**Для Напарника:** Цвета Напарника в oklch лучше держать как сырые значения плюс смысловые токены (muted-foreground и т.д.), как уже делает SKY record; не использовать сырые значения в компонентах.


---

## 2. Относись к дизайн-системе как к продукту: минимально жизнеспособная система
`дизайн-система · процесс` · [05:08](https://youtu.be/b_FbLYvqmA4?t=308)

**Мысль:** Не стоит месяцами строить идеальную библиотеку по образцу Polaris или Material; нужно делать наброски, показывать, итерировать и запускаться с v0.1, например с одним набором кнопок.

**Слова автора:**

> This idea of treating Your Design system like a product let's say that you're creating a new software startup the last thing that you're going to do is go into hiding for a full year and build this product that's fully fleshed out with all of the features that you think your users could possibly need no you're going to find whatever ever your MVP looks like and then you're going to iterate your way to success from there which is why Dan's advice really resonated with me stop making the foundation stop trying to make the perfect Library first that's not what you're making you are making a product so if you were to make that product what would you do you would exactly what you just said you would make a couple of sketches you'd sketch right whether that's sketching in code or sketching in figma and then you would show it to a bunch You' schedule a bunch of conversations you show it to a bunch of people you get feedback on it and then you iterate and you would do that a bunch of times until six times and you would go I think our accordion is ready for prime time you know let's get let's get 30 people in here to use it not 3,000 not 30,000 you know let's get 30 people in here to see if you know see to kick the tires on this the problem is that too many people are looking at systems like Polaris and material and they're letting that shape what their output should be but these are massive systems that have been refined over years but if you treat your system like a product then you're not going to build this V one that is robust and comprehensive it would be the equivalent of launching a new e-commerce startup and looking at Shopify as the measuring stick for what you have to build to launch instead we need to find that minimum viable system to launch with and we're going to do it by following a pretty familiar product process you're going to talk to people do user interviews get feedback on early Concepts and pattern matching and maybe we're going to end up launching with something that's pretty small maybe it's even one set of buttons.

**Для Напарника:** Не раздувать общие компоненты Напарника заранее; добавлять примитив только когда его реально используют несколько экранов.


---

## 3. Лучшие команды удаляют компоненты и поддерживают лишь самые ценные
`дизайн-система · процесс` · [07:23](https://youtu.be/b_FbLYvqmA4?t=443)

**Мысль:** Системы со временем сокращаются со 150 до 50 компонентов, потому что меньший набор можно поддерживать лучше.

**Слова автора:**

> Design system life cycle as well because the best product teams are the ones that are eliminating feature bloat whenever possible they're often actually deleting code and removing things from the product and a design system works the same way once you get the data and you're seeing how designers actually use these components and you're getting all of this feedback along the way you can start to identify your highest value components and then only support that you can actually remove the rest from the system because what Dan shared is that the best design system teams are not the ones building the biggest most comprehensive systems they're the ones that are relentlessly trimming the fat.


---

## 4. Главная как sizzle reel: один скролл-трек лучших моментов
`лендинг · конверсия · вкус` · [09:05](https://youtu.be/b_FbLYvqmA4?t=545)

**Мысль:** Типовой портфолио-шаблон «герой плюс сетка карточек» дробит историю; лучше один видео-трейлер самых сильных работ, как у 3D-художников, а страницы проектов отдать в приложение.

**Слова автора:**

> Is the structure of a design portfolio and it all stems from a deep dive that I had with Yen W who is the head of design at Maven and when I say design portfolio you probably have an image pop into your head it's that same hero section with some kind of a generic statement and then you have a grid of cards with thumbnails and a CTA that takes you to your individual project pages but the problem is this type of layout fragments our narrative we spend so much time obsessing over how to tell the best project story and all of the details and our process and the output and what we learned and the takeaways and how we've grown that we forget to tell our compelling story and at the end of the day that's what's most important what if we started to view project Pages as more of an appendix and not the primary way that people consume our work that's why I really like un's take where she says that more designers should start to draw inspiration from 3D artists because they always have this one video that is the perfect embodiment of who they are and what they're capable of making and if we started doing this as product designers we'd probably start to view our homepage as more of our Sizzle reel and then we'd have a single place to tell our story share all of our best UI accomplishments prototypes all in a single scroll track just like showed the best stuff like kind of like the what is it call like the Highlight rail that like the 3D designers usually would pack together like it's just like a trailer of like all the super cool stuff that they made I think maybe we designers like product designers should do more of that too.

**Для Напарника:** Лендинг Напарника: один сквозной показ лучших моментов (кот у костра, рост острова, награда) вместо сетки описаний фич.


---

## 5. Система это не продукт: рисуй поверх скриншота продакшена
`процесс · дизайн-система` · [10:44](https://youtu.be/b_FbLYvqmA4?t=644)

**Мысль:** Адриен из Linear делает небольшие улучшения прямо поверх скриншота живого приложения, потому что пользователь видит продакшн, а не красивый файл; время на систему это время, не потраченное на продукт.

**Слова автора:**

> The only thing that matters is what's in production and that's totally true but man is it hard to fight this urge to keep figma clean and treat it like it's the source of truth that's why I so appreciated Adrian reo's perspective he's the founding designer of linear and obviously everything about their product is exquisite and yet what Adrien says he does is a lot of times he's just taking a screenshot of what is currently in production drawing rectangles over it to hide any elements that is necessary and then he's actually designing on top of that screenshot and that's a big part of how he is collaborating with the engineers at linear most of the time if I do small Improvement I will just take a screenshot of the app and just design on top of it because in the end what is the user looking at like okay maybe your file look fancy and super nice but if in production you don't have the same thing that there is a problem for me like everything that's happening behind the SC is nice I'm very excited to see that happening and I think we have better TOS to do that so for sure it's cool but in the end people that are looking at your productivity what do they see now if you know me at all you know that I love organizing things in figma and building different systems and for sure I am a big believer that strategically using components in figma can make you a much more effective designer but every once in a while I need to be reminded that the system is not the product and the product is the only thing that matters I think when you are very early on your product spending the time designing systems it's to me the time that you don't spend improving your product so it's the philosophy behind there was that if you are alone or if you one or two designer working on a prodject the all the time you will spend designing the design system is the time that we are not building new things or improving the thing you already have.

**Для Напарника:** Проверять правки на реальном рендере и данных, как в методологии CLAUDE.md §6, а не по абстрактным компонентам.
