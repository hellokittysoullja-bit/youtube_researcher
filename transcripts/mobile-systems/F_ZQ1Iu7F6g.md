# Atomic Design 101: How to Build Systems That Actually Scale
Design Talk · 10 мин · 27 просмотров · en · https://youtu.be/F_ZQ1Iu7F6g



[00:00] When the internet first began, products and applications were viewed as nothing more than a collection of distinct pages, each with a distinct purpose and set of appropriate components. Nearly every screen would have distinctive characteristics, which led to the design being inconsistent and confusing. Therefore, design systems were introduced. Hello, my name is Max. Welcome to Design Talk. Just like the name, this channel will talk mostly 

[00:30] about UI, UX design. Don't forget to subscribe and turn on the notification to know more about product design. [Music] The process of developing a design system can be approached in a variety of ways. One of the approaches for structuring a design system that makes the lives of designers and developers easier and their processes significantly more effective is atomic design. Let me give you guys a quick review of 

[01:00] what atoms and all its process are. All matter is composed primarily of atoms. Each chemical element has unique features that cannot be further subdivided without losing their significance. Groups of two or more atoms bound together by chemical bonds are called molecules. These atomatom pairings become more real and functional than individual atoms and develop their own special features. Organisms are collections of molecules 

[01:31] that work as a single entity. A process called atomic design uses five separate steps to develop interface design systems in a more methodical and hierarchical way. one atom. If atoms are the fundamental building components of matter, then the atoms of our interfaces are the fundamental building blocks that constitute all of our user interfaces. These atoms contain fundamental HTML components such as form labels, inputs, 

[02:01] buttons, and others that cannot be broken down any further without losing functionality. Two, molecules. Molecules and interfaces are relatively basic collections of UI components that work together as a unit. A form label, search input, and button, for example, can be combined to produce a search form molecule. When these abstract atoms are united, they gain meaning. The input atom is now defined by the label atom. 

[02:33] The form is now submitted by clicking the button atom. Consequently, a basic portable and reusable component may be plugged in whenever search capability is required. As a result, building basic UI molecules facilitates testing, supports reusability, and promotes uniformity across the interface. Three, organisms. Organisms are rather sophisticated user interface components made up of groupings of molecules, 

[03:03] atoms, and or other organisms. These creatures create different interface parts. Organisms can be made up of similar or dissimilar molecular kinds. A header organism may have several features like as a logo image, principal navigation list, and search form. These creatures may be found on nearly every website we visit. From molecules to more complex species, designers and developers get a crucial sense of context. 

[03:35] Organisms show those smaller, simpler components in action and serve as separate patterns that may be repeated. Four, templates. Templates are page level objects that include components layout and express the underlying content structure of the design. To expand on our earlier example, we may use the organism heading then inserted into a homepage template. The fact that templates focus on the pages underlying content structure rather than the pages 

[04:07] final content is a significant feature because design systems must account for the dynamic nature of information. It's particularly useful to clarify crucial component attributes such as picture sizes and character lengths for headers and text sections. Last but not least, pages. Pages are special examples of templates that demonstrate how a UI appears with actual representational content in place. Continuing with our previous example, we 

[04:39] can take the homepage template and insert representative text, photos, and media to demonstrate genuine content in action. The page stage is the most definite level of atomic design, and it is critical for a variety of reasons. After all, this is what visitors to your experience will see and engage with. Your stakeholders will sign off on this. And it is at this point that all of those components come together to make a beautiful and functioning user 

[05:09] interface. Now that you know stages of atomic design, we will now talk about the advantages of using atomic design. One of the most significant advantages of atomic design is the capacity to instantly switch between abstract and concrete forms. We can see our interfaces stripped down to their atomic elements while also seeing how those pieces combine to generate our final experiences. Here are other benefits of using atomic 

[05:40] design. They enhance uniformity and continuity across the experience as well as speeding up your team's workflow, saving time and money. They provide a more collaborative workflow among all disciplines participating in a project. They create a common vocabulary for everyone in a company, including outside vendors. They give useful material to assist stakeholders, co-workers, and even third parties in their education. They help 

[06:10] with cross browser device performance and accessibility testing. They provide a futureproof framework for teams to change, expand, and build upon over time. Atomic design gives us a structure to travel between the pieces and the total of our UIs. Which is why it's important to emphasize that it's not a linear process. Consider the stages of atomic design to be a conceptual model that allows us to construct final UIs in their underlying 

[06:43] design systems. At the same time, atomic design is sometimes misunderstood as an approach to webspecific technologies such as CSS and JavaScript. In reality, atomic design has nothing to do with webspecific topics like CSS or JavaScript architecture. Atomic design is concerned with the creation of user interface design systems regardless of the technology employed to produce them. Take for 

[07:13] example, are you developing an e-commerce website? Site search, a shopping cart table, a placeholder product detail page, the homepage, and checkout pages may all be configured. Developing an online service. Begin by labeling the sign up and login forms, as well as the lost password flow and dashboard. Most websites will also include a header, footer, and main content section. After you finish creating the 

[07:44] design system, you will need to collaborate with different division. Let's take a brief look at how to develop design direction across disciplines to build fundamental information architecture in certain predicted UI patterns. UX designers might generate low-fi drawings. Visual designers may gather the aesthetic values of the team, then develop style tiles and element collages to explore early design ideas. Front-end developers may create project 

[08:16] dependencies, stub out basic templates, and define structural markup for patterns that the team expects to use throughout the project. The next important thing you need to do after finishing the design system and collaborating is to maintain the design system. To create a design system that can be maintained, you should make your design system official by dedicating actual time, money, and resources to it. Make it adaptive by anticipating change and 

[08:48] developing a clear governance strategy. Make it maintainable by pursuing the holy grail and making modifications to the design system simple to deploy and convey. Make it cross-disciplinary by making your pattern library a gathering place for the whole organization. Make it approachable by creating an appealing simple to use style guide with associated documentation. Make it visible through discussing change, advocating the design system, 

[09:19] and making it available to the general public. include brand, voice, and tone, code, design concepts, and writing rules to make it bigger. Make it agnostic by labeling patterns based on structure rather than context or content. Make it more contextual by illustrating what patterns make up a certain pattern and where each pattern is employed. Make it last by establishing a firm foundation on which to build for many years. 

[09:50] So that's all about atomic design. It's important to bear in mind that atomic design itself is not a design system. It's a method to create design system. What do you guys think? Do you have another way to create design system? What kind of design system is your favorite? Let me know in the comment section down below. In the next video, we will talk about design sprint. Please give this video a thumbs up if you enjoy it. See you in the next video and take 

[10:21] care. 
