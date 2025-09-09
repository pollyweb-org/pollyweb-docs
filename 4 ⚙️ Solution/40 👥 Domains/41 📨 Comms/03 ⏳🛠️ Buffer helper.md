<!-- #TODO -->

⏳ Buffer domains FAQ
===

1. **What is a Buffer domain in NLWeb?**

    Buffers ⏳ are point-to-point [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that:
    * ingest events from [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) with high availability and high ingestion throughput; 
    * and then throttle the deliver of those events to [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) according to an agreed delivery policy. 
    
    ---

2. **How do Buffers work?**

    ![](<.📎 Assets/📨⏳ Buffer.png>)

    |#| Step
    |-|-
    |1| Before sending an event, [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) read the public key from the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>).
    |2| When sending an event, [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) encrypt the content of the event with the Subscriber's public key, then send the encrypted event to the Subscriber's Buffer ⏳.
    |3| Upon receiving an event, if the queue of the Subscriber's Buffer ⏳ is empty, then the Buffer ⏳ wakes up the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>).
    |4| The [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) then wakes up and consumers all the events in the Buffer's ⏳ queue, decrypting them with its own private key from the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key-pair; once the queue is empty, it goes back to sleep.
    
    ---

3. **Why are Buffers important?**

    Buffers ⏳ handle the difference in speed and availability between two [domains 👥](<../44 📜 Manifests/00 👥 Domain.md>), allowing for faster [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) to continue without waiting for the slower receiver.

    * **Sending**: Buffers ⏳ allow [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) to publish events in real-time with a high-throughput push architecture, without considering the receivers' availability or ingestion capacity.
    
    * **Receiving**: Buffers ⏳ allow slow intermittent [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) to consume the events at their own pace by using a poll architecture, while allowing for near-real-time event delivery by leveraging wake-up calls.

    ---

4. **How can Buffers improve network latency?**

    Buffers ⏳ may use the following techniques to improve network latency when the [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>) and geographically distant from the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) (e.g., in different continents):

    * Use content-delivery networks (CDNs) to place the ingestion API as close as possible to the [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>), and the delivery API as close as possible to the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) (e.g., AWS Points of Presence).
  
    * Instead of using the public Internet to transfer the events, use instead a private global network from a single cloud provider (e.g., AWS Network) to reduce the number of network hoops between the [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>) and the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>).

    * Compress the event payload.

    ---

5. **Is the content of events kept private from Buffers?**

    Yes. 
    
    * When a [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>) is about to push an event to a receiver's Buffer ⏳, it first reads the public key of the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) from its [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) DNS record, then uses the public key to encrypt the content of the event.
  
    * When the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) polls the events, it uses its private key to decrypt the event's content.
    
    * This way, Buffers ⏳ cannot read the content of events.

    ---



1. **For how long do Buffers hold events?**

    It depends.
    * [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) define how long they want their Buffers ⏳ to store pending messages, by setting how long to keep the events before they expire.
    * These settings include:
        * expiration for unhandled events in the queue;
        * expiration for failed events in the dead-letter queue (DLQ); 
        * and expiration for replay events.

    ---



2. **What if a wake-up request fails?**

    Sometimes, [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) may be unreachable due to downtime, malfunctions, and unexpected network issues. 
    * To account for network issues during a weekend, Buffers ⏳ retry to wake-up [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) with exponential back-off for 3 days.
    * To account for downtimes and malfunctions, [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) should perform a poll whenever they restart. 

    ---

3. **Do Buffers allow events to be replayed?**

    Yes, optionally.
    * Replay allows a [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) to change their handling logic, then go back into the past and process again all events received from a given date (e.g., for A/B testing of new features).
    * [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) can choose to store all events received by their Buffer ⏳, for some time, for future replay.
    * This includes both successfully and unsuccessfully handled events.

    ---


2. **Do Buffers allow Subscribers to poll in batch?**

    Yes, optionally.
    * Buffers ⏳ allow [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) to poll in batch (i.e., multiple events per poll). 
    * [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) can choose to poll only individual events or batches of events.
    * [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) choose the size of the batch - i.e., the maximum number of events per poll.

    ---

3. **Do Buffers allow Subscribers to poll in parallel?**

    Yes, except for first-in-first-out (FIFO) delivery.
    * [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) can use multiple parallel connections to increase the polling throughput.
    * When a [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) polls events, Buffers ⏳ hide the events polled for a while until their successful handling is confirmed.
    * [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) can confirm either the success of the entire poll with one or more events, or confirm only specific events in the case of a partially successful pool.
    * If an event is not confirmed after a while, it becomes available again for polling.

    ---

4.  **Do Buffers ensure delivery order?**

    Yes, but optionally and without parallel pooling.
    * [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) can ask their Buffer ⏳ to be first-in-first-out (FIFO), based on when the [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>) pushed the event.
    * The Buffer ⏳ will wait for the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) to confirm the successful handling of older events before releasing new ones.

    ---

5. **What if an event is not confirmed?**

    If an event is not confirmed before it expires, then the event becomes available again for polling.
    * Buffers ⏳ will repeat this for a few times (typically three), until the event is removed from the queue.
    * If the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) asked for a dead-letter queue (DLQ) then the event is moved to there until DQL timeout.
    * If the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) asked for replay storage, then the event is stored for replay until replay timeout.
    
    ---

1. **Do Buffers support re-drive?**

    Yes.
    * [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) may ask their Buffer ⏳ to move all the events in the dead-letter queue (DLQ) to the main queue, ad-hoc.
    * This allows [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) to fix bugs and handle transient errors.
    * Re-drive can also be performed periodically (e.g., every night) or conditionally (e.g., when the queue is empty).
  
    ---