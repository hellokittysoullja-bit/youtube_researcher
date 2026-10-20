# Onboarding User Flow: Bike Rental Case Study - Vitaly Friedman

**Канал:** UX Salon · 15 мин · субтитры: en (авто YouTube) · https://youtu.be/IeZGw2fPVcI

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Цель человека проста (сесть и поехать), а онбординг заставляет пройти 20-25 экранов
`онбординг · активация · мотивация` · [00:00](https://youtu.be/IeZGw2fPVcI?t=0)

**Мысль:** Сплэш, регистрация, 17 экранов условий, геолокация, туториал и карта: человек перед велосипедом просто хочет уехать, а получает длинную цепочку барьеров.

**Слова автора:**

> Right now a very typical example for that is where it's really going to extremes is when you are about to get on a bike to go from one place to another i mean you might have seen thousands of those applications right like hello bike and what is it called i always forget how they call turn and others where you are in front of a bike you want to get on a bike to get from where you are to where you want to be you don't have an account yet you don't have anything but you are in front of the bike you are interested in just taking it on the right your goal is very simple you want to get to that point quickly right now what is the common onboarding experience or navigation experience really for getting from i'm here in front of the bike too i'm here leaving the bike because i'm done like what is the experience most of the time now this is what the experience is often most of the time you get a splash screen first right because you have to download the app you came to the bike there is a qr code or the url that you need to go to and then you download there that's something that you probably should be expecting right so you do that you download the app and you get a welcome splash screen with a sign up button and login button okay well then that means you need to sign up so you go and sign up and that means a couple of input fields then you get the terms and conditions which is 17 screens which of course you will read and mark as i agree then you need to give the app access to your location because it needs okay you know it needs access to a location to know where you are and where you're going to navigate you or maybe to just you know track where the bike is at the moment right then after that you get a tutorial and it's not just one tutorial it's two or three or four or seven screens explaining how it actually works and then you get to the map right and eventually of course you will probably need to plug in your credit card data and give access to other things as well sounds familiar more or less right maybe right and this is all over right and this is such a painful experience now if you think about this you have to go through sometimes 20 25 screens to actually start writing to start pedaling that's not a great ux at all.

**Для Напарника:** Первый запуск Напарника: цель человека одна (начать), пусть первая сессия идёт максимум в два-три действия.


---

## 2. Люди должны чувствовать прогресс; экраны условий этого не дают
`онбординг · мотивация · иерархия` · [03:06](https://youtu.be/IeZGw2fPVcI?t=186)

**Мысль:** Большинство шагов не создают ощущения продвижения и не сообщают, что человек движется к цели.

**Слова автора:**

> That's not a really great experience because we need to make sure that our customers always feel like they're making progress and most of the steps that we saw right now they're not helping there at all they're not telling people that they're making progress when you're looking at the 17 terms and condition screens that they have to go through.

**Для Напарника:** Если онбординг многошаговый, показывать реальный прогресс и каждый шаг делать видимо полезным.


---

## 3. Lime: не спрашивать имя и email сразу; начать с телефона и автоподстановки кода
`онбординг · активация · доверие` · [03:28](https://youtu.be/IeZGw2fPVcI?t=208)

**Мысль:** Спрашивают только то, что нужно сейчас: телефон, потом код из SMS подставляется сам. Имя и почта потребуются позже, например для чека.

**Слова автора:**

> So how can we make it better well there are a couple of really nice examples of how we can make it better like for example when we look into something like let me just jump to it like lime is a little bit different it never asks you for your name because it's not so important i mean it will be important eventually right when you will need to want your receipt maybe right but it might not be necessary at the first place at all email is it important to have email maybe it's more important to have a phone number so that's what they're starting with start writing now and you get the phone number that's being asked from or you can continue with facebook and then they would get your email right and then there is a next button and it says we'll send a text to verify your phone which is okay right so you type in your number you get a notification it automatically picks it up from that you know sms that you're receiving.

**Для Напарника:** Просить имя и прочее не сразу, а когда это даёт пользу; согласуется с принципом «один вопрос за визит».


---

## 4. Объяснить зачем разрешение до системного запроса; без туториала; подсказка на самом действии
`онбординг · доверие · уведомления` · [04:23](https://youtu.be/IeZGw2fPVcI?t=263)

**Мысль:** Перед системным окном геолокации и камеры показывают, зачем это нужно; нет туториала, потому что люди умеют ехать; фонарик и ввод номера вручную как запасной путь; оплата через Apple/Android Pay.

**Слова автора:**

> And then it explains to you before just showing that prompt it prepares you for it so it tells you oh please enable location services it will use it to show nearby scooters and bikes on the map right and you click on enable location services preemptively and then that thing shows up where you can actually allow to use the location so it's always explained why you actually need it right and then you have the same for notification notifications prompt right and then you have a map and then you have the camera access prompt again explaining why they need it right there is no tutorial explaining how this works because people know how to pedal instead you know maybe just enable camera access because lime will use a camera to scan qr code to start your ride and look at how helpful that is have a flashlight in here so it turns on flashlight if it's dark right that's very nice and if you don't want to you can just paste in if you don't want to scan a qr code you can just plug in the type in the number and then it gives you access would you like to access a camera right because again line will use the camera to scan qr we actually saw it in the previous slide right but actually when you click on this button you don't see this as two screens it's kind of a part of the same step towards the end right and then you have to verify payment when it happens in apple pay or android pay and that's it you can start writing you confirm and you go that's it.

**Для Напарника:** Перед запросом уведомлений или звука объяснять причину в голосе кота; никаких туториалов, а подсказка в момент действия.


---

## 5. Центр клиента, а не продукта: что минимально нужно, чтобы человек начал
`онбординг · мотивация · активация` · [05:50](https://youtu.be/IeZGw2fPVcI?t=350)

**Мысль:** Онбординг не обязан содержать туториалы; нужно найти минимальный объём информации, без которого нельзя начать.

**Слова автора:**

> Right it's still quite a lot because they need to get like terms and conditions and to get the permissions and so on but i would argue that because at this point this is very me centric not like product center it's kind of it's about the customer okay phone number location services permissions go that's way better right and this is the same problem that all of them are solving so maybe onboarding doesn't have to include tutorials and maybe we need to really look into what is the minimal piece of information that we need but in order to somebody to actually start rolling or stop pedaling.

**Для Напарника:** Определить минимум для первой сессии (имя не нужно, длительность по умолчанию 25 мин).


---

## 6. Малые победы вместо функций: люди хотят удобство, скорость и приватность
`онбординг · активация · метрики` · [06:47](https://youtu.be/IeZGw2fPVcI?t=407)

**Мысль:** Сегодня большинству не важны новые функции; ценятся удобство, скорость и приватность, а гонка за функциями приводит к разрастанию.

**Слова автора:**

> But in general when it comes to onboarding we want to identify key data input and the minimal number amount of information that we need right and focus on it first and drive towards small wins not features frankly maybe just me and i know that many companies have a very different mindset but frankly i think at this point as of today most people don't even care that much about features so if we try to attract somebody saying hey we have more new features we have more new cool things i'm not sure if this is always going to be the winner because people want convenience and speed like and more importantly as we've seen over the last couple of years privacy focus on privacy so if we can provide that maybe we don't need to invest that much money into making things we're adding more and more features and this which would of course end up in a feature creep eventually.

**Для Напарника:** Не наращивать функции Напарника; полировать быстрый старт и приватность (локальное хранение).


---

## 7. Nordstrom: свобода сотрудникам потратить $100 на счастье клиента даёт больше, чем любая функция
`мотивация · доверие · дизайн-система` · [07:44](https://youtu.be/IeZGw2fPVcI?t=464)

**Мысль:** Одна история с такси для пожилой женщины разошлась по сети и дала больше маркетинга, чем реклама. Дизайн и забота влияют сильнее, чем функции.

**Слова автора:**

> There is this really famous quite well known notion of when we think about design is usually much more impactful than some features can be right this is why companies like nordstrom for example invested so much into delight and i'm not you know i know delight is a very fancy word but the point was really they were trying to do a lot of things like destiny is all the same story they were trying to do many things to get more customers and bring more features and more characters and speed up the delivery and all the things and one thing that was incredibly successful and way more successful than any feature that they brought up in the last decade or so was to give a voucher of hundred dollars to every employee and tell the employees that they can spend this money like 100 per week i think not a day per week they can spend the money in any way they like in order to make the customer happy right that was the only goal right they would not invest in anything else they just keep the money but this money has to be spent on customers it cannot be spent on something else so you ended up with a lot of stories like there was a an older woman coming in and she had a lot of backs around her and she was buying something at nordstrom which is just a big retailer in the us and so she was buying all the things that she was carrying this bag and so on and so the employee the cashier at the register said oh maybe we can just order a cab for you and she was like yes please that would be very convenient and they spend this money like 30 bucks or so on that tab receipt cab receipt to drive this old lady older lady to home that's it so she told her daughter and her daughter told her friends and all of a sudden it has become a huge story on twitter right and this brought notes from so much positive marketing right you would never be able to reach that with instagram ads or facebook ads or google ads right and that's just by giving like a little discount a voucher to people who are working there that's it to spend on customers that was quite significant and that has nothing to do with features so i think that if we can bring our interfaces in the same spot more or less even if you're stalling and you don't deliver every feature like every year right this will give you incredible results.

**Для Напарника:** Редкие тёплые сюрпризы кота (находка, неожиданная реплика) работают как такие истории; награда заслуженная и контингентная.


---

## 8. Disney: «где можно тронуть сердца» — исследование привело к браслету Magic Band
`игровой-дизайн · исследования · мотивация` · [11:06](https://youtu.be/IeZGw2fPVcI?t=666)

**Мысль:** Команда начала с вопроса, где затронуть сердца, провела исследование с детьми и за четыре года пришла к браслету, дающему детям ощущение суперсилы.

**Слова автора:**

> And the story went like this they essentially thought let's see about where we can touch people's hearts that was kind of one of the things that they had in the agenda how can we touch people's hearts and they did research and this is why i'm saying that research is so important they did research they talk to people they talk to children because of course they don't have just you know cartoons they also have parks right entertainment parks which people can go to right and so they've invented over the course of four years the thing that they call the magic band and the magic band essentially is a band that you receive when you check in right and it has all on it's just you know it's just it has a couple of what's called the an nfc chip on it or nfc technology in place and you know whenever you want to buy something you pay with a band whenever you walk around you know you can activate certain parts of the journey with a band right so it kind of gives this superhero feeling to children coming into those parks.

**Для Напарника:** Спрашивать не «какую функцию добавить», а «где тронуть» человека с СДВГ; идея для редкой находки на острове.


---

## 9. Персональный сюрприз и отсутствие жёсткого маршрута делают парк особым
`награды · дофамин · игровой-дизайн · персонализация` · [12:12](https://youtu.be/IeZGw2fPVcI?t=732)

**Мысль:** Парк без карты и порядка, где персонажи знают о дне рождения ребёнка, создаёт ощущение особого статуса; история вышла в новости, потому что тронула глубоко.

**Слова автора:**

> Went six or seven years old went with his parents on a journey in disneyland and parents were really kind of preparing for it of course but they didn't have like a whole plan about what is going to happen right they just didn't have that and so they ended up in there and they were walking around the roots and they're enjoying the experience and it's also so interesting because they that was the first time the first year when they redesigned this entire park normally if you think about the park experience and it's part of navigation as well it's like go here first this is point one go to two then go to three then go to four then go to five then go to six it's very structured right most parks around the world are very structured well not disney park because it has all these little hidden parts there is no map like go here first go there first start where you want to and they have all these different paths you can take and it's probably not going to happen that you're going to explore all of them at once it's just not going to happen you will always find something new because they have different music different things happening different places and so on so what happened there was this child was kind of walking around and because he had a magic band and again this is a little bit of a privacy concern but because they had a magic band all the creatures like mickey mouse and donald duck and others they all knew that this person had a birthday because he had a birthday today so everywhere he went he was kind of all in a special treatment in a way right so he was always getting attention and he was getting a lot of like surprise gifts and this and that and they would even sing happy birthday to him right and they would play happy birthday song when he would enter and things like that he felt like he's in a major clan and this became such a big story as well because his parents were all over the moon this child desperately tried to get to the attraction park like at least once a year right and has become a big story covered by major news companies and so on just because it touched people's heart on such a profound level and you could never reach that by having like say a map go from here to here to here to here.

**Для Напарника:** Остров без единственного маршрута; кот помнит и называет значимое (первая сессия, возвращение), а не просто считает.


---

## 10. Хороший дизайн дешевле и влиятельнее, чем 200 инженеров ради 0,5 секунды
`процесс · метрики · вкус` · [14:26](https://youtu.be/IeZGw2fPVcI?t=866)

**Мысль:** Инвестиция в дизайн даёт больший эффект, чем гонка за мелкими улучшениями производительности и функциями.

**Слова автора:**

> Notion of airbnbs and others came in where designs offset matters this matters because it's much cheaper than building features like good design is expensive but it's not as expensive as hiring 200 engineers who would work non-time like full time right trying to improve a performance by 0.5 seconds right it's just much cheaper to invest into design and it has a much more profound impact and benefit as well which is why i think that we are lucky and we're happy to be in this place because we can have a tremendous impact.

**Для Напарника:** Приоритет эмоциональной полировке ключевых моментов (RevealIsland, ответ кота) над добавлением новых фич.
