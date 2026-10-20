# The challenge of designing AI products

**Канал:** Dive Club 🤿 · 10 мин · субтитры: en (авто YouTube) · https://youtu.be/EeaAtVDuJ7I

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Правильный уровень абстракции: пользователю нужен эффект, не техника
`ИИ · доверие · онбординг` · [00:00](https://youtu.be/EeaAtVDuJ7I?t=0)

**Мысль:** Чем больше абстрагируешь, тем меньше контроля; нужно решить, сколько сложности показывать. Людям нужно понимать, как контроль влияет на результат, а не что происходит технически.

**Слова автора:**

> Users don't care about your system prompts or what model you're using under the hood I mean most of the time they don't even want to think about Ai and that's why one of the biggest challenges of designing an AI product is figuring out the right level of abstraction what features do you expose when the underlying model can do almost anything the majority of the work that we've done over the last couple of years is trying to identify the right level of abstraction and there's a real trade-off there because the more you abstract something the less control you have over it and so we needed to make a decision about how much complexity do we expose for the benefit of giving people control versus how simple do we want to make the product for the benefit of being easy to use and intuitive to use that's Colin Dunton the founder and designer of one of my favorite AI tools visual electric and a highlight from our conversation was hearing how a big part of Designing a product like visual electric is helping users establish new mental models for AI you don't actually need to understand what's happening technically you just need to understand how it's going to affect the output.

**Для Напарника:** Не показывать пользователю промпты, модель, параметры; в Напарнике ИИ скрыт за голосом кота.


---

## 2. Слова для контролов важны; два слайдера, которые никто не различает, склеить
`ИИ · микрокопирайтинг · этика` · [01:20](https://youtu.be/EeaAtVDuJ7I?t=80)

**Мысль:** Название и подача контролов формируют ментальную модель; команда обнаружила, что слайдеры креативности и референса путают, и решила оставить один.

**Слова автора:**

> This makes language like the very specific words that you're using to describe affordances in incredibly important so it's not just the sort of UI controls but it's also what do you call this thing and how do you expose that and so we came up with the creativity slider and the creativity slider is this really useful tool where you can basically tell the model how much noise do you want to add colum went on to use the creativity slider as an example of how they're constantly iterating on this balance between power and simplicity there's a bunch of settings that you can Expose and we expose the creativity slider but we also expose something called a reference slider because when you're upscaling an image you don't want the image to change you presumably really like the image you just want it to be higher resolution with more detail so you want to minimize the amount of changes that happen during the upscaling process so if it's a photo of a person that you know you probably want that slider to be at the highest level because you don't want that to change at all even small changes in somebody's face are highly recognizable but if it's a photo of a landscape it's okay if it changes a little bit because it may actually be better if it changes because it can add more detail it can hallucinate a little bit more and it will actually produce a better looking image but that's an example of actually I think exposing too much complexity I think we have both of those Sliders in the product right now and I don't think anybody understands what the difference is between those two things so we're probably going to remove the reference slider and just have the creativity slider and that will affect your reference level.

**Для Напарника:** Названия кнопок и длительностей в Фокусе должны быть человеческими и различимыми; не плодить контролы с близким смыслом.


---

## 3. Чат как скрытие сложности: может, это и есть дизайн-ход
`ИИ · чат` · [05:46](https://youtu.be/EeaAtVDuJ7I?t=346)

**Мысль:** Открытое поле ввода называют временным недоразумением, но оно становится только популярнее; чат абстрагирует огромную сложность и, возможно, этого достаточно.

**Слова автора:**

> Interfaces are super open-ended right here's a text box like you figure out what to do with it are sort of misguided they're like a temporary historical blip that we will get over soon I'm hoping even if you give them like inline suggestions or like have a couple buttons it's still not guiding them through a specific workflow to a specific goal that's Maggie Appleton from last summer when she was leading design at elicit and I'll admit a year ago I was right there with her it felt like a no-brainer that we were going to move past the prompt box as the primary entry point for AI but there's a reason that it's only become more common in the last 10 months it reminds me of when Amar Rashi from 11 Labs was telling us about his conversation with Nate parrot who I interviewed back when he was the found designer at the browser company I was chatting with Nate Parr the other day and we were kind of debating back and forth I was like is the prompt box just the text field and a generate button really the best we can do and his opinion was actually that you know we're abstracting away a ton of complexity to just chatting and that is actually like maybe the design move like maybe that is actually as simple as it needs to be.

**Для Напарника:** Дом Напарника как чат оправдан: простой вход скрывает сложность, а подсказки и чипы дают мягкое направление.


---

## 4. Динамическое поле ввода, которое подстраивается и учит по ходу
`ИИ · онбординг · чат` · [08:57](https://youtu.be/EeaAtVDuJ7I?t=537)

**Мысль:** Вместо требования описывать всё текстом поле меняется под задачу (лирика, жанр с готовыми таблетками) и учит интуитивно без тултипов.

**Слова автора:**

> Could have started with just text and you just describe every single aspect and what that needs though requires is that you need your user to need to know all those things to be able to craft a great prompt to get a good result right and I was starting to think about this more in terms of a almost a dynamic Island kind of prompt box where if you need to change lyrics it morphs into a prompt box that's basically best designed around like how lyrics need to be edited and the parts of lyrics if you're about to choose genre instead of you thinking about it populates with pills of all the genres that you actually need to like maybe want to play with or think about and you could talk to it and maybe it'll actually point to you and grow like the UI will expand and grow based on that so still expanding on that base idea of chatting and prompting but teaching you along the way in a way that's very intuitive rather than tool tip here click that try to understand the thing yeah and I think that's the thing that with designing with AI you need to still capture the essence and the magic of it without putting the burden on the user.

**Для Напарника:** Поле ввода на Доме может подстраиваться под контекст (чипы вариантов шага, длительность) вместо длинных инструкций.
