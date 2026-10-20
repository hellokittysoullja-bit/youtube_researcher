# WWDC24: Design great visionOS apps | Apple

**Канал:** Apple Developer · 19 мин · субтитры: en (ручные) · https://youtu.be/9QcD2pGLwzg

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Найди «ключевой момент» приложения, оптимизированный под платформу
`процесс · крафт · внимание` · [01:18](https://youtu.be/9QcD2pGLwzg?t=78)

**Мысль:** Во встроенном приложении осознанности цветок мягко пульсирует и расширяется, побуждая дышать и фокусироваться; это опыт, возможный только на этой платформе.

**Слова автора:**

> When we first work with a team we encourage developers to find their key moment, which is the moment in an app that’s optimized for visionOS. The Mindfulness app is an example on the system. The flower has a gentle pulse that encourages you to breathe and focus. When the flower expands it gives a sense of life to the scene.

**Для Напарника:** Определить ключевой момент Напарника (например, проявление острова в конце сессии) и вложить туда основную полировку.


---

## 2. Не переносить интерфейс как есть: десятки прототипов ради лучшего опыта на платформе
`процесс · крафт · игровой-дизайн` · [02:40](https://youtu.be/9QcD2pGLwzg?t=160)

**Мысль:** Команда Loona решила не делать оконный порт, а построить много прототипов; плоские эскизы стали 3D-моделями с деталями и тонкой анимацией.

**Слова автора:**

> Great solutions take time to build and they’re a result of iteration and prototyping. This is Loona. The iOS app offers gracefully animated scenes that combine relaxing activities, storytelling, and atmospheric sounds to help you calm down or fall asleep. Bringing this UI into a windowed experience on visionOS would have been reasonable. But listen to how the team approached it. This is Sergey Gonchar, the co-founder of Loona: We just put ourselves in the mindset, we’re going to build a lot of prototypes, because we want to find the best possible experience we can shape for this platform. Take a look at the early sketches of their scooter concept. The 2D prototypes felt dimensional, they were begging to be broken into pieces to play with. And it took time, but these sketches evolved into 3D models, which took on a life of their own, with tons of fun, incredible detail and subtle animations.

**Для Напарника:** Прототипировать несколько вариантов экрана Мира и награды, а не шлифовать первый.


---

## 3. Звук как проводник, поощрение и награда, а не только фоновая музыка
`звук · награды · крафт` · [07:34](https://youtu.be/9QcD2pGLwzg?t=454)

**Мысль:** Как хаптика на iOS, звук может направлять, подбадривать и вознаграждать; продуманный звуковой момент делает опыт запоминающимся.

**Слова автора:**

> Another way to leverage immersion is to design meaningful auditory moments with thoughtful sound design. To clarify why sound can be a type of immersion, it might be helpful to first understand how visionOS handles sound. Sensors on the device understand the characteristics of your physical space, like the size and materials of the room. Then, the system adds reverberation to make it sound like the things you’re interacting with are really with you. This intricate level of recognition and accurate play-back make Spatial Audio on Vision Pro really powerful. In the same way that haptics on iOS can be a form of feedback for people, think of audio as not just ambient music, but an opportunity to guide, encourage and reward people.

**Для Напарника:** reward-sound.ts: короткие осмысленные звуки на события мира (старт, финиш, редкая находка), без постоянного фона.


---

## 4. Подсвечивай интерактивное и не подсвечивай просто читаемое; зона нажатия достаточная
`доступность · иерархия · мобильный` · [13:56](https://youtu.be/9QcD2pGLwzg?t=836)

**Мысль:** Если эффект наведения есть у каждого элемента, интерфейс запутывается; слишком маленькие цели заставляют быть точным, а это раздражает и утомляет.

**Слова автора:**

> Even though the interface requires a lot of data and information, this app does a great job of using hover effects correctly. Every element that's interactive and has a detail view, like hourly temperatures, uses a hover effect. But the data that is meant to be read like details around dawn and dusk, don’t require a hover effect. And having one would be more confusing and complicate the interface. Keep in mind, interactive elements need sufficient tap targets, so use at least 60 points of space. If hover effects are too small, a person may feel like they need to be very precise to interact with your app and that becomes frustrating and uncomfortable. When hover effects are designed properly they instill confidence in someone’s interactions.

**Для Напарника:** Чётко отличать нажимаемое от информационного в Мире и Доме; крупные зоны нажатия для людей с СДВГ и неточной моторикой.


---

## 5. Интерактивное держи близко, а движение используй, чтобы показать, что элемент нажимаем
`анимация · внимание · крафт` · [14:42](https://youtu.be/9QcD2pGLwzg?t=882)

**Мысль:** Мы ожидаем, что объекты в пределах руки интерактивны; тонкая пульсирующая обводка вокруг иконки направляет на первое действие, потому что мы чувствительны к движению.

**Слова автора:**

> Delightful experiences match our expectations of reality and honor our spatial awareness. DJay is exactly what people would expect from a DJ’ing app: a completely realistic DJ setup with two turn tables for your records, complete with tonearms and tempo syncing. The turn tables are placed in front of you, within arms reach, which compels people to interact with them directly. In this case, you can scratch the records, pickup the tonearms and slide the tempo in the same way you would with a physical turn table. We expect objects in arms reach to be interactive, because they’re close to us. When designing spatial experiences, this is an important principle to follow. Keep interactive content close to people, even though they can reposition it wherever they'd like, or interact it with indirectly. Our awareness of content around us is also heavily driven by animation and motion. When you launch the app, the first thing you need to do is select a track. Notice the pulsing stroke outline around the music icon. This is a subtle way to guide you to tap on the music library. It’s a simple detail with a big impact. Movement and animation are great ways to get peoples attention and let them know something is interactive because we’re inherently sensitive and receptive to it.

**Для Напарника:** Один мягкий намёк на главное первое действие в Фокусе (одна цель), без постоянной пульсации остальных элементов.


---

## 6. Тестируй на людях ложные срабатывания и убирай сложность, не нужную для главной радости
`исследования · процесс · крафт · запуск-задачи` · [16:53](https://youtu.be/9QcD2pGLwzg?t=1013)

**Мысль:** Жест поднесения руки к уху пришлось проверять на ложные срабатывания; сложный ручной подбор темпа автоматизировали, чтобы человек сосредоточился на творческой части.

**Слова автора:**

> They realized they had to account for false positives, such as when someone may be raising their hand to fix their hair or adjust the strap on Vision Pro. Here’s how Karim, the CEO and co-founder of Algoriddim, approached this: This required a lot of user testing. We had to gather feedback to ensure the gesture was accurately recognized. Getting feedback is so important. You may be surprised by the way people use your app and certain behaviors they have that may be different than your expectations. Understand the opportunities where it’s possible to abstract away the literal interpretation in order to make something more approachable and less complex. For DJay, let’s take a closer look at the turn table. Turn tables have existed in their analog form for quite some time, but the technology surrounding them has evolved tremendously. For example, matching tempos and syncing tracks can be complex on traditional hardware. There’s a barrier to entry for people who aren’t familiar with it. The Algoriddim team saw this as an opportunity. In the 3D environment, we asked ourselves, “Why a DJ would even need to manually match tempos? When we could completely automate the process under the hood?" This abstraction not only reduces complexity, but also enhances the user’s ability to focus more on the creative aspects of DJing. Removing complexity can help people enjoy the aspects of your app that resonate the most.

**Для Напарника:** Убрать из Фокуса всё, что отвлекает от главного: автоматические умолчания (25 мин) вместо настроек; проверять на реальных пользователях неожиданное поведение.
