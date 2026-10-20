# WWDC21: Practice audio haptic design | Apple

**Канал:** Apple Developer · 16 мин · субтитры: en (ручные) · https://youtu.be/qcO9NMKn3Ao

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Apple: причинность, гармония, полезность — три принципа хаптики
`хаптика · звук · принципы · крафт` · [03:07](https://youtu.be/qcO9NMKn3Ao?t=187)

**Мысль:** Обратная связь должна быть очевидно связана с причиной, согласована по органам чувств (маленькое звучит и ощущается маленьким) и приберегается для значимых моментов, иначе становится назойливой.

**Слова автора:**

> To help achieve magic and delight in your app experience, here are three principles to guide the work. They have been useful to us internally, and I hope they can help you as well. They are causality, harmony, and utility. For feedback to be useful, it must be obvious what caused it. It's about making the source or the cause of the feedback clear and obvious. The simplest form is getting feedback as the ball hits the wall and the boundary of the phone. It's a collision with associated sound and haptics. Similarly, the haptics rolling texture is only presented when the background visual is shown. You understand that the grid is what created that sensation. Our second principle, harmony, highlights that our senses work best when they are coherent, consistent, and working together to create a given experience. It should feel the way it looks, and the way it sounds. A small ball should feel small and sound small. A large ball ought to sound and feel heavier, like it has real extra mass. Our third principle, utility, is about providing clear value to your app experience. Don't add feedback just because you can. It can quickly become overwhelming and unpleasant. Reserve haptics and audio for significant moments in your app, like the growth of the ball.

**Для Напарника:** Хаптику и звук в Напарнике привязывать к событиям мира (находка, финал сессии, рост острова), а не к каждому тапу; вибрация, звук и анимация одного события должны совпадать по характеру и длительности.


---

## 2. Гармония: подбираем хаптику под звук, а не наоборот
`хаптика · звук · анимация · крафт` · [09:14](https://youtu.be/qcO9NMKn3Ao?t=554)

**Мысль:** Дизайнер слушает два ассета и видит, что дискретные удары не совпадают с плавным звуком; берёт непрерывную хаптику и звук из первого ассета, чтобы чувства усиливали друг друга.

**Слова автора:**

> The problem is the haptic and the sound don't really match. The haptic is made of three transients... While the audio is continuous and progressive. There's no harmony between the two senses. Let's look at the alternate asset which is called ShieldContinuous. It has a continuous haptic progression... And a wobbly audio that decays. Again, I can feel and hear that the haptic and audio don't really match. But I like the haptic. It feels like a good transformation for gaining a shield. Let's hear the haptic again. My plan is to use that continuous haptic pattern but use the sound from the first asset. I'll use the two assets and take the audio I like from the first pattern and use it in the second continuous haptic pattern. Let's see how I do that in practice. First I open the ShieldContinuous.ahap file in a text editor and scroll to the end of the file. You'll see this event where we specify the audio file to play with the haptics. It's using the EventType AudioCustom with a filename for the audio file. You can specify and adjust the volume using a ParameterValue. To use the preferred audio, I change the file reference from ShieldB.wav to ShieldA.wav. The revised and final asset looks like this. The haptic... and audio are coherent. They support and reinforce each other.

**Для Напарника:** На финале сессии (RevealIsland) профиль хаптики (нарастание или короткие удары) должен повторять форму звука и анимации; проверять на устройстве, что нет рассинхрона.


---

## 3. Интенсивность хаптики привязана к скорости объекта
`хаптика · анимация · крафт` · [12:26](https://youtu.be/qcO9NMKn3Ao?t=746)

**Мысль:** Непрерывная текстура модулируется параметром движения, поэтому ощущается как физический контакт, а не как заранее записанный эффект.

**Слова автора:**

> The function updateTexturePlayer is called on every frame the texture is active. We use it to update the intensity of the haptic based on the speed of the ball.

**Для Напарника:** Если появится драг-взаимодействие (перетаскивание, свайп к ответу), вибро-отклик можно масштабировать скоростью жеста; но на вебе ограничено Vibration API, не применимо на iOS Safari.
