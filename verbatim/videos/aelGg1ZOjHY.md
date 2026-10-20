# Add Haptics to Your SwiftUI App - Modern .sensoryFeedback Tutorial (iOS 17+)

**Канал:** None · 8 мин · субтитры: en (авто YouTube) · https://youtu.be/aelGg1ZOjHY

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. На iPad и Mac вибрации нет: дублируй звуком или визуалом
`хаптика · доступность · мобильный` · [05:43](https://youtu.be/aelGg1ZOjHY?t=343)

**Мысль:** Haptic-вызовы на устройствах без мотора ничего не делают, поэтому обратная связь должна иметь запасной канал.

**Слова автора:**

> Haptic is different depending on the device. For the iPhone, full haptic engine, all patterns work. For the iPad, there's no haptic hardware. Haptic calls do absolutely nothing. You'll maybe want to pair haptics with a sound or maybe a quick visual change on any iPad models.

**Для Напарника:** В вебе вибрация доступна не везде; события наград должны быть понятны и без хаптики (звук, анимация, реплика кота).


---

## 2. Хаптика: правильный паттерн, меру, единообразие и настройки пользователя
`хаптика · доступность · мобильный` · [06:29](https://youtu.be/aelGg1ZOjHY?t=389)

**Мысль:** Success для успеха и error для ошибки, не частить (иначе отключат или удалят приложение), быть последовательным, уважать системные настройки и давать альтернативу звуком, цветом или анимацией там, где вибрации нет.

**Слова автора:**

> So, one, use the right pattern for the right moment. Success for success, error for errors. Don't break those user expectations. Also, don't overdo it. you don't want your phone to like be buzzing constantly, otherwise people will turn haptics off or uninstall your app. You also want to be consistent. If one success action vibrates, all of the other ones should also vibrate. But again, don't overdo it. Also, respect any system settings. Users can disable haptics. Don't override that. And provide those alternatives for iPad and Mac OS. They don't vibrate. Use a sound color change or any animations to fill in the gaps.

**Для Напарника:** Совпадает с правилом §2 CLAUDE.md: хаптика на события, а не на тапы. Нужен фолбэк на звук и визуал для устройств без вибрации, плюс уважение prefers-reduced-motion и настройке выключения.


---

## 3. Шпаргалка: какой тип хаптики для какого момента
`хаптика · микрокопирайтинг · мобильный` · [07:13](https://youtu.be/aelGg1ZOjHY?t=433)

**Мысль:** Подтверждение кнопки: лёгкий impact; сохранение: success; ошибка: error; смена в пикере/тумблере: selection; pull to refresh: medium impact; пороговые значения: increase/decrease.

**Слова автора:**

> So, when should you be using haptics and what kind of style would I recommend? Any button confirmations? probably an impact with a weight of light. Any successful save or submit, maybe success or invalidation error or you can't log in. The dot error is fine. Any picker changes, maybe a toggle flips, you can use the dot selection to pull to refresh or trigger, you know, when you kind of slide down like when you get to the bottom of your YouTube or maybe Instagram feed and you want to refresh those. Probably the impact with a weight of medium. Any drag and drop or snapping on Mac OS, use the alignment. any threshold crossings, maybe max volume reached, you can use the dot increase or dot decrease. So, if you have a custom volume slider and you want that haptic feedback there, totally feel free to use the increase and decrease.

**Для Напарника:** Подтверждает решение из CLAUDE.md §4: selection-хаптика на смену значения в пикере длительности (только при реальной смене), success на завершение сессии.
