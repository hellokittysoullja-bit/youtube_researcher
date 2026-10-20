# I used AI to design my app's mascot (this is how)

**Канал:** Adam Lyttle · 8 мин · субтитры: en (авто YouTube) · https://youtu.be/zmfzCi_fpJc

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Маскот даёт причину возвращаться и «душу» приложению
`маскот · удержание · доверие` · [00:35](https://youtu.be/zmfzCi_fpJc?t=35)

**Мысль:** Эмоциональная связь с персонажем удерживает пользователей, а не просто делает приложение симпатичным.

**Слова автора:**

> Mascots don't just make an app look cute. They give users a reason to keep coming back. They give an app a soul.

**Для Напарника:** Подтверждает роль кота-напарника как главной причины возвращаться на Дом.


---

## 2. Маскот должен иметь функцию в продукте, а не «приклеенную» роль
`маскот · персонаж · игровой-дизайн · процесс` · [02:17](https://youtu.be/zmfzCi_fpJc?t=137)

**Мысль:** Идея пришла из вопроса, как маскот взаимодействует с пользователем: полосы на лбу как чёрные клавиши, белый кот как белые клавиши, спящий кот просыпается при ошибке.

**Слова автора:**

> Then I had to think how this mascot would actually interact with the app itself so it doesn't just look like it's being plonked in there. If the identity of the app is going to be rebranded and based entirely around this mascot, I needed to serve an actual purpose for it so it actually fits in. So I started brainstorming some ideas. It's a piano app after all. So the mascot should have some simple element of music iconography. My original sketches revolved around this David Bowie inspired cat. But I just I wasn't connecting with it. I had to go back to the drawing board. I had to ask myself, how does this mascot interact with the user? How does this mascot make sense in the app? And that's when I had a bit of an aha moment. Instead of lightning bolt, why not make three stripes on the cat's forehead symbolic of the three black notes? From there, everything else just flowed really nicely. Instead of a gray cat, it's a white cat representing the white keys. And I felt like, hey, this is kind of a cool dude. He needs a little bow tie. And this is the first mascot that I've ever designed. I don't want to design something that's hard to animate. So, what's the easiest pose to animate? Well, if he's asleep the whole time, it's going to be really easy to animate. Then, when you hit a wrong note, the cat wakes up and you lose a life. This grounds the mascot into the app itself, and now it kind of makes sense.

**Для Напарника:** Роль кота в Напарнике (присутствие у костра, реакция на сессию) задавать как функцию продукта; без наказаний вроде потери жизни.


---

## 3. Выбери образ, отражающий суть продукта, и свой уровень навыков
`маскот · процесс · крафт` · [03:47](https://youtu.be/zmfzCi_fpJc?t=227)

**Мысль:** Метафора продукта (помодоро: томат) и интеграция в приложение; не берите сложный стиль на первую попытку.

**Слова автора:**

> So, to come up with a mascot, you need to think about what type of animal or object best represents your app. For example, a pomodoro timer could have a tomato. A relationship app could be flowers or a love heart. You get the picture. And then you really need to think about how the mascot interacts or feels part of the app and not just plonked in there. You should also consider your own skill level at this stage, too. Don't go animating a 3D Pixar inspired mascot on your first attempt.

**Для Напарника:** Кот у костра как метафора присутствия; держать стиль простым и анимируемым.


---

## 4. Шаблон маскота + собственный набросок позы + ИИ только полирует
`ИИ · маскот · процесс · крафт` · [05:03](https://youtu.be/zmfzCi_fpJc?t=303)

**Мысль:** ИИ хорош в полировке своих идей и посредственных шаблонных идеях; эскиз позы и шаблон сохраняют пропорции.

**Слова автора:**

> This acts as my template and I can ask Chat TPT to manipulate my mascot into any pose I want while keeping the design and proportions consistent. First, I do a rough sketch of a pose and then I use the prompt I want this character doing XYZ in this pose. I provide chat GPT with a mascot template and my sketch. A so cute. It's important to do some of your own creative thinking here. You can't really outsource the design elements to chat GPT. It's really only good at two things. Polishing the ideas you've already come up with or coming up with its own bland, boring ideas. If you sketch your idea first, helps to prompt Chat TPT to provide a better mascot and pose. Plus, it saves you a bit of back and forth trying to get the mascot absolutely perfect.

**Для Напарника:** При создании поз/выражений кота давать ИИ эталонный шаблон и грубый эскиз; идеи придумывает человек.


---

## 5. Мелкие детали оживляют статичную картинку: хвост, голова, гравитация
`анимация · маскот · крафт` · [05:47](https://youtu.be/zmfzCi_fpJc?t=347)

**Мысль:** Раздельные слои с независимой анимацией (хвост, поворот головы, лёгкий отскок при посадке) превращают рисунок в живой образ.

**Слова автора:**

> Next, we're going to add this mascot to our app. And I guess you could just add the image into your app and call it a day, but it kind of feels so lifeless and a little bit boring. With a few Swift UI view animations and a few timers, you can turn a static image like this into this. The secret to making it look like a real life mascot comes down to the small details. a wagging tail, a dynamic expression, a rotating head, and gravity. Yes, gravity. When the cat drops into its default position, the head moves slightly and independently of the whole body, and everything kind of bounces a bit slightly when it hits the ground. This is achieved using Swift UI with animation bouncy and a few view layers as well. Then each layer has a different part of the mascot overlaid and independently animated. Seriously, this is worth your time giving your mascot those tiny, subtle qualities. It turns a beautiful design into a living design.

**Для Напарника:** Слои кота анимировать независимо с bouncy-посадкой при появлении; не трогать MascotSvg ради отдельного экрана, только осмысленно в общем компоненте.
