# Figuring Out My Game’s Core Loop in Figma (Devlog 1)
Sirevix · 18 мин · 30 просмотров · en · https://youtu.be/rh9-4wZVoW8



[00:01] All right. So, um I have absolutely no idea how to do this properly. So, I kind of wingle it. I hit record in Figma while I was trying to put together this user flow for the players in my game. Oh, wait. I should have started by that. I I'm building a game. And then later dragged the whole recording into Premiere and recorded a voice over it. So this is what you're seeing. This is the 

[00:33] end result like the user flow like how the players will behave into the game. So basically you're about to watch me thinking out loud while I try to figure out how the game will actually work. I know it's messy, chaotic, whatever, but yeah, that's gamedev. Uh, one thing was that uh my OBS like the recording was cropped and sometimes you don't see the whole 

[01:05] video like luckily the majority of the video happens at it at the center of the screen but there are bits that are missing. So I added this diagram that you see here and try my best to explain what is happening outside the camera view. Yeah, I will not record again because the user flow is already built and I just wanted to go with it like I don't want to build another one is my 

[01:36] first ideas and later we will modify it but yeah if I do another one it will be like a copy of this and I wanted to keep it. So that's what I'm going why I'm going with a cropped recording. So yeah, I don't know. Yeah, that's it. Let's jump into Figma and I'll work through what I was trying to build while doing my best to explain that. 

[02:08] Um, so okay, uh, this is a multiplayer world. So everyone's objectives is the town. So we start with town. So that's the main objective of the of the game. The idea is that you have multiple multiple players like working together to achieve one end goal. So you start in the town, you go mining. 

[02:40] There's like a bus that takes you there and one have to stay in the town. So since this is a multiplayer game, they can decide who goes mining. So you go mining, you take the resources and you have to carry them. How we designed this is like resources have 

[03:10] weight. You have limited inventory where you would keep your pickaxe and everything and you can carry so much. So between the people that's going to the to the aisle, they have to decide who carries the resources, who mines and all that. You return to the town, you take the bus, and once in town. 

[03:41] So maybe all this happened during one day. Let me think about this. So there are two players like they decide to go to to the mining area. 

[04:15] So like the They both mine. Okay, I'm seeing that the recording cut out. Never mind. We'll try to do with what we got. 

[04:50] So yeah, it's the same thing happening in the left side. Let me show. So yeah, uh better than what happened with the recording, but it cut out it corrupted. But this is the end result. I will add this later at the end. So they basiculate the players. They both go mining. They go take the resources. They carry them to the bus and it's like a community goal between this group of 

[05:23] people that went mining. So while they were mining, there is another group of people that stayed home and has to craft like taking the resources, craftings and upgrade the town. Now let me add the the collection 

[06:00] and of course there's an exchange. Uh again this is out of screen but this is connected to the resources. So they take the resources, they unload them at the town, they exchange it, and they go to craft things with those things upgrade the town. 

[06:32] And that's like the second group of players. Is that down? There are the the miners. They collect all the resources while 

[07:04] mining and Yeah, this was the bus takes the stuff to the unloading area. 

[07:34] This could be like another group of people that carry the resources. Like while player one miles, he unloads everything at the loading bay and another player carries the stuff to the bus. Like you carry from the mine to outside and somebody else carries it from the 

[08:06] right from the entrance of the mine to the to the bus. I think this is basically it. Like the core gameplay of the miners, the people that go mining. I'll just uh speed through this bit like 

[08:40] I'm just creating another player flow, user flow or whatever you call it. So that was like the player one and two. And while that happens, there's like another player that stayed at base. They didn't go mining. So they take the resources from the bus to like unload it. Oh, wait. This is important. 

[09:19] Okay. So, as I said, this was player three. He takes the resources then exchange for electricity or currency. I don't know, stuff like that. And with those things, it buys the crafting equipment and I don't know, wood, walls, stone, stuff to upgrade it down. 

[09:58] I would like like a general resource for the whole town like electricity like everyone has to be concerned about that. So there will be another group of people that will generate electricity and yeah what I see in the video this is 

[10:29] a hamster wheel. You will see now. So with that electricity, maybe you power the crafting page. 

[11:02] Okay, it's not Minecraft, but somehow you power stuff to upgrade the tower, like to craft the things for the tower. And with the currency, you could buy stuff for yourself or stuff for the town. Wait, this is Yeah, it was out of view again. So, I had to add the the PNG there. So, you can buy upgrades with a 

[11:34] currency, but it can be visual or something useful like a pickaxe or something like that or just a hat for yourself. But if you use it for yourself, maybe people will get angry with you or something because they mine those resources for the town and you're using it for personal gain. So I was thinking on maybe pay taxes like at the end of the day the game sums all 

[12:07] the everything that you have everything that was unloaded that was sold and 10% of that is distributed between everyone in the in the town between all the players that could be a system. So, as you can see, I added that there because was that out of screen. This is me editing it. 

[12:39] Um, the taxi system was added later because was after that after I finished everything I decided to add it. But yeah, that's it. Uh have no idea what ending out of Sing again. Oh yeah. And this was another player's job while the other one allows 

[13:11] resources. This one takes the things to to do that. Um, I have to add some kind of thread like I have the the monster and the the fighting. So like the whole objective of the game is to defend the town but for that you need resources, electricity, upgrades. Like there is a shield even though you 

[13:43] can see it. And there is player five probably that will have to fight the big bad monster. Yeah. No, player five is the crafting stuff and it will be player six 

[14:15] there. So you can see how everything is interconnected. Okay, PNG time again. This was auto screen. So there is a monster. You can see it's big bad. Uh if it gets to a town, destroys one building or I don't know something happens. Maybe the buildings have uh HP and all buildings lose something. If he attacks, then somebody has to defend 

[14:49] and yeah, defend the town because that's everyone's objective. So, uh, let me adjust this. Okay, so you can see that there's a the monster. You defend the town and that's it. Um, next. Oh, wait. I think I have this in in the video. Let me switch for a second. 

[15:20] Yeah. So, um you have to perform repairs. If that if the monster destroys a building or something, then you repair the dog. that takes defend. And that's another player. I think it's player seven. 

[15:56] I'm adjusting everything to have everything in view. But yeah, as I said, this is like it's not an MMO. Yeah, I'm adding the crown to the town like everyone's objective. Um, this is not like massive multiplayer, but I was thinking on adding a server. 

[16:27] Let me add the PNG. Okay. So, um hopefully you can see it. Um yeah, this is like an not a big MMO, but there will be one server and one town or maybe multiple servers, I don't know. And that everyone has to contribute to upgrade it. 

[16:59] So that that's basically it. You have to defend it. You have to mine resources and buy stuff, craft, upgrade. Oh, and this for important thing. It's not crafting about crafting upgrades. Yeah. The 

[17:29] upgrades for defending will be stuff like this. Maybe you could have weapons and stuff, but more like things on the ground. And I was thinking maybe there is a mist or something that you cannot go out of town. And you expand the town by building stuff. 

[18:00] Like if you place a building, it will expand the area of the town when until it becomes gigantic. So I think that's the core idea. I will definitely add stuff later. like this is not this is an a live document. It will change a lot but it's a cool idea. 

[18:31] Okay. Oh, and have I said this is VR? Yeah. 
