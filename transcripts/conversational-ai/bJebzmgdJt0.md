# How To Show An Alert Message In Bubble.io (Complete Guide)
Building With Bubble · 10 мин · 6547 просмотров · en · https://youtu.be/bJebzmgdJt0



[00:00] if you're relatively new to Bubble you might be asking yourself what on Earth is an alert element great question I remember when I first got started in bubble it took me a couple of months to actually get my head around alerts and understand what they were actually useful for well in this video you're going to learn everything there is to know about alert elements you'll learn what they're used for when they should be used how to design them and build out the workflows to power them and finally how you can customize alerts to display different messages look thankfully this one is a relatively straightforward 

[00:31] process so I'm going to hand this one over to Luca and he's going to cover everything you need to know hello today we're going to be going over quickly how to build in alerts into your blood application and then how to actually building alerts which changes the alert message based on what you're updating within your application so all in alert is basically is a temporary message that pops up after it fades in in it holds and then it fades out 

[01:03] usually alerts are actually used for when something has been changed with in a bubble application but maybe that change isn't necessarily as visible so you give them a visual cue just to tell them that something has been updated within that bubble application to give you an example of this I've just built out a little user account and as you can see when we press our update button we get our fading in and then fading out 

[01:33] let's jump over into our bubble application so we can show you how to do that so if we go to our bubble editor here as you can see on the page we have a alert now this alert can be placed anywhere you want on the page and if you collect this checkbox here you can see that the position of the L will always be at the top of the page now if you want to put the alert somewhere else you would have this unchecked and then place it anywhere you would want the alert to 

[02:06] come up on the page uh but it's standard UI design have the come on to the top of the page so I'm just going to like keep this checked so let's get into building out our alert message so first of all I'll delete the ones that we have created for and then we can get started so what we're going to want to do is go over to our visual ele field here and scroll down to alert here now we're just going to place it anywhere on the page 

[02:37] and we're going to click and update our text within this alert and just set this as update now what we're going to do is check this box here because that will mean it will always be at the top of the page no matter where you put it on your page it just makes sure that it comes up and it fades in and Fades out from the top which is standard UI design so I'm just going to click that one there if you wanted it to appear anywhere else on the page you 

[03:07] would uncheck that and then place it in the position that you would want the alert to be but as I said because having the alert message at the top is standard U design I'm going to leave it there so if we go over to our layout tab here and we uncheck make this element fix width it will expand the full length of our page and that's exactly how I want my alert message to look just going to quickly go over to here I'm going to 

[03:40] make our alert message nice and green to say it's success so we're going to go to on the text going to click green I'm going to choose a dark green because I'm going to set our background style a light green by just clicking the green and then set perfect and if we scroll down to the Border I'm take our border off lovely so now we're going to want to go and attach a workflow to this alert 

[04:13] to make sure that it appears where we want it to appear so I'm going to go onto our update button over here right click and click the start sledit workflow so what we're going to do is we're going to add an action onto this button we type in alert you can see there's this action called show message in an alert box going to click that and because we've only got one alert on the page it has automatically format added to the alert 

[04:43] which is perfect now if you wanted to change the length or duration of how long this message came up for we can basically change these numbers in milliseconds here so at the moment it's feding in for half a second holding for two seconds and fading out for half a second as well so just for the sake of this tutorial I'm going to change this to a second because maybe that's too long so if we check out of here and preview our application you can see when 

[05:17] this button is pressed our alert message comes up and then Fades out because we've changed the milliseconds of the hold it's now there for half the amount of time it was before so how would actually get this alert message to change its message based on which input value had been changed either the password or the name let's jump over into our bubble Editor to show you how to do that so what we're going to want to actually do here is move our show 

[05:49] message in an alert update to before we've updated the current user and that's because we're going to see the difference Within the input for let's say the name and the current user's name because if someone's updated the name and then is clicking this button we're going to want to be able to differentiate between the current user and the updated input so it sounds complicated but I'll show you how that 

[06:19] works in a second what we're going to want to do here is actually click change the alert message and we're going to have this message come up when we've updated just the name so if you update it do name updated perfect now here I would show you exactly what I was talking about for in terms of having inputs and it being 

[06:49] different to what the current users value is so for example we only want the message in this alert to come up when the in put for the name value is not the current user's name so when this condition is true a user's gone onto their user page edited their name and clicked update but if we were to have this action after make 

[07:21] changes to a current user this condition wouldn't actually be true so we wouldn't be able to differentiate but if when we do it before before is before the input value is updating the current user so then it's fine so if it's just the name we're going to want to do this and for the input password for the input passwords value this is going to be the same as the 

[07:53] current users password there go the password hasn't been updated what we want to do now is just fill out all our other alert messages that are possible so if we're going to copy we're going to paste this one's going to be password updated and so it's the opposite to what we did before so the input signups name is going to be the same as the current 

[08:25] users name because in this condition we're not we're only updating the password and the input password's value is not the current users's password now we're going to do the condition where we've updated the name and the password so in this scenario the input values will both be different to the values stored in the C user so is not is not name this so you might be wondering how 

[08:58] we're actually pulling these input value and if we go onto our design tab you can see that I've got the initial content to be the curren's name for the input and the initial content for the passwords input to be the current users's password and the initial content basically is what is outputed in these inputs before they are edited or gone into and CH 

[09:29] basically so that's how we're drawing those values within our only when conditions here so if we are to preview that now and we change the name you can see the name has been updated if we are to change the name and go and change the password the name and password have been updated and if we are to change just the password you can see the password has been 

[10:00] and that's a nice little bit of customization to really upgrade your UI experience for your users and just like that you now know everything about using alert elements inside a bubble in my opinion alerts are almost essential for any application as they just help create a better end user experience look if you found this video useful and you wanted to stay up to date with any additional tutorials I share I'd always recommend hitting that subscribe button so that way you can be the first to know whenever I drop a new 

[10:30] video in the meantime though I just wanted to say a massive thank you for taking the time to watch this particular video and I wish you all of the best on your own no code Journey [Music] 
