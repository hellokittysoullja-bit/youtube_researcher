# What EXCEPTIONAL Onboarding Actually Does - Building Successful Apps

**Канал:** Philipp Lackner · 16 мин · субтитры: en (авто YouTube) · https://youtu.be/kouFJkcLKAQ

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Холодный пользователь: у него нулевой кредит терпения, длинный онбординг = потеря
`онбординг · активация · удержание · мотивация` · [00:55](https://youtu.be/kouFJkcLKAQ?t=55)

**Мысль:** Новый пользователь не знает, полезно ли приложение, поэтому терпимость к трате его времени минимальна: регистрация без необходимости, десять разрешений, длинные туториалы заставляют уйти. Потеря происходит не из-за функций, а из-за онбординга.

**Слова автора:**

> And the moment a user opens your app, they are completely cold at this point. They've opted in downloading your app kind of, but they still have zero ideas whether this app is really beneficial for them and their life. So, fresh users who don't have the context about how useful your app could be don't really have a very high tolerance against you or your app wasting their time. And onboarding very often is an absolute waste of time for from the user's perspective. If the user simply has too much too much time before even being able to get something from the app. So, they maybe have to sign up even though you they technically wouldn't need that account in order to use your app in some way. They have to accept 10 different permission prompts. They have to click through a long tutorials where some kind of speech bubbles keep on appearing everywhere. Then, what they will do is they will quit again and that is the moment you've lost the user, not because the functionality of your app is bad, but because your onboarding is trash.

**Для Напарника:** Первый заход в Напарника: никакой регистрации и разрешений до первой ценности. Человек с СДВГ уходит ещё быстрее; цель — первый шаг сессии за секунды.


---

## 2. Не требовать регистрацию и разрешения, пока человек ничего не получил
`онбординг · доверие · активация · этика` · [04:23](https://youtu.be/kouFJkcLKAQ?t=263)

**Мысль:** Пользователь уже заплатил местом на устройстве; если следующим шагом вы снова что-то берёте (данные, время), терпение заканчивается. Регистрацию показывать внутри приложения, а не как обязательное первое действие, если без неё можно пользоваться.

**Слова автора:**

> First of all, if your app has the feature of users signing up, only require that if it's really, really, really needed for the core behavior of your app. If having an account is a benefit for the user, but it's optional, then do not prompt the user with an immediate sign-up action. Obviously, apps like Instagram also require a sign-up because without having an account, you can't use anything of the app. But, if you have, I don't know, a file editor app, the signing up just allows also synchronize the different files you've edited, but without having that account, you can at least edit them locally. Then, only present the sign-up option inside the app already, but not as a primary first mandatory action. This really lets users use your app instantly without actually have to click around first, find out what this all is even about, without having to give you their data, without having to go back to the email, click a verification link. It's super annoying. You know this yourself. But, otherwise, if you instantly prompt them with a sign-up with and permission prompts as I mentioned, you are already asking the user something at a point where they don't owe you anything of having your app occupy storage on their device. So, now the next thing is they want to have something from you. But, if you again in the next step take something from them, like their data, their time, then a lot of users' patience will end there.

**Для Напарника:** Данные уже в localStorage без аккаунта (lib/memory.ts), это соответствует принципу. Имя, чек-ин и уведомления просить позже, по одному вопросу за визит.


---

## 3. Не спрашивать необязательные данные, если они не улучшают опыт
`онбординг · микрокопирайтинг · отступы · активация` · [05:38](https://youtu.be/kouFJkcLKAQ?t=338)

**Мысль:** Каждый лишний вопрос — лишний шаг. Спрашивать имя в счётчике калорий не нужно; необязательное можно отложить на потом. Исключение: данные, которые заметно улучшают результат (несколько фото в дейтинге).

**Слова автора:**

> Second general rule here for onboarding don't ask for optional data unless that optional data really improves the app experience for the user. So, we can actually take this example for a calorie counter app. Do we really need the user to provide their first and last name? No. Maybe our app used this data in some way, but if this is optional, we can have the user optionally provide this at a later point. This is just an extra step that is really not necessary here. And also having the user provide their first and last name, I would not know why a calorie counter app needs that in order to improve my app experience in order to help me better track my calories. Another example where optional data could be shown during an onboarding flow is again our dating app. Let's say your profile can consist of up to 10 profile pictures. Now, it may be mandatory to just upload one profile picture, but having multiple profile pictures uploaded will on average probably improve the user's app experience because you will likely get more matches if you upload more photos. So, in that case, during the onboarding flow, I would present the user with the different options to at least make one photo mandatory, but also present them the option to select up to 10 photos immediately. So, that's a bit of a tricky scenario, but always think about does this information that I'm getting here really improve the app experience for the user?

**Для Напарника:** Имя спрашивать только если оно реально используется в репликах кота; иначе не спрашивать. Для каждого вопроса проверять: улучшает ли ответ мой следующий экран?


---

## 4. Порог качества онбординга: >50% не делают ключевое действие за 24 часа — плохо
`метрики · активация · онбординг · исследования` · [06:53](https://youtu.be/kouFJkcLKAQ?t=413)

**Мысль:** Если больше половины пользователей не совершают ключевое действие приложения за 24 часа после регистрации, онбординг слабый. Ключевое действие зависит от продукта; нужно ещё смотреть, на каком экране люди отваливаются.

**Слова автора:**

> And a general tip here, if you're really also serious and you launch your apps, and you have real users using that, then you have to track this. You need analytics in order to find out how good or how bad your onboarding flow is. If more than 50% of your users do not trigger the key action of your app within 24 hours after sign up, then your onboarding is likely not very good. So, the key action of course depends on your app. In a dating app, this could be actually having your first swipe or getting your first match. In a file manager app, it could be uploading your first file. And the time between sign up and getting to that key action, if that is more than 24 hours for more than 50% of your users, then really work on that. Track that data, and also of course track where exactly you are losing your users. So, which screen they really drop off, where the sessions end. Only with that data you can really improve your onboarding flow.

**Для Напарника:** Ключевое действие Напарника — первая завершённая сессия Фокуса. Метрика: доля новых пользователей, дошедших до неё за 24 часа, и экран, на котором обрыв.


---

## 5. Заголовки велком-экранов: выгоду для человека, а не список функций
`онбординг · тексты · микрокопирайтинг · лендинг` · [07:59](https://youtu.be/kouFJkcLKAQ?t=479)

**Мысль:** Разработчики перечисляют функции («отслеживай привычки, статистика, уведомления»), а нужно говорить, что человек получит («больше нет оправданий, ты видишь, как растёт серия»). Ценность для жизни пользователя, а не возможности продукта.

**Слова автора:**

> And the most common mistake people make here is how they phrase these headlines. Especially developers who don't have, you know, a big marketing background like to just list their apps features here. So, they really just explain what users can do with your app. They explain which features it consists of. Hey, you can track your habits. You can create so many habits. It's It's incredible. Custom schedules. Oh my god. Powerful statistics. View detailed charts. Stay notified. We can actually send you notifications. But, this communicates the wrong thing. What you always want, if you have such welcome screens, is to communicate how your app benefits the user and not what it can do. So, if we take a look at some improved variants here, then you can see what I mean. It's the exact same onboarding screens, but with different texts. You just lost your last excuse. Now, with this app, you have no more excuses of actually sticking to your habit, of finally getting to the gym regularly, because you can't use "Oh, I forget about it" as an excuse anymore, because our app will take care of it. You build real momentum. Oh, you We actually always show you your streaks. You see it grow by day. You never lose motivation again. You never forget about what matters to you anymore. If you say, "It matters to me that I regularly go to the gym," then our app will make sure that you don't forget about that anymore, that you will stick to what matters to you. So, do you know what I mean? You should really communicate how your app benefits the user. What value does it bring to their life, rather than just listing features.

**Для Напарника:** Тексты онбординга и лендинга формулировать как результат для человека («начать станет проще», «остров растёт от твоих шагов»), а не «таймер, ИИ-дробление, статистика».


---

## 6. Всегда давать пропуск: основатель любит продукт сильнее, чем пользователь
`онбординг · доступность · активация` · [09:28](https://youtu.be/kouFJkcLKAQ?t=568)

**Мысль:** Основателю интересно показывать все фичи, пользователю обычно важно одно, и он хочет попробовать сам. Все пропускали туториалы, значит пропустят и ваши.

**Слова автора:**

> Another thing you can notice is if you just have such read-only screens, offer an option to skip. If users don't care, then you should give them the option to not care. If you're maybe a founder of your app, you care way more about your own app than your users do. This is completely normal. And you maybe find it super cool to show them all these different features and what cool things your app can do. When for the user, maybe only one thing actually matters. And even that thing they just want to try out themselves. You've probably also skipped tutorials in the past. And so will your users. So, give them the option to skip if something is skippable.

**Для Напарника:** Любой вводный экран Напарника должен пропускаться в одно касание, без штрафа. Пропуск не должен вести к чувству вины.


---

## 7. Сбор данных: убрать сложные решения, добавить «решу позже», объяснять зачем
`онбординг · активация · СДВГ · иерархия` · [09:59](https://youtu.be/kouFJkcLKAQ?t=599)

**Мысль:** Лишние поля убирать; к цели добавить «не знаю / решу потом»; пояснить, зачем нужны личные данные; сложный выбор (разбивка макросов) не навязывать новичку, а показать расчёт с пометкой, что это можно изменить в настройках.

**Слова автора:**

> Let's now take a closer look at these information gathering onboarding flows. I've already mentioned optional data should be dropped. So, here in this calorie counter app, we definitely don't need the first and last name. This screen I would completely drop from this whole onboarding flow. If we take a look at the second screen, what's your goal? This is probably something that is needed here to some degree because the goal dictates about the initial calorie count that we want to present the user here. And depending on whether they want to lose weight, build muscle, of course the amount of calories they need to track changes. In this case, I would say the different goals that are presented here are a little bit too little. Maybe the user says, "Hey, I actually don't yet know what my goal is. Just let me try the app and see if I can actually get along with it. If I can actually if I actually like the way of tracking my meals. And then I can decide about what I actually want with all this." So, here I would say it would be reasonable to also present them an I don't know or decide later option. What's your size and weight? That is definitely needed information also calculate the amount of calories per day. So, of course keep it simple. Maybe I would also add a note here of why you're actually getting that data because it's of course quite personal data. And if you take a look at the last screen here where they can then decide about how they split their macros, this should be left away. This is something where you're already prompting the user with something they may have no idea at all about. Especially if you don't have a lot of knowledge about nutrients, about macros. And maybe on this screen you even find out that macros are about protein, carbs, and fats. And then you suddenly have to make a decision here as a user how you split these, which really much dictates your success. Because if you get this wrong, then I don't know, maybe you lose muscle if you set the protein amount to just 10%. So, such difficult decisions should be taken from the user and rather give the power users or those who are experienced with that the option to customize that in the settings. So, I would also completely skip that screen or rather give the user some kind of breakdown of what your app has calculated for them and with the note, "Hey, you can actually change this in settings if you say this is not what you agree with, but here this is something you can instantly get started with.".

**Для Напарника:** Выбор длительности сессии: дефолт 25 мин с меткой «рекомендуем» (Default Effect) вместо требования решить. Везде, где есть выбор, предлагать вариант «пока не знаю» и разумное значение по умолчанию.


---

## 8. Сохранять состояние онбординга после каждого шага
`онбординг · удержание · доверие · процесс` · [11:58](https://youtu.be/kouFJkcLKAQ?t=718)

**Мысль:** Если приложение убито системой или человек вышел, потерянные данные заставляют проходить всё заново, и он бросает. Данные каждого шага записывать в локальные настройки и возвращать к месту остановки.

**Слова автора:**

> And a tip for these onboarding flows that collect data, always save the current onboarding state in local preferences. Especially if you have some longer forms and the user maybe has to fill out some text fields, has to really give you your data, it is super frustrating if they maybe quit the app, the app is killed by the system because of memory pressure, pros that happens and all that data is lost or they simply quit the app, come back later, and they have to go through all that again. This makes them quit. So, it's simple, really just with every single step add a little bit of data, so exactly the data that was filled out in that in that step to your local preferences, and then just read the entire onboarding state from local preferences so you can directly lead the user to the next onboarding step where they've left at.

**Для Напарника:** Недозаполненные формы имени, чек-ина и очередь шагов хранить в localStorage (saveStepQueue уже так делает); при возврате продолжать с того же места без укоров.


---

## 9. Финал онбординга ведёт к ключевому действию, но оставляет вторичный выход
`онбординг · активация · иерархия · запуск-задачи` · [12:41](https://youtu.be/kouFJkcLKAQ?t=761)

**Мысль:** Последний экран показывает рекомендацию и главный призыв к ключевому действию («запиши первый приём пищи»), а рядом даёт необязательную кнопку «продолжить», чтобы человек мог просто осмотреться.

**Слова автора:**

> Then let's take a look at a better example here again from a UX perspective. The designs are really not great. So, here for what's your goal, I added a decide later option. In that case, we would just maybe assume to that they want to keep their weight. We say, "Okay, your size and weight." As I mentioned, that is mandatory data. And then here this is just a screen where we present what we recommend to the user, this amount of calories based on your goal. This is a balanced way to start with. You can find tune these percentages anytime in the settings maybe. And we want to present them a call to action to finally get them to the key action, to whatever you want them to get to that really starts showing the users the advantages of having this app. In this case, hey, track your first meal now. But this case, I would still also provide an optional secondary continue button. The user is currently somewhere where they don't have any context on what kind of meal they track, they still should be led to the overview screen or so they can start playing around with it.

**Для Напарника:** Завершение онбординга: главная кнопка «Начать первый фокус», второстепенная — «Просто осмотреться» (Дом). Не заставлять в первую секунду.


---

## 10. Туториал по требованию на ключевых 20% функций, а не показ всего на старте
`онбординг · активация · удержание · игровой-дизайн` · [13:39](https://youtu.be/kouFJkcLKAQ?t=819)

**Мысль:** Люди хотят сразу начать использовать приложение; жёсткие туториалы раздражают. Лучше показывать краткую подсказку в момент, когда человек впервые идёт к функции, и только для 20% функций, которыми пользуются 80%, если они неочевидны. Подсказки привязаны к функции, а не к одному флагу «видел».

**Слова автора:**

> If you've personally ever skipped a tutorial, whatever form that tutorial is, be it a tutorial for game, be it a tutorial inside an app that explains all its features, if you've ever skipped that, then you know why. And you can be sure that your users will also skip it. The moment someone installs an app, they want to start using that app as soon as possible, rather than being forced into some kind of rigid onboarding flow they have to first click through. This is something that really frustrates a large amount of users. Still, you may want to instruct the user a little bit on how to work with given features, especially if you have some complex features. So this is definitely a type of onboarding that you can stick to, but the much better approach here is to make it on demand. Do not, when the user just goes to the first screen of your app, do not show them everything of your app, everything it can do. Show multiple pop-ups that the user just clicks away. But when the user is actually going to a certain feature, initiating certain action, like tracking meal, then you could say, "Okay, now just for that feature, give them a brief introduction. Hey, here you can enter the title, here is the description, this is optional, you don't need this, and here is in the end whatever food you've tracked." Just as an example. So just on demand, when the user is about to do something, so when they already say, "Hey, I want to now finally use the app for what it is intended for," then you can show them, "Hey, this is how it works." I also wouldn't blindly do this for every single feature, but I would stick to the Pareto principle here. So that means for the 20% of your app's features that are used by 80% of your app's users, I would add such an onboarding flow if using that feature is not obvious or if there are some maybe uncommon tips you can give the user that may not be obvious. So, such good onboarding flows with tutorial like onboarding that happens across sessions and not just in the first session. So, it's not like you show them a tutorial and then after having clicked through that, you flip an internal flag in your settings and they will never see that again, but you actually have it per feature.

**Для Напарника:** Мини-подсказка кота при первом входе на Мир или первом разделении задачи на шаги, а не тур при старте. Без всплывающих окон/тостов: подсказка как реплика в чате или инлайн.
