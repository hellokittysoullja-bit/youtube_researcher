# Building a Mobile Design System
try! Swift Conference · 19 мин · 5796 просмотров · en · https://youtu.be/Fvq8PQKJj_k



[00:08] hello everyone sorry if my voice is a little horse I went karaoke last night and had a little bit too much fun okay welcome to my talk on mobile Design Systems my name is Christina Fox and I am a senior iOS engineer at a company called into it I primarily work on a Financial app called QuickBooks self-employed that helps Freelancers and contractors manage their business 

[00:38] finances for the past year and a half I've been building out the design system components for the self-employed app and I am here to share all of my learnings with all of you first off you may be asking what is a design system it's a relatively New Concept in the mobile software industry and basically describes an alternative way of thinking about how we build our 

[01:13] apps it is a series of components that can be reused in different combinations Design Systems help you manage design at scale let's take a step back from the that for a second what does that mean similar to how you can take individual Lego blocks put them together in a particular way and see these individual pieces in a 

[01:45] whole different light you can do the same for software take all of these individual UI elements a title label an underline view some text and an icon put them together in a custom view component and repeat where necessary to create an entire 

[02:16] screen here's a look at a screen that I built in the app that I work on thinking back to the last few slides that you saw how can we break this down into its individual components so we take a look at the top portion you focus in on the top portion of the screen you'll see that we have all the same characteristics as our wireframe from before highlighted in the 

[02:47] red boxes there's a really amazing blog post from a a man named Brad Frost for what he calls Atomic web design similarly in our case we're taking individual pieces combining them together to form even larger pieces until we get to the full screens for our iOS apps now who does this 

[03:17] benefit since it's called a design system it seems like it should mainly be for designers right that may be true but and engineers and end users benefit too let's start with designers first for our designers Design Systems help unify the look and feel of your app and can cut down on design time it also 

[03:48] makes it easier to build consistent flows throughout the app if you follow the same Paradigm as features built before right Engineers it cuts down significantly on building time and lets you ship features to your end users much faster it promotes code reuse and if any additional features get built into your components like accessibility for example then Engineers 

[04:21] won't have to worry about whether or not they're forgetting to implement some of these additional aspects for our end users it can make it a lot easier to recognize your brand and understand how to use different parts of the app faster especially if it all behaves the same way where is this applicable what kinds of apps do Design Systems work best 

[04:55] for it is really best to use for apps that can be broken up into multiple component pieces and who want to develop a particular brand style let's take a look at the Airbnb app for example you can see how the homepage of the Airbnb app is comprised of multiple listing cards and multiple impact display cards they were able to reuse these view 

[05:27] components in their collection view here another great example is the LT app take a look at the lift redesign using their new design system on the right hand side this setting screen has a lot of repeated UI table view cells which makes it the perfect candidate for reusable views now that we know what a design system is and how useful it is for 

[05:59] everyone involved let's take a look at how to get started building it let me start off by clarifying one thing this is not a guide on how to create your own design system this is something that's largely personal to each team or company who may who it may be supporting and should be based off of your own beliefs your user experience your mission and your own company's brand 

[06:30] that being said there are many great resources out there on how to do this yourself I highly recommend this one especially if you're on working at a company that doesn't necessarily have enough design or development staff to solely focus on a design infrastructure team this one focuses on how you can start small and work your way up this talk will be a guide on how to get started implementing the design 

[07:02] system once you have the philosophy of your design system in place now remember this little flowchart that we saw towards the beginning of the talk we're going to start building out these little pieces now until we get to the bigger picture at the end okay so if atoms are the most basic building blocks of ourselves what are the most basic building blocks of apps 

[07:33] fonts and colors pretty much every app has some text to display and generally has their own custom color palette behind it chances are that you already have a utility class for both of these in your established codebase can anyone raise your hand if you already have custom fonts or colors in your code base seems like a lot of people do congrats you're already well on your 

[08:04] way to having an implemented design system now for the sake of starting at the beginning let's take a look at how to build these into your code base so here the look at a typography system that we can implement we show the name of the font style on the left side and describe what it should look like on the right side for custom font one way that we can Define these font Styles is to create an enom that defines 

[08:35] all of the different typography Styles in your app when you're building these Styles you can add a switch statement that Returns the correct UI font styling for you for colors there are a few different options on how you can Define these you can either do something similar to your font system and Define enum for each one of your new colors or you can add these colors to your 

[09:05] asset folder and call them by name similar to how you call UI images from your asset folder Liz Marley showed an example of this yesterday in her color accessibility talk it is worth noting that I'm providing several options because there are multiple ways to do this and your team may prefer one or another my team personally uses a high hybrid ver a hybrid of both of these versions where we have defined enims for 

[09:35] the named colors because it's really easy to mistype a string and we really wanted to make it autocomplete ready now that you have your basics down let's move on to our UI components and controls now for UI controls this one can be optional depending on the customizations of your design system if you have custom Style that you want to add on top of UI kit controls then this would be the next step an example of this would be 

[10:07] something like the UI switch control here is what the UI kit standard switch looks like now take this and compare it with the one that's used by my team you can see that we've sha changed the shade of green color and it's slightly darker which matches the greens that I use throughout our entire app now compare this to the lift switch control they've taken it one step farther and slightly modified the shape 

[10:39] as well as the color of the off and on States it really depends on what you want to do with your own brand styling okay now that we're done with our controls let's move on to custom UI components now one thing to consider when you're building out your UI component is that it's really not just about creating that reusable view there is a bit of API design involved in this because you want to make sure that you 

[11:11] too can read that it's not only usable by any engineer that's trying to implement your view but it should be easily understood by any engineer who is not even familiar with your design system that's trying to read through the code too now let's take a first look at this example here we're creating a done button which is a custom button that I've created called action button it's extremely important to make it easy to understand glancing through all the different styles which type of style 

[11:43] should be applied here and keep it consistent throughout your entire app in this case we want to set this style to be a save Style on the other side for a delete button you can see that the concept Remains the Same in terms of its implementation all we need to do is switch the style and now you have a whole different look and feel to your components now once you have all of these smaller pieces in place it's time to fit them all together and create our 

[12:13] larger reusable views let's take a look at some of the components from the Airbnb design system you can see that they've largely defined things like table view cells collection view cells and headers in their system they have a lot of content where they want to display photos of their listings so many of their components require images to be 

[12:44] shown now here is an example from the app that I work on since we're a financial app we have to take in a lot of user input so many of our components our table view cells with text fields in various States as you can see my app's view components are quite different than airbnbs and mainly because we have very different goals in mind for our end users now you can see why the journey to 

[13:17] building a design system is very much a personal one to each company or team working on the app the last part of this section deals with taking all of your individual pieces and putting them together just like the Legos that we saw earlier there doesn't have to be anything fancy about this you can take all of your individual views and combine them together using UI kit as usual in 

[13:48] fact this is what my team does however I did want to point out another company in our industry that has taken it one step further there's a framework called epoxy by Airbnb that allows you to easily combine views and build complex screens now unfortunately for us iOS Engineers they've only open sourced it for Android at this point but you can take a look at their cotlin implementation and see how 

[14:20] it is used in this example we're creating the equivalent of a table view called a list adding a header and populating it with photos you can see that to create the header all you need to do is Define three simple things the identifier the title and the description it's a really similar process to add photos they iterate through building 

[14:53] many photo views with an identifier and a URL for each photo essentially at the end of the day they've taken all of the boiler plate and hidden it behind this framework so that their Engineers can increase the speed of development significantly another great thing about this is that it allows you to have separation of concerns and forces you to split up presentation code from your business logic great now we've walked through how 

[15:26] to get started by going from your most basic building blocks of fonts and colors all the way through figuring out how you want to piece together your views this seems like a lot of information how do you keep everyone on the same page now that you've got the system up and running for the most part you need to keep a line between two separate parties the engineers implementing the design system and the designers working on the 

[15:57] design system as a whole for the engineers depending on how large your team or company is you may be able to set up a meeting explain how to use it all and be done with it in one go however what happens if a new person joins your team what if your design system is too complex to remember all the little details here documentation is the solution the best documentation you 

[16:29] usually comes with information on how to use the view any implementation details and screenshots whatever your feeling about Google's material design it honestly is one of the most comprehensive Design Systems out there and has equally comprehensive documentation to back it up the second thing to do is to keep aligned with design I don't have a lot of suggestions here but the main thing 

[16:59] that you want to do is to make sure that updates to your design system are communicated out now this may be in the form of a regular meeting with your design team or by having Engineers involved in any design system change discussions you now have a much deeper connection to your design team because of this since I've been going through this process for the last year and a half I've had more than a few lessons learned 

[17:31] throughout this experience I wanted to leave you with a couple of things in to keep in mind while you're building out your design system I once worked with an engineer who by default would create reusable views utilities and tools for basically everything he touched just in case it needed to be done at a later point a few weeks before this conference my team team went through and deleted a bunch of unused code and ended up 

[18:03] finding a lot of this person's code at the mercy of our delete button basically the lesson learned is that just because you can componentize something doesn't mean it always needs to be done please keep that in mind as you're building your design system or really anything else for that matter the last thing is that it's really worth calling out that you you will be able to get much more from building out a design system than just 

[18:33] some you reusable components it can bring about a much more meaningful working relationship between designers and engineers at the end of the day both parties want to make sure that their users are getting the best experience possible but things like deadlines and Technical setbacks they can get in the way one of the most important things that I've learned through throughout my career is figuring out when and how to push back and say 

[19:03] no in the context of design systems similar to our last lesson just because a designer has imagined it doesn't mean it has to be built either if something seems too hard or too timec consuming especially if you have a hard deadline go back and see if you can compromise I've built some really amazing working relationships with our design team this way often because many 

[19:34] of them just don't understand how difficult it is to build something and they'll work with you to come up with a solution that works for everyone involved thank you [Applause] 
