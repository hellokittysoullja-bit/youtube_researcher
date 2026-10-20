# How Do You Design Accessible Filters for Cognitive Disabilities? - Web Accessibility For All
Ariel Ferro · 14 мин · 71 просмотров · en · https://youtu.be/9E6jKXq97mY



[00:01] Is blindness a barrier? no. Is deafness a barrier? No. Are mobility, learning, cognitive disabilities, speech impairments and others, or even a combination of them, barriers? No way. Lack of Accessibility IS! Welcome to Web Accessibility For All. Follow the blind! This journey starts now. 

[00:34] Let me take you back to a moment. I was helping a team, test an admin dashboard for a medical nonprofit. Real-world users, real-world stakes. A voluntary nurse, who was using a switch device and a screen reader, was trying to find patients with urgent appointments scheduled for the next day. She used the 

[01:07] filter drawer, toggled a few options and hit Apply... Nothing happened. Turned out the page had silently sorted by name, not by date. And the Urgent label was hidden inside a collapsed accordion section. She sighed: -Honestly, it feels like this app 

[01:38] considers I am the broken part here! That stucked with me, because when filtering, sorting or searching go wrong, it's not a UX glitch. It's exclusion And too often the people excluded are the ones with the most to gain from digital systems. Hey, my friend! Welcome back to Web Accessibility For All! i am Ariel, 

[02:10] your host, and today we're going to talk about one of the trickiest most misunderstood parts of the modern web. this episode is for the designers and developers ready to build search and filter features that everyone can use. Why filtering sorting and searching are accessibility minefields? Now, when we talk about web accessibility most folks think about screen readers 

[02:43] and color contrast. Maybe captions. Maybe keyboard access. But filtering sorting and searching? These rarely make the list, and yet they are everywhere. E-commerce. Government Dashboards. Health Portals. Learning Platforms. Banking apps. And here is the kicker! These features are critical 

[03:15] interaction points. If they break down for someone they don't just get frustrated. They get locked out of content they need, and it's not always the obvious disabilities that get hit the hardest. Neurodivergent users, when filters are inconsistent or overwhelming, users with motor impairments when 

[03:46] dropdowns are too tightly packed, or require fine tuned gestures. Users with cognitive challenges, when search results shift unpredictably or when filters apply silently. Common developer pitfalls: Pitfall 1, no clear labels or headings: You've seen this before. Sidebar with 10 

[04:16] filter options, all unlabeled checkboxes or toggles. To a screen reader user it sounds like: No context. No grouping. No clue what any of these filters do! And this affects everyone. A sighted user with 

[04:47] ADHD or cognitive fatigue may scan the page and bounce. Because there's no structure or clarity. Use headings to chunk filters into categories. Wrap groups in fieldset with legends, even if it's a visual drawer. Make the HTML meaningful. Let the structure reflect the 

[05:18] logic. Pitfall 2, filters auto applying with no feedback: Ah, yes! The magic interface where filters apply automagically without hitting a button. It's sleek, right? But here is what goes wrong: users with cognitive delays might not realize the page just changed. Screen 

[05:49] reader users may not know results updated, because there's no focus shift. If you're going to auto apply, give clear feedback; announce changes with polite area leave regions. Move focus to the results heading. Or better yet! Let users apply filters manually, so they are always in 

[06:20] control. Pitfall 3, unclear reset functionality: How often do you see a Clear Filters button that is barely visible? For users with executive function difficulties, or short-term memory challenges, this is a nightmare! They can't remember what they chose and can't figure out how to start 

[06:51] over. Always offer a Reset or Clear All function. Make it visible. Announce it. Clearly filtering sorting and searching aren't just UI conveniences; they are decision making tools. But when those tools go wrong, people don't just get confused. They get 

[07:24] excluded, overwhelmed. And this happens across disability types. Let's dive into real world problems with filtering, searching, and sorting. problem one filtering is often a puzzle not a tool filtering interfaces can feel like sudoku especially for users with cognitive or executive function disabilities too many choices filters 

[07:56] that interact in weird ways or unclear default states turn what should be a helpful refinement tool into a wall of options design tip make defaults visible show active filters in plain text and always give users an easy way to backtrack problem two searching doesn't mean understanding 

[08:27] search bars are treated like a silver bullet but for users with language processing issues dyslexia or memory impairments typing search term is not simple spelling errors phrasing differences or how to complete that is visually hard to scan all turn search into a frustrating guessing game and that's not even counting the people 

[08:59] who struggle with the search results if your results are sorted in confusing ways or inconsistent in format users have to read everything just to figure out what's relevant. That's a huge cognitive load. Design Tip: offer filterable results after search. Highlight search terms and 

[09:29] structure results with clear hierarchy and headings. Problem 3 - sorting could be a cognitive mess: Let's talk about tables. Oh, boy! You add sort buttons. Great! But, does the sort apply to one column or multiple? What if the table is paginated? What happens if two rows are 

[09:59] identical in the primary column? How do users know what the current sort order is? This becomes a minefield for everyone. But especially screen reader users, those with attention disorders who lose track of data patterns, and mobile users who can't even see the whole table. Design Tip: Always announce sort order 

[10:31] changes. Let users clear all sorts easily. Indicate current sort visually and programmatically. And test sorting logic for edge cases. Cognitive challenges: Now let's talk about invisible friction. if you are neurodivergent, have brain fog, or experience cognitive fatigue from chronic illness, then every ambiguous 

[11:05] label, every unpredictable result, every tiny font rapid visual shift, takes a toll. Examples: sort dropdowns that reset on every new search. Filter options that don't match the terms in the data. Interfaces where nothing tells you how many results your search returned, so you don't know if it is 

[11:35] working or not. For some people, the ambiguity causes stress. For others it causes shutdown. Either way it means loss of access. Reduce ambiguity. echo back the user action. -showing 24 results for hiking boots size10. Let users Undo a sort or filter without 

[12:08] starting over. And test your interface with real users who think differently. Wrapping up: Accessibility isn't just about labeling things right. It's about agency. Can users do what they need to do in the way that makes the most sense for them? Can they recover from mistakes without starting over? Can they move at their own pace using their preferred input method? 

[12:41] Filtering, sorting and search often fail not because they are hard to use, but because they are rigid! We want to reduce clicks, But people needs space to think. We want instant results, but some users need clear checkpoints. We want minimal UIs, but clarity and affordance matter more than clean lines. This is the shift we need. 

[13:20] Thanks for listening to Web Accessibility For All! If this helps you, please like, subscribe and spread the word! Build with care, design with heart. Web accessibility is for everyone That includes you. Goodbye. Thanks for joining us today. Subscribe for a new challenge next week. And don't be shy. Leave us a review or ask your accessibility questions online. 

[13:52] See you next week for another episode of Web Accessibility For All! 
