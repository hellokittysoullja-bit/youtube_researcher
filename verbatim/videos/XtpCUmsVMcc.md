# Gleam: Lessons on App Design When Vibecoding | App Breakdown #35

**Канал:** App Breakdown · 16 мин · субтитры: en (авто YouTube) · https://youtu.be/XtpCUmsVMcc

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Порядок: спроси, дай ценность на основе ответов, и лишь потом аккаунт
`онбординг · активация · доверие` · [02:11](https://youtu.be/XtpCUmsVMcc?t=131)

**Мысль:** Типичная последовательность: вопросы, знакомство, польза, основанная на ответах, затем просьба; здесь онбординг только просит и не даёт ничего взамен.

**Слова автора:**

> All right, now they ask to create an account. So in this case, they didn't even give me anything before trying to get me to create account. Usually the sequence is you ask for stuff, you get to know the user, you give them some value based on what they just answered, and then you ask for account creation or any other ask that you have. In this case, they didn't even give the value. They just ask for things. This whole onboarding is just asking.

**Для Напарника:** Любой диалог с человеком в Напарнике: сначала что-то вернуть (реакция, мини-награда), потом просить.


---

## 2. Фейковый системный запрос уведомлений: работает, но это манипуляция
`уведомления · тёмные-паттерны · этика` · [03:33](https://youtu.be/XtpCUmsVMcc?t=213)

**Мысль:** Приложение имитирует системное окно, чтобы человек механически нажал «разрешить», а потом показывает настоящее; конверсия высокая.

**Слова автора:**

> Fake notification prompt to get you to allow notifications. If you tap here, real pop-up comes up. If you've not seen this before, a lot of apps do this thing where essentially they use a fake system prompt inside of the app to get you to mindlessly scroll allow or not scroll to mindlessly tap allow. And when you tap, then they actually display the real prompt to get you to accept. It's something that actually works if you see if you see it in the data, this actually works. I'm not sure if it works on this app specifically, but if it's well done, then you're going to get high conversion rates.

**Для Напарника:** не применимо: имитация системного диалога это тёмный паттерн, противоречащий тёплому честному тону; использовать честный экран голосом кота.


---

## 3. Ритуал обязательства: приложи палец, дай слово, тактильный отклик и анимация
`запуск-задачи · онбординг · хаптика · мотивация` · [04:15](https://youtu.be/XtpCUmsVMcc?t=255)

**Мысль:** Жест (подпись, отпечаток, несколько тапов «я согласен, я сделаю») превращает намерение в обязательство, и хаптика с анимацией делают этот момент запоминающимся.

**Слова автора:**

> Oh, okay, this is an interesting pattern. So, your journey starts now, and basically they want me to give my word to the app. And some apps do this in different ways, for example, with multiple taps on something like, "Yes, I agree, and yes, I'm going to do it." And then click continue. Other apps, for example, like Honk have the little signature. So, for example, you do something on the app, you give your word, and then you sign as a sign of like commitment. In this case, it looks like I'm going to put my fingerprint to give my like commitment to it. So, this is a very cool pattern. The design itself is not out of this world, but I really like this structure here. So, let's actually put my fingerprint. Nice little haptics and animation on the back. Boom, coming in and loading what it unlocked with my fingerprint. I really love this interaction. It's my favorite part of the app this far.

**Для Напарника:** Ритуал старта сессии: удержание пальца на камине/коте «зажечь очаг» с хаптикой (hapticStart) и анимацией; вызывать без давления и вины, как приглашение.


---

## 4. Не веди новичка в тупик, особенно в первой сессии
`онбординг · доверие · иерархия` · [06:37](https://youtu.be/XtpCUmsVMcc?t=397)

**Мысль:** Крупный заметный элемент, ведущий на заблокированное, тратит тапы и сбивает с толку; главный сигнал должен вести к реальной ценности.

**Слова автора:**

> Me to tap on something where everything is locked. Basically, here, if you see the screen, there's two things that they want you to tap, or at least it's this is what they're signaling. The big orange box and the circle star. But, the big orange box actually does not do anything cuz everything is locked inside of it. So, this is just a big waste of empty space and of CTA when the main thing you're calling for attention is actually a dead end. Never lead users to dead ends, especially when it's their first session, cuz they're going to feel confused and they're going to waste taps. You do not users feeling confused or wasting taps, so never lead them to dead end.

**Для Напарника:** Самая заметная кнопка на Доме должна запускать Фокус, и нигде нет заметных, но недоступных элементов.


---

## 5. Стрик с первого дня: пламя, которое надо поддерживать
`стрики · геймификация · этика` · [09:20](https://youtu.be/XtpCUmsVMcc?t=560)

**Мысль:** Приложение выдаёт «1 день» до реального использования, чтобы создать пламя, которое жалко потерять.

**Слова автора:**

> And we have a one-day streak. Of course, they're trying to keep you hooked from day one by having a streak from day one cuz it's actually been zero days since you've used the app but they give you a one streak so that now you have a flame on the app that you have to keep burning.

**Для Напарника:** не применимо: стрики через страх потери противоречат принципу без стыда и вины; рост острова должен быть накопительным.


---

## 6. Не обрезай самую важную часть интерфейса
`иерархия · типографика · доступность` · [11:35](https://youtu.be/XtpCUmsVMcc?t=695)

**Мысль:** Спроси, что самое важное в экране; если это текст задания, его нельзя усекать многоточием.

**Слова автора:**

> Okay, so this here's a good example where the design could be better just with a little bit more thought put into it cuz if you're designing something to tell a user what a quest is, then the first question you should ask is, "Okay, what is the most important part of the design?" And the most important part is telling the user what the quest is. Therefore, you cannot truncate it. Like you cannot truncate the best part of the design, the most important part.

**Для Напарника:** Текст шага/задачи на экране Фокуса показывать целиком (перенос строк), а не усекать.


---

## 7. Главный экран держи на частом и лёгком действии
`привычки · удержание · запуск-задачи` · [13:25](https://youtu.be/XtpCUmsVMcc?t=805)

**Мысль:** Чтобы продукт встроился в жизнь, основное действие должно быть частым (5-минутный урок), а редкое и трудное (квесты) вторично.

**Слова автора:**

> Make sense that you would need today to be the home because just from a like app continuity and app success perspective, it is a lot easier to have people do these 5-minute lessons per day than it is to have them go out and talk with strangers. So, you need something that creates some kind of a habit and you need actions that people do frequently for your app to make sense and to actually blend into people's lives. So, it makes sense that quests is sort of a side thing and the main thing is actually the 5-minute lessons. That's just the nature of blending things into people's days.

**Для Напарника:** Дом: центральное действие это короткая сессия (до 25 мин с вариантами поменьше); тяжёлые цели оставить на второй план.


---

## 8. Когда человек сам нажал «Upgrade», не переубеждай его
`конверсия · цены · этика` · [14:30](https://youtu.be/XtpCUmsVMcc?t=870)

**Мысль:** Нажавший уже убеждён: в этот момент не нужен трёхшаговый экран, нужна возможность сразу оформить; различие между «толкаю пользователя» и «пользователь толкает меня».

**Слова автора:**

> I'm not a huge fan, to be honest, especially when you tap upgrade to premium. Basically, if you have a button on a profile that says upgrade to premium and someone taps it, they are likely already convinced that they want to upgrade. You're not trying to convince them just like you were on the onboarding or in any other flow because here it's not so much that you are getting them to upgrade is that they are telling you that they want to upgrade. And so, whenever an upgrade opportunity like this arises, I like it when apps just pull up the Apple Pay. Like, if I tell you I want to upgrade, just let me upgrade and that's it. Don't show me a three-step screen. But yeah, that's a basically a tiny but very important difference in pushing the user to do something versus the user pushing you to try to do something.

**Для Напарника:** Если человек сам открыл платёжное действие (когда появится), показать его без лишних шагов; не применять давление.
