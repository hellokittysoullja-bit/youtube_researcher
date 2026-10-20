# Redesigning The Worst Healthcare App on the Internet (MyChart)
Demystifying Design · 5 мин · 813 просмотров · en · https://youtu.be/MmUuUY43hEw



[00:00] today we're redesigning one of the applications that I use to go to the doctor whenever I need something done it's called My Chart man is it hard to use look at this interface it's clear that whoever built this interface just wanted to jam a whole bunch of stuff at the top of the screen and just hope that the user found it there's not very much care put into this design here and we're gonna fix it today so as always we've got the style guide we're just going to use their nice blacks and orange Hues and we're going to use a nice rounded 

[00:30] Sans font to get a more kind of friendly feel into the app more approachable feel and see what we come up with here's the stories this is everything I'd want to achieve in this app of course they're trying to do a little more and I would suggest that perhaps they should do a little less to reach a better outcome for the customer but nonetheless we're going to try and Tackle all of these at once let's just get in there [Music] starting out by modernizing the navigation to include a nice little 

[01:02] navigation bar at the bottom that's the standard Paradigm for how you navigate through mobile apps these days so it's a pretty easy win for us foreign the header and I actually make a mistake here by including the hamburger menu in the user menu because it's a too complex and B just kind of takes the existing 

[01:32] problem of way too many links on the current APP and ports into this new one So eventually we switch to a completely simpler Paradigm where we take all of the links that would be in the hamburger menu and move them into different parts of the UI but for now we'll start with the basic default header [Music] I almost never opened the myshar app 

[02:03] unless I have an appointment upcoming in which case that's kind of the first thing I want to see for checking in and getting details about that appointment so floating that way up to the top and trying to control the visual hierarchy so that people's attention goes straight to this card first [Music] personally I really struggle adding metadata to cards and in this situation 

[02:35] I was just hitting wall after wall I I wasn't really making much sense of this design so I decided to just put a pin in this and come back to it later once I had some more time to work on the other components [Music] [Music] it's getting a little more experimental here but whenever you have an app that has some kind of shared set of actions 

[03:05] that people commonly do it's a good idea to just kind of make them easily accessible somewhere and the default experience usually the home page so here we're adding a couple of buttons that are essentially embedded hot links that will take users to perform those tasks in the app really quickly and as soon as they click on them [Music] of course I would also be interested in 

[03:35] any urgent Communications coming from my clinic through this platform so having a little dedicated space to float any urgent notifications or messages that I haven't read yet to the home page separate from the actual messages page itself makes a lot of sense [Music] 

[04:06] and the final but probably most impactful change here is that we're moving away from the traditional title and user menu header setup and we're just asking the user a question hey how can we help you today which naturally leads into the quick actions just below it and kind of sets the stage for the purpose of the app the app is here to serve you not the other way around so adding that text there just explicitly sets the tone and gives us a lot more space to work with in the header 

[04:39] all right there we go a new MyChart interface I think this is significantly better than it was before um everything's organized in a manner they pulls your attention very specifically through the UI um you've got pretty much everything you could possibly need in this home page at the very least and everything else is abstracted away into the appropriate parts of the UI when it makes sense but it still feels a little off I think there might be a little bit too much text uh just just get the sense that something's missing here so let me know in the comments how you would improve this further and of course have a lovely 

[05:09] week folks hope you enjoyed this one I'll see you in the next one bye [Music] thank you foreign [Music] 
