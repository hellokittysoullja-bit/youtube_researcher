# WWDC26: Principles of great design | Apple

**Канал:** Apple Developer · 17 мин · субтитры: en (ручные) · https://youtu.be/Xa9L2yx_QH8

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Каждая фича просит время, внимание и доверие
`процесс · доверие · внимание` · [00:32](https://youtu.be/Xa9L2yx_QH8?t=32)

**Мысль:** Дизайн это создание с намерением; каждая функция требует от человека ценных ресурсов, поэтому выбор что строить часто есть выбор, что не включать.

**Слова автора:**

> For us at Apple, design is making something with intention. It's focusing on what's most important to people, so you can build something they will truly value. Every feature you add to your product, asks something of the person using it. It asks for their time, their attention, and their trust. These are valuable things you can't afford to waste. So choosing what to build, is often a matter of deciding what not to include. Before you a draw a single sketch, or write a line of code, think about whether what you're making has purpose.

**Для Напарника:** Фильтр для любой новой механики Напарника: чего она просит у человека с СДВГ и стоит ли это; склоняться к вычёркиванию.


---

## 2. Агентность и прощение: выбор, undo и осторожные прерывания
`мотивация · доверие · СДВГ` · [01:43](https://youtu.be/Xa9L2yx_QH8?t=103)

**Мысль:** Люди вовлечены, когда сами управляют темпом; ошибки неизбежны, поэтому нужна возможность отмены, а подтверждения только перед серьёзными ошибками. Прощение даёт уверенность исследовать.

**Слова автора:**

> Agency is about putting people in control. People feel in control, when you let them do things their way. For example, do you want to take this next part? Oh, I'm okay, you can keep going! Okay! Offering choices is the best way to bring agency into your experience. An interface should never stand in the way of what someone is trying to do. Instead of guiding someone down a pre-determined path, let them dive right into your experience. And give them the autonomy to decide what to explore at their own pace. People are far more engaged when they have agency to control their own experience. Of course, that does mean people will make mistakes, or go down paths they didn't mean to. When that happens, offer forgiveness. People accidentally send, change, and delete things all the time. You can provide forgiveness by making it easy for them to undo any of their actions. And, when someone's about to do something destructive, double-check it's what they actually mean to do. In some cases, interruptions can be helpful. But use interruptions carefully, and only when someone is about to make a big mistake. Oops, I don't wanna do that! Just one sec here. Let's keep going. People really appreciate it, when you help them avoid disaster. Forgiveness supports agency because it gives people confidence that they can always recover from anything they try, and helps them feel capable, secure, and free to explore.

**Для Напарника:** Совпадает с тоном без стыда: дать откат шага/сессии и прерывать только перед необратимым; не вести по принудительному пути.


---

## 3. Не требуй данные до контекста; проси в правильный момент
`доверие · онбординг · этика` · [03:49](https://youtu.be/Xa9L2yx_QH8?t=229)

**Мысль:** Запрос телефона или разрешений сразу при запуске, до понимания пользы, разрушает доверие; просить только необходимое и объяснять зачем.

**Слова автора:**

> And even though there's tons of information you can request from someone, it's not the best way to build a relationship. Imagine someone comes up to you like this: Hey! Hi! Give me your phone number. For what? I just need it. why? I'll tell you, once you give me your phone number. You wouldn't trust a person like that in real life. And yet, interfaces do this all the time. They throw permission prompts the second you launch them. Long before you've figured out what the app actually does. Or ask you for information, without providing context for what it's for. A responsible design treats people and their private information with respect, just like you would in the real world. Responsible interfaces wait for the right moment to ask for personal data. They only ask for what's necessary, and are transparent about the data is for.

**Для Напарника:** Имя и чек-ин на Доме спрашивать в нужный момент и по одному за визит (nameOffer/checkinOffer), с объяснением зачем.


---

## 4. Ответственность при ИИ: предвидеть сбои модели, добавить защиту
`ИИ · этика · доверие` · [04:51](https://youtu.be/Xa9L2yx_QH8?t=291)

**Мысль:** Модель может выдать неожиданное или неточное; нужно реалистично оценить вред, ввести предпросмотры, подтверждения, дисклеймеры или убрать фичу.

**Слова автора:**

> That's why in addition to privacy, you should keep people safe. For interfaces, this means looking closely at what functionality you offer, and asking yourself some hard questions. How could this feature be misused? Who would be harmed by this? And how do I prevent it? Think about what it means to responsibly add AI capabilities to your product. When you build intelligent features, you have to anticipate that a model might generate something unexpected or inaccurate. Take something as innocent as a recipe app. If someone logs an allergy, you have to anticipate that the model may suggest an ingredient that could cause a severe reaction. That could do real-world harm and it's just something you can't leave to chance. Think realistically about what could go wrong, and add safeguards. Previews, confirmations, disclaimers can help, but consider removing features entirely, if the risks to people's safety outweigh the value.

**Для Напарника:** Реплики напарника и дробление задач (api/companion, api/breakdown): страховка от токсичных или стыдящих формулировок и от вредных советов.


---

## 5. Метафоры не слишком буквальные и не абстрактные; консистентность
`иконки · доверие · дизайн-система` · [06:48](https://youtu.be/Xa9L2yx_QH8?t=408)

**Мысль:** Хорошая метафора опирается на знакомое и позволяет предсказать поведение; одинаковое выглядит одинаково и ведёт себя одинаково, действия на одном месте ускоряют.

**Слова автора:**

> The trick to metaphors, is making sure they aren't too literal or abstract. In an interface, an inspector shows details of whatever is selected. If your inspector metaphor is too literal, people might not be familiar with what you're trying to show. If it's too abstract, you risk your idea not getting across. A good metaphor draws on something people know and helps people predict what it will do. When used correctly, metaphors instantly click. When used incorrectly, metaphors can be surprising, in a bad way. Let's go back to the trash can. If you use a trash can icon to mean something other than delete, it goes against people's familiarity with what this symbol represents, in other software. The same is true if you take creative liberty with the delete icon. People don't get that immediate recognition. For common actions, there's no need to reinvent the wheel. Just use the metaphors people are already familiar with, and make sure they do what people expect. Familiarity is also a product of being consistent. Consistency helps people predict what will happen next. Simply put, things that look the same should behave the same. If one of these buttons moves to a different screen, another toggles an action, and another pops up a modal, there's no pattern to understanding how this interface works. Consistent behavior helps people navigate your interface, because they can anticipate what will happen and where they're going. And so does consistent placement. On Mac, you can always close a window by going to the top left corner. It's always in the exact same spot. When someone can find an action in the same location across screens and devices, it speeds them up. They don't have to think about it.

**Для Напарника:** Метафоры кота и острова удерживать понятными; одинаковые кнопки (Следующий шаг vs Повторить) различать иконками, как уже сделано.


---

## 6. Гибкость и персонализация, когда единого решения нет
`доступность · СДВГ · мотивация` · [10:07](https://youtu.be/Xa9L2yx_QH8?t=607)

**Мысль:** Аудитория различается по возрасту, языку, опыту, потребностям доступности; там, где одного решения нет, давать настроить расположение и скрыть ненужное.

**Слова автора:**

> Another way make your design flexible, is to cater to the wide range of abilities people have. Get curious about who your audience is. How old are they? What languages do they speak? Are they a pro or a novice? Do they rely on accessibility features? You might not solve for every type of person on day one, but you can start examining how your experience can be more inclusive. Often, adding flexibility means you're not going to land on a single design solution that makes everyone happy. Sometimes, the best option, is to let people personalize your experience to suit their own preferences. Take something like controls. It's really hard to nail down a single layout that works perfectly for every person, so offer people the flexibility to rearrange them, to support their personal workflow. Or allow them to hide controls they never use.

**Для Напарника:** Настройки Фокуса (длительность, звук костра, хаптика) для разных сенсорных профилей СДВГ; дефолт разумный, выбор опционален.


---

## 7. Простота это не минимализм: краткость, ясность, иерархия
`иерархия · тексты · микрокопирайтинг` · [11:04](https://youtu.be/Xa9L2yx_QH8?t=664)

**Мысль:** Спрятать всё в одно место значит минимально, но не просто. Простота: простой язык без жаргона, меньше шагов, иерархия порядком, отступами, контрастом, ответы на что смотреть и как взаимодействовать.

**Слова автора:**

> Simplicity is about stripping away the unnecessary, so the core purpose of your design can shine. When we say simple, we don't mean minimal. If you bury all your functionality inside a single place, that might make your interface look more minimal, but it doesn't make it simple. Simple designs are frictionless and intuitive. People can find what they need without effort. And they get there by being concise and clear. Concise interfaces use plain language. They strip away jargon and speak naturally. They avoid redundancy and get straight to the point. Concise interfaces also respect people's time. They reduce the number of steps it takes to get things done. You can also achieve simplicity through being clear. A clear design perfectly communicates what it does. Clarity is built with hierarchy, using order, spacing, and contrast to guide people to what's most important. When your hierarchy is strong, the most important item on the screen is always the most obvious one. Clear interfaces answer people's questions: What do I pay attention to? What can I interact with? And how do I interact? In a simple interface, every element earns its place.

**Для Напарника:** Тексты Напарника короткие и разговорные; на каждом экране один очевидный главный элемент.


---

## 8. Упрощение иногда значит добавить контекст
`иерархия · внимание · крафт` · [12:40](https://youtu.be/Xa9L2yx_QH8?t=760)

**Мысль:** Дистиллировать данные до сути (график вместо сложных данных, сводка), но иногда добавить контекст (где я, сколько осталось) ради информированного решения; цель, чтобы было ровно достаточно.

**Слова автора:**

> So take a look at your design and identify where there's information you can distill down to its essence. Is there complex data that might be better understood as a graphic? Are there opportunities to summarize information so people can focus on what they care about? Make sure every element helps clarify your point. And in some cases, making an interface simpler can mean adding more to it. Take this video play/pause control. It's simple and familiar. I can pause what I'm watching, and when I come back to it later, I need more context. This control clarifies where I am and how much time is left. Sometimes, simple means adding context and information, so people can make informed decisions. Simple interfaces support the reason people are there. And you'll know you've arrived at simplicity when you have exactly enough!

**Для Напарника:** Таймер Фокуса: показывать, сколько осталось и где человек, а не только голое число; сводки сессий на Мире.


---

## 9. Крафт: халтура чувствуется, тщательность вселяет уверенность
`крафт · доверие · вкус` · [13:39](https://youtu.be/Xa9L2yx_QH8?t=819)

**Мысль:** Задержки на кнопке, дёрганый скролл, смещённые иконки, ломающаяся при повороте вёрстка делают продукт хрупким и подрывают веру в результат.

**Слова автора:**

> Craft is the attention to detail that tells people you really care about the experience you're giving them. We all know what a cheap product feels like. A rickety door that doesn't close properly. A shirt that unravels when you wash it. You can just tell when someone took shortcuts. And it's the same with software. You know exactly what it feels like to use an interface that was rushed out the door. You tap a button and you just have to wait for it do something. Scrolling is jittery. Icons are misaligned. You rotate your phone, and the layout gets all messed up. It feels fragile. When software feels thrown together, you question the quality of the results you'll get from using that product. But a meticulously crafted design does the exact opposite; it inspires confidence.

**Для Напарника:** Прогнать Дом/Фокус/Мир на дрожание анимаций, выравнивание и поворот; работать на доверие человека с СДВГ.


---

## 10. Восторг это выбранная эмоция, а не конфетти в конце
`дофамин · награды · вкус` · [15:51](https://youtu.be/Xa9L2yx_QH8?t=951)

**Мысль:** Радость создаётся определением эмоции, которую хочешь вызвать (спокойствие, уверенность, воодушевление), и её усилением по всему дизайну, а не украшательством.

**Слова автора:**

> Delightful interfaces are satisfying, enriching, and create a real emotional connection. That connection starts when an experience feels human. The way to make a design delightful isn't by adding confetti or tacking on extra flourishes at the end of your process. You create a delightful interface by identifying the emotion you want your audience to feel. Relaxed, confident, excited, and finding opportunities to reinforce that through your design. Delight is the sum of the consideration you put into your product. It's the natural result of getting all the design principles right.

**Для Напарника:** Выбрать эмоцию для каждого экрана (Дом: тепло, Фокус: спокойная уверенность, финал: пик) и усиливать её дизайном, а не декором.
