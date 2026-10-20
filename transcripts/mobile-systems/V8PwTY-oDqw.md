# Design Systems at Scale: Maintaining UI Consistency in Dynamic Plugin Architecture - DevConf.IN 2026
DevConf · 19 мин · 339 просмотров · en · https://youtu.be/V8PwTY-oDqw



[00:00] Hello everyone. Uh good morning. I think I am audible. So welcome to this session. I am currently working as senior software engineer at Red Hat and I am active contributor to uh RSDS and back stage. Let me introduce you what's RSDS and backstage is. So RSD is an internal developer portal based on back. It's consist of 100 plus plugins that's being 

[00:31] contributed by uh different teams and red hat from different companies also there is a backstage community who is also contributing to the plugins. So now I will uh inform you to how we are able to how you are able to get UI consistency despite of being redhead consist of hundred of plugins. 

[01:01] So firstly let's understand what plug-in architecture is. So in plug-in architecture there is a host application and host features or capabilities can be extended using any number of plugins. So, uh, have anyone of you have anyone of you have ever used an application which is based on 

[01:33] plug-in based architecture? Can you raise the hand? Okay. I think very less of you have raised the hand. If I name the few applications you will definitely say that you have used you have already used the plug-in based architecture application. So have you ever used VS code? Everyone has used that and Figma, Shopify, WordPress all these big applications has been built based on 

[02:05] plug-in based architecture. So why plug-in based architecture is so common in big applications? because the functionality of the applications can be extended without depending on the core team. So it solve the core business problem extendability without bottlenecking on the core team. As I already told in plug-in 

[02:36] architecture the applications capabilities can be extended using any number of plugins and those plugins can be developed by third party vendors also and completely independently at their own speed. They can have different release cycle. So with this flexibility plug-in based architecture come with few challenges. So we will be discussing that too. 

[03:09] So different teams from different ors are contributing the plugins and as we know different teams have different design preferences. Someone likes blue as the primary color. Some may likes green as the primary color. Some teams use eight pixel as spacing. Some teams may use 16 pixels as spacing. Some may likes rounded button, some may likes corner button. So, 

[03:39] so like with their preferences the UI become a scattered and uh no matter how your big application is, how much plugins is consist of the UI should be consistent otherwise it will confuse the user. Second most challenges come. Let's see. Plugin A is using React 18.1. Plugin B is using 18.2. Plug C is using React 18.3. So dependencies, conflicts, drifts 

[04:13] happens. The third major problems come with is CSS conflicts. So CSS is by nature global in natural in nature. Let's see. Plugin A define a class name MUI button color and provide the style as background color red and plugin B define a same class MI button color with the style as 

[04:43] color background color as blue. So, so yeah. So, like in different part of the applications, uh the brand color the butterc colors will look different. So, these are the major challenges comes with the plug-in based architecture. So how we can solve this? 

[05:16] While developing RSDs or back stress, we have followed these five strategies to maintain UI consistency in our whole application. First one is central theme system. So start with building a package which controls all the visual styles of the application. Be it color, be it font, be it spacing, be reusable components. Also define how it 

[05:48] will behave in different themes. Why that theme package should be centralized? Let take an example. If plug-in A developer comes with the primary color and they put some hex code that is different set of blue. Plug-in B developers can put some different hex code and that can be different sets of blue. So different different plugins can have different set of the same color which will again make our UI 

[06:19] inconsistent. With the central theme, we'll be defining the primary color at one place in our theme package and every plugins will be importing the primary colors from that theme and everywhere the same blue will be seen. So that's how we can maintain the consistency. how we can implement that theme. 

[06:52] So we can define an uh typescript interface and there we can start adding colors like primary colors, secondary colors, semantic colors, uh semantic like error, warning and some component specific tokens like sidebar color uh table headers color. So that the plug-in developer just need to type theme dot platelet. primary dot 

[07:25] main and the same color for that main will be shown throughout the application. As we also know the benefits of defining the type script interface. If we define using type script interface, it will s while while developing it will auto suggest to the users the dollars and all and also if it will reduce the 

[07:56] typos because if he writes something wrong it will in the in the editor itself it will show start showing the error also while compiling it will throw the error. So without So that wrong color or wrong code will not go to the production. It can be detected while uh development itself two is runtime dependency series. Let's 

[08:28] take an example. If each plug-in bundle in it, each plug-in if bundle react in itself like each plug-in bundles contain reacts. So while running the applications we will have multiple instances of the react running at the same time that will lead to lot of errors and we will get errors like that is not working that function is not working also including react in each 

[09:01] plug-in bundles will increase bundle size a lot. So how we can solve this? There comes the model federation. So what we can do? The host application will load react, react, router, state management, libraries once and at the runtime plug-in all the plugins will consume 

[09:32] whatever being provided from the host application. So what we need to share definitely something which should be a singleton in nature and also the UI libraries that's being used by more than 50% of plugins we can use that but we should not share something a particular plug-in is using 

[10:03] like let's say some plugin is displaying some charts and on using D3 or chart.js don't share D how we can implement the module federation so different bundas provide different APIs for for implementing the module federation in webpack we do have module federation plug-in where you just need to put the 

[10:33] dependency in the react and only copy of that dependency will be there while running the application. Strate three is style isolations. So let's take an example. Plug-in A define MO button as background color red and plugin B define M color as blue. So when 

[11:03] both the plugins is loaded in the application the class name conflicts come and we can't decide which one will get applied. It's all depend on the loading orders which plugins the plugins which is loaded at the last wins the race and wins the race and the styles will be applied from that plug-in. 

[11:34] So how we can solve that? So there are different techniques different isolation techniques. First one is class prefix. So what we can do for each class each class names in the plug-in we can add some add class name as a prefix and it will make it unique and there will be uh no CSS conflict between different plugins. 

[12:07] Different libraries give different functions to achieve that. MUI gives us class name generator where we can configure it such like it will prefix the plug-in name before each classes of that particular plug-in. Second technique is shadow down. So set is a technique where we can configure in such a way that the plugins do doesn't get affected by other 

[12:38] plug-in styles and also this DOM styles will not lead to other plugins DOM. Third one is CSS modules. So in CSS modules each class CSS modules generate a unique hash code for each files and it append to each class name as suffix. So that's also make the class name unique and that's how we 

[13:09] we get rid of the styles conflict between the plugins. Strategic four. So this is for extension contracts. One minute. Let me 

[13:45] Extension contracts. This is clear contract between the plugins and the host application. How a plugins can can integrate what else a host application will provide. So without without contracts plugins can modify anything. it it can even change whole layout. It can appear 

[14:16] at any place also plugins developer can use some internal APIs of the host application and when the host application developer want update that API it will lead to it will let the plugins break. So it's result into no pred predictable structure of the application and also 

[14:46] the update of the host plug-in become difficult with clear contract the host application provide the slots and the plug-in says I will fill that particular slot with this component. So it makes the UI very much predictive. We ex we know exactly where the plug-in UI will be displaying. 

[15:18] Also due to this named slot we have a stable integrations. This slot name and the configuration change real. In this diagram I have shown like how a platform or host applications provide the name slot and plugins say that I will fill that particular 

[15:50] that particular uh slots. Now the last strategy that is configuration driver UI customizations. Different customers can have different brand logos, different colors and they make us for having those styles, logos and 

[16:21] colors. So we have two options. One is we ask the developer make the code changes raise the PR PR get reviews tested and PR get m deployed and we achieve whatever we want to do but this is very slow process and it take lot of effort in configuration driver customizations the 

[16:52] operations teams or platform engineers, maybe admin, they just need to update the configurations and they it may happen without redeploying the whole application and they they can achieve the UI or branding color logos whatever they want. So what all should be configurable? So mostly brands uh companies have their 

[17:25] own logos. They wants their own brand colors. So those should be configurable also like how it should look in dark theme, light theme. So the companies should be able to override all the theme colors, logos and they will be able to achieve whatever brand color logos they want. 

[17:58] So key takeaways from this presentation build the central theme early so that all the plugins can consume it. Share the model federation. Share all the dependencies at runtime not at the build time. So that there will be only one copy of the library while running the application. 

[18:31] Third is a style isolation. So we talk write uh using different different techniques we can have a style expressions that will resolve our CSS conflict and there should be clear extension contracts and all the colors logos should be changeable by configurations and using these all the techniques we can achieve consistent UI. 

[19:06] Thank you. Uh these are the some dogs link resources about backstage RSTs. Thanks. [applause] 
