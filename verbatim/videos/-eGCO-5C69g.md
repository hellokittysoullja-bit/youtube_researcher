# WWDC21: Design for spatial interaction | Apple

**Канал:** Apple Developer · 18 мин · субтитры: en (ручные) · https://youtu.be/-eGCO-5C69g

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Интерфейс меняется с масштабом: щедрый допуск вдали, строже вблизи, доминанта обратной связи сменяется
`анимация · хаптика · дизайн-система · крафт` · [04:22](https://youtu.be/-eGCO-5C69g?t=262)

**Мысль:** Одна и та же кнопка меняет роль по мере приближения; допуск по углу сужается незаметно для человека, а на малом масштабе ведущей становится хаптика. Принцип прогрессивного уточнения без лишних объяснений.

**Слова автора:**

> In fact, the same button that gave me directions when I was far away has now become a button that will help me find it as I'm closer. Augmenting elements of the design when at the appropriate scale is a great way for people to discover and use these new abilities. As iPhone is locating my AirTag, I'm invited to move around and search my surroundings. Once connected, an arrow forms and points directly to where I need to go. As I align with the direction of my AirTag, the design lights up to reinforce this. We emphasize this facing direction and provide guidance when not facing this direction. In a subtle way, this distinction also scales based on distance. When further away, we found that it is really hard to remain facing a specific direction. To remedy this, we are actually more generous with the angle that iPhone considers facing. As you get closer, this forgiveness becomes more narrow to become more and more specific. This happens without you noticing as you're gently guided to your AirTag. When you're finally within arm's reach of your AirTag, the arrow defers to a form of feedback that we find much more effective at this small scale. The design transforms to highlight haptic feedback as you pass your iPhone over where your AirTag might be hiding. With this example, we've shown you how your design can transform based on distance, whether you're very far away or within millimeters. Think about how your design can best accommodate varying abilities we all share as humans. Be forgiving with angles at a distance, and consider changing the dominant form of feedback to one that works best at smaller scale.

**Для Напарника:** Фокус: чем ближе к концу сессии, тем более тихой и точной обратная связь (мягкая подсветка кота/кольца, хаптика на финише) вместо громких сообщений.


---

## 2. Непрерывная обратная связь: видимая, слышимая, ощутимая; прерывание и отмена
`хаптика · звук · анимация · крафт` · [06:13](https://youtu.be/-eGCO-5C69g?t=373)

**Мысль:** Обратная связь делает функцию обнаруживаемой, обучает, сообщает об успехе или неудаче и признаёт, что движение может начаться, остановиться или прерваться в любой момент.

**Слова автора:**

> We've gone to great lengths to make onscreen interactions fluidly and dynamically respond to touch input, but this continuous feedback is even more critical when interacting in the physical world where your device becomes a more literal extension of your body. The right type of feedback applied and choreographed at the right time throughout these interactions can help make the feature you're designing discoverable, provides instruction, and can communicate success or failure. It also acknowledges that our movements can start, stop, and be interrupted at any time. We're going to talk about how you can use feedback you can see, hear, and feel to help connect your interaction to the physical world. Though dependent on the capabilities of the devices used, there are multiple types of feedback worth considering and using together. These can include visual feedback -- such as user interface changes, lights and hardware interactions, and visual feedback coordinated across both devices -- audio feedback , and haptic feedback. We'll also talk about natural interruption and cancellation and the importance these play in creating a successful interaction between two devices.

**Для Напарника:** Сессия Фокуса: человек может прервать/уйти в любой момент, и отклик должен быть тёплым и без вины; используй слой плавной визуальной реакции, а звук/хаптику оставь для ключевых моментов.


---

## 3. Две пороговые зоны и обратная связь, прямо привязанная к движению тела
`анимация · хаптика · крафт` · [07:33](https://youtu.be/-eGCO-5C69g?t=453)

**Мысль:** Баннер, размытие и хаптика непрерывно следуют за расстоянием; тот же жест, что подтверждает, позволяет и отменить, без лишних кнопок. Прямота связи движения и отклика критична.

**Слова автора:**

> With HomePod mini, we use multiple types of feedback to establish a physical relationship with your iPhone, provide direction, and ultimately confirm that your music has been successfully transferred. We achieved this by creating two discrete boundaries around the HomePod, and respond to your movement across and between them. Feedback is provided when your iPhone reaches the first zone, between the first and second to instruct you to move closer or allow you to cancel the interaction, and finally when your iPhone reaches the second zone, to confirm and transfer music. Feedback is continuously provided from the moment iPhone reaches the first distance threshold. On screen, the banner position, scale, and modality created by the background blur increase fluidly and in direct response to your distance from the HomePod. When designing visual feedback, look for opportunities for the onscreen elements to animate in a way that feels related to your physical movements -- like how the movement of this banner is related to the linear movement of your hand towards or away from the HomePod. Haptic feedback complements this with a physical acknowledgement that the two devices are aware of each other, and increases in strength to encourage you to continue moving closer. In addition to the feedback on iPhone, HomePod mini acknowledges the proximity of iPhone through the animations on the top of the speaker. Great spatial interactions use natural body movements to not only confirm but also to cancel actions. When moving an iPhone near a HomePod mini, clear and continuous feedback that tracks your distance from the HomePod makes it clear that you can simply pull away to cancel or interrupt the gesture. This allowed us to create an interaction that can be done entirely without looking at the display or requiring additional onscreen buttons to cancel or confirm user intent. All of these aspects are driven by and respond to the movement of your body as it brings iPhone closer to or farther away from the HomePod. The directness of the relationship between someone's movements in the physical world and what they're seeing, hearing, and feeling on one or both devices are critical when designing a spatial interaction.

**Для Напарника:** Анимации в Напарнике должны быть связаны с действием человека (перетягивание реплики, удержание кнопки старта) и быть обратимыми, без отдельной кнопки отмены.


---

## 4. Отзывчивость к большим и малым движениям; пульс ускоряется по мере приближения
`хаптика · звук · анимация · крафт` · [10:06](https://youtu.be/-eGCO-5C69g?t=606)

**Мысль:** Дизайн должен реагировать на каждый шаг и поворот, связывая действие с откликом; ритм пульса и хаптики ускоряется и становится чётче при приближении, а при отклонении интерфейс возвращает на путь.

**Слова автора:**

> A spatial interaction feels great when it's responsive and follows your motion. That means responding to movements that are big as well as ones that are subtle. Even as iPhone is connecting to the AirTag, the interface gently rotates and responds as I turn, implying the nature of the interaction that is about to follow. These dots also provide the building blocks for a continuously adapting experience. Once connected, the distance between me and my AirTag also appears. This distance responds incredibly precisely as I walk in any direction. It instantly updates and tells me if I'm walking toward, or away, from where I want to go. As I walk around, the same dots smoothly form an arrow pointing me in the right direction. This moment is reinforced further using a delicate haptic and sound to mark its importance. It feels as though the arrow floats in space as my iPhone moves around it. As you saw earlier, the interface reinforces moments when I am on the right path. When facing the direction of my lost AirTag, the screen boldly lights up and I also feel and hear the arrow snap into place. By responding to every step and subtle turn, the design feels tightly coupled with me and the space I'm in. When designing your spatial interaction, consider how people will connect their own movement with what they experience on the device. Try to make a clear link between action and feedback in a way that is mindful of the particular motion. Just ahead of the arrow, there's a dot that starts to pulse in my hand. The pace of this pulse picks up as I get closer, and the haptics become tighter and crisper along with it. If I break away from this direction, the pulse stops and the interface guides me back. If I walk far enough away from my AirTag, the arrow disassembles to mark the loss of signal. Nuance in moments like these also provide important and very helpful guidance. Be mindful of how feedback can complement human motions that are varied and unpredictable, and build a design that is resilient and can adaptively change to accommodate the way we move.

**Для Напарника:** Индикатор прогресса сессии/острова: ритм дыхания существа или костра чуть меняется по мере приближения к концу таймера (медленно, диегетично, без пульсации ради пульсации).


---

## 5. Слои обратной связи: визуал как непрерывный слой, звук и хаптика для важных моментов
`хаптика · звук · крафт · внимание` · [11:56](https://youtu.be/-eGCO-5C69g?t=716)

**Мысль:** Для разных масштабов подходит разная модальность (на малом расстоянии звук не нужен, хаптика эффективнее). Звук и хаптику применяют сдержанно и с повторяемой причиной и следствием.

**Слова автора:**

> When within arm's reach, we visually zoom in on this dot, and the pulse changes to continuous haptic feedback that shifts with my movement. This haptic response changes in character as I move closer and further away. I can move my iPhone over where AirTag might be and sense through my hand more precisely where it's hiding. Note that we do not use sound for this part of the experience, as haptic feedback does a much more effective job. As with any continuous feedback, your design should be mindful of how haptics, sound, and visuals work together in concert across the senses. Similarly to the way we perceive what we see, hear and feel in the world as one holistic experience. When designing your interaction, it is important to consider the different strengths of each form of feedback and how they can be used together. Seek to provide a visual layer of continuous feedback tied to physical motion and use additional feedback to emphasize important moments in your interaction. Use haptics and sound judiciously and at the right levels, with a repeatable cause and effect so it is clear what is being communicated.

**Для Напарника:** Подтверждает принцип проекта: хаптика на события мира, а не на каждый тап; визуал несёт непрерывный слой.


---

## 6. Опираться на естественное физическое действие, а не на абстрактный список опций
`игровой-дизайн · крафт · мобильный` · [13:13](https://youtu.be/-eGCO-5C69g?t=793)

**Мысль:** Вместо списка AirPlay человек просто подносит телефон к нужной колонке: интерфейс уступает физической задаче, «этот/тот» вместо навигации по меню.

**Слова автора:**

> In the case of HomePods, we use spatial awareness to make the task of selecting a speaker more natural. Oftentimes, I'll be listening to some music, and I'll want to move it from my iPhone to a better speaker near me. Previously, if I wanted to play this song on a different speaker, I'd have to go into the AirPlay list. In this list, all of the other devices in my space are presented equally, whether they are near me or not. What I am really interested in, though, is this particular HomePod. With this new human-scale interaction, I can finally transfer a song to this HomePod without navigating an onscreen UI, or having to interact with the screen at all, for that matter. We provide visual feedback on the HomePod itself to show that the music is about to be transferred. The light modulates precisely with my movement, growing in intensity as I approach, and shrinking as I move away. And of course, the ultimate confirmation of the transfer is the music playing from the speaker itself. By embracing the physical action, a previously intangible experience now feels completely tangible, visceral, and instinctive. Think of ways that your own interfaces can support a natural physical motion, rather than an abstracted list of options. Try to make your experiences and designs defer to the physical task at hand.

**Для Напарника:** Дом: вместо длинных меню выбора, один жест или одна кнопка прямо у объекта (например, тап по коту или по костру начинает действие).


---

## 7. Крупная жирная типографика и несколько модальностей, когда взгляд занят другой задачей
`доступность · внимание · типографика · мобильный` · [15:19](https://youtu.be/-eGCO-5C69g?t=919)

**Мысль:** Интерфейсы, которые читают периферийным зрением (навигация, пульт, калькулятор), делают крупными и контрастными; несколько режимов обратной связи доступны разным людям; нельзя конкурировать с основной задачей; хорошие состояния нужно подкреплять и отмечать.

**Слова автора:**

> When it comes to the visual feedback on iPhone itself, make sure it can be read when performing a task that extends beyond the bounds of the display. We often design our interfaces to work in this manner when we anticipate it will be viewed in the periphery. For instance, when using turn-by-turn navigation, the typography of when and where I need to take my next turn is bigger and bolder than other notifications that might occupy the same space. The buttons and active area of TV Remote are extra large and are designed for your eyes to be directed to the TV itself, rather than the control for it. The digits and operation buttons in Calculator are large and bold, as we anticipate you might be referencing numbers on a restaurant bill to calculate a tip, for instance. As in the previous examples, the type size we use for the distance when finding an AirTag is set much larger than in other parts of the system, and the entire UI revolves around the central element of a giant arrow. Bold color changes can be read in my periphery. Sound reinforces key moments and states -- I can actually feel the distance getting smaller as I walk without ever having to look at the screen. This ultimately supports a more natural pose as I use it. When in arm's reach, haptic feedback can guide me closer even if the screen is not in my periphery. These large and bold UI choices enable those with varying abilities to access the experience as well. Make sure your design uses more than one mode of feedback, and that each one is salient enough to be clearly understood. Your design shouldn't demand too much attention to communicate its information or compete with the primary task. Lastly, try to reinforce good states and celebrate positive progress along the way to completing a spatial interaction. Always consider the physical action your experience is complementing.

**Для Напарника:** Экран Фокуса: пока человек работает, оставшееся время и состояние кота читаются краем глаза, крупно и с цветовым сдвигом, без требования внимания; хорошие шаги празднуются тихо.
