# Fast idle animation technique in Blender
Pierrick Picaut · 16 мин · 262904 просмотров · en · https://youtu.be/OkhcLqjamqg



[00:00] hi everyone this is perry from p2 design in this video i will show you the method i've used to create this idle animation in less than 20 minutes [Music] once we have created a strong pose we will only manually animate the center of gravity of our character then we will use space switching to animate the other features of the body stay till the end of the video i have a little surprise 

[00:30] for you the first thing we need to do is to build our base pose you will generally create this kind of idle animation for your game animation and as for any other kind of animation it's super important to take in account the point of view in this example i like to go for a fighting game style point of view so i will position my camera in front of the character slightly beneath its shoulder line if you are working on 

[01:01] a moba platformer etc the point of view will be very different what i advise you is to create a specific layout to check your animation from point of views that you may have in your game when i'm working on noira i have a specific layout that allows me to see my character through different angles available in the game you can easily create a new layout by clicking the little plus icon and then customize your windows setup once your point of 

[01:33] view is set up it's time to go ahead with the posing of your character create a strong and appealing pose is not in itself and you should always try to find references using pinterest for example i also advise you to have a big mirror in the room you are working or to take pictures of yourself to create your own references as you act the pose you will feel the different point of forces in your body and that's super important to 

[02:05] progress as an animator i've made a whole chapter about the art of posing and exercises in my blender animation course alive take the time to create a strong and appealing pose and make sure to check the following points first make sure that you have a clear silhouette this one is decent i've made it quite rapidly but maybe i should do something with the spear so that it doesn't overlap with the head the second point is to have a clear line of action in 

[02:37] this case my character is leaning forward ready to strike with his weight on his rear foot his whole body is pointing toward the attack the secondary line of action all supports the anticipation and we clearly understand the threat of the spear your character needs to be balanced make sure his center of gravity or cog is in between the feet when you draw a straight line from the center of gravity to the ground 

[03:07] finally make sure that the secondary features of his body communicate his will like the orientation of the eyes or the tension in the left hand ready to parry any attack i should polish more the pose but for this example it's gonna be okay let's animate this creating our base animation is going to be super simple i'm duplicating the current pose onto frame 30 assuming that the up and down cycle of the character is going to be one 

[03:39] second animating at 30 frames per second from there i will select the center of gravity of my character or torso root go on frame 15 and lower his body i will then check the animation and see if it's too slow or too fast it's a bit too slow for my taste so what i will do is that i will move those keys to frame 12 and make the cycle on 24 frames i will set the frame 23 as being the end of the 

[04:10] animation so that i can see the proper cycle in blender now the result is more pleasing to me so i will jump into the graph editor i will press ctrl tab in the action editor to switch to the graph editor select my torso root controller and i will add all the curves but the location curve i will zoom on my curve select all the control point of the z curve and i will scale them the idea is to bring a bit of contrast into our spacing to make 

[04:42] sure i can scale all the handles individually i will switch to individual points as i scale up those control points the curve creates some kind of plateau on the down pose and the up pose and so the character will hold a bit more those poses so this is our base up and down motion now i need to repeat it twice because there will be the up and down but also the back and forth motion i 

[05:13] will simply select the keys on frame 24 and duplicate them on frame 48 and then i will duplicate my keys on the up and down rz location curve and offset them so that it repeats twice upon those 48 frames now i want a more bouncy cycle so i will reduce the scale of the lower control point so that it doesn't hold the pose down and i will scale up the up pause 

[05:45] controller point so that he hold the pose up a little longer and now we have a more appealing reason in the up and down motion for the back and forth motion it's gonna be a bit of the same process but this time i will directly edit my curve so whenever the character is going down i will pull him back and when he's going down on the second cycle i will push him forward and i make sure that the first and last keys are aligned so that i have 

[06:18] a seamless cycle from there what i will do is that i will select all my keys duplicate them and offset them by 48 frames the whole cycle and i will play with the position of all my x location curve so that i can offset a bit this animation in time from there i can play my animation and move the curves from left to right and see how my character behaves until i get a satisfying result in the end i've 

[06:49] created a two frame offset now i will go on frame 48 and add a new keyframe i will press v to change the handle type to free and i will duplicate this key on frame 0 so that i have the same key on frame 0 and frame 48 since i've set the handle to 3 removing the surrounding keys won't change the curvature of our curve here there is a little problem as i have keyed the frame 47 but i have 

[07:21] fixed the issue of camera from there feel free to add a bit of motion on the y-axis now let's jump in the fun part animating the rest of the body with space switching if you want to learn character creation rigging and animation and take your skill to a professional level you will find extensive interpreted blender courses on p2design.com hundreds of professionally edited videos shipped with all the models rig and 

[07:51] blender files use the code p2 design you will now get 10 images any of the crosses we are going to animate all the remaining parts of the body using space switching i will try to go through it pretty quickly but if you want a more in-depth introduction to space switching check out this video the first thing we need is an empty so i've switched to object mode i will press shift a and add an empty plane axe and we need this empty to copy the 

[08:22] motion of the chest controller to do so i will go to the constraint and use a copy transform constraint i will source my character rig and source the chest bone now the empty follow the motion of the chest bone to do so i will press f3 and search for bake i will choose bake action i will use visual cane only selected bones or object clear the constraint and overwrite current action 

[08:53] by default blender will set the start and end frame as the start and end frame of your current animation range as i click ok our empty will lose its constraint but it will still be visually following the chest as it has created an animation that behaves in this manner the principle of space switching is to then constrain the chest with the previously constrained empty make sure that you use bone constraint 

[09:25] not object constraint and add a copy transform and source dmt now nothing's happen visually because the chest is following dmt that was following the chest previously but if i move the empty we can see the chest moving so now the trick is to select all the curve from the empty press shift e and add a cyclic modifier now if i play the animation and slightly offset in time all the curves from the empty i will see 

[09:57] the chest starting to bounce there is a little glitch because i've only keys on my empty curves i will simply duplicate the very first key and move it on frame 48 so that i have my whole cycle and for the next baking i will make sure that i bake from frame 0 to frame 48. with two frames of offset i'm quite satisfied by the result but it's a bit 

[10:29] too strong now i can get back onto my bone and reduce the influence of the constraint and now i have the same timing but with a softer spacing let's now bring a bit of rotation into the chest to do so we are going to use aimspace with a dumped track constraint what i will do is that i will select my empty i will display its axis through the viewport display option and then i 

[10:59] will switch my transform orientation from global to local now the idea is to duplicate this empty along its z-axis because it's the axis that point forward whenever we are looking at the character now i want this empty to follow the motion of the first empty so i will add to it a child of constraint and source our original empty if i now play the animation the current empty will follow 

[11:29] our original empty i will now bake its action i've added the baking option to my quick favorite i will make sure that i bake 48 frames this time as before the constraints disappear but the object is still moving as it has created an animation i will now add a dump a track constraint to the first empty and i will target our new empty using the z-axis if i now move the second empty we can 

[12:00] see our original empty tracking it and influencing the chest of our character so as before i will select all the curve of the second empty press shift e and make them cyclic and i will offset them in time now the chest is both bouncing and also rotating a bit but it's a bit too subtle so i need to separate location and rotation on our chest to be able to 

[12:31] tweak those values i will get rid of the copy transform and instead add a copy location sourcing the first empty and the copy rotation sourcing also the first empty but now i can play with both influences with different values i can reduce the influence of the copy location to reduce the amplitude of the bouncing and then if i want to increase the rotation i can select the second empty offset it in time if i want or even 

[13:04] scale its up and down motion or z location curve to increase the rotation motion of the chest once we have a satisfying motion we can select the chest bone and bake its action make sure you bake over 48 frames and make sure to choose overwrite current action so that the current motion is baked upon your idle animation with those two mechanism we can cover all the 

[13:37] parts of the body of our character i will now show you another example with the shoulder where i will be only using copy location so i will constraint both my empties to each shoulder controllers and bake the action and then i will constraint each shoulder to an empty using a copy location constraint i will repeat the process on the left shoulder and then i will make sure that i offset 

[14:09] the animation of the empties and make it cyclic then using the influence i will make sure that the right shoulder has a little more bounce than the left shoulder because it's holding the spear that has some weight and i will also slightly delay the left shoulder so that i have a bit of difference in the bones of each shoulders from there i will show you last example with the arms where i do exactly the 

[14:42] same thing as we did with the chest i'm first baking the two empties to the arms and then i will create a target for each of those empties those targets will be a child of the previous empties i'm making them with a different shape so that it's easier to identify them and once their motion is baked i will use them as a target for a dumped truck constraint on the two other empties and those two other empties will add a 

[15:14] copy rotation constraint onto the arm controller you can use a copy transform constraint if i now offset the animation of those round empties it generates an overlapping motion of the arms of the character then as we did before i can play with the influence of the constraint or i can scale the curves of the spherical empties increasing the rotation of the arms and i can use those technique for the 

[15:45] different parts of the character i will use it on the hands on the spear on the head on the hips so you may find this a bit cumbersome or tidies and you are right but it's four times faster than doing it by hand at the very least and my friend finn is about to release his add-on the space switch toolkit that will automate all the process it has been in production for almost two years 

[16:16] and we've been testing it in production trust me this is going to be a must have for any animator with this method and the help of this addon i was able to do this animation in less than 30 minutes a fantastic process to prototype your animation and a fantastic addon to fix a lot of issues with complex mechanisms stay tuned as i will soon publish a full demo of the addon for its release in the meantime i salute 

[16:48] you and i will see you in the next video 
