# WWDC24: Design Live Activities for Apple Watch | Apple

**Канал:** Apple Developer · 8 мин · субтитры: en (ручные) · https://youtu.be/MH5etXiIz0Y

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Показывай только значимые состояния; один контрол
`иерархия · мобильный · внимание` · [05:58](https://youtu.be/MH5etXiIz0Y?t=358)

**Мысль:** Показывать то, что нужно для значимых состояний: прогресс, требуемое действие, важное изменение; контролы нужны для запуска/паузы; на малом экране лучше один.

**Слова автора:**

> Is how much information is too much or too little? To answer that, we recommend showing only what is necessary to communicate significant states in the live activity. These are states that help people understand progress, like how long until your flight touches down. Or states that might require action, like getting to the curb because your Uber is arriving. Or these could just be states that someone might really care about, such as a change in the score of a game. Another common question is whether or not controls make sense for your live activity. Controls are best for live activities that need to be played, paused or resumed. For example, a workout, a timer, or a voice memo. Whatever the control is, we strongly recommend sticking with just one, as multiple controls are challenged by the small space, which also need to provide enough information to communicate state.

**Для Напарника:** Экран таймера Фокуса: время/прогресс и одна кнопка (пауза/готово), остальное убрать.
