# Apache Kafka Fundamentals You Should Know
ByteByteGo · 4 мин · 447161 просмотров · en · https://youtu.be/-RDyEFvnTXI



[00:00] kfka power some of the world's largest data pipelines and real-time streaming applications but for many getting started feels overwhelming in the next few minutes we'll break down the essentials into straightforward b-size Concepts let's start at the top what exactly is Kafka think of Kafka as a distributed event store and realtime streaming platform it was initially developed at LinkedIn and has become the foundation for data heavy applications here's how it works producers 

[00:31] essentially the sources of a data send data to CFA Brokers these Brokers store and manage everything then consumer groups come in to process this data based on their unique needs now onto messages the heart of Kafka every piece of data Kafka handles is a message a Kafka message is three parts headers which carry metadata the key which helps your organization and the value which is the actual deploy payload this structured approach is what make kfka so 

[01:02] efficient handling large volumes of data now that we understand what the message is let's look at how Kafka organizes these messages using topics and partitions messages aren't just tossed into Kafka they're organized into topics categories that help structure the data streams within each topic Kafka goes a step further by dividing it into partitions these partitions are key to Kafka scalability because they allow messages to be processed in parallel across multiple consumers to achieve 

[01:34] high throughput so why do many companies choose Kafka let's talk about what makes it so powerful first Cafe is great at handling multiple producers sending data simultaneously without performance degradation it also handles multiple consumers efficiently by allowing different consumer groups to read from the same topic independently kka track was been consumed using consumer offset store within kfka itself this ensures that consumers can resume processing from 

[02:05] where they left off in case of failure on top of that Kafka provides this spased retention policies that allow us to store messages even after they've been consumed based on time or size limits we Define nothing is lost unless we decide it's time to clear it finally capus scalability means we can start small and grow as the needs expand now let's look at prod producers the applications that create and send messages to Kafka producers batch 

[02:35] messages together to cut down a network traffic they use partitioners to determine which partition a message should go to if no key is provided messages are distributed randomly across partitions if a key is present messages with the same key are sent to the same partition for better Distribution on the receiving end we have consumers and consumer groups consumers Within a group share responsibility for processing messages from different petitions in parallel each petition is assigned to 

[03:07] only one consumer within a group at any given time if one consumer fails another automatically takes over its workload to ensure uninterrupted processing consumers in a group divide up partions among themselves through coordination by cfa's group coordinator when a consumer joins or leaves the group Capa triggers a rebalance to redistribute partitions among the remaining consumers the kfka cluster itself is made up of multiple Brokers these are servers that store and manage our data to keep our data safe 

[03:40] each partition is replicated across several Brokers using a leader follower model if one broker fails and other one steps in as new leader without losing any data in earlier versions Capco relies on zookeeper to manage broker metadata and leader election however newer versions are transitioning to craft a building consensus mechanism that simplify operations by eliminating zookeeper as an external dependency while improving scalability lastly let's quickly touch 

[04:11] on where cfers excels in the real world it's widely used for log aggregation from thousands of servers is often chosen for realtime event streaming from various sources for change data capture it keeps database synchronized across systems and is invaluable for system monitoring ing by collecting metrics for dashboards and alerts across Industries like Finance Healthcare retail and iot if you like our videos you might like a system design newsletter as well 

[04:43] it covers topics and Trends in large scale system design trusted by a million readers subscribe at blog. byby go.com 
