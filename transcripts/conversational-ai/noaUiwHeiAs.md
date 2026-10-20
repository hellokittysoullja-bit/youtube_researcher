# Token Speed
Balamurugan Balakreshnan · 4 мин · 13 просмотров · en · https://youtu.be/noaUiwHeiAs



[00:01] Welcome back. Hi everyone. Today we're going to talk about the token speed. It's basically like how fast is your LLM um what the number means, what it drives, and what can we do about it. So the idea here is like LLM generate text one token at a time. A token is about 3/4 of the word. Speed is not number one. how long the user waits before anything appears and how fast tech streams once the starts and how many tokens the whole system produces per second are are three different things 

[00:32] and improving one can hurt another. So the first thing is like time to first token which is how long until the first word appears. Um this is dominated by the prefill phase reading the whole prompt long prompts and drag document make it worse and we can target it as low as possible and then the inter token latency um the gap between the tokens once uh streaming starts which is basically the producing the consecutive other tokens dominated by the decode phase. Humans read about 

[01:05] five to 10 tokens per second. Anything faster than 20 or 30 tokens per second, the user feels instantly uh feels instant for chat agents and code toolings much more faster. And then the end to end latency which is the time to first token and the number of tokens uh output inter token latency all put together is what the user actually uh experiences. um throughput tokens per second across all users on the system. Then depending on like how many users 

[01:35] are connecting and you know it's going to uh hit hard um as the user counts go up and up and up. Trade-off bigger batches raises throughput but slow um each use it use it down pick the latency you need and then maximize the throughput of the latency. Um so the these are um what drives the speed is the prefill and decode. This is also what we call disagregated framework um serving. Prefill is very much compute bound and tokens are processed um in 

[02:06] parallel. Speed depends on the GPU math throughput. Decode is memory bound. Every token is kept in the memory and then rered from the whole weight of plus the KV cache from GPU memory. Um so speed depends on the memory speed. Um and the so you can do a rough calculation. You can see it in the on the left hand side. Now how do we make it faster right like I mean you can also quantize and make it few bit for token to make it faster and smaller footprint. You can use speculative decoding with a draft model purpose and have the bigger 

[02:37] model to verify them. That might increase the speed. Also, uh prefix and prompt caching like reuse the KV cache repeatedly um as much as possible to lower the first time to token. continuous batching and uh um and and paged KV cache like we like how VLLM SG lang and tensor RT keep the GPU busy no wasted memory and then disagregated prefill and decode run on separate GPUs so that you don't share and it is not bottlenecking use a smaller or distal 

[03:08] model when quality allows use a faster for more GPU in parallel but the business benefits are better uh user experience faster for token smooth streaming if the user interactive and he doesn't feel like uh oh man it's slow or something like that lower cost per token so that you can get higher throughput means fewer GPU for the same traffic more capable products fast decode makes much um uh much multi-step agents and real time uh voice u practical and then 

[03:38] you can also do SLAs like measure the first time to token and then the inter token latency and the throp separately and set targets for each um so always benchmark your application before you uh put into production to understand like how it is behaving so you can actually track and that's just the gist of it um that's the concept of token speed have fun time um building AI applications and helping your customers and please subscribe to the channel if you haven't 

[04:09] thank you and have a great 
