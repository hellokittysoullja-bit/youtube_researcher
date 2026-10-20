# How to test for Color Contrast | TPGI & WebAIM | WCAG
The Accessibility Guy · 6 мин · 9271 просмотров · en · https://youtu.be/D8TPUqbhRmA



[00:00] Today we're going to be learning all about color contrast and how exactly to test for it in whatever authoring environment you are in. Welcome to the Accessibility Guy channel. My name is Shawn Jordison and thank you for joining me today, under WCAG, there are a couple of different levels of conformance. For level double A, there is a minimum contrast ratio of 4.5 to one. And for large texts 18 Point and above, there's a color 

[00:31] contrast ratio requirement of three to one. Now sometimes it can be a little confusing to keep track of the actual standards, so I highly recommend downloading a free color contrast checking tool, and today we're gonna go over two of them. The first is called the color contrast analyzer tool from TP Gi. I will provide a link in the description below if you want to download this tool. But before we dive in, please 

[01:01] take a second to hit that like and subscribe button. Now what's great about this tool is it has the WCAG 2.1 standards at the bottom of the tester when we have text that is black fonts on a white background, we have the highest contrast ratio of 21 to one. And what we're going to do is just test a couple of colors. The first thing I'm going to do is using the Eyedropper tool on the foreground color or font color, I'm going to select the 

[01:33] color I want to test. In this case, I'm going to test the gray font. Sometimes this tool can be a little touchy, and I needed to resize my windows. With that said, this gray font passes are one point 4.3 Or one point 4.6. And our 1.4 point 11 We have a seven to one contrast ratio. That is perfect. Something that's interesting about color contrast is typically it also applies to non text content. So in this example, let's test this 

[02:04] blue bullets that I use in my presentation, I'm going to select that color. And in my sample preview box, I'm just visually comparing that it's the same color. And this actually fails all of our color contrast requirements. What if I made my title, maybe this green color that's built into Microsoft PowerPoint, what I'm going to do is use the eyedropper tool and test this green color. And currently it has a ratio of 2.1 

[02:34] to one, which is a failure under double A and triple A requirements. But what if I were to highlight that color in black, let's change the background color from white to black, and ensure that our sample preview is correct. And it now passes our color contrast requirements. So sometimes you can apply a highlight to the background in order for it to pass color contrast requirements. Though, if it were me, I would rather just keep the color black and keep things 

[03:08] simple. Now there's some pretty cool things we can do. Using the color contrast analyzer. Let's go back and test these colors again. And I'm going to select this slider option in the foreground color. And I'm going to select this box called synchronized color values. And what I can do is actually actually drag this slider. And I'm visually looking at the sample preview below. And what this does is it allows me to 

[03:38] find a color of green that's very similar, but that passes double A and triple A compliance. So if I keep sliding my color, we now have a new hex color we can use to replace our font color within our PowerPoint. So that is a brief over overview of the color contrast analyzer tool. I also want to show you the web aim color contrast checker. This works very similar to our other tool. Essentially, we can come in here, use an eyedropper tool and test in a very similar way. 

[04:12] And it automatically updates to where we have a contrast ratio of 2.05 to one which fails under normal text, large text and graphical objects and user interface components. So it fails under all of these things. Again, we can use the slider to move to different shades of that same green and then take this color and come back to our PowerPoint to actually update the color to a passing color contrast example. So I like to 

[04:43] use both of these tools. It just sort of depends on the project I'm working in. Sometimes the color contrast analyzer can be a little buggy depends Hang on where you are testing. And then similarly, the web aim tool is web based. And you kind of have to have a lot of screen real estate to be able to test properly. It's important to note that color contrast also applies to things like bar charts, and the labels that appear on this 

[05:14] content. Now, there's a whole section on color and meaning which I'll probably cover in another video. But it's important to test the values of the content inside of the bar charts. So let's go ahead and take this color picker. And we're going to take the blue fonts, and we can quickly determine that the white on this light blue font fails all of our color contrast requirements. Additionally, this color must pass against the background of the bar chart. In this 

[05:48] particular case, I applied a black border around the content, which is enough to make it past accessibility standards. In terms of it being a graphical object, however, that label needs to be a different color. And we would want to change it to probably black or have it highlighted black as in this example. So that concludes our brief demonstration on how to test for color contrast requirements. As always, I can 

[06:18] be your personal accessibility expert. And I want to thank you for joining me today and I hope to see you next time 
