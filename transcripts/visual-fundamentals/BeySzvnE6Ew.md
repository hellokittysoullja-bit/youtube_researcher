# User-Defined Dark/Light Mode (CSS ONLY) | UI Design Theme (prefers-color-scheme)
codeSTACKr · 10 мин · 3045 просмотров · en · https://youtu.be/BeySzvnE6Ew



[00:00] [Music] in today's video we're going to build this there are several ways that you can implement themes in your user interface generally these only choose between light and dark mode but any color scheme could be a choice in the last video I showed you how to accomplish this with only CSS and a checkbox this time we're only going to use CSS no checkboxes or JavaScript I still have two more ways to implement a mode picker after this video 

[00:32] those will be a bit more advanced and they will use JavaScript so stay tuned for those there will also be some extra cool things thrown in throughout each video so be sure to watch to the end to pick up all of my tips and tricks a link to the code is in the description below and if this video helps you out help me out by liking the video and subscribing for more videos like this let's get started so we're going to use code pin and we'll start with the HTML and we'll have a header pretty simple there and then the next thing we will have is a 

[01:03] div with the class of BG wrapper within this div we're going to have an image and I'm gonna paste the source in and then in our alt we'll just say background and we're going to add a class to this and that is going to equal BG just keep it simple and that is actually it for the background okay so right now let me just move this over we just have this big image 

[01:37] it has a dark side and the light side all right let's move on to the CSS first thing that I'll do is import the font from google polar 1 we are going to use CSS variables so I'm going to paste those in so in our route we're going to define white as this YZ 0 black is going to be one's the background color we're going to initially set to our variable of white the text color is also going to be set 

[02:09] to our variable of white and then our text alt color is going to be our black you'll see why we have these settings in just a minute background translate we're going to track that and we'll set that to 0 initially we're also going to set our header text from our CSS initially the text is going to be light side all right now let's implement some resets so we'll say star and then we'll set our margin to 0 our padding to zero and our box 

[02:40] sizing to border box all right and then after that let's target our body we're going to display this as flex we're going to align items Center justified Center and we'll set the height to 100 th 100 viewport height 

[03:11] and that's just going to make everything in the center here next we're going to set our background to be our variable of eg color then we're going to set a transition and we're going to set that on our background color of 0.6 seconds and we'll set an ease so whenever the background color transitions from dark to light or light 

[03:43] to dark we're going to have a nice transition all right now let's style the header in the header we're going to set a position on this of absolute so we're going to take it out of the document flow and we're going to set it at the top of 0 and the left of 0 and then we're going to set a width of 100% and then height that 2/3 rim background is going to be 

[04:14] our variable of background color and I a transition we're going to set the same transition on the background of 0.6 seconds and ease we're also going to set a z-index on this of 1 so that the header is always on top of everything else alright now we're going to do some cool things with the header we're going to set the text like I said using a 

[04:44] variable so header after and use a pseudo element we're going to position this as absolute then we're going to set the content using our variable of edittext all right so we're setting that up here better text light side there we go we can see it here all right so now we're going to set our color is going to be 

[05:15] our variable of text color now we set the text color the same as the background color and you might have been wondering why we also have an alt color before I do that let's actually change the font family we're going to set that to polar one and sans-serif as the fallback and the reason why we're setting the text color as the same as the backgrounds because we're going to add a text stroke around the font 

[05:46] we'll use that by using WebKit text stroke and we're going to set that to two pixels and the variable of text color alt and there we go I'll set the font - REM we're also going to set a margin of one rim top and bottom two rim left 

[06:16] and right and then we're going to set a transition of 0.5 seconds ease and now let's target our background rapper that was BG rapper and we're going to just set the overflow on this - hidden because right now we can see we can scroll left and right but we want the overflow to be hidden so that we don't see the part of the the image that's off the screen so now we can only scroll up and down that is what 

[06:49] we want now let's target our BG which is our image first we're going to set the width to 200 viewport width is basically 200% of the viewport size that's so that we can only see one side of the image and we're going to set transform and the translate X which is our left and right or horizontal we're set that to the variable of BG translate alright initially we set that 

[07:20] to zero so that's going to stay here on the left side of the image and then we're going to set a transition on the transform of 0.6 seconds ease in out so when we transition from the left side of the image to the right side of the image we'll have a nice transition alright so that's all of the main styles now we're going to go up here just after our route settings and this is where the magic happens we're going to say media 

[07:52] prefers color scheme dark so this is in the users operating system settings and if they have set dark as their preferred color scheme then we're going to make some changes to our custom variables so we're going to change in our route we'll take all of these here and these are the ones that we're going to change so we'll paste them down here fix that all right so our background 

[08:22] color we want it to be the opposite so we'll say black text color the same it's gonna be black text alt color will be white the opposite now L&R translate this is where we're changing the position of the image initially it's set to zero so in order to see the right side of the image we're gonna translate X a negative 100 V W the remember our image is set to 200 V W the first 100 which starts at 0 is going to be the 

[08:53] left side of the image and the second 100 on the right side so if we translate a negative 100 we're going to move the image 100 viewport widths to the left which will then show us the other side of the image all right and then we're going to change our header text to dark side so that's actually it for the code I'm going to pull up my operating system settings now you can see here that in my operating system I'm using Windows and I have it set to light if I change this to 

[09:23] dark you can see that our header text changed and the image moved to the right side of the image which is our dark side I'll change it back to left and it goes back to the light prefer dark so we're gonna leave it at that so in this example I'm not providing a toggle for the user to choose the theme I'm using what the user has already set in their preferences in their operating system settings if the user prefers dark themes then the site 

[09:55] will default to dark automatically this provides a great user experience so that's gonna be it for this video remember that I'm going to have two more videos that are going to show you alternate methods to implement theming look out for those very soon like this video to help me out and subscribe if you haven't already for more videos like this [Music] 
