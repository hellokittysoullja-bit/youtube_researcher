# 6. Design Login Activity For Chat Application
Suvidha J Malaviya · 14 мин · 145 просмотров · en · https://youtu.be/lwynqkyaq94



[00:00] [Music] hello guys today i am going to show you how to design the login screen and register screen for the chat app so first of all uh in the last video we are creating the button style and edit text style which is needed here as well as we are creating three icons inbuilt icons you can also use the icons which is downloaded for from the external sites and uh logo for research 

[00:31] so we are first creating the login activity uh open the login activity and change the layout as a scroll scroll view so that if the content is uh go is beyond the your mobile screen then also it is visible so uh um create a linear layout inside the scroll view and then give it match parent and match parent also give orientation as a vertical and close this deck 

[01:01] now inside this uh here we also give uh we are creating one image we are starting with image which is of 200 db we are attached source as a cat app logo here you can see that it draws inside the drawable folder chat app logo which we are using so see this one this logo is used inside this 

[01:32] so we give source as a drawable jet upload and here we are setting the gravity as a center so you can see the low is set to the center again we are setting gravity for this image you as a center so that this is visible in the center now we are creating the edit text that is edit text match parent that content we are setting 

[02:03] the hint for this one that is enter email uh this is we can use directly the text here but for the simplicity we are using the string.xml file here we are creating the string login english hint and paste this text here 

[02:36] and use this in a login activity so accurate string type name not type name login email it ah this is the not visible perfectly but it is here uh we are setting the background for this as a edit text style okay now you can see here our edit text is visible but it uh 

[03:06] is a very uh not shown perfectly so we are giving the padding when we are setting the external background into the edit text it cannot looks perfect without giving the padding to it so we are setting the padding is a 10 db you can see and it does look perfect but we have to give some padding margin into our parent layout so give the margin here as a 20 db or 10 db whichever you want now copy this okay 

[03:39] now we are starting the email icon which we are creating in the last video that is this one we are creating this email he said it edit text so yeah double left grabber email or you can directly write email icon uh you can see here icon is visible we can give uh durable padding so that the text is looks perfect so i am giving the 

[04:09] 5d padding for drawable and you can also change the input and uh it means colors of the drawable so use the drawable tint tag for this we are using primer in dark okay this looks perfect you can also give margin inside here that margin top so that the design looks perfect okay now copy this edit text and paste it you give here 

[04:41] id so that we can uniquely identify this added text in the code that is login email here we give login password okay here we are not using this string we are using here password hint which we are creating now okay copy this one and here 

[05:12] okay enter password okay now again go to the activity login you can see here it is visible enter password we are changing the drawable as a password icon okay rest of the things is perfect is not showing okay you can see here this is the password icon and this is our video okay now we are creating the button login button for this so use tech button 

[05:42] match parent and wrap content leave the text that is login now uh when you are using this one uh you cannot need a you have not need to uh manually add the this text to the string you can simply un alter enter here and extract string resource and you use the login underscore button and it is automatically added to the string.xml file you can see here 

[06:14] this will automatically added so now you can see button is created we are setting the background for this as button style which we are creating the creating in the last video you can set margin top as a 20 db and you have to change the text color as a color i sent and also you can change the size of the text as a text 

[06:44] size is it 20 dp okay now this is done now we have to create one label that is a forward password for that one you have to use the text view take match sorry match parent and wrap content we are using here match parent and rep content leave the text as a forward password 

[07:19] okay here give the id button id that is uniquely identifier that is login but okay here also give to id as a forget password okay now change the text color by using the text color as a color primary well we can color family dark uh no 

[07:52] we are using color primary not dark so it is visible perfectly okay now set the text alignment text alignment as a text end so that it is going to end okay here now we are creating a one text view so copies copy this text to you and paste it 

[08:25] and remove this id because this is not needed in this textview we simply uh giving the message that if you don't have the account then create a new account before that we are using that we can also login using the mobile number so for that we are creating the label that uh here or okay we are not using this here simply or robin says at all here we are not 

[08:55] using this color so go to the color.xml file and create one new color that is a gray dark grey so click here i'm using this one okay now go to the login activity and here give the color gray and text alignment as a center and give the text size that is uh let's say 18 db okay here also you can now 

[09:28] give the text to size as a 15 db okay and also here we are giving the text to style as a board so it is visible perfectly okay now copy this label again this and paste here and here new ideas create account 

[10:02] okay and here also we are using the create account string sorry enter enter this okay uh but before creating the account we commenting this code out we're using ctrl shift and slash 

[10:33] or login using the mobile number so we are creating one another next view that is here and here we are uh okay expand this frame and here we are using login using your mobile number login using your phone here we giving the color as a primary okay and uh 

[11:07] mold this text next style mold okay uh here we're doing 15 db so that is perfectly matched now again copy this button sorry copy this text view and paste it here and here you login using 

[11:38] mobile okay now give the string as a phone and extract this string okay here now we are setting the background for this as a button background okay and we are setting the padding here of mdp so this is perfectly shown okay we are setting the text color as a color dot ascent 

[12:09] this one and set the size which is 20 and text alignment as a center and set the drawable left which is sorry mobile okay and set the tint mode for the 

[12:39] drawable which is color ascent okay now uh commenting out this code by using ctrl shift and slash key and we are using this create account but before that we are adding the text to you this is great execute this this one copy this one and paste it here that is already have an account 

[13:11] for not having account okay and here give the marching top as a 20 db so that design looks perfect and then use this text when set this text alignment as a center and change the string as a create account but uh create a new account okay 

[13:47] okay now go to the activity see this one looks perfect now you can change the design according to your needs now i'm running this application you can see that the design of our login activities looks perfect 

[14:17] [Music] 
