# How to activate Haptic Feedback on Tabbar Item
Aryaa SK Coding · 5 мин · 985 просмотров · en · https://youtu.be/jswe4ubqE5o



[00:01] hey guys welcome back to another uh swift tutorial so this is where i'm going to be explaining how to detect when a tabber button has been clicked and um one of my viewers asked how to activate how to feedback when it's clicked so i'll show you guys how to do that and yeah it's just gonna be showing you guys how to detect when a tab up button has been clicked and uh what you can draw those on so let me just call this a tab click demo all right i'll just create it there 

[00:33] and okay so what we're going to do first is i'm just going to create the tab bar so if i just go here and tab controller we can add that in here and now we can just replace this first item with view controller and i'll just attach this like this control drag and relationship segment i'll just move that over there and also i will change this image so it actually looks like an image so let's just have a 

[01:04] pencil this one i'm going to say view one oh oops that was the wrong thing this is the title view one and for this i'll just have a view too i don't have a trash can i always use the same sort of symbols and i just have a different uh background color for each so for this one i'll have like teal okay so now if i run this this should be our basic tab bar setup 

[01:35] and now i'll show you guys how to detect when a button is clicked so oh let's make this initial so this isn't actually going to be uh for each individual view controller it's just going to be in the actual tab bus so you can only do generic operations but it'll still be quite useful so now to show you guys how to detect when it's clicked first i'm going to do is going to create a new file in this so click new file and click touch first and make sure it's subclass of your tabber and i'm just 

[02:06] going to call this a haptic actually i'll just call this um tabar class but you can name that anything you want click create i'm just going to drag this in over here so now what i can do is first i'm just going to delete all of this this so you can see this is basically like a normal class except for tab bar and i'm going to attach this to this table which we have here so make sure you have the same thing tab bar class you see it appear there and 

[02:37] now we can start coding here so we need to do is we need to import the delegate so ui tab controller delegate and then interview did load we set that self so self.delegate is equal to self and now that you've done that all you actually have to do now after this is you just type in did select and you see there's two and you want to go for the second option i mean it doesn't really matter but the second option actually gives you the view 

[03:08] controller so it's more useful and now what you can do is if i just print uh items selected then we should just get this printed every time we click on an item in the tab bar so click that click that and you can see it keeps saying item selected so if i click it again there's another one and yeah so that's how you detect when it's selected and you also get the view controller so you can't really do much with this but you do know which one it 

[03:38] is and yeah now my view asked uh how would i perhaps feedback in this so what you do is you can see it's detecting every time so we can do is i'm just going to print feedback and what we have to do is just use normal haptic feedback code so let generator this is equal to ui impact feedback generator oh i type image your impact feedback 

[04:09] generator just select any style here so i'm just going to go with let's just say medium it doesn't really matter and then you just do generator dot impact occurred and this should create haptic feedback so on obviously i'm not really going to feel anything but you can see it's activating here click again the third one activates and click again you can just see it's adding on and every time that adds on some more 

[04:39] haptic feedback has been pressed so yeah this is how you do it first you create the class here and then you just link it up you connect it to your tab bar and then you can just see we did nothing in the view controller it's all in the tabber and then in did select function we just do the haptic feedback so yeah thanks for watching and i'll see you guys in the future tutorial bye 
