# How Do You Design Accessible Filters for Cognitive Disabilities? - Web Accessibility For All

**Канал:** Ariel Ferro · 14 мин · субтитры: en (ручные) · https://youtu.be/9E6jKXq97mY

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. История: фильтр применился молча — «приложение считает меня сломанной»
`доступность · доверие · исследования` · [00:34](https://youtu.be/9E6jKXq97mY?t=34)

**Мысль:** Тихая смена результата без обратной связи не UX-мелочь, а исключение: человек винит себя, хотя сломан интерфейс.

**Слова автора:**

> Let me take you back to a moment. I was helping a team, test an admin dashboard for a medical nonprofit. Real-world users, real-world stakes. A voluntary nurse, who was using a switch device and a screen reader, was trying to find patients with urgent appointments scheduled for the next day. She used the filter drawer, toggled a few options and hit Apply... Nothing happened. Turned out the page had silently sorted by name, not by date. And the Urgent label was hidden inside a collapsed accordion section. She sighed: -Honestly, it feels like this app considers I am the broken part here! That stucked with me, because when filtering, sorting or searching go wrong, it's not a UX glitch. It's exclusion.

**Для Напарника:** Любое изменение в Напарнике (сохранилось, шаг отмечен) подтверждать голосом кота инлайн, не молча.


---

## 2. Авто-применение без обратной связи путает когнитивно уязвимых
`доступность · СДВГ · микрокопирайтинг` · [05:12](https://youtu.be/9E6jKXq97mY?t=312)

**Мысль:** Люди с когнитивными задержками не замечают, что страница изменилась; лучше явная кнопка применить или чёткий отклик и перенос фокуса.

**Слова автора:**

> Pitfall 2, filters auto applying with no feedback: Ah, yes! The magic interface where filters apply automagically without hitting a button. It's sleek, right? But here is what goes wrong: users with cognitive delays might not realize the page just changed. Screen reader users may not know results updated, because there's no focus shift. If you're going to auto apply, give clear feedback; announce changes with polite area leave regions. Move focus to the results heading. Or better yet! Let users apply filters manually, so they are always in control.

**Для Напарника:** Если в Мире/Доме появятся фильтры, применять их явным действием и озвучивать результат котом.


---

## 3. Сброс должен быть заметен для людей с проблемами рабочей памяти
`доступность · СДВГ · иерархия` · [06:24](https://youtu.be/9E6jKXq97mY?t=384)

**Мысль:** Слабо заметная кнопка «Очистить» — кошмар для тех, кто не помнит, что выбрал и как начать заново.

**Слова автора:**

> Pitfall 3, unclear reset functionality: How often do you see a Clear Filters button that is barely visible? For users with executive function difficulties, or short-term memory challenges, this is a nightmare! They can't remember what they chose and can't figure out how to start over. Always offer a Reset or Clear All function. Make it visible. Announce it. Clearly.

**Для Напарника:** На экране Фокуса дать понятный «начать заново/сменить шаг» без наказания.


---

## 4. Показывать активные настройки простым текстом и давать откат
`доступность · иерархия · СДВГ` · [07:35](https://youtu.be/9E6jKXq97mY?t=455)

**Мысль:** Невидимые состояния по умолчанию превращают фильтр в судоку; активные значения нужно показывать явно и легко отменять.

**Слова автора:**

> Problem one filtering is often a puzzle not a tool filtering interfaces can feel like sudoku especially for users with cognitive or executive function disabilities too many choices filters that interact in weird ways or unclear default states turn what should be a helpful refinement tool into a wall of options design tip make defaults visible show active filters in plain text and always give users an easy way to backtrack.

**Для Напарника:** Выбранную длительность/режим на экране Фокуса показывать текстом, с лёгким возвратом назад.


---

## 5. Невидимое трение: неопределённость = стресс или shutdown
`доступность · СДВГ · микрокопирайтинг` · [10:44](https://youtu.be/9E6jKXq97mY?t=644)

**Мысль:** Каждая двусмысленная подпись и непредсказуемый результат — налог на усталый мозг; помогает эхо действия («показано 24 результата») и отмена.

**Слова автора:**

> Cognitive challenges: Now let's talk about invisible friction. if you are neurodivergent, have brain fog, or experience cognitive fatigue from chronic illness, then every ambiguous label, every unpredictable result, every tiny font rapid visual shift, takes a toll. Examples: sort dropdowns that reset on every new search. Filter options that don't match the terms in the data. Interfaces where nothing tells you how many results your search returned, so you don't know if it is working or not. For some people, the ambiguity causes stress. For others it causes shutdown. Either way it means loss of access. Reduce ambiguity. echo back the user action. -showing 24 results for hiking boots size10. Let users Undo a sort or filter without starting over. And test your interface with real users who think differently.

**Для Напарника:** Эхо действия голосом кота («Записал: шаг «X»») и возможность отмены без потери прогресса.


---

## 6. Доступность — это агентность, а не только метки
`доступность · вкус · иерархия` · [12:18](https://youtu.be/9E6jKXq97mY?t=738)

**Мысль:** Людям нужно пространство подумать, чёткие контрольные точки и возможность восстановиться; ясность важнее минимализма.

**Слова автора:**

> Wrapping up: Accessibility isn't just about labeling things right. It's about agency. Can users do what they need to do in the way that makes the most sense for them? Can they recover from mistakes without starting over? Can they move at their own pace using their preferred input method? Filtering, sorting and search often fail not because they are hard to use, but because they are rigid! We want to reduce clicks, But people needs space to think. We want instant results, but some users need clear checkpoints. We want minimal UIs, but clarity and affordance matter more than clean lines.

**Для Напарника:** Не прятать важные действия ради «чистоты» интерфейса; ясность и понятность кнопок — приоритет.
