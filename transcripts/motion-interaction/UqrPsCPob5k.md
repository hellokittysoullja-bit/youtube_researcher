# How to integrate haptics in XR with the Interhaptics SDK
WYVRN · 8 мин · 440 просмотров · en · https://youtu.be/UqrPsCPob5k



[00:00] hello from interactive in this tutorial we will go step by step creating an XR project in unity for The Meta Quest for time considerations we will cut the loading asset part which can take quite long while keeping the same steps as when creating a project from A to Z I have chosen the VR core sample so we'll have most of the packages including the XR plugin manager and its main headset Integrations already installed in the project 

[00:32] we will put Oculus instead of open XR for both desktop and Android then switch the platform to Android afterwards we open the package manager to add the interactive score SDK package which you can get simply by copying the GitHub address from this video be careful at the same time not to have an extra Blank Space when copying the address otherwise you might have an error 

[01:04] we can see that we have an XR sample scene which has multiple 3D cubes with different haptic sources for example haptic spatial Source event haptic source audio haptic source and a special implementation made for XR controllers like The Meta Quest we will not delve deep into this sample scene which can be directly played on your quest headset once the interactive SDK package is imported as we'll recreate and explain most of 

[01:36] its features in a new scene so without further Ado let's create a new scene from the samples in XR we'll just copy paste the XR rig in the previous scene which contains already the basic blocks from the unity XR system the main camera and controllers and also the haptic body parts from the interactive score SDK package 

[02:09] as you can see these are tailored for The Meta plus 2 controllers but the collider can be changed to other controllers from meta like The Meta Quest Pro controllers next we'll add the haptic manager which is an empty game object in which we add the haptic manager script which controls the haptic 

[02:39] supports thank you next we'll add the haptic game objects we'll create the first one to contain a spatial haptic source we can add it like a normal component from the inspector panel or from the component interactive spatial haptic source 

[03:12] as you can see the script has added a rigid body component and it needs a haptic material which we can directly drag and drop from the haptic materials library inside the entirety score SDK I choose a haptic material and activate debug mode to receive console messages on Twitter slash Collision enter and exit 

[03:43] of course we set the haptic source to start on trigger enter so we have to have only one Trigger or origin and that's it next we create a new Cube and for this one we'll add an event haptic source which we can add the same way to the game object 

[04:24] for this one as well we can assign a haptic material from the haptic materials folder foreign for which we will have an event in which the piece or shot is triggered only on the right meta controller here we have to add the haptic body 

[04:56] parts so we'll add only the right controller which contains the haptic body parts for the right hand thank you we just drag and drop it from the xrp normally we should have something like a script which tells us when to call this event haptic source we will use in this case an already 

[05:26] existing basic script with ontrigger enter in which the event haptic source is played with a delay of two seconds thank you and finally we will create a new Cube and on this one we will add an audio haptic source 

[06:01] as you can see adding the oh you have the source adds an audio source to the game object thank you we will choose one of the sounds from The Sounds Library corresponding to the haptic materials Library so this one is snare buildup we uncheck play on awake on the audio source and next we have to choose the haptic 

[06:33] material corresponding to the sound as you might already know the haptic composer has the ability to create haptic materials directly from sound with the Press of just one button this audio haptic Source can be played on a way if we check this variable in the component or we can add on already existing basic script which will just play and stop the audio haptic 

[07:04] Source on events you have already seen that I have added both controls to play When the audio haptic source is called thank you this is the existing basic script and if one trigger as it is commanded out audio and haptics will continue playing 

[07:35] Even After exiting the trigger foreign as we finish setting up the haptics on this XR game object in the scene we can just hit play and try the septic 

[08:05] Sensations added to the the VRC which will and surely enrich your immersive experiences for any other feedback or information we are available at interactives.com and on our Discord in which you can Jump Right In following the links in the video description thank you for following this XR haptics tutorial and we are waiting for you on this YouTube channel for other tutorials in the weeks to come 
