🔔 Subscriber domain role
===

1. **What is a Subscriber domain role in NLWeb?**

    A Subscriber 🔔 is any [domain 👥](<../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) that 
    * leverages a [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>) 
    * to subscribe to events from a [Streamer 🌬️ domain](<../75 🌬️ Streamers/🌬️🎭 Streamer role.md>).

    ---
    <br/>

1. **How do Subscribers work?**

    ![alt text](<.📎 Assets/🔔 Subscriber.png>)

    |#| Step
    |-|-
    |1| A [Subscriber 🔔 domain](<🔔🎭 Subscriber role.md>) binds one single time with a selected [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>).
    |2| The [Subscriber 🔔 domain](<🔔🎭 Subscriber role.md>) then subscribes to a stream from a [Streamer 🌬️ domain](<../75 🌬️ Streamers/🌬️🎭 Streamer role.md>), informing the [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>).
    |3| The [Streamer 🌬️ domain](<../75 🌬️ Streamers/🌬️🎭 Streamer role.md>) pushes an encrypted event through the [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>), who places it in a queue.
    |4| If the queue in the [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>) is empty, then it wakes up the [Subscriber 🔔 domain](<🔔🎭 Subscriber role.md>) to start polling.
    |5| The [Subscriber 🔔 domain](<🔔🎭 Subscriber role.md>) polls event [3] from the [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>), and decrypts it with its [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) private key.
    |6| The [Streamer 🌬️ domain](<../75 🌬️ Streamers/🌬️🎭 Streamer role.md>) pushes another encrypted event.
    |7| The [Streamer 🌬️ domain](<../75 🌬️ Streamers/🌬️🎭 Streamer role.md>) pushes yet another encrypted event.
    |8| The [Subscriber 🔔 domain](<🔔🎭 Subscriber role.md>) polls again, consuming events [6] and [7].
    |9| The [Subscriber 🔔 domain](<🔔🎭 Subscriber role.md>) polls again but the queue is empty, so it goes back to sleep.
    

    ---
    <br/>
 
1. **Do Subscribers implement a push or a poll architecture?**

    [Subscriber 🔔 domains](<🔔🎭 Subscriber role.md>) implement a combination of both:
    - they support push wake-up notifications from their bound [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>);
    - then poll events from [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>) until no events are returned.

    ---
    <br/>

1. **What are examples of event subscribers?**

    * [Graph 🕸 helper domains](<../../45 🤲 Helper domains/50 🕸 Graphs/🕸🤲 Graph helper.md>) build their graph databases with subscriptions to [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/📜 Manifest.md>) updates from [Listener 👂 streams](<../../45 🤲 Helper domains/60 👂 Listeners/👂🤲 Listener helper.md>).
  
    * [Finder 🔎 domains](<../../50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) build their search index with subscriptions to [Graph 🕸](<../../45 🤲 Helper domains/50 🕸 Graphs/🕸🤲 Graph helper.md>), [Advertiser 👀](<../../45 🤲 Helper domains/12 👀 Advertisers/👀🤲 Advertiser helper.md>), and [Reviewer ⭐](<../../50 🫥 Agent domains/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) streams.
    
    * [Firewall 🔥 helper domains](<../../45 🤲 Helper domains/40 🔥 Firewalls/🔥🤲 Firewall helper.md>) subscribe to [Listener 👂](<../../45 🤲 Helper domains/60 👂 Listeners/👂🤲 Listener helper.md>) and [Graph 🕸](<../../45 🤲 Helper domains/50 🕸 Graphs/🕸🤲 Graph helper.md>) streams to ensure domain compliance.


    ---
    <br/>

1. **Do receivers need to poll indefinitely?**
    
    No. 
    * [Subscriber 🔔 domains](<🔔🎭 Subscriber role.md>) can sleep when no events are returned from a poll. 
    * [Buffer ⏳ helper domains](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>) will wake up [Subscriber 🔔 domains](<🔔🎭 Subscriber role.md>) whenever necessary. 

    ---
    <br/>



1. **Can a Subscriber perform multiple polls in parallel?**

    Yes, except when using FIFO (first-in-first-out).
    * [Buffer ⏳ helper domains](<../../45 🤲 Helper domains/27 ⏳ Buffers/⏳🤲 Buffer helper.md>) manage the visibility of in-flight events, allowing [Subscriber 🔔 domains](<🔔🎭 Subscriber role.md>) to perform polls in parallel.
    * After a [Subscriber 🔔 domain](<🔔🎭 Subscriber role.md>) pools an event, it needs to confirm its successful handing.
    * Otherwise,  after a pre-defined time, the event will become available again for polling.

    ---
    <br/>
