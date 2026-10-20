# Making the Web Neurodivergent-Friendly   - Web Accessibility For All
Ariel Ferro · 15 мин · 81 просмотров · en · https://youtu.be/LtGBHMQkNog



[00:00] [Music] Is Blindness a barrier no is deafness a barrier no are Mobility learning cognitive disabilities speech impairments and others or even a combination of them barriers no way lack of accessibility is welcome to web accessibility for [Music] all follow the blind this journey Starts Now 

[00:30] [Music] close your eyes for the moment well unless you're driving or doing something risky now imagine the web not as a virtual space But as a b 

[01:09] City the websites are storefronts apps are cafes and search engines are street signs this city should feel welcoming inclusive and easy to navigate for all its visitors but for many the streets are confusing the signs are blurry and the noise is 

[01:47] overwhelming hello my friend welcome back to web accessibility for all the podcast where we break down the barriers of the digital world and build Bridges to inclusivity I am your host Ariel today we are diving into a topic that's not just about accessibility it's about understanding and designing for the diversity of human Minds we are talking about 

[02:20] neurodiversity if you are wondering what is neuro diversity or why should it matter to web developers designers and any anyone building digital spaces you are in the right place let's get to it setting the stage let's start with the definition neurodiversity is a concept that views neurological differences like autism 

[02:52] ADHD dyslexia and others not as deficits but as natural variation of the human brain according to research from the CDC Centers for Disease Control and prevention about 1 in 36 children is diagnosed with autism and nearly 5% of adults have ADHD that's a significant portion of your user base neurod diversion users often face challenges with interfaces 

[03:26] designed for neurotypical users this includes sensory overload complex navigation or even flashing elements that can trigger adverse reactions let's set the stage with an example imagine a busy e-commerce site loads of flashing ads out playing videos and popups for someone with 

[03:58] ADHD that's not just annoying it's paralyzing okay Ariel I get it but do these issues really impact that many people I mean can't they just adjust adjust ha if only it were that simple let me explain you know those helpful capcha tests for me as someone with dyslexia they're nightmares the text is blurry tilted it's like the sight is screaming you're not welcome 

[04:28] here waa I I never thought about it like that so what's the solution great question we'll get to that but let's first understand why these challenges exist historical context historically interfaces were built with the assumption that all users think process and interact in the same way this mindset ignored those with 

[05:00] cognitive disabilities or neurod diverent conditions for example in the early days of the internet websites were text heavy for someone with dyslexia that meant walls of text hard to read neurod Divergent conditions often involve differences in brain activity and processing for instance a person with hhd might struggle with tasks requiring 

[05:34] sustained attention studies from the National Institute of Mental Health confirm that excessive sensory input can overstimulate these regions leading to cognitive fatigue wcag and legal Frameworks let's talk about the rules or in this case their limitations the web content accessibility guidelines or weag has been instrumental in setting Global 

[06:07] accessibility standards however because weag focuses on testable success criteria it struggles to fully address the needs of neurod diverent users for example there is no specific criteria for reducing cognitive load such as simplifying complex navigation or eliminating unnecessary distractions guidelines like 

[06:41] 2.2.2 pause stop hide while helpful are only a partial solution for those who struggle with information overload or decision paralysis wait so you're saying wcag isn't enough exactly weag is a baseline not a blueprint for neurod Divergent accessibility yeah the guidelines are helpful but they don't really get at 

[07:11] what it feels like to use a chaotic site it's not just about stopping autoplay it's about having a space where my brain doesn't feel attacked great Point designers and developers need to think beyond the we Haag for instance incorporating user testing with with neurod diversion participants can uncover barriers that aren't addressed by the guidelines and let's not forget there are legal implications for ignoring 

[07:43] these broer needs while laws like the Ada reference weag they also emphasize the spirit of accessibility ensuring everyone can participate fully even if there are barriers aren't explicitly listed in wiag use cases and possible solutions all right it's time to bring Theory into practice let's explore some 

[08:13] common challenges faced by neurod diversion users and how we can address them case study one sensory overload Maya our neurod Divergent user visits a News website as the page loads a video starts out to playing adds flash on the sidebar and notifications pop up asking her to 

[08:44] subscribe she feels overwhelmed and leaves the site let's explore some possible solutions one disable autoplay videos use the muted and controls attributes on the video element avoid how to play by default check out how this is implemented in the following HTML code snippet less video controls muted 

[09:18] greater less Source SRC equals example. MP4 type equals video/ MP4 grater your browser does not support the video tag less slide greater two pause animations for users with motion sensitivity respect the prefers reduce motion media query to disable or simplify animations for users who have 

[09:48] motion preferences set use something like the following in your CSS style shets at Media Left pen prefers Das reduced Dash motion colon reduce right pen left brace star left brace animation colon nonone important semi transition colon nonone important semi right brace right brace three provide clear settings for notifications use JavaScript to allow 

[10:21] users to enable or disable notifications case study two simplify ified navigation Charlie who has ADHD struggles with websites that have complex multi-level navigation menus he finds it hard to focus and quickly loses track of where he is on the site so what can we do here provide clear simple 

[10:55] navigation that supports keyboard use and highlights the current location one use a skip link for quick access include a skip to content link as the first interactive element you can check the episode where I Cobo skip links in detail code included two highlight active navigation use CSS to visually indicate 

[11:27] the current page in the navigation bar and AR attributes like AR current page to do the same for screen reader users three keep menus keyboard friendly Implement JavaScript manage Focus within droptown manuals case study three dyslexia friendly fonts Maya who also has dyslexia struggles with reading the the 

[11:59] dance s serif fonts used on a popular website let's try the following one add a font switcher allow users to Tagle between regular and dyslexia friendly fonts you could try something like this in your main JavaScript code con toggle font equals left pen right pen equals greater left brace document body. class list. toggle left 

[12:31] pen dyslexia Das font right pen semi right brace semi blank document. query selector left pen font toggle right pen do add event listener left pen click toggle font right pen semi two use accessible fonts and styles Define a dyslexia friendly font in your 

[13:02] CSS body. dyslexia Das font left brace font Das family colon open dyslexic aial s- serif semi line- height colon 1.6 semi right brace blank slash ensure fallback if open dyslexic is unavailable slash at font-face left brace font Das family colon open dyslexic semi SRC colon URL left p/ fonts slopen 

[13:35] dyslexic d regular.ttf right pen format left pen true type right pen semi right brace three apply line spacing line spacing helps readability for dyslexic users you could try something like this P left brace margin - bottom colon 1.5 M semi line- height colon 1.6 semi right 

[14:07] brace final thoughts and resources designing for neurodiversity isn't just about compliance it's about inclusion when you design with diverse brains in mind you create better experiences for everyone if you're wondering where to start check out resources like the cognitive accessibility road map by w3c or the 

[14:39] athd accessibility design guidelines I'll include these links in the episode description and hey if this episode resonated with you share it the more people understand neurodiversity the more inclusive are digital world becomes thanks Ariel you know you just made me feel seen and heard same here I'm definitely rethinking how I approach 

[15:09] design as you can see solving these issues is about empathy and thoughtful design that's what this podcast is all about until next time keep building for everyone goodbye thanks for joining us today subscribe for a new challenge next week and don't be shy leave us a review or ask your accessibility questions online see you next week for another episode of web accessibility for all 

[15:45] [Music] 
