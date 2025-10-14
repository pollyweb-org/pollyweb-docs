🔔 Subscriber domain role
===

1. **What is a Subscriber domain role in NLWeb?**

    A Subscriber 🔔 is any [domain 👥](<../41 📨 Msgs/00 👥 Domain.md>) that 
    * leverages a [Buffer ⏳ helper domain](<03 ⏳🛠️ Buffer helper.md>) 
    * to subscribe to events from a [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>).

    ---
    <br/>

1. **How do Subscribers work?**

    ![alt text](<../41 📨 Msgs/.📎 Assets/📨🔔 Subscriber.png>)

    |#| Step
    |-|-
    |1| A [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) binds one single time with a selected [Buffer ⏳ helper domain](<03 ⏳🛠️ Buffer helper.md>).
    |2| The [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) then subscribes to a stream from a [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>), informing the [Buffer ⏳ helper domain](<03 ⏳🛠️ Buffer helper.md>).
    |3| The [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>) pushes an encrypted event through the [Buffer ⏳ helper domain](<03 ⏳🛠️ Buffer helper.md>), who places it in a queue.
    |4| If the queue in the [Buffer ⏳ helper domain](<03 ⏳🛠️ Buffer helper.md>) is empty, then it wakes up the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) to start polling.
    |5| The [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) polls event [3] from the [Buffer ⏳ helper domain](<03 ⏳🛠️ Buffer helper.md>), and decrypts it with its [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) private key.
    |6| The [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>) pushes another encrypted event.
    |7| The [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>) pushes yet another encrypted event.
    |8| The [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) polls again, consuming events [6] and [7].
    |9| The [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) polls again but the queue is empty, so it goes back to sleep.
    

    ---
    <br/>
 
1. **Do Subscribers implement a push or a poll architecture?**

    [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) implement a combination of both:
    - they support push wake-up notifications from their bound [Buffer ⏳ helper domain](<03 ⏳🛠️ Buffer helper.md>);
    - then poll events from [Buffer ⏳ helper domain](<03 ⏳🛠️ Buffer helper.md>) until no events are returned.

    ---
    <br/>

1. **What are examples of event subscribers?**

    * [Graph 🕸 helper domains](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>) build their graph databases with subscriptions to [domain Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>) updates from [Listener 👂 streams](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>).
  
    * [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) build their search index with subscriptions to [Graph 🕸](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>), [Advertiser 👀](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>), and [Reviewer ⭐](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) streams.
    
    * [Firewall 🔥 helper domains](<../43 👍 Trusts/03 🔥🛠️ Firewall helper.md>) subscribe to [Listener 👂](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>) and [Graph 🕸](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>) streams to ensure domain compliance.


    ---
    <br/>

1. **Do receivers need to poll indefinitely?**
    
    No. 
    * [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) can sleep when no events are returned from a poll. 
    * [Buffer ⏳ helper domains](<03 ⏳🛠️ Buffer helper.md>) will wake up [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) whenever necessary. 

    ---
    <br/>



1. **Can a Subscriber perform multiple polls in parallel?**

    Yes, except when using FIFO (first-in-first-out).
    * [Buffer ⏳ helper domains](<03 ⏳🛠️ Buffer helper.md>) manage the visibility of in-flight events, allowing [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) to perform polls in parallel.
    * After a [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) pools an event, it needs to confirm its successful handing.
    * Otherwise,  after a pre-defined time, the event will become available again for polling.

    ---
    <br/>
