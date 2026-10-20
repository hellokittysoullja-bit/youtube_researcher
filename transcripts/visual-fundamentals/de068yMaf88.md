# How to Design Figma-Quality UI with AI (Detailed Prompts, Skills & Gemini 3.1 Pro)
Made by Sourasith · 18 мин · 15355 просмотров · en · https://youtu.be/de068yMaf88



[00:00] AI can now generate user interface landing page dashboard animation just from text [music] instruction. A lot of AI generate UI look generic, right? >> [music] >> This doesn't happen because AI is bad. Most of the time it happened because the instruction are not clear or not detailed enough. So, if we want better design, we need to learn how to guide the [music] AI properly. 

[00:30] So, this design actually took more time because it's in light [music] mode, which is harder to design because light mode everything is visible. You cannot [music] hide small imperfection. You can see everything at a glance. Hi everyone. Welcome back to my channel. In this video, I'm going to show you my full [music] process of designing with AI to get Figma quality result. I'm 

[01:00] going to start with sample prompt and then detail prompt and then moving on adding skill for design task and finally I'm going to show you a more advanced technique [music] like structure prompting and then design section by section. So, let's jump into it. So, the tool that I use is Aura build, which is an AI builder similar to lovable, visual bolt, and many other. 

[01:31] So, I'm not sure exactly how the workflow work in the other platform, but with Aura I can choose which AI model I want to use. So, before I used ChatGPT mostly for UI and Claude for animation, but since Gemini 3.0 and now especially Gemini 3.1, which is even better, I use it for both UI and animation. So, each AI model has its own strength. For example, I usually don't 

[02:04] use Claude Opus because it's more expensive. But many developer love using it because it's very good for building real product with React and more complex code. But for designer, I think ChatGPT and Gemini work very well. So, first let's talk about a basic prompt. A basic prompt is usually very vague. The instruction are very simple. For example, you might write something like create a SaaS landing page for a 

[02:34] sell analytic platform. Because the instruction are so simple, the AI will generate something same and often very generic. Actually, it's okay, but it's not wow enough for me. With my experience in this field, I feel like it's missing something. You can also write a sample prompt, but guide the AI with a reference like image or existing component. 

[03:05] Uh let's go to Framer. Uh right now I don't have specific example, so I'm just going to improvise. I'm going to look for a template. Let's take this one and I'm going to take a screenshot of the arrow section and use that as reference. And now I can type my sample prompt. You can also reference a reusable component. I'm not sure if other platform have component library, but you can also just paste the code of 

[03:37] a specific component if you want the AI to follow that style. Hmm, I'm not sure which one I'm going to pick. Let's take this one. It should follow the same layout style. If you look at the result using the image reference made the AI add the green glow at the top of the desktop because it visually understand the structure and the color. But without a detailed prompt or even a sample prompt, the design visually stay pretty basic 

[04:09] without extra effect. So, the AI focus mostly on the structure of the arrow including the color, but not really on the desktop dashboard as you can see. So, that's why you should never stop at just one prompt. Never, never, never. Spend more time refining the section and after that focus on the component. Okay, by the way, when you take a screenshot from other design, make sure to adapt them to your own style. The screenshot 

[04:41] should only guide the structure, not copy the exact design. So, think of the image more like a wireframe. It help guide the layout and the structure of the section because we cannot use shape tool like rectangle or circle the same way we do in design tool like Figma. So, one of the best way to guide AI visually is by using an image reference. So, now if you write a more detailed prompt, we can include more information. For example, the layout 

[05:14] structure, the container width, the color palette, the UI component or product visual. So, once you add these detail, AI can generate a much more specific design. But however, a detailed prompt usually generate just one specific result. If you want a different design later, you usually need to write another prompt. So, the role of a detailed prompt is simple. It help generate one specific result. So, you 

[05:46] can see the different with a detailed prompt even without a reference image, the desktop dashboard look much better than my previous example. Designing with AI is not about writing random prompt. It's really about translating your design thinking into clear instruction. So, if you want to structure prompt like a designer, there are a few important thing you should include. First, 

[06:17] describe the product. Explain what the product is and what it do. Second, give a design direction. For example, light mode, neutral background, and maybe green accent color, and a premium SaaS analytic, etc. Next is the layout structure, which is basically the skeleton of the page. It tell AI how the 

[06:48] section should be organized. For example, you want a center container, a arrow section at the top, feature section, maybe a dashboard preview, then pricing, and finally the footer. Once you define this in your prompt, the AI can build a much more structured layout instead of something random. Next is the visual system, which define how the interface should look and feel. It's not 

[07:20] about the structure of the page, but about the design language used across the layout. You can specify if you want a round or shape border, minimal shadow, editorial spacing, grid line, or framing element. You can also define the color system like using a neutral background with one accent color. This help AI keep the design consistent across all section instead of 

[07:51] generating different style for each part of the page. And then specify the component you want like chart card, analytic dashboard, metric panel. And finally, add some technical instruction like using Tailwind CSS, making the layout responsive, keeping the HTML structure clean. So, when you structure prompt this way, the result improve dramatically. 

[08:22] If you're not sure how to write a detailed prompt, you can actually use AI to help you. Just describe your idea as clearly as possible, then ask AI to turn it into a detailed prompt. Make sure it include design direction, layout structure, visual system, component, and some technical instruction. So, now I want to talk about skill, which are different from prompt. Usually 

[08:54] people who use Claude or OpenAI create skill to make the AI behave consistently for a specific task without repeating the same instruction every time. For example, a skill can define a role, a expertise for writing posts, article, or coding in a specific style, or helping with productivity workflow, etc. Designer can also create skill for 

[09:26] design task. In Aura, there are already a few skill that are useful for designer. To be honest, I don't use them very often because I work project by project and each project has a different style, layout, or direction. I usually don't reuse them, so instead I create different detailed prompt each time. But skill can still be useful for thing like web design guideline, responsible layout 

[09:56] rule, or rule for designing light or dark mode. Here I create a skill for this SAS light mode design. So you guy can use it too. It's basically like a very detailed prompt, but with extra rule and code pattern to guide the AI. So the AI already understand the layout structure, the design system, and the visual style I want for the page. 

[10:27] So my workflow is very simple. I always start with the arrow section first. I never use a one-shot prompt to generate the whole landing page. Yes, of course it's cost more credit, but honestly if you go with one prompt, you will just get something generic. Anyone can do that. Using AI doesn't mean your job is done. You still need to guide it and make decision. So I start with a detailed prompt for my arrow, and 

[10:58] I add some skill that I create like light mode SAS design. And I add a web interface guideline and responsible design. Okay, so when you design a Figma, you follow the mobile or web interface guideline. But using AI builder, you need to mention the design system and style every time. So this skill will help you create a consistent and professional website. Uh also Aura and very well responsible design. I don't 

[11:30] always focus on this part, but of course it's not always perfect, but adding skill for responsive design make sure you design work well on all its size, which is very important. Okay, if you want to create your own skill for design tasks, it's similar like detailed prompt, but with more rule, more direction, and also you can add some code. So don't tell J Don't just tell AI what to build, but tell AI 

[12:00] how to think like act as senior product designer. Then make sure to define the system, the overview what this skill do. Make sure to talk about the visual direction, the layout rule, component rule, interaction rule like motion and behavior, and add some constraint what to avoid. Once your arrow section is generate, don't make the mistake of stopping here. 

[12:32] Even if your prompt was detailed and the result look clean and professional, you still need to go deeper. Focus on these small details like changing the font, adjusting color if you don't like them, refine spacing, etc. Then move to the component, especially the dashboard. You can leave it as it is, but personally I like to polish it more. And yes, unfortunately, you still need to prompt again. So I recommend writing a more detailed prompt or even using a 

[13:04] reference image for chart to give the AI visually. And since you are already using a credit for a prompt, add animation detail at the same time. It will save you from wasting another prompt later. At the beginning I used to focus only on the UI first, and then I think about animation after, but I realized the best strategy is to add animation at the same time. So when I refine a card, I also include how it 

[13:34] should move and behave. And at the very end, when I have my landing page, I can add a global animation like on load and on scroll. So I really focus component by component. There are still These two card that annoy me so much, but I do like the other card. So I'm going to copy it. Make sure to select the parent container and replace the other card. So of course, you can edit thing manually 

[14:05] if you are comfortable with the code. And then I have to adjust the code a bit so everything fit properly. Another tip, if you are subscribed to ChatGPT, Gemini, or even Claude directly in the app, so what you can do is copy the code and ask AI to fix the code for you and improve it for you. So of course, you only do this if you already have access. Otherwise, you can just prompt directly inside your AI builder, but the 

[14:35] different inside AI builder is you have a limit of prompt. Otherwise, you have to buy more prompt or credit. So, but don't subscribe to another tool if you you did not use it before. Another tip is I can also reuse my old component. Uh for example, I remember I create a donut pie chart before. So I'm just going to find it and reuse that part, and then 

[15:08] refine it. Okay, just like in Figma, I can copy and paste property directly without wasting a prompt or editing everything manually. So, okay. Now that the header for the card is more consistent. I'm just going to keep the real-time activity log like this. Okay, so now my dashboard look much 

[15:40] better. So when you're done, just move on to the next section. Again with a new detailed prompt, and repeat this process until you have a full landing page. So I don't stop there. I keep focusing on the visual of each card. Right now it still look basic, but since I cannot show everything, I will do it quickly and move on to the next section. But you, don't do that. Take your time to 

[16:13] polish. Here I can just duplicate the section and prompt only that part instead of making the UI recheck the full code, which is slower and honestly annoying. Um I'm not going to show the entire process because like I said, I can make a design in 5 minute, 30 minute, or even more than that. So it's very depend on how much time I want 

[16:45] to spend polishing it. So the goal of this video is to show you my workflow, how I design using detailed prompt, how I use skill for design task, and how I guide the AI visually not just with text, but also using images and reusable old component. After that, you can add a motion background to the arrow section, and then add on load and on scroll animation. 

[17:15] Okay, so you can still prompt for the animation or do it manually. I'm going to show you And the code you will see code snippet. I use animation keyframe and on scroll. Place this in the head of the code, then apply them using Tailwind class on each component. And before I end this video, I also want to show you how I add more pages. From there I can create new page. Um 

[17:47] you can also define how the transition work between pages, and then generate the new page and adapt it. Uh again, use a detailed prompt and that's it. So now back to the home page. To link this page, just click on the product text or whatever page that you create in the header navigation and link it to the product page. Then repeat the same process. So that's it for today. Let me know what you would like me to cover 

[18:18] next. So thank you so much for watching this video. I hope that you like and enjoy. So don't forget to like and subscribe. See you another video. Bye. 
