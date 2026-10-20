# Here's What Makes Incremental Games FUN!
Developing Ideal Idle Incremental Game · 10 мин · 26388 просмотров · en · https://youtu.be/hty_r4LIRb0



[00:00] the concept of idle instrumental games might not sound fun at first you watch a number go up buy upgrades to make it go faster and when you hit a price wall you just reset your progress to gain a production bonus and Advance a bit further next time does that sounds fun to you however there are hundreds even thousands of extremely popular Idol incremental games with a huge community of Highly dedicated players so what is this magic what makes incremental games 

[00:33] fun as a solo game developer I've been working on my own Idol incremental game get a little gold for more than 10 years I've studied this topic quite a bit and came to the conclusion that majority of great idle incremental games share this one concept that I'm about to show you to prove my point I'm going to create a completely new incremental game just for the sake of this video video this game will include only this one single 

[01:03] mechanic and nothing else I hope it will still be engaging and fun so let's get straight to work shall we first of all I need to come up with the idea of main currency it could be anything cookies leaves pixels eggs even any matter Dimensions initially I thought I wouldn't try to be original and use dollars or bucks as a main currency but that I decided to change bux into Ducks 

[01:33] because in this way I can use this highly funny quacking sound to every button in the game and that already sounds fun to make things a little bit easier for myself I borrowed a background and btom design from the main project get a little gold after all I'm trying to create the most basic incremental game and don't need really fancy Graphics or unique design to prove my point that this single mechanic can 

[02:05] make the game really engaging and fun the most essential element of every incremental game is the counter of the main currency ducks in our case so let's add it right in the middle of the screen the initial amount of ducks will be 10 because that's how much our first generator will cost if you've played other incremental games you probably know what generator is but for those who don't generator is just upgrade a 

[02:36] structure or a building that produces or generates hands the name the main currency in our case the first generator will cost 10 ducks and produce two ducks every second so let's quickly create a simple button that lets us to purchase this first generator we also need a text field showing our actual duck production speed measured in Duck per second here is where the magic begins at their core 

[03:08] the vast majority of idle incremental games are just a seesaw between profits and costs this means that with every next generator you buy your profits grow linearly while your costs grow exponentially to make this clearer let's take a look at the formulas I'm using for a do game average generator you buy will increase your dock production by two ducks per second this means that 10 generators will produce 20 ducks per 

[03:38] second and a 100 generators will produce 200 docks per second that's what linear growth is however the cost of each subsequent generator will be 10% higher than previous one given this exponential growth the cost of the 10 generator will be 24 docks and the 100s one will cost more than 100,000 ducks that escalated quickly now what do these numbers really mean let's say you already have nine 

[04:08] generators producing 18 docks per second it will only take you two seconds to purchase your 10 generator but you would need to wait more than 10 minutes to progress from 99 to 100 generators and if you've already purchased 199 generators it would take more than 50 days to buy the 200 one which would cost more than two billion docks That's The Power of exponential growth so at the earlier stages of the game your 

[04:38] production will exceed costs but the more generators you buy the higher the price of the next one becomes until eventually the waiting time for the next generators becomes prohibitive and you hit the wall remember the one and only mechanic that makes incremental games fun I mentioned about well in my opinion all the enjoyment and engagement of idle inal game stems from its ability to offer creative ways to overcome this 

[05:09] wall potentially there are tens or even hundreds approaches to it covering them all would definitely be beyond the scope of this video however there are two basic and essential ones that without exaggeration are used in every incremental game I ever played and I firmly believe that using just these two are sufficient to create a reasonably engaging game so once we hit the wall and the speed of our game slows down 

[05:39] what can be done to speed it up the most obvious and widely used solution is to create another type of generator whose uh price would be much higher but whose production is also greater in our case we create a second type of generator which will cost uh one 1,000 ducks and will produce 100 Ducks per second at first glance it might seem that this generator is less preferable because its 

[06:09] production rate compared to its price is lower however due to the exponential nature of price growth in fact this second type of generator produces more ducks and costs less let me show you an example you will spend more than 11,000 ducks to buy 50 generators of the first type which produce 100 Ducks per second this same production will cost you only 1,000 Ducks if you buy the generator of the second type now it will cost you 

[06:41] almost 1 and a half million ducks to purchase 100 100 generators of the first type producing 200 Ducks per second but you can reach that same level of production by buying just two generators of the second type for 2,100 Ducks I hope that makes sense at the same time doesn't really matter how much more appealing the second type of generator is because sooner or later it will also become irrelevant only the game designer decides how many types of generators 

[07:11] there will be in the game for the Duck game I limited myself for three types of generators the last one produces 5,000 ducks per second and it cost starts from 100,000 ducks in my main game project get a little gold there are 15 types of generators ranging from fan to a white hole something opposite to a black hole and if you are into incremental games you've probably seen hundreds or even thousands type of various generators but 

[07:43] is there something Beyond generators well the second approach to Breaking the wall is the well-known Prestige mechanic again if you play it incremental games before you almost suddenly come across the concept of prestige Mechanic In A not it's a mechanic that allows you to reset the progress in the game in exchange for some permanent boost that allows you to progress faster next time for our Duck game Let's implement the most basic Prestige mechanic first we 

[08:15] should add the variable to keep track of all ducks produced during the game now once the number of ducks reaches 1 million will'll show a button offering to reset the progress and obtain a 100% boost to all duck production we can either Prestige now or wait longer to collect more ducks and increase our potential bonus each subsequent step require 1 million more Ducks than previous one and we'll add another 100% to the bonus so to reach 200% bonus we 

[08:48] need to collect a total of 3 million docks and to reach 300% bonus we need to collect 6 million Ducks hope that makes sense another important aspect of virtually every incremental game is offline earnings so let's add them to the DU game the simpler the game the easier is to add the offline earnings mechanic in our case it will be a breeze we just save the time when the player close the game and count how many seconds they were offline once they start the game again then we can 

[09:19] multiply these seconds by the duck production value and receive the amount of ducks produced when the player was offline the only thing left is to add winning conditions because I do want this game to have an ending and probably encourage players to compete with each other to try to beat the game in the shortest time possible I guess 1 billion docks sounds like a good Milestone to beat the game I personally managed to do this in 14 minutes 44 seconds would you 

[09:51] be able to beat my record I feel like it should be easy because I wasn't even trying leave your records in the comments in case you decided to give it a try and yes I've already uploaded the game to each IO I'll leave a link to it in the description below let me know if it was engaging enough for you to beat it and if you like incrementals like I do make sure to subscribe to this channel because I'm planning to continue publishing videos just like this one for now though thank you for watching and 

[10:22] I'll see you in the next one [Music] 
