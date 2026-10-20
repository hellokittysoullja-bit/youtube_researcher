# A Study on Visual Perception of Light Field Content - Ailbhe Gill
IMVIP · 14 мин · 58 просмотров · en · https://youtu.be/Pr8RrT50ah4



[00:00] hi my name is alba gill and i'll be presenting my research on visual perception of light field content so our research focuses on the capture and analysis of visual attention of light field data and in this presentation i'll be going through the background motivation of our research the rendered light field data set how we collected our eye tracking data our results and finally our conclusion 

[00:30] so what are light builds these are light rays traveling within a 3d space captured using a light build camera examples of the lightweight camera are here so we have a camera within micro lens array we also can have a grid of cameras set up to capture the scene from different angles or a single camera moved around on a gantry to capture the scene at different angles and these can be stored as 2d images as vocal stacks which we use in our research or as 

[01:02] sheared perspective views so the shared perspective views are where each image captures the light rays of the scene approaching from different angles and the focal stack are slices of a light field focused at a sequence of jets so what's visual attention this is the subjective term describing perceived pertinent regions or elements of the scene which stand out in the same context so for example here on the image on the left we have some stationery in a pot and here on the right is an example of a 

[01:34] visual attention or saliency heat map which shows the probability of where people look when they view this image so here you can see that this area is highly salient compared to the rest of the image where could visuals saliency prediction in life fields be a benefit the higher dimensionality of light fields brings with their challenges for example when rendering light fields for displays this high dimensionality can make 

[02:04] rendering of light fields slow and so visual attention prediction could allow us to keep a high level of detail in important regions which we find to be highly salient and allow artifacts in less important regions this would mean that we could speed up live field rendering for displays and visual attention prediction could also be of benefit in areas such as quality assessment and compression of light fields 

[02:36] has been previous research into like field saliency and visual attention however we believe there are some shortfalls in previous live field visual attention research the ground truth in previous life of visual attention research is a binary map obtained by human segmentation of images as you can see here on the right the regions chosen may not encapsulate all visual attention they lack interpretability for eye fixation prediction they don't account for attention in the pre-attentive stage before people 

[03:07] recognize what they're seeing and they fail to capture all aspects of visual interest for example non-object regions such as text and this is why we have decided to make our own like field visual attention ground truth data set so we decided to collect our own visual attention data by first generating light field renderings that were representative of the 3d nature of light fields but for 2d display so first we created vocal 

[03:40] sleep renderings and we made videos 10 second videos displaying each slice of a focal stack in order one after the other and these simulated traversing is a 3d scene but for a 2d display so here in the front to back rendering the area of focus goes from foreground to background and for the back to front rendering the region of focus goes from the background to the foreground in order to compare our 

[04:11] ground truth results to previous light field visual attention ground shoots [Music] works we also generated a 10 second video displaying the all-in-focus image so this is where all areas of the light field are shown in focus we um also uh decided to have two region and focus videos um where we kept 

[04:43] they focus on only one plane for the entire 10 second video and these were one slice from the focal stack and these gave us an idea of how powerful the vocal cue was in directing visual attention compared to the other renderings we generated so how to choose a data set uh the light fields we chose were based on the following criteria they contained multiple regions or objects with high 

[05:14] color contrast they contained regions with great edge density and local contrast at various depths and spatial locations and they were required using different methods or camera types and some examples can be seen here below so how did we collect our eye fixation data we used the sr research ilink 1000 plus to collect user fixations we first showed the users all in focus videos to avoid first-time viewing bias we then had a calibration step we showed 

[05:45] the participants the full set of videos displayed in randomized order and we collected the eye fixation data of 21 participants for the five renderings of 20 light fields so we then used our collected eye fixation data to generate saliency maps so here you can see our five renderings of one of our light fields we had recorded for each participant eye fixation data these were then combined 

[06:17] and we used a gaussian with a sigma equal to one degree of visual angle and we generated a saliency map for each of the renderings over all participants we also generate and split the videos into two second intervals and calculated and generated saliency maps of each interval for all participants for each rendering for all light fields so here are some examples of the scan 

[06:48] paths of participants when they viewed each rendering so the scan paths show the path that the users took when they were viewing scene and areas in blue indicate the um start of the scene and areas in yellow indicate the end of the scene so if we look at the front and back and back to front renderings we can see there's clusters of similar colours so this shows that many of the users followed the same path when they were viewing the scene 

[07:20] and we can also see for these that the path of focus was going from foreground to background and it shows that this was where users followed so they followed the path of focus while watching the video we can also see for the region one and region two examples that many of the users tended to um look at the regions that were in focus more often than the regions that were out of focus 

[07:51] and we can also see for the own focus renderings that there's lots of dispersion which would indicate that the viewers looked all around the scene we can also see in these examples that there was not a clear path of focus so the yeah the user the users didn't follow the same path to focus um as much as they did in the focal sweep renderings so here we have an example of the saliency maps generated 

[08:22] for each of the five renderings over the entire 10 second video over all participants you can see here in the on focus rendering and the saliency map generated from it that users look at the entire scene and that the salient map is more dispersed than some of the others you can also see in the region one and region two saliency maps that there's um 

[08:54] greater saliency in the regions that were in focus you can also see in front and back and back to front rendering in this example that there's kind of a line down the center and that suggests to us that there's some center bias and that uses are yeah staying in the center more often than the sides and possibly following the line of focus 

[09:26] so this is another example of a saliency map generated over the entire 10 second video and here we can see that the this building on the left is in the foreground this building on the right is in the mid ground and this building here is in the background so if we look at the front to back and back to front renderings we can see that there's some areas such 

[09:57] as here that are not present in the all-in-focus rendering and this is an example of why we think that um just using all-in-focus renderings for ground truth does not give a full representation of the salient regions present in a light field so here's an example of temporal saliency maps where we split the 10 second video into two second segments 

[10:28] and found the um and generated our saliency maps on each segment for all the participants so here for the couch light field we have temporal savings to maps of the front to back and all in focus renderings so here in the front to back rendering the line of focus goes from foreground to background and the saliency maps over the 10 second video revealed that 

[11:02] participants tend to um to look at regions that are in focus and move to the objects of the scene as they come into focus so then also in the all in focus we can see that there's many more regions that appear to be salient and we we think that the all-in-focus um rendering gives us a 

[11:35] very good idea of the areas that are salient when you take the focus queue out of consideration so here's another example of temporal saliency maps for the taro small light field so here we have the region in focus rendering and we can see here that this is the area that is in focus um throughout the entire 10 second video but if we look at the saliency maps 

[12:06] generated we can see that yes this region in focus has salient regions we can also see that this object here um is also showing up as a place viewers look although it is not in the region in focus and when we look at the on focus rendering for this light field we can see that this center object is the main salient region throughout the 10 second video and this indicates that if an 

[12:36] area is highly salient in the all-in-focus rendering then it is often also salient in the other renderings even when it is not an area in focus so we wanted to see if the dispersion we were seeing in the saliency maps of the all focus renderings um could be quantitatively observed so we did this by calculating the entropy of fixation maps we created 

[13:07] which indicate a one if there was a fixation and a zero if there was not a fixation um and we did this for all the renderings of all the light fields um averaged over the observations of participants of all participants and we found from this that the average entropy of the all in focus rendering was higher than the other renderings and this was confirmed with a two-tailed 

[13:38] t-test that the on-focus result was significantly different to the others and this higher entropy suggests a greater randomness in the data so what did our findings reveal well the saliency maps that we generated give an insight into where user fixates when showing different light field renderings we also reveals with our findings that using segmented objects of all focus renderings as ground truth doesn't fully capture 

[14:08] visual attention of light fields so salient information not present in all-in-focus renderings was revealed by saliency maps of vocal sweep renderings more dispersion was found in all-in-focus renderings and vocally varying renderings and we also observed that fuhrer did not only viewers did not only fixate on objects but on other non-object regions so finally our research output was fixation data captured for different light field renderings and saliency maps that depict the 

[14:39] likelihood of eye fixation for use in eye fixation prediction and we also showed the limitations of the ground truth of other light fields saliency research thank you for listening and below is our research webpage 
