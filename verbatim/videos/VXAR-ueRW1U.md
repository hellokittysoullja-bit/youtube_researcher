# How a Niche Aviation App Became a Masterclass in App UI Design | App Breakdown #84

**Канал:** App Breakdown · 16 мин · субтитры: en (авто YouTube) · https://youtu.be/VXAR-ueRW1U

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Просьба о разрешении с превью самого уведомления: сначала покажи ценность
`уведомления · онбординг · доверие · микрокопирайтинг` · [03:12](https://youtu.be/VXAR-ueRW1U?t=192)

**Мысль:** Над системным запросом показан пример реального уведомления, чтобы человек увидел, что получит, и только потом принял решение.

**Слова автора:**

> And they ask for notifications in a very cool way. So, notice how up top they have a preview of a notification so that you actually get the value of what you're going to get. So, like Delta A340 loses engine power, and they show you real instant alert. So, it's a great example of showing a user, "Hey, here's the value you're going to get. Now, accept it.".

**Для Напарника:** Если Напарник будет просить разрешение на уведомления: показать превью реплики кота («Я тут, когда будешь готов») и объяснить в его голосе, что именно придёт и как редко.


---

## 2. Честное объяснение зачем нужно разрешение на трекинг повышает согласие
`доверие · этика · онбординг · микрокопирайтинг` · [05:00](https://youtu.be/VXAR-ueRW1U?t=300)

**Мысль:** Автор обычно отказывает в трекинге, но согласился, потому что просьба была поданна честно и приятно: «необязательно, но это помогает нам понимать, как мы растём».

**Слова автора:**

> On the next screen, clicking allow is optional, but it helps us know how we're growing. Okay, this is a pretty cool way to ask for tracking. I usually say no on tracking, but in this case I'm going to say yes just because they prompted in a very cool way.

**Для Напарника:** Любые просьбы к пользователю (аналитика, уведомления) формулировать с правом отказа и без манипуляций, в голосе напарника.


---

## 3. Тёмный паттерн: бесплатный пробный период только при выборе годового плана
`цены · тёмные-паттерны · этика · конверсия` · [06:09](https://youtu.be/VXAR-ueRW1U?t=369)

**Мысль:** Пробный период привязан к годовому плану: человек подписывается не думая, потому что сегодня платить не надо, и компания выигрывает или от конверсии, или от забытой отмены.

**Слова автора:**

> And you only get the free trial if you go for the yearly plan. Okay, this is an interesting dark pattern where their goal here with the free trial is really that you go into it without thinking much of it because you're not spending money right now, and then either they hopefully convert you into an actual user and you want to keep the membership or you forget to cancel it. and in both of these cases, it's way better if you pre-subscribe for the yearly than if you pre-subscribe for the weekly.

**Для Напарника:** Не применимо: этот приём манипулятивен и противоречит доверию к тёплому продукту. Если появятся цены, честный пробный период без скрытых условий и напоминание перед списанием.


---

## 4. Кнопка слегка дрожит, чтобы научить, и перестаёт, когда заметили
`анимация · онбординг · микровзаимодействия · внимание` · [08:24](https://youtu.be/VXAR-ueRW1U?t=504)

**Мысль:** Движение направляет внимание на функцию, которую человек ещё не нашёл, и прекращается после первого использования или замечания. Анимация имеет конкретную цель, а не декоративная.

**Слова автора:**

> For example, I noticed that when I went back, this button here for skip silence was shaking, teaching me that it was there. And now, it's no longer shaking.

**Для Напарника:** Принцип контингентности: движение только пока оно нужно. Если нужно подсказать новую возможность Дома или Мира, один раз подсветить и затем остановить, как в механике island-grow (один раз, при первом визите).


---

## 5. Жирный шрифт везде красив, но иерархия слабеет
`иерархия · типографика · вкус` · [09:08](https://youtu.be/VXAR-ueRW1U?t=548)

**Мысль:** Если всё выделено, ничего не выделено: чрезмерный акцент размывает иерархию, хотя чистота делает это приемлемым.

**Слова автора:**

> I love just how bold they went with the typeface everywhere. Maybe it's a bit too much, like they give a bit of too much importance to everything, and so things kind of lose the hierarchy, but it's so clean that I really love it.

**Для Напарника:** В Доме и Фокусе ограничить число жирных/крупных элементов до одного главного на экран; остальное спокойнее, чтобы ключевое действие читалось.


---

## 6. Плотность данных растёт при скролле: сверху главное и просторно, ниже плотные строки
`иерархия · сетка · мобильный · навигация` · [11:35](https://youtu.be/VXAR-ueRW1U?t=695)

**Мысль:** Посещённые страницы становятся приглушённо-серыми, чтобы было видно, где был; на длинной странице верх с малой плотностью для важного, дальше плотность растёт.

**Слова автора:**

> I love this loading of the timeline at the bottom. And notice how the pages that I've already visited turn into this more muted gray. It's a nice touch for you to know where you've been. And if we keep scrolling, it seems like the data density increases. And so I'm assuming we're going to get to a point where it's just rows. So if we keep scrolling, now we have planes. Yep, and now we have just rows. So it's a good rule of thumb that usually whenever you have a big scroll view, you start with less data density up top so the things that really matter and that you want to give more space for and then data density increases as the user scrolls on the page.

**Для Напарника:** Лента реплик в чате: свежее и важное крупно, старые реплики тускнеют (depth-fade уже есть). Подтверждает направление ChatBubble.


---

## 7. Единая оболочка (sheet) для всего контента: быстро осваивается
`навигация · дизайн-система · онбординг · иерархия` · [13:04](https://youtu.be/VXAR-ueRW1U?t=784)

**Мысль:** Когда любое содержимое открывается в одной и той же форме, пользователь всегда знает, где он, и быстро осваивает интерфейс.

**Слова автора:**

> So it seems like the entirety of the app is a shell into these sheets, which is cool because you always know where you are and you become familiar with the interface very fast. I've been recording this just for a few minutes and I feel like I can navigate the app very easily.

**Для Напарника:** Три экрана /app, /session, /world делят AppBackdrop и AppNav; держать единообразные паттерны открытия деталей, чтобы не плодить новые формы.
