# How To Design Color Accessible Webpages

**Канал:** Stefany Newman - Accessibility Instructor  · 13 мин · субтитры: en (ручные) · https://youtu.be/BW_PjPR825w

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Ошибка: не только красный, а иконка плюс жирность или размер
`доступность · цвет · иконки` · [03:44](https://youtu.be/BW_PjPR825w?t=224)

**Мысль:** Для ошибки нельзя ограничиваться цветом: добавляют иконку предупреждения и выделяют текст размером или весом, потому что цвет ненадёжен (дальтонизм, серый экран читалки).

**Слова автора:**

> Now the most important thing is do not rely on colors to transfer meaning. For example, if you have an error do not just add red to the arrow. Okay? Use a warning icon, you know, make the text stand out by making it bold or increasing the font size. Do not just rely on color because color is very elusive.

**Для Напарника:** Ошибки и подтверждения в голосе напарника: тёплая реплика плюс иконка, цвет только как вторичный сигнал.


---

## 2. «Мне читаемо» не критерий: проверяй контраст инструментом
`доступность · цвет · типографика` · [07:28](https://youtu.be/BW_PjPR825w?t=448)

**Мысль:** С возрастом способность различать цвета падает; серый на сером кажется читаемым молодому дизайнеру, но проверка контраста чаще проваливается. Критерий — чекер, а не глаз.

**Слова автора:**

> And don't forget if people have visual impairments or people are older. For example, our vision starts to go downhill by the time we reach 40. So whenever we get older, our ability to distinguish colors decreases. So we'll be having difficulties distinguishing between low contrast colors. So I have here a grey background and grey text, so it's difficult to read. Now I can read it. It's a little bit difficult for me but I can read it, but I'm 25. So remember if you are designing an interface or coding a website, if you're thinking, okay, this is a little bit difficult to read, but I can read it just fine. Then it's wrong. You should run it through a color contrast checker and check that it is the correct contrast,.

**Для Напарника:** Приглушённые тексты на фоне Напарника проверять измерением (muted-foreground 6.63:1), а не на глаз.


---

## 3. Дизайн в градациях серого: иерархия без опоры на цвет
`цвет · доступность · крафт · иерархия` · [11:09](https://youtu.be/BW_PjPR825w?t=669)

**Мысль:** Сначала строишь выделение размером и жирностью в чёрно-белом, потом добавляешь цвет как усиление; если хорошо в сером, в цвете будет лучше.

**Слова автора:**

> If you are a designer and you design a lot of mockups in Adobe Illustrator, what I suggest is try to design your mockups in grayscale. Do not add any color. Just use font size or, you know, boldness to make things stand out, and then add the color. This is what I do in web design too, in web development, like I will create a component and then I will grayscale the page and see how it stands out. And then when I add color, it will just progressively enhance it rather than make it just rely on color exactly. And I know from graphic designers that they sometimes make logos only in grayscale and they say if it looks good in grayscale, it's going to look even better in color.

**Для Напарника:** Проверять экраны Дома и Фокуса в grayscale: иерархия должна читаться без оттенков неба и акцентов.
