# Perfect Typography Scale for UI Design (Exact Blueprint) | Figma Tutorial

**Канал:** Mizko · 10 мин · субтитры: en (авто YouTube) · https://youtu.be/hwjiExdMiNY

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Отдельные стили для лейблов и абзацев: у лейбла маленький line-height, у абзаца большой
`типографика · дизайн-система · крафт` · [02:26](https://youtu.be/hwjiExdMiNY?t=146)

**Мысль:** Лейбл это слово-два без нескольких слоёв, ему тесный интерлиньяж не мешает, а абзацу нужен больший, иначе текст сжимается.

**Слова автора:**

> They generally will set up a type Style for paragraphs and we tend to use paragraphs for all sorts of text anything that's text we generally have paragraph Styles but the issue is that if I go over to a real world project that I just wrapped up you can see here we have a dashboard of videos that have been uploaded for this company called screen app which is sort of your own dashboard and then we also have another screen once you click onto a video we have a bit of a transcription of the video and the user can ask questions into the AI and it will pull cool insights out as you can see over here the summary which generally has a bunch of paragraphs of text this is meant to be a paragraph style because a paragraph is really just a combination of multiple sentences put together so if you don't have a large enough line height then your text becomes very tight so for example let me just change this over to the label style you can see that it actually becomes SS very tight and it doesn't look that good so you want to expand that a little bit so that's why I have different styles for paragraph text and I also have different styles for labels because as you can see over here this is a label where it talks about for showcases who was the user that uploaded this video and this is also a label to Showcase how long the video is this is also a label to Showcase how many people were in this video as well so as you can see if I directly select this text we are actually using labels so really to summarize the difference between a label and a paragraph is that a label is just a couple of words or even just one word and it generally doesn't need a large line height because we don't have multiple layers of labels on top of each other however with a paragraph because there's going to be multiple lines of text we need larger line height.

**Для Напарника:** В дизайн-системе Напарника завести разные типографические токены для коротких подписей и для реплик в чате.


---

## 2. Шкала с шагом 2px: лейблы 10-12-14-16, абзацы 12-14-16-18, заголовки 18-52
`типографика · дизайн-система · сетка` · [04:24](https://youtu.be/hwjiExdMiNY?t=264)

**Мысль:** Простое увеличение на два пикселя даёт согласованную шкалу, а интерлиньяж растёт на 2–4 пикселя.

**Слова автора:**

> The secret to my scale for real world UI design projects is just incrementing them by two pixels label for extra small is 10 pixels label for a small is 12 14 and 16 and you can see that the line Heights increments by two as well or sometimes it's 2 to four depending on what is going to work perfectly this is the approach that I've used for all my projects and as you can see with these designs the type works perfectly fine it looks great the spacing is correct even on this design where we have paragraphs you can see that the line height is a little bit different if I was to show you the actual tablet design you can see that the types perfect the type over here is also perfect and if we go to mobile you can see that it all looks perfectly balanced as well and that is the benefit of using ship faster UI or having this Inc m al approach where it's just two pixels it allows your topography to be very consistent.

**Для Напарника:** Принять инкрементальную шкалу размеров с шагом 2px и закрепить в токенах, не изобретая промежуточных.


---

## 3. Реальный проект: база 16px, большинство текстов это лейблы; абзацы только для больших кусков
`типографика · иерархия · крафт` · [07:11](https://youtu.be/hwjiExdMiNY?t=431)

**Мысль:** Метаданные делаются мелкими (12px), заголовки и лейблы дают иерархию, а абзацный стиль нужен только для длинного текста.

**Слова автора:**

> There was no magic pill that I took it really is using 16 pixels as a base and anything from there I would either increase it by 2 pixels or decrease it by two or four pixels so as you can see most of the labels which are generally should be labels so one words are generally labels not paragraphs you should only be using paragraph styles for large chunks of text it's generally going to be a medium because I personally like using 16 pixels as a base font because I generally like to use 16 pixels as a baseline for my projects because I think 16 pixels is quite easy to read you can see that we have a large label which is semi bold but then the meta data for this card which I wanted to create more visual hierarchy we are using the label small medium so generally as you can see small is going to be 12 pixels and anything else will be around 16 to 14 pixels now let's take a look at this screen over here we've got a model for actually sharing or inviting people to this collaboration folder once again we have a heading which is H4 and then we have paragraph which is medium that's 16 pixels then we have a label that's 16 pixels because it's medium and then everything else is also Medium as well you don't really need crazy type scales for your projects.

**Для Напарника:** На Фокусе почти всё это лейблы и заголовок шага; абзацный стиль оставить для реплик напарника.
