# Advanced Haptics: The when, what, and how of new haptic APIs (Android Dev Summit '19)
Android Developers · 5 мин · 8952 просмотров · en · https://youtu.be/00jRoEFnpk8



[00:00] [Music] hi everyone my name is Claire I'm Tyler today we're going to talk about advanced haptics api including when to use what to use and how to use so you want to add haptic effects for your app and you found these two constants class haptic feedback constants and vibration effect but you may still have questions like so what's the difference between these two or what should I use for my app we are 

[00:31] here to answer your question first if you're working on very specific UI element with specific input event such as keyboard for typing or button for clicking then haptic feedback constants is a good place to start assuming that you're working on button then it comes with a click event then just remember one thing the reason that you want to have haptic feedback for click event is in general to simulate the behavior of 

[01:03] the physical heart button which mostly come with a pairwise interaction model of pressing and releasing just remember the pairwise interaction of press and release and go find your haptic constants for example for keyboard you can find keyboard press and keyboard release effect for any other clickable element you can also find another pair such as virtual key and virtual key release then what about gesture haptic for juster is usually happening like dual 

[01:33] fashion while I apply my gesture I want to feel haptic we call this types of effect as haptic texture haptic texture is recommended to be subtle yet crisp because it has to be repeated very quickly so think about the clock app along the clock UI you want to apply gesture your set time to set time and then you want to deliver haptic texture to represent the virtual tick mark under your finger similarly when you drag the 

[02:04] blue text handler in the text view left and right when the selected area is changing by letter or word you want to deliver haptic texture to represent the change to support these types of interaction we predefined constants call clock tick and text handle move so now assuming that you know which constants to use in this case virtual key and virtual key release then the next step is to call those constants by perform haptic feedback and you're good to go 

[02:35] now there's another API the vibration effect API and that's through the vibrator service and this API you want to use when you care more about like the strength of the haptic happening rather than more the semantic meaning or like the gesture involved with it the other advantage to this API is you can use it without a view so haptic feedback constants require a view but this you can call on a background service you 

[03:05] know in case you're trying to notify the user without a UI so the basic starting in haptic we have is effect click this is kind of a medium strength haptic very crisp nice feeling on modern devices so we recommend you use that if you want a lighter haptic feel you can use effect tic and for a stronger more intense haptic you can use effect heavy click there's also effect double-click which 

[03:37] is just two clicks one after another and using this is pretty easy you just call vibration effect create pre-baked and then you pass it the constant of the effect you want to use there's also a way that you can define your own custom waveform and this is - if you want to create your own like custom haptic but it's pretty cool so in this example we have basically a waveform that looks you 

[04:09] see this image down here that's kind of what we're trying to make but basically you pass this function create wave form an array of timings and array of amplitudes so we're gonna start out with a full strength vibration which is amplitude of 255 for 100 milliseconds and then we're going to pause for 200 milliseconds that's the amplitude of 0 and then we're going to do a half strength vibration for 300 

[04:41] milliseconds so you can see that in these arrays and you get what's down in the corner there if you want to feel these for yourself on a new pixel 4 come find us upstairs in the afternoon we have demo app you can try out all the constants and make your own waveforms and if you have any questions or feature requests for future haptics please come talk to us as well thank you [Applause] [Music] 

[05:19] you [Music] 
