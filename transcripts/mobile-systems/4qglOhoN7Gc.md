# How To Test Color Contrast for Accessibility with #WebAIM
James Warnken · 11 мин · 5301 просмотров · en · https://youtu.be/4qglOhoN7Gc



[00:00] hello hello my name is James and today we are going to be talking about colors and color contrast and more specifically how do we make sure that our color contrast is at an accessible level so when it comes to color contrast and it being accessible the main groups or audiences were thinking about are people with low vision people like myself people with color blindness and just in terms of General usability color contrast is an important thing to keep 

[00:31] in mind to make sure that users can see the text and the user interface components on the screen especially on smaller screens and smaller devices when it comes to color contrasts and contrast ratios there's really two important ratios to keep in mind three to one and four point five to one three to one apply specifically to large text anything that is 18 points or larger or anything that is 14 points bold or larger as well as user interface 

[01:03] components like links buttons controls toggles check boxes form Fields so on and so forth when it comes to small text that would be anything below 18 points or 14 point bold and that ratio is going to be 4.5 to 1 because it's smaller so we need a little bit higher of a color contrast ratio since it's going to be smaller so these two ratios apply to the double a success criteria for the web content accessibility guidelines version 

[01:35] 2.1 and images of text are included but in general we want to typically stay away from images of text let's jump over and look at a few color combination examples and determine whether or not those are going to be accessible for these two different color contrast ratios so before we jump in and look at different color combinations and determine whether or not they are accessible this is a very good very 

[02:07] useful tool to figure out whether or not your color combinations are accessible and this is the contrast Checker by webbing so what this tool does is we plug in our foreground color our text color the color of our check boxes into the left hand side we plug in our background color or an adjacent color into the background color and it will actually calculate the ratio for us by default it's on a blue foreground color a white background color which gives us 

[02:38] a contrast ratio of 8.59 to 1 and we can actually scroll down and see for the double and AAA criteria whether or not that ratio passes or fails for the different success criteria so this 8.59 to 1 remembering we need three to one or four point five to one for the double delay criteria this would pass for small text large text and graphical objects in user interface components we can then scroll down and get a little bit of an 

[03:09] explanation as to what the different ratios are that we need typically we don't really ever go to a triple A level but again the higher the ratio is the higher the degree of contrast between the two colors will be so we can use this to evaluate our colors and figure out that ratio we do typically want it to be as high of a ratio as we can possibly get so let's look at a few different examples and see what their color contrast ratios 

[03:41] are yes okay so here we are inside of canva on the left screen we have the color contrast Checker by webaim on the right side of the screen and we're going to walk through a few examples and plug these in to see what ratios we get out of them so our first ratio for the colors are going to be a blue background color with white text or white user interface components so all we need to do within the color contrast Checker is plug in our either RGB values our hex 

[04:14] values whatever color code you want to use I personally like to be a little bit more accurate so I will grab the eyedropper tool and just hover over my foreground color here which is white I'm going to click to confirm that selection you can see that it's updated the foreground color box on the contrast Checker we're going to do the same thing for the background color in this case it's going to be blue our ratio here is 8.13 to 1 so if we scroll down normal 

[04:46] text passes large text passes and graphical objects in user interface components pass so this would be an accessible color combination for the wcag double A standards if we scroll down and we look at white text on black I know there's a lot of controversy between dark backgrounds black on white white on black you're going to get the same ratio depending no matter if you plug it into the foreground color or the background color 

[05:17] so here our foreground color is staying white our background color is now black and we have a ratio of 21 to 1. so this is easily passing for everything this is the highest ratio that you can get and if we were to inverse this to make the background white and the foreground color black we would still have a 21 to 1 ratio this is the highest ratio that we can get it's probably the most common 

[05:47] color combination that we see on web pages as well so next I want to look at this orange on this darker blue color this is probably not a very common color combination that that's going to be used but if we check the foreground color as orange and the background color as this sort of bluish color we do get a 5.31 to 1 which does indeed pass for the double A criteria it would fail for the AAA but 

[06:20] in general we're going for double A conformance so it would pass for large text and graphical objects and user interface components this is a little bit surprising because it is a little bit difficult to read especially the small text but it does meet that 4.5 to 1 or greater contrast ratio so now let's look at the black text or black UI components on a red background and see what that gives us so our 

[06:50] foreground color is black our background color is going to be red and our ratio is 5.73 to 1. so this again passes for all three according to the double a standard when we get to this type of combination so now we have pink on white or sort of a purplish pink but if we were to plug that in as our foreground with white as our background nope 

[07:20] we can see that we get a 3.07 to 1. so for small text this is not going to be accessible for large text and graphical objects user interface components it is going to be accessible so we could use this for something like a heading 1 a heading two we could use it for our toggles our check boxes our links things like that but if the text is smaller than 14 point bold or 18 point regular we would not be using an accessible 

[07:51] color combination and we get that same thing but an even lower contrast ratio when we look at this sort of bluish light very light blue on white we actually get a 1.57 and this color combination would not be acceptable for any type of text or user interface component because it's again below that three to one or four point five to one so when we're looking at our own web pages our websites we can pop into the 

[08:23] web aim contrast Checker grab our foreground color grab our background color and very quickly determine whether or not that combination is going to be accessible let's jump over to a website and take a look at it in real in a real life example so here we are on my personal website and a lot of the combinations I use are going to be either black and white gray and white some combination of those three colors so here I have a few 

[08:53] sentences down here underneath this picture of myself let's go ahead and see what this white on this charcoal gray gives us so we got white as our foreground we'll grab our background color and if we scroll down my ratio for this white on Gray is equal to 12.63 to 1 which is well above those minimum contrast ratio thresholds if we scroll down we have black on white 

[09:24] which we've already talked about is going to be our highest contrast ratio that we can get and I think those up we can check this sort of teal color over here on the gray which might be a little bit questionable so let's check it out um that text is a little bit small and hard to read or hard to grab the color for Rather so let's zoom in a little bit so we get a little bit more pixels so there we go 

[09:56] sometimes it can be a little bit tricky to get the right color but there we go our ratio is 5.97 to 1 for this sort of bluish teal on this dark charcoal gray which would indeed pass for large small and UI components at the Double a level but not for normal text at the AAA level so this color contrast ratio could be a little bit higher I could make this just a slightly 

[10:27] lighter shade and it would probably have a higher ratio but in this case it does pass those double A criteria so that is a quick sort of tutorial on how to check your own color combinations to figure out whether or not they are accessible we do want to be mindful of the sizes of our text again 18 point or above 14 point bold or above is considered to be large text anything below that would be normal text I hope 

[10:58] this video was helpful please let me know if you have any questions and I will see you in the next one 
