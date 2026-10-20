# SRE for AI Systems — Why AI Infrastructure Breaks Differently
ReliableSystems · 10 мин · 2 просмотров · en · https://youtu.be/9U7aOKiE4oE



[00:00] How can an AI service return HTTP 200 and still fail the user? Imagine a support assistant answering a question about refunds. The end point is reachable. Authentication works. The request returns successfully. The response is fluent and arrives on screen, but it quotes last month's policy because the retrieval index is stale. From the API's point of view, the request succeeded. From the user's point of view, the service failed. That is the 

[00:32] first mental shift when S sur moves into AI systems. Infrastructure health is still essential. But it is only one layer of reliability. An AI product can be available while its answers are too slow, outdated, unsafe, irrelevant, or simply unable to complete the task. Successful transport is not the same as successful work. What actually happens inside one AI request? The request rarely travels 

[01:03] straight from a user to a model and back. It may enter an API gateway, pass authentication and rate limits, retrieve documents from a search or vector system, wait in a model serving queue, run through a model runtime, call an external tool, and then stream a response. Every handoff can add delay or fail independently. The retrieval system can return stale context. The tool can time out. The serving queue can fill. The external provider can throttle 

[01:34] requests. The model can be healthy while another dependency breaks the user journey. This complete chain is the request path. The model is an important component, not the whole product. Which dimensions make an AI service reliable? Start with what the user expects. They need the service to be available. They need the first useful response quickly enough. They need the task completed correctly enough for its purpose. They may need current information, policy compliance and predictable cost. Those 

[02:06] expectations become different reliability dimensions. Availability can use successful request evidence. Responsiveness may use time to first token and total duration. A retrieval product may track freshness and groundedness. An agent may track whether the intended task completed. Cost per successful task may act as an operational guardrail. Not every product needs every dimension and not every metric belongs in an SLO. The design 

[02:36] begins with the user journey, not a fashionable dashboard template. Why can't an error counter measure answer quality? An ordinary error counter can tell us that a request crashed or returned a failure status. It cannot tell us whether a technically successful answer was useful. Model outputs can vary. Two responses can both return HTTP 200 while one is clear and grounded and the other is misleading. Quality therefore needs evaluation 

[03:07] evidence, carefully designed test cases, task completion checks, user feedback, human review where appropriate, and measurements across important traffic slices. Those signals have limitations. Automated evaluators can be wrong. Feedback can be sparse or biased. A single average can hide failure for one language, workflow or customer group. So quality monitoring is not one magic score. It is a body of evidence tied to a defined user expectation. 

[03:38] If this kind of practical production engineering is useful to you, subscribe. We build reliability from real system behavior one layer at a time. Why does AI serving hit capacity differently? The familiar S sur question remains. How much useful work can the service complete while meeting its objective? But AI serving introduces different constraints. Model size and runtime state consume accelerated memory. Concurrency and batching affect 

[04:10] throughput. Requests can wait for a serving slot before inference begins. As that queue grows, time to first token rises even while the endpoint remains available and accelerator utilization looks impressively busy. A serving system can expose request duration, Q duration and compute duration separately. That distinction matters. If Q time is growing while compute time is stable, the model did not suddenly become slower. Demand is waiting for 

[04:42] capacity. Measure saturation through its user consequence, not only through a utilization percentage. How can healthy infrastructure produce stale or wrong answers? Return to our support assistant. The gateway is healthy. The model servers are healthy. Q time is normal. Yet the answer still uses an old refund policy. The failure lives in the data path. Perhaps document ingestion stopped. Perhaps the retrieval index was not refreshed. Perhaps a new 

[05:14] embedding version is incompatible with the stored vectors or a tool returned incomplete information that the application treated as valid. This is why production machine learning guidance includes data schemas, freshness, drift, model age, and real world outcome monitoring. Healthy compute cannot prove that the information entering the system is current or correct. AI reliability needs lineage. Which model, configuration, prompt, index, data 

[05:46] version, and tool result produce this answer. What should we measure across the AI request path? Think in connected layers. Infrastructure signals describe accelerator memory, node health, power, network, and storage. Serving signals describe request rate, Q time, time to first token, tokens per second, total latency, and errors. Application signals describe retrieval success, tool outcomes, and task completion. Quality 

[06:18] signals describe relevance, groundedness, freshness, safety, or another product specific expectation. Cost signals show what each successful outcome consumes. Distributed traces can connect those layers for one request. A slow trace might show 2 seconds in retrieval, 8 seconds in the serving queue, and normal model execution. That is far more useful than one red box labeled AI. Layered observability makes 

[06:49] a system explain where the user experience changed. How should we triage an AI incident? Begin with the symptom and scope. Which user journey degraded? When did it begin? Which models, regions, versions, languages, or traffic slices are affected? What still works? Then classify the likely layer, infrastructure, capacity, dependency, data, model configuration, output quality or governance. The 

[07:19] classification is not the conclusion. It gives you a smaller set of hypothesis to test. If time to first token rose with Q depth, investigate serving capacity. If latency is normal but answers became stale after an ingestion failure, investigate the data path. If one model version regressed on known evaluation cases, compare it with the previous version. Use the familiar loop. Scope, hypothesis, evidence, isolate, mitigate, 

[07:51] and verify. Do not turn every incident into the model is bad. What does an AI SLO look like? There is no universal AI SLO template. A conversational assistant, fraud classifier, and code generation tool promise different outcomes. One service might define an availability objective for valid requests, a time to first token objective for responsive interaction, and a task completion objective measured 

[08:23] on a carefully governed sample. Freshness may be a separate objective for retrieval. Harmful output rate may be a safety boundary. Cost may remain an internal guardrail unless it directly changes the user promise. Each signal needs a clear population threshold, measurement window, and known limitations. Quality evidence especially needs review because the measurement can drift with the product and evaluator. 

[08:55] Start from what users need the system to do, then choose the smallest set of signals that represent that promise. What should an SR team do first? Pick one important AI user journey and draw the complete request path. Name every dependency and owner. Add a trace that connects retrieval tools and model serving. Baseline request rate, Q time, time to first token, task completion, freshness, and cost where they matter. 

[09:25] Then run one controlled failure exercise. Make retrieval stale. Constrain serving capacity or fail a tool in a safe environment. confirm that the right signal changes, the alert reaches the right owner, the system degrades safely and verification checks the user outcome. AI infrastructure does break differently but it does not replace S sur. It adds new evidence and failure modes to capacity, observability, incident response, SLOs's 

[09:56] and safe change. Next, we will separate high availability from disaster recovery because keeping a service running and recovering trustworthy state are not the same 
