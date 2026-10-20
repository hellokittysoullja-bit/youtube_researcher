# 10 UX Patterns Every AI Chat Interface Needs

**Канал:** Kristian · 10 мин · субтитры: en (авто YouTube) · https://youtu.be/bppkpufBJsI

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Прокрутка чата должна работать, где бы ни был курсор
`чат · мобильный · доступность` · [00:11](https://youtu.be/bppkpufBJsI?t=11)

**Мысль:** Overflow auto ставить на обёртку беседы, а не на содержимое, чтобы страница прокручивалась целиком.

**Слова автора:**

> So the first one is scrolling. I have a task for you. Try to find a difference between the two. So here's the first one. Here's the second one. Do you see the difference? And the difference is that in a better example, I have to put my cursor inside of this chat conversation container for it to scroll, right? the way you should do it and the way it should work is that no matter where your cursor is, you should be able to scroll the whole conversation. So the way to do it is to put the overflow auto to the conversation wrapper and not the conversation content. And this way your content now will scroll as a page and not only this small content chunk of your page.

**Для Напарника:** CompanionChat: убедиться, что скролл ленты не требует точного попадания в контейнер.


---

## 2. Прилипание к низу при стриминге, с возможностью прервать слежение и вернуться
`чат · ИИ · крафт` · [00:46](https://youtu.be/bppkpufBJsI?t=46)

**Мысль:** Самодельная реализация почти всегда неверна; нужны липкость к низу, прокрутка к последнему сообщению при обновлении страницы.

**Слова автора:**

> Number two is to use some kind of library that helps you implement scrolling logic when your AI streams the response. So here in this example if I send this you will see that my cursor will now follow the stream. But at any time I can easily like break this following but then get back to the following of the stream. And I can do it any time and it sticks to the bottom of the stream and continues with the stream. And it's really important because the way you implement it, if you will try to implement it yourself, you will probably get it wrong. So it handles a lot of stuff like the stream stickiness. It also handles that when you first refresh the page, it like scrolls down to the last message, which is also helpful. And you don't need to worry about implementing it. You can just use a library like use stick to bottom. You can just implement this component stick to bottom. stick to bottom content and it will just automatically work.

**Для Напарника:** Лента реплик кота: при стриме ответа держаться низа, но не отнимать управление у пальца.


---

## 3. Автофокус в поле ввода чата
`чат · мобильный · запуск-задачи` · [03:31](https://youtu.be/bppkpufBJsI?t=211)

**Мысль:** В чате человек сразу печатает, поэтому автофокус экономит клик.

**Слова автора:**

> Next one, please just add autofocus to your input. What I mean by that is that when you go to the chat interface, usually you would just start typing and if you don't have autofocus to your input, users have to click to the input to start typing. And it's so easy to implement and it doesn't matter where you are. If you are in a new conversation, if you are in a like ongoing conversation, it should be always out of focus. And all you need to do is to add auto out of focus to your input.

**Для Напарника:** Не применимо к Дому: по CLAUDE.md автофокус на многоцелевом экране поднимает клавиатуру раньше решения; допустим только на Фокусе с одной целью.


---

## 4. Сохранять черновик ввода между беседами (и настройки, с оговоркой)
`чат · СДВГ · запуск-задачи` · [04:05](https://youtu.be/bppkpufBJsI?t=245)

**Мысль:** Случайно начатый и потерянный текст раздражает; значение ввода критично, настройки по беседе опциональны.

**Слова автора:**

> Next is to save the value of the input. So let's say I accidentally start typing in this conversation and I want to go into the new chat. If I go here, I save the input value. If I go to chat GPT, chat GPD, if I do the same thing, you will see here that they are not doing it. And there were so many times where I was so pissed off that they don't have that. But I guess they are saving it for the conversation. And if I go to the conversation, yeah, so they're they're storing it but in a different way. But still, this thing pissed me off so many times. So save the value of the input across the conversation. The next one is really tightly related to the previous one is to save the not only the value but also the settings. So let's say I here I will choose the search and the model. Let's say I'll do it in this conversation. I'll choose the model and the search and I can go back and it saves. It didn't save but it did maybe in my example there are some bugs. No, it works. So I choose the Gemini 3 Pro. I go back to the conversation and it saves the not only the value but also the settings. And this one might be a little bit on the edge because if what if your conversation has its own settings and you don't want to interfere with those settings in this specific conversation. that's a good point. So you should consider that and that's maybe even the optional one but the input value is crucial.

**Для Напарника:** Сохранять недописанный шаг на Фокусе и текст в чате при уходе с экрана.


---

## 5. Состояние загрузки до первого текста: статус «streaming» ещё не значит, что есть контент
`чат · ИИ · анимация · микрокопирайтинг` · [05:49](https://youtu.be/bppkpufBJsI?t=349)

**Мысль:** Между отправкой и первым токеном бывает пустая пауза; нужно показывать загрузку, пока нет текста или рассуждений.

**Слова автора:**

> Next is how you handle loading state before AI starts streaming. So in the SDK in their use chat hook they have statuses and based on that statuses you can see that they have submitted streaming ready and error. You might think that based on the submitted when a user submits we can start showing the loading state and once it start streaming starts streaming we can remove this loading state because now it's in the streaming status which means that AI started streaming right but that's not really how it works. The reason for that is let's say I'll I will send this how to improve sleep request to Kimik K2 and you will notice that we're only rendering the loading state on the submitted status what you will notice here. So it responded really fast. Not the best example. so let's try another one. So here I submitted and I don't see the for some time I didn't see the loading state. As I understand how it works, status changes to streaming when the client receives streaming headers but not the content. So that's why you might see this weird state where it's no longer when it's not yet streaming but it's no longer submitted. So this is the state of streaming but we are not seeing any text yet. So I found a way how to do it and instead of looking at the status or only the status we can look also at the messages and the last message of the system. So based on the status if it's submitted then we're also showing the loading state. If it's streaming, we're also finding the last message of the assistant and looking for text or reasoning. And if we don't have text or reasoning, that means that we have to show, we still have to show the loading state because we don't have any content and it's in streaming state or status. And this way we can be sure that we don't have this weird press streaming state.

**Для Напарника:** Пока кот «думает», показывать его индикатор в его характере (не спиннер), без пустой паузы.
