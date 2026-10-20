# How to easily design 3 car effects thanks to haptics | Haptic Composer Tutorial
WYVRN · 12 мин · 341 просмотров · en · https://youtu.be/JqdN0paHLcE



[00:00] welcome to a new haptic composer tutorial we will see today how to design haptics for car sounds we will design a haptics for these sounds a burnout a car crash and a car engine 

[00:33] [Music] first of all remember to download the haptic composer from www.interhaptics.com you can download the asset used in this tutorial while downloading your samples let's start for a current we'll save it in our tutorial desktop and start the perception here which is a vibration and as usual we start for a sound to design our haptics let's import our audio 

[01:04] it's located and input a car engine we see the envelope of our of our our sound here so this is the imported sound [Music] let's extract our young haptics so at the beginning we have a rambly feeling of the engine and at the end we have that is accelerated goes away so and these days as we see this is our 

[01:37] extracted haptics so we have the transients the frequency and the amplitude let's check first our amplitude transient and hide the frequency so at the beginning we have this lower amplicity that we see relatively well here with the audio so this this speaks so it works really well to follow up with the with the haptics the audio at this stage because this uh wobbling failing is something that is very low frequency 

[02:08] and the user can really feel however our haptics motor have hard time to generate such a stronger such a strong feeling so one proposal is to recreate based on the envelope this kind of feeling and modulated with the existing frequency let's go here I will accelerate a little bit too help you to visualize the results after this stage we have the car which 

[02:40] drives away so we see here the envelope of the intensity of the of the of the sound our proposal to and use this as a guidelines to design uh to design the haptics because at this stage we are not representing any more the low frequency rambling feeling that you get while waiting for this massive engine to to develop but it's more like a a modulation of higher pitch frequency that help you to visualize these these 

[03:13] effects and there is also some related Fade Out haptic so the card is going away from you and the sound is getting a lower intensity a lower frequency and it it worked relatively well if we use the haptics with this Fade Out you see this amplitude going down let's check now the frequency the frequency at this stage we see well that our algorithms picked up a relatively low frequency at the beginning around 40 Hertz right yet this 

[03:44] picks up well this low frequency rambling so at the iPhone minimum is 60 but we can leave it at 40 and our algories will pick it up by itself and we see the frequency of the rest of the of the of the haptics that picks up and go higher as we were discussed before so to make it more um to make it more effective or at least more less uh confusing by the user uh you we can create a 

[04:14] and upwards frequency when we are accelerating out from the activity so we can go up here oh going here till around 350 Hertz and then slowly fading out by the time and reducing the frequency it works really well to convey this uh you know adopter effect of going away let's check now the transients in this case the tracks are picked up because they were a strong sound but there is no Associated event of shocks 

[04:46] so my suggestion would be to just remove the sun into the transit let's check it out how it is so we have a beginning rambling and dedicated uh modified amplitude let's save it so this is our uh see our haptics let's send it to the player to test it out to fee if you are happy okay now to test it out we can go to the second material because uh burnout let me save it let's go and add another vibration and 

[05:17] import the sound burnout feels like this okay we can see well on our envelope that we have an initial part with the low rambling but the key part of the interaction is the the wheels squeaking right let's see what our system does so our algorithms picked up really well 

[05:48] this um public speaking and the background vibration so let's go and edit it out so one thing about transient is that they tend to be they can be quite uh if you have to test it out straightforward it becomes quite frankly but at the at the usage of for this for this case what we wanted to um be sure that we are realigned is that we are enhancing what we are enhancing the first 

[06:20] um the first wave or the first hit of the sound so that our haptics is simulating this you know this small acceleration that you get when uh the the the wheel is squeaking and what you do don't want is to have the uh you have to translate all have the same hate otherwise what you picked up is basically the frequency so my suggestions this case are to enhance this physical interaction would be to determine a transient at each wavefront 

[06:53] here that you see really well we envelope the extraction that we have in our algorithms and modulate a little bit the the amplitudes to not to be picked up as you know as a frequency as a frequency modulation sorry as a continuous bit so we added transient over here and we make it relatively decrease over time so that we have this uh fading away effect so this you see that is really help us 

[07:25] time is really well so you can test it out to the app let's check now the amplitude the amplitude due to the fact that this is high frequency pitch the our amplitude extraction is more like on the low frequencies what we do want is to support this build up here of the of the car sound to initiate this uh Transit effect but during the transit we can leave it really low as it is we don't have to change anything and similarly when it fades away we can 

[07:56] help it out by giving the a small Fade Out we can even increase it a little bit to generate this Fade Out effect and we can save it let's check the frequency now the frequency what's going on with the frequency we are at uh quite high frequency at the beginning because the the noise is revving up that's a bit modulated by the sound on the transient we have the transient we take the ownership then it goes down let the under low frequency so I think we can leave it like this let's save it 

[08:26] Let's test it okay so we test it out it makes sense how it has been designed right now we go with the third haptic effect which is called car crash save it in the tutorial let's add a perception which is vibration and as well as checkout how how our haptics and sound looks like 

[08:57] let's hear the sound okay let's extract our haptics and sound and see how we can do it from there so we hear a sound having the first squeak and then the huge crash so from Happy point of view the the the squeezing and sliding doesn't have a lot of uh Associated uh expected feeling however the car crashes where we should 

[09:27] concentrate so let's go in our audio system at the beginning we have this transgender come from the squeaking let's remove the frequency first that we really don't want them because there is it it's sliding it's generating a lot of noise so the system picks it up but uh we are not really creating haptics effect however we should concentrate at this stage where our haptic crash happens we should concentrate the maximum of haptics here because this is the most impactful event during the whole haptics 

[09:59] interaction so we can add here transient to generated is this a strong effect that was Associated to the Sun and then we have some nice um sound of object which are colliding with the ground so at the end of the at the end of the of the sound we can go and enhance a little bit this vibration of effect which are rounding and generating a 

[10:29] little bit of active movements to create the impression of having the vibrations or at least the interaction with these objects so this is relatively fast and easy because at the beginning we have this overbearing sound we can leave the vibration as it is to follow a little bit the uh the sound and uh we can use this transient to generate this uh shock effect which is randomized and a bit following the the crash which is going on 

[11:01] we check now the frequency and go to the minimum frequency and the maximum frequency up so the frequency is as we see the sound is really high frequency at the beginning we can leave it as it is even if it's quite High the algorithm will normalize by itself so you're looking already high frequency during the car crash it's not because the frequency drops down and it follows this modulation again we can leave it as it is and then for the object colliding 

[11:32] we can leave it as it is a heretic feeling because the object colliding the biggest haptics Factor will be our amplitude that announces some of these some of these interactions so we can save it and go and send it to the player for testing okay so if you're happy with the haptic design we close it here and we remind you that you can recharge in our community and download all of the assets over our website where you can have some of these 

[12:02] assets which are already already designed and you can start from there to create your own experiences thanks for listening and see you next time 
