# I Redesigned the ENTIRE Spotify Wrapped
Lucas Chae · 8 мин · 4862 просмотров · en · https://youtu.be/owSfkYqfEOU



[00:00] We need to talk about Spotify Wrapped. So, as you know, for a lot of people, Spotify Wrapped has become like an end-of-the-year tradition. But, unlike past years, when checking your Spotify Wrapped felt like unwrapping your favorite toy on a Christmas day, this year's felt like a $10 gift card from your co-worker. Spotify Wrapped was a flop. I'm sure you've already seen a lot of posts about how bad it was. In fact, I think I saw more of these complaints 

[00:31] than my friends actually sharing who their top artist was. And no, it's definitely not because I don't have any friends. Anyways, I waited a whole year for this, and I wasn't going to let it slide. I decided to take matters into my own hands and decided to build my own Spotify re-wrapped for 2024. So, to figure out how to fix it, I wanted to see what exactly went wrong. 

[01:02] After reading hundreds of feedback online, I've narrowed it down to three main issues: lack of content, like genre analysis or top albums; lack of clarity, like these ambiguous music type categories; and of course, AIs making it feel inhuman. And this video from 2020 by Spotify really shed a light on where they missed the mark. campaign is that we are telling stories through data. We're telling stories through data. Storytelling is crucial in binding 

[01:33] content, clarity, and personality all together. And this year, story was truly the missing link above them all. Now that we've identified the problem, it's time to actually start building. I looked at all of Spotify Wrapped since 2018 to see what they were doing well before. I then put all the features in a list and sorted them by priority and importance based on how much people liked them. Design-wise, the biggest difference would be that my wrapped will be a website and not inside the Spotify 

[02:05] app. And personally, Grinder did an amazing job of creating a web-based wrapped. Each card had a clear theme and it flowed very naturally. So, this will be my main source of reference. So, based on all that information, I made a set of wireframes for the re-wrapped experience. Here are a couple highlights. I wanted to create these music festival lineup posters, except where each artist is your top artist for that season. And here's a sneak peek of how that turned out in the end. I also 

[02:35] have this listening pattern analysis where it tells you what time of the day you tend to stream music and sort you into a fun category like night owl or early bird. So, with the wireframe complete, I'm going to jump straight into coding on day two. Now, you might be wondering, "Should I need some kind of design before writing code?" Ideally, yes. But with 2024 ending, I was running out of time. Fortunately, the internet comes with a 

[03:05] cheat code called UI libraries and I can easily use them to make anything look shiny on the go. So, solely based on my wireframes, I went on Claude and wrote out all my requirements in fine details, including what kind of libraries I want to use. Now, I'm not dumping everything to Claude. I picked two to three core features, the ones I can use as building blocks. And as you can see here, in no time, I had a file upload system with a few basic stats. I didn't know that the 

[03:36] first song I played this year was Paint the Town Red. Yeah, I'm already having so much fun looking at this cuz I didn't know that I usually listen to music around this time. Then, I had Claude spoon-feed me all the steps I needed to set the project up. I just had to follow the instruction like an IKEA manual, except instead of a bed frame, I get a functioning website. Now, I believe this is exactly why you still need to know how to code, because knowing that will really help you better 

[04:08] communicate with AI for faster and optimal results. It's like when the CEO knows how to code or understand the technical side of the product, everyone is just happier. And as you're building up from your boilerplate, obviously you'll have to constantly fix UI bugs like these, and you'll bump into errors like these 

[04:38] all the time. But you just have to communicate with AI like you're the product manager and they're your fellow engineer, and work it out together as a team. I spent the rest of the day on styling and adding a few more cards, and with that sorted, I was ready for the final day, where I'll be turning this from something that barely works to something that's really exciting to use. To make my Spotify Wrapped really pop, 

[05:10] I'm using a library called Aceternity. They have so many free components and they're all immaculate. Browsing this library just makes me want to build different websites for fun. I listed up all the components that are suitable for this project and implemented them one by one. I then searched for some seasonal festival posters for inspirations and used Midjourney to create my own poster backgrounds. 

[05:42] Last but not least, I have a genre on the card. But did you know there are over 6,000 genres on Spotify? But, thankfully, this website called Music List has descriptions for each and every one of them. So, I built a quick API myself for the first time in my life, thanks to AI, and just made it fetch these descriptions on demand when user creates their own Rewrapped. So, with that, everything was complete. And here's the final result. 

[07:19] So, that's a wrap. This whole project took about four full days. Considering my last proper web dev experience was back in college, which is an eternity ago, it wasn't that bad at all. The biggest caveat is obviously users having to manually download their Spotify data, which can take up to 5 days. But, from a developer's perspective, there's nothing I can do about that. If you have any suggestions to make this a smoother, more user-friendly experience, please leave a comment below. The website is 

[07:50] live now at rewrap.xyz, so please go and create your own. If you have any feedback or want to connect, I'm most reachable on Instagram or Twitter, so let me know. Till next time, ciao. 
