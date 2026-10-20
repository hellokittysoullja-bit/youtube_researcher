# GraphRAG vs. Traditional RAG: Higher Accuracy & Insight with LLM
IBM Technology · 4 мин · 222952 просмотров · en · https://youtu.be/Aw7iQjKAX2k



[00:00] Imagine you're running a health care support line where patients and providers are calling in with complex multi-step questions. This is where GraphRAG comes in. It helps map relationships, providing precise, personalized answer faster, and this is critical where accuracy and speed matter. Today, we're going to take a look at how GraphRAG helps in delivering higher accuracy and more complete answers, easier development and maintenance and enhanced governance. We'll go over what is GraphRAG and uncover the benefits of GraphRAG relative to traditional RAG in development, 

[00:34] Production, and governance. To understand GraphRAG, let's first break down how Baseline graph works. We start off with a private data set, can be both structured and unstructured, so this is our traditional, and we break them down into text chunks, and we store those embeddings in a vector database. 

[01:08] Then when we want to query, we use our vector database to extract the context, and then we send that context to our LLM, and then it provides the answer. We all know how tradition RAG works. Now GraphRAG builds on top of that. We start off with leveraging same text chunks, 

[01:39] but on top of that, we're also extracting entities and more relative information to be able to map out these information in a knowledge graph. This way graph doesn't just retrieve isolated answers. It connects relative information which enhances the quality responses and added accuracy and insight. Let's consider an example to demonstrate the capabilities of GraphRAG. Suppose we have a sentence like this, "an immunologists discussed virus 

[02:11] response strategies with the CEO of a health care company." Traditional text analysis might have detected immunologist and CEO as named entities. However, GraphRAG goes further by identifying and mapping the relationships between these entities, and this provides a deeper context and insight into their interaction. So GraphRAG recognizes that the immunologist is deeply connected to immunology and the medical research. 

[02:41] Whereas the CEO has more of an indirect yet related connection through her leadership at the health care company, This analysis goes beyond just simply noting co-occurrences. The LLM quantifies the strength and nature of these relationships, enabling the construction of weighted graphs that reveal insightful patterns. Transforming data into knowledge graph creates a network of connected and linked entities, and the linked multilayered knowledge graph then supports a wide range of applications, 

[03:12] and generating targeted questions to crafting rich and contextually relevant summaries, ultimately providing a depth of insights that traditional RAG cannot achieve alone. So going back to production, development and governance. GraphRAG provides a higher accuracy, and complete answers a runtime. As from a developer perspective, once you build up the graph, it's easier to maintain it. 

[03:46] Than it is with a traditional RAG. And subsequently, once you're  querying it, you will get better explainability, and traceability, and access controls. Thank you for watching. And hope you like this video. If you have any questions or comments, let me know below and don't forget to like and subscribe for more content like this. 
