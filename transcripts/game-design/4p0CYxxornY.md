# Devlog 40 - Combat Juice, Dialog, and Quest System in UE5
Dani Marti · 4 мин · 943 просмотров · en · https://youtu.be/4p0CYxxornY



[00:01] foreign welcome to a new devlog in this episode I will continue working on a combat and test the narrative plugin for the quest and dialogue system so let's get started this week I have been refining the combat system I have added the possibility of random attacks for the enemy which gives more variety and makes the combat seem more complex than it is for that each type of enemy has an array 

[00:34] of any montages for the attacks and in the attack event I choose one at random as you can see here in the blueprint I use this system for other animations like the heat animations and even later for the weapon Trail and heart sounds on the other hand I have implemented the stun mechanic both a player and the enemy now can be stunned for this I have added the new stat boys which is the resistance to block attacks every time an attack is blocked the damage that 

[01:05] would be received is reduced from The Voice and if this is completely consumed the character enters the star animation that leaves him vulnerable to more attacks for some seconds the boys will be Auto regenerated depending on the enemy type and the player level I have also started to add visual effects like weapon Trails both for the player and enemy in the case of the enemies it's a bit more subtle because part of the game design is to 

[01:35] give more prominence to the player the ideas to add effects to impacts Trails of blood for when the opponent is hard and so on at the same time I have also started to add sound effects for the moment only for weapon trails and when the player hits the opponent for these I use animation notifiers you can use the play sound animation Notifier if you want to play the same sound each time but since I want to add more variety and Randomness I am using a 

[02:05] custom Notifier so similar to the attack animations I have an array of different sounds both for weapon trails and hard sounds and I play one at random one of the epicularities of custom notifiers is that I can pass parameters so with the same Notifier I can play sound for different situations as you can see here I have an atom with different types of sounds this Notifier communicates with the characters blueprint through an interface which called the band where I have all the 

[02:36] sounds organized by typology this not only gives more variety but also more realism because it's not as repetitive as using the same sounds over and over again The Sounds at the moment are placeholders they are not the final sounds adding sounds and effects is what they call the juice in game design and these juice not only helps give feedback to the player but also makes interactions in this case combat much more satisfying I'll leave a very interesting GTC talk about this topic in description below if 

[03:07] you want to elevate your game and the game feel don't forget to check it out finally I have started to play around with the narrative plugin my game has a strong and dialogue component so I thought it would be interesting to try it out the developer has an almost 2 hour video tutorial describing in the F the ins and outs of the plugin so far I just follow the tutorial and did a couple of tests here you can see how when I talk to these two characters they give me a quest to find about when I 

[03:38] find it and talk to them again the dialogue changes and the questions mark as completed I was surprised by the Simplicity and Clarity of its use besides combining quests with dialogues it allows you to create all kinds of quests the potential to create from dialogues with multiple branches to complex quests with different tasks allows you to create any game you have in mind I'll leave the link in the description if you want to take a look and I watch all this week's progress in the next days I will continue refining 

[04:10] and adding juice to the combat as well as dive in deeper into the quest and dialogue system as always thank you very much for watching and see you next week [Music] [Music] foreign 
