# How to create mobile surveys without code
Appcues · 4 мин · 1095 просмотров · en · https://youtu.be/sbT3LKOqCkM



[00:00] - Hey, everybody. My name is Sam and I am a senior product designer here at Appcues. And today, I wanna show you how you can use mobile surveys to gain new users and reduce churn. And the best part is there's no developer required. (mid tempo electronic music) So the first thing that I'm going to create in the Appcues mobile builder is a basic rating question to ask my users how much they're enjoying the app. 

[00:32] And this is gonna kind of serve as a temperature check for our users. Users that rate the app low, I'm gonna give them different content than users that rate the app high. So we're gonna come into the Appcues builder and we're gonna create a rating. And now the rating, I can style this a few different ways. I could use a number, I could use a star rating scale, or I could use an emoji rating scale as well. But for the purposes of today's video, I'm gonna use a star and I'm gonna change the selector color 

[01:03] to match the theme of my app, as well as the selected state color to match my button. Next, I'm gonna change this question label to say, how are you enjoying the app? And I'm gonna center it and change the font size so that it's exactly as I want it. I'm also gonna shift everything down a little bit. Perfect. So now with that I've got it styled correctly, I need to actually include some logic in order to trigger other content. 

[01:34] I'm gonna go to my submit button here and I'm actually going to track an event and I'm gonna call this event rating submitted. So I'm gonna use this rating submitted event to trigger some follow up flows depending on how the user responded. Next I wanna target this flow to a specific audience. So I'm actually gonna target this flow to my regulars. These are people that have used the app and know its features and functionality enough that they can actually give a useful assessment of the app. And I'm gonna target this flow to a specific screen. 

[02:05] I'm gonna target it at my file screen since that is where I expect users to hit their aha moment with my app. And now I'm gonna go ahead and publish this. And there you have it. There's our rating. All we found out from our rating though, is how much our users like our app, which is useful internally, but we can do so much more with that data. Did you know that moving from three stars to four stars in the App Store can result in an 89% increase in conversion? So for this next flow, I want to drive those users 

[02:36] that rated my app five stars to go to the App Store and leave a review. So I'm gonna create this new modal that's gonna show up afterwards. This is a separate flow. So I'm gonna make this button that says rate five stars and I'm gonna make this button action go to a specific link and I'm gonna send users to the App Store with this little deep link appended to the end of it, action write review. And this is gonna prompt users automatically to leave a five star review. So I'm gonna target that by using the event that I set up before 

[03:07] called rating submitted. I'm also gonna narrow this down so that the only people that see this flow are people that left me a five star rating and now I'm gonna publish that. So if I were to rate this app five stars, now I'm gonna get prompted to go rate it in the App Store. And there you have it. Now I'm prompted to write a review. Now on the flip side, if users only rated me a one or a two, I'm gonna want to ask for some feedback. So to ask for feedback, 

[03:37] I'll add a text input box and I'm gonna make that a long answer. So this time, I'm gonna ask customers, what can we do to improve the app? And I'll style it similarly to the other one. And so again, I'm gonna target this flow when the rating submitted event occurs and at users who either rated the app one, two, or three. And so this time if I rate the app two stars, I'm gonna get prompted to offer feedback for how we can improve the app. Thanks for watching, 

[04:08] and be sure to subscribe to Appcues for more great product content. 
