# Workflows at Scale: Design Systems, Platform Engineering, and the AI Workflows that scale
Design Systems London · 16 мин · 102 просмотров · en · https://youtu.be/pI12krTC5n8



[00:00] Good evening everybody. My name is Abeke Ante. I have over 10 years experience as a front-end engineer and for the last 4 years I've been working at the intersection of design and engineering at Conde Nast building the things that keep the design system alive when it scales. I've worked across all Conde Nast brands and some of them you may know. Brands like GQ, Vogue, Wired and Glamour all being served by one design system. 

[00:30] Today I'd like to tell you what I've learned about treating your design system as infrastructure. What that looks like in practice and what happens when you introduce AI to those workflows. But first, let's go down memory lane. So when design systems first came about there were static style guides that lived in PDFs or static websites. And they were often a one-and-done project, but around 2015-2016 we started seeing a shift towards 

[01:00] treating design systems as products with the hope that they would help with adoption, redundant work, and establishing a source of truth. Well, at least that was the goal. Um, and whilst treating your design system as a product does solve some issues, others remain persistent. We hoped that it would help create a shared language, but I think most of us here can share at least one story of a let's say lively conversation at hand. Oh. 

[01:33] Um, and if truth be told, most companies, if not all, have two design systems running in parallel, one in Figma and one in the code. When I first joined Conde Nast we dedicated time to um upskilling because knowledge and understanding around the design system varied across the whole company, despite the design system being 7 years old at that time. This involved workshops, building documentation, fortnightly calls with 

[02:03] designers and engineers. All in the hope of building visibility and adoption. And on the surface this was working because user confidence was growing. But a closer look at the code showed that we hadn't even scratched the surface. There when you're working with such scale of a product with teams that fiercely protect their brands, you can only imagine what happens in the code. There were still plenty of hardcoded tokens and custom configurations and to be honest it's moments like these that 

[02:33] can make you feel really defeated. But let's take a step back, look at it objectively and identify the disconnect. Whilst treating your design system as a product solves some foundational issues, it only works for a small number of teams. When those teams start scaling to 5, 10, 15, the system starts to implode. And I guess in a way it's not really meant to scale because products only solve a specific user problem. It 

[03:04] doesn't come with the infrastructure that safeguards that scaling. The introduction of AI has not only compounded that problem, but it's put a magnifying glass to the silent problem. Before there was one, maximum two locations, deviations and changes would occur. But now with AI in the equation, every designer and engineer has a version of the design system that they can chop and change as they build. And then days, weeks, months go by and all of a sudden your product feels 

[03:34] different and you don't know why. And your user experience is taking a hit, but on the surface you're doing everything right. Adding AI to the current definition of design system opens a Pandora's Box. And if that doesn't give you a mild panic, boy. Yeah, you're better than me. But what if I told you that doesn't have to be the case, and actually going back to the definition of design systems and the framing of design systems could be the solution? Whilst treating your 

[04:05] design whilst defining design systems as a shared language isn't incomplete or incorrect, it is incomplete. Well, let me say that again. >> I think the slides are moving if you moved on. >> No, I'm not on it, but thank you. Um whilst treating your design system as a shared language or way to keep it consistently isn't incomplete, sorry, isn't incorrect, it is incomplete. Because design systems aren't just a 

[04:37] shared language, they are infrastructure. In the same way your continuous integration and continuous delivery system is infrastructure. But before we get into the weeds, I thought we could define a few things to make sure we're starting on the same page. Infrastructure has French origins with infra meaning below or underneath. It serves as the underlying foundation that supports everything that's built above. Whilst continuous integration and 

[05:08] continuous delivery is the set of automated practices that help software teams build, test, and release code. Treating your design system as infrastructure not only requires a might your mindset shift, but it also requires you to shift in how you build, maintain, and most importantly fund it. As the focus moves away from how it feels to how from how it feels and how it looks to how it scales, endures, and supports 

[05:39] velocity. As products, again, only solve a specific user problem whilst platforms provides the infrastructure and guardrails that allow teams to scale. It is the system below the system. So, what is this mindset? It's It's platform engineering. So, let's imagine you have 10 teams. Each team creates their own application, their own CI/CD pipelines and databases, which creates a lot of duplicated 

[06:10] effort. What platform engineering does is it creates a starter pack with predefined CI/CD pipelines and database and monitoring all written within the company standards for all the teams to use. In the context of design systems, that would be the rules that help with adoption, consistency, token drifting, and hallucination. With this in place, you don't have to wait 3 to 6 months to measure impacts, but from the moment that starter pack is 

[06:42] downloaded and compiled, as your product is now being driven by a system that's self-governing and self-healing. Uh Condé Nast has over 60 websites and more than 1 billion users globally, uh leaving a lot of room forever. I'll just give you an example. Um we're working on a CSS migration um as part of a theming product. This 

[07:12] involved removing all tokens, mapping to CSS variables, and when you're working with legacy code with brands at this scale, the code becomes a bit of a landmine. I made some changes, added tests where tests were missing, everything passed, everyone was happy. And for context, these are all the locations that Vogue appears. Um so, when it goes wrong, it goes really really wrong. Anyway, the next morning I get my 

[07:43] coffee, sit at my table, open my laptop, and there was a message on Slack in capitals like Vogue is in midnight mode. We don't have a midnight mode. We don't even have a midnight theme. So, open Vogue, and all you could see were titles, pictures, and videos. And so, this was bad. This was really bad. You could just imagine the mild panic that just took over me. What happened is somebody added some custom configuration somewhere else in 

[08:14] the code that even with all the tests and checks, we still didn't catch it. And between myself and an engineering manager, we were able to roll back the changes without any hiccups. And yes, I laugh while I tell this story, but at the time it was very much not happy funny. On the flip side of that, having this in place shrinks the gap between idea and production. And when it works, it's just simply magic. We were developing a platform 

[08:44] localization and right-to-left like localization feature that allowed us to launch Vogue Arabia, GQ GQ Middle Eastern, and Wired Middle Eastern, which created an opportunity for an estimated $16 million in revenue. Applying a platform engineering mindset doesn't mean failures won't happen. They do. But, the value lies in how well you handle those failures. 

[09:16] Google released a software reliability book which talks about platform engineering, building the systems and the resources for developers um to build products. And DevOps, or DesignOps in our case, being the culture and practices that take an idea into production. This is the ethos we're applying when treating our design system as a platform as infrastructure. And there's a number of benefits to 

[09:46] applying this mindset. For example, brand compliance and accessibility, these are no longer manual checks in the code or mere hope, uh but they're baked into the platform. Instead of your team being bombarded with requests, applying a platform mindset provides the self-servicing tools and guardrails so teams can build what they need for themselves. And that's just to name a few of those. 

[10:17] So, now that we've established that your design system that treating your design system as infrastructure is the foundation, what happens when you add AI on top of that foundation? And here's the part we often skim over. AI doesn't fix a broken design system. It amplifies what's already there. If your system is inconsistent, AI will generate inconsistency at scale. If your tokens are hard-coded and your components undocumented, 

[10:48] AI will guess and AI will guess wrong confidently. But if your system is structured, your tokens semantic, your APIs consistent, and your documentation clear, AI becomes a genuine multiplier. Okay, there are three things you have to get right. Context, infrastructure, or aka context of your prompts. Most people think scaling with AI is about writing better prompts. It isn't. 

[11:19] It's about context. The agent is only as good as what you give it to work with. If you're If you give it your entire codebase without constraints, it will produce something that technically works but visually fails. If you give it your token file, your component file, or your brand guidelines, you're not prompting, you're briefing. And that's a very different thing. Think of it like you're onboarding a new designer. You don't just give them a laptop and say, "Good luck." Well, 

[11:49] I hope that's not what you do. You'd give them the brand guidelines, the component library, the do's, the don'ts. AI needs the same briefing. The difference is your design system infrastructure is that briefing. Before I left Condé Nast, I was exploring this very thing. I gave Cursor our Vogue CSS variable file, and I was able to write rules and guidelines without connecting an MCP or Storybook. Cursor was able to produce something 

[12:19] that was remarkably close to our Vogue website, but not because it was somehow smarter, but because the foundations were clear. This taught me something very important. Architecture isn't just good for humans, but it's also good for agents. The decisions we made to make Theme and Faster and semantic token token names turned out to be the exact thing that made our design system AI readable or AI ready, whichever one. 

[12:49] Security and rollbacks, aka guardrails, not gatekeeping. When you introduce AI into your team workflows, the design system stops being one thing, one thing managed by one team. It start It becomes distributed. Every designer and engineer has an agent making decisions, creating components, updating or modifying patterns quickly 

[13:21] without permission without asking for permission. This isn't a reason to panic, but it is a reason to build guardrails. Guardrails that are baked into your platform that agents can so that agents can generate freely within your system without breaking it. They are constraints that make autonomy safe. Token boundaries that tokens cannot that agents cannot cross. API component APIs designed to make misuse 

[13:52] harder than correct use. And documentation written clearly that an agent not only understands what a component does, but where to use it. The goal isn't to stop AI from generating, but to stop AI or to make it impossible for AI to generate off-brand. And lastly, monitoring. I like to think of this as governance you can see. When your code isn't exclusively written by humans that have spent years learning 

[14:23] and caring for your brand, you need to be able to see what's going on. Monitoring a AI-native design system isn't about uptime, but it's about drift. Are your components drifting from your token library? Are the agents introducing new patterns that aren't in your library? Are the things being generated actually accessible? The good news is if you treat your design system as infrastructure, if it's the foundation that everything is built 

[14:54] on, you can make the invisible visible. You build in drift detection into your pipelines, so you catch the inconsistencies before they're shipped, instead of six months down the line. And gone are the days of begging for feedback. With the right infrastructure, the feedback is built in. Lastly, I'd like to leave you with a quote by James Clear from his book Atomic Habits that really helps me frame my mind to this way of thinking. 

[15:26] You do not rise to the level of your goals, but you fall to the level of your systems. Before adding AI to your workflows, audit them. What's not working? Why? What's working? How do you multiply it? Before because AI will amplify what's already there. Build the foundations first. The agent will follow. And remember, the devil's in the details, not in Nevada. 

[15:57] Thank you. 
