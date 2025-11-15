⏳ Buffer helper domains
===

> Mentioned in [📨 Domain Message](<../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)

> Reference by [Domain@Graph 🚀 method](<../Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Domain/🕸 Domain 🚀 request.md>)

<br/>

1. **What is a Buffer domain in NLWeb?**

    A [Buffer ⏳ domain](<⏳🤲 Buffer helper.md>) 
    * is a point-to-point [Helper 🤲 domain](<../$ Helpers 🤲/🤲👥 Helper domain.md>)
    * that ingests events from [Streamer 🌬️ domains](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) with high availability and high ingestion throughput
    * and then throttle the deliver of those events to [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) according to an agreed delivery policy. 
    
    ---
    <br/>

1. **How do Buffers work?**

    ![](<.📎 Assets/⏳ Buffer.png>)

    |#| Step
    |-|-
    |1| Before sending an event, [Streamer 🌬️ domains](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) read the public key from the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>).
    |2| When sending an event, [Streamer 🌬️ domains](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) encrypt the content of the event with the Subscriber's public key, then send the encrypted event to the Subscriber's [Buffer ⏳ domain](<⏳🤲 Buffer helper.md>).
    |3| Upon receiving an event, if the queue of the Subscriber's Buffer ⏳ is empty, then the [Buffer ⏳ domain](<⏳🤲 Buffer helper.md>) wakes up the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>).
    |4| The [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) then wakes up and consumers all the events in the Buffer's ⏳ queue, decrypting them with its own private key from the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key-pair; once the queue is empty, it goes back to sleep.
    
    ---
    <br/>

1. **Why are Buffers important?**

    [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) handle the difference in speed and availability between two [domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>), allowing for faster [Streamer 🌬️ domains](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) to continue without waiting for the slower receiver.

    * **Sending**: [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) allow [Streamer 🌬️ domains](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) to publish events in real-time with a high-throughput push architecture, without considering the receivers' availability or ingestion capacity.
    
    * **Receiving**: [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) allow slow intermittent [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) to consume the events at their own pace by using a poll architecture, while allowing for near-real-time event delivery by leveraging wake-up calls.

    ---
    <br/>

1. **How can Buffers improve network latency?**

    [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) may use the following techniques to improve network latency when the [Streamer 🌬️ domain](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) and geographically distant from the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) (e.g., in different continents):

    * Use content-delivery networks (CDNs) to place the ingestion API as close as possible to the [Streamer 🌬️ domain](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>), and the delivery API as close as possible to the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) (e.g., AWS Points of Presence).
  
    * Instead of using the public Internet to transfer the events, use instead a private global network from a single cloud provider (e.g., AWS Network) to reduce the number of network hoops between the [Streamer 🌬️ domain](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) and the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>).

    * Compress the event payload.

    ---
    <br/>

1. **Is the content of events kept private from Buffers?**

    Yes. 
    
    * When a [Streamer 🌬️ domain](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) is about to push an event to a receiver's [Buffer ⏳ domain](<⏳🤲 Buffer helper.md>), it first reads the public key of the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) from its [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) DNS record, then uses the public key to encrypt the content of the event.
  
    * When the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) polls the events, it uses its private key to decrypt the event's content.
    
    * This way, [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) cannot read the content of events.

    ---
    <br/>



1. **For how long do Buffers hold events?**

    It depends.
    * [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) define how long they want their [Buffer ⏳ helper domains](<⏳🤲 Buffer helper.md>) to store pending messages, by setting how long to keep the events before they expire.
    * These settings include:
        * expiration for unhandled events in the queue;
        * expiration for failed events in the dead-letter queue (DLQ); 
        * and expiration for replay events.

    ---
    <br/>



1. **What if a wake-up request fails?**

    Sometimes, [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) may be unreachable due to downtime, malfunctions, and unexpected network issues. 
    * To account for network issues during a weekend, [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) retry to wake-up [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) with exponential back-off for 3 days.
    * To account for downtimes and malfunctions, [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) should perform a poll whenever they restart. 

    ---
    <br/>

1. **Do Buffers allow events to be replayed?**

    Yes, optionally.
    * Replay allows a [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) to change their handling logic, then go back into the past and process again all events received from a given date (e.g., for A/B testing of new features).
    * [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) can choose to store all events received by their [Buffer ⏳ helper domain](<⏳🤲 Buffer helper.md>), for some time, for future replay.
    * This includes both successfully and unsuccessfully handled events.

    ---
    <br/>


1. **Do Buffers allow Subscribers to poll in batch?**

    Yes, optionally.
    * [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) allow [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) to poll in batch (i.e., multiple events per poll). 
    * [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) can choose to poll only individual events or batches of events.
    * [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) choose the size of the batch - i.e., the maximum number of events per poll.

    ---
    <br/>

1. **Do Buffers allow Subscribers to poll in parallel?**

    Yes, except for first-in-first-out (FIFO) delivery.
    * [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) can use multiple parallel connections to increase the polling throughput.
    * When a [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) polls events, [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) hide the events polled for a while until their successful handling is confirmed.
    * [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) can confirm either the success of the entire poll with one or more events, or confirm only specific events in the case of a partially successful pool.
    * If an event is not confirmed after a while, it becomes available again for polling.

    ---
    <br/>

1. **Do Buffers ensure delivery order?**

    Yes, but optionally and without parallel pooling.
    * [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) can ask their [Buffer ⏳ domain](<⏳🤲 Buffer helper.md>) to be first-in-first-out (FIFO), based on when the [Streamer 🌬️ domain](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) pushed the event.
    * The [Buffer ⏳ domain](<⏳🤲 Buffer helper.md>) will wait for the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) to confirm the successful handling of older events before releasing new ones.

    ---
    <br/>

1. **What if an event is not confirmed?**

    If an event is not confirmed before it expires, then the event becomes available again for polling.
    * [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) will repeat this for a few times (typically three), until the event is removed from the queue.
    * If the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) asked for a dead-letter queue (DLQ) then the event is moved to there until DQL timeout.
    * If the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) asked for replay storage, then the event is stored for replay until replay timeout.
    
    ---
    <br/>

1. **Do Buffers support re-drive?**

    Yes.
    * [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) may ask their [Buffer ⏳ domains](<⏳🤲 Buffer helper.md>) to move all the events in the dead-letter queue (DLQ) to the main queue, ad-hoc.
    * This allows [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) to fix bugs and handle transient errors.
    * Re-drive can also be performed periodically (e.g., every night) or conditionally (e.g., when the queue is empty).
  
    ---
    <br/>


1. **What API methods do Buffers expose?**

    | From | Method | Purpose
    |-|-|-
    | 👥 domain |[🐌 Feedback](<⏳🅰️ Buffer methods/👥🐌⏳ Feedback.md>) | Feedback on sent messages.
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) | [🚀 Queue](<⏳🅰️ Buffer methods/🔔🐌⏳ Queue.md>) | Create or change a queue.
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) |[🚀 Unqueue](<⏳🅰️ Buffer methods/🔔🐌⏳ Unqueue.md>) | Delete a queue.
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) |[🚀 Purge](<⏳🅰️ Buffer methods/🔔🚀⏳ Purge.md>) | Clean up a queue.
    |[🌬️ Streamer](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>)|[🐌 Push](<⏳🅰️ Buffer methods/🌬️🐌⏳ Push.md>) | Add a message to a queue.
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) |[🚀 Poll](<⏳🅰️ Buffer methods/🔔🚀⏳ Poll.md>) | Poll messages from a queue.
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) |[🚀 Confirm](<⏳🅰️ Buffer methods/🔔🚀⏳ Confirm.md>) | Remove a handled message.
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>)  | [🐌 Replay](<⏳🅰️ Buffer methods/🔔🐌⏳ Replay.md>) | Replay confirmed messages.
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>)  | [🐌 Redrive](<⏳🅰️ Buffer methods/🔔🐌⏳ Redrive.md>) | Replay messages in the DLQ.
    |