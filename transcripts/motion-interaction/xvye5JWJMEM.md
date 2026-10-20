# How to use Haptic FeedBacks in SwiftUI
MasteringProgramming · 4 мин · 587 просмотров · en · https://youtu.be/xvye5JWJMEM



[00:00] [Music] welcome back to our brand new episode of mastering programming in today's episode i will show you how you can play and start haptic feedbacks on your iphone now obviously for this episode you're gonna have to use your actual physical iphone and not the simulator and i actually won't be able to show it to you because it's something that you feel using the iphone anyway let's get started so the first thing i'm going to be doing is i'm actually going to be creating a v-stack and i'll do that by typing in v-stack 

[00:31] open and close the bracket and we're not going to get rid of the text we're actually going to copy it or cut it and paste it inside instead of the text that says hello world we're just going to say that me instead and i'm not going to do anything to the text first uh because i first want to show you how we can use buttons to cause haptic feedback so i'm going to be creating a button just like this uh there's multiple ways you can create a button this is just how i do it there we go and after that what i'm going to be placing is actually inside of the action itself 

[01:03] that's what i'm going to be calling the haptic feedback so i'm going to say let impact is equal to ui impact oh sorry ui impact feedback generator over here i'm going to open a bracket and i'm going to pick the second one and here that's when you actually get to put the style that you're after so if i just put a dot we have multiple options here such as heavy light medium rigged 

[01:34] rigid and soft uh let's go ahead and pull light or actually let's go ahead and put heavy for the button and after that so now that we created that impact or the haptic feedback we then need to start it so i'm going to say impact dot and then i'll say impact occurred now if you call this anything else you're obviously going to call over here and then say impact occurred and as you can see now that we used it at the speed let's obviously add some text for the button so we can actually see it and i'm 

[02:04] just going to say tap me i'm not going to focus too much about the design here i just want to show you how you can do the haptic feedbacks so that's great and if you actually run this app you will now work on the button um but what if you want to add it to text what if you have some action to text and you actually want to add it to to do that what we're going to do is first we need to create an extension so i'm going to go here at the end of the page and i'm going to type in extension view 

[02:35] and we're going to say fun and then i will say haptic feedback you can actually call this anything you want i'll open a bracket and inside of here i'll create parameters the first one will be called style and it will be of type ui impact feedback generator dot fee sorry dot feedback style as then i'll then say it's equal to dot and here again you have the option to put light or whatever it is because we picked heavy for the button for the text i'll keep it as light 

[03:07] and then we're going to say some view and what we want to do after that is we actually want to open a bracket and inside of here we're going to say self dot on tap gesture and then open and close a bracket and i will say let impact equal to ui impact and we actually typed it up at the beginning over here so i'm just gonna do the same 

[03:38] there we go and i actually just realized i did a mistake this is meant to be a normal s and there we go now no actual works so that's actually actually all you need to do for the extension i'm just gonna highlight it all and click on i just to make sure that you have the good um low key and over here we can simply go to that text and i will simply say dot and then i will say haptic feedback and if i run this 

[04:09] app now it will actually work so again i will run it you won't be able to see anything but once i do run it it will actually work running on the right side and like i mentioned you won't actually be able to obviously feel the haptic feedback but as i'm clicking on tap me the text and the button i'm definitely feeling the vibration in my hand and from the phone and if you do this you should also be able to feel it as well and i would recommend you playing around with the different styles so that you get to feel how it feels like to have different styles for the haptic feedback thanks so 

[04:40] much for watching and i hope that you enjoyed it see you next time 
