# Mastering Outsystems UI #2:  Creating Dynamic Screens with Checkbox Widget In Outsystems.
Lowcademy · 5 мин · 1622 просмотров · en · https://youtu.be/HkwRrqFgYs4



[00:02] hi guys in this lecture we will talk about check box I believe you might have seen the checkbox before as well whenever we fill any form on the web we get a option right just accept the terms and conditions so we get a checkbox there generally we accept that so this is the bootstrap website and we'll have just opened this website to show you if we have to design um something using the HTML how we will Design what code will require to write so for the check box this is the checkbox side will require to write this 

[00:34] particular line This input Class Type checkbox will require to write right and we'll give an ID if we'll just bet the value by this ID in the JavaScript or jQuery code will get true or false if it will be checked we will get true if if it will not be checked it will get the false so let's see if we have to design a checkbox using out systems how we can do so this is my outsystem service Studio I 

[01:05] have already created one application created one module and created one screen as well this is my screen this is the checkbox widget that is that is available under the screen uh widget toolbar toolbox so this is the checkbox widget I will just drag and drop let's talk about the properties name name is simply name and ID of the checkbox so when outsystems compile this code this name will be converted as the ID you see this ID it 

[01:38] will be um the the ID the name will be Associated to the ID of checkbox variable so this will be a Boolean type variable don't forget it it will be a Boolean data type variable whenever we'll select so if it will if the checkbox will will be checked the pro value will be assigned to this particular variable whatever we will Define here if it will be unchecked the false value will be um just 

[02:08] um set here automatically enable true and false if it is enabled it will be enabled if it is false it will be disabled user will not be able to perform any action style class simple this is Style by default it is check box here we have form check input because this style class is associated to the bootstrap CSS outsystem has written its own CSS side so as per the outsystem CSS we have a checkbox class if you want to 

[02:38] apply more classes we can add the classes here attributes I have already shown we can Define data or any other attribute on change if you want to perform any action when user perform the check and check operation we can handle this on on change event we can call anything whatever we want we can go anywhere else we can redirect to the another URL we can call any action and apart from on change if we have to perform another action on specific event 

[03:08] for example when on Builder on click on focus on key press on key up on touch start action event triggered what we want to do we can handle that inside the action what we Define here so what I will do I will just select this and on change event I will just show what user has selected in a form of message so we'll require a variable obviously it is giving the same error you can see the error as well the 

[03:39] variable must be set so right click and add a variable and check box value check box value it will be a Boolean it type of variable not the text so just give a description check box value and it will be a Boolean type of variable we'll just go here I have just clicked and we'll just set the variable checkbox value now on change event will handle that is not a mandatory event only with link and button we get the um on click event as a mandatory so 

[04:11] every time we have to handle that what needs to be performed when user clicked on the button but for this checkbox it is not mandatory if you want to handle we can so once we handle this uh on click event it automatically create the action and here I can just show the value in the message I can show the value of checkbox so let me just show you it is not giving a suggestion because in general message this message except a 

[04:41] text variable or a text expression we don't have any text variable available that's why it is not giving us suggestion but we can select rate under expression editor click here like open expectator that is under the scope we can click here now it will give true or false whatever you select so let's have a look okay then let me open so I will just what I have done I have just clicked on this open in browser and it will open the application for me 

[05:14] so you see this is my personal URL so when you will click there it will redirect you to your personal environment URL okay if I click it is giving me true false true false true falter false So based on this checkbox click uncheck event or uncheck value we can we can do anything we can hide something show something or we can just perform any action as per our requirement right 

[05:44] so that's it it was just a simple use case how we can use the checkbox and what is the properties of checkbox widget that's it yes that's it for this that's it thanks for watching 
