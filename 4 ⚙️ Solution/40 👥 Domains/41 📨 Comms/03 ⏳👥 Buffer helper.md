#TODO

⏳ Buffer domains FAQ
===

![](<./📎 Assets/📨 Buffer.png>)

1. **What is a Buffer domain in NLWeb?**

    Buffers are point-to-point services that transport events from one domain to another, while committing to high availability and high ingestion throughput. 
    
    ---

1. **Why are Buffers important?**

    Buffers handle the difference in speed and availability between two domains, allowing for faster [🌬️ Streamers](<02 🌬️🎭 Streamer role.md>) to continue without waiting for the slower receiver.

    - For Streamers, Buffers allow high-throughput Streamers to publish events without considering the receivers' availability or ingestion capacity.
    
    - For receivers, Buffers allow slow intermittent receivers to consume the events at their own pace.

    ---

1. **Do Buffers implement a push or poll architecture?**

    Buffers implement a combination of both:
    - they use push notifications to wake up receivers;
    - then requires receivers to poll the pending events.

    ---

1. **Do Buffers support multiple subscribers of an event?**

    No. 
    - Buffers are domain to domain only.

    ---

1. **Do receivers pool indefinitely?**
    
    No. 
    - receivers can sleep if there are no more events to poll. 
    - Buffers wake up receivers when new events arrive. 

    ---

1. **What if a wake-up request fails?**

    Buffers will retry to wake-up receivers with exponential back-off for up to 30 days. 

    ---

1. **Do Buffers support dead-letter queues (DLQ)?**

    Yes. 
    - receivers define the Buffer's retry policy, indicating when events should be moved to a DLQ if polled but not confirmed within the expiration window.

    ---

1. **Is the content of events kept private from Buffers?**

    Yes. 
    - When a [🌬️ Streamer](<02 🌬️🎭 Streamer role.md>) is about to push an event to a receiver's Buffer, it first reads the receiver's public key from its DKIM DNS record, then uses the public key to encrypt the content of the event.
    - When receivers poll the events, they use their private key to decrypt the event's content.

    ---

1. **How can a Buffer be implemented on AWS?**

    ![](<./📎 Assets/📨 Buffer@AWS.png>)

    Buffers rely on the following components for domain [📨 Messaging](<01 📨 Domain Message.md>):
    - 🏌️‍♂️ **Distributer**: a DNS plus CDN configuration;
    - ⛳ **Endpoint**: an API endpoint that verifies message signatures;
    - 📮 **Async Post**: an async message outbound that signs messages.

    ---

1. **How can a Buffer clients implement message polling on AWS?**

    ![](<./📎 Assets/📨 BufferPuller@AWS.png>)

    Buffer clients rely on an Inbox components for domain [📨 Messaging](<01 📨 Domain Message.md>) - this is an API endpoint with CDN that verifies message signatures.

    ---
