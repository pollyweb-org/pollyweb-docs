🌬️ Streamer domain role
===

1. **What is a Streamer domain role in NLWeb?**

    A Streamer 🌬️ is any [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) that 
    * pushes and replays events to [Subscriber 🔔 domains](<../Subscribers 🔔/🔔🎭 Subscriber role.md>) 
    * via the Subscribers' [Buffer ⏳ helper domains](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>).

    ---
    <br/>

1. **How do Streamer domains work?**

    ![](<.📎 Assets/🌬️ Streamer-simple.png>)

    |Steps|Description
    |-|-
    |0| [Subscriber 🔔 domains](<../Subscribers 🔔/🔔🎭 Subscriber role.md>) first need to subscribe to a [Streamer 🌬️ domain](<🌬️🎭 Streamer role.md>) by providing their [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>).
    |1, 2, 3| [Streamer 🌬️ domains](<🌬️🎭 Streamer role.md>) then publish events at any time to the [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>).
    |4| [Buffer ⏳ helper domains](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) deliver the events to [Subscriber 🔔 domains](<../Subscribers 🔔/🔔🎭 Subscriber role.md>) according to a set delivery policy.

    ---
    <br/>

1. **What are examples of domain event streams?**

    * [Listener 👂 domains](<../../45 🤲 Helper domains/Listeners 👂/👂🤲 Listener helper.md>) and [Graph 🕸 domains](<../../45 🤲 Helper domains/Graphs 🕸/🕸🤲 Graph helper.md>) stream domain [Manifest 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) updates.
    * [Advertiser 👀 domains](<../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) and [Reviewer ⭐ domains](<../../50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐🫥 Reviewer agent.md>) stream feedbacks about [Host 🤗 domain](<../Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).
    * [Persona 🧢 agent domains](<../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) stream changes performed by the user.

    ---
    <br/>

1. **Do Streams guarantee unique delivery?**

    No. 
    * The same event may be delivered more than once.
    * [Buffer ⏳ helper domains](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) are responsible for deduping when necessary.

    ---
    <br/>

1. **Do Streams guarantee ordered delivery?**

    No. 
    * While events have timestamps, they may be delivered out of order.
    * [Buffer ⏳ helper domains](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) are responsible for ordering events when necessary.

    ---
    <br/>

1. **What if a push fails with a timeout or 5XX error?**

    Upon receiving a timeout or 5XX error from a [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>), 
    * [Streamer 🌬️ domains](<🌬️🎭 Streamer role.md>) will retry to push events with exponential back-off for up to 24 hours. 
    * After that, the event is discarded.

    ---
    <br/>

1. **What if a push fails with a 4XX HTTP error?**

    Upon receiving a non-authorized 4XX error from a [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>), 
    * [Streamer 🌬️ domains](<🌬️🎭 Streamer role.md>) assume that the [Buffer ⏳ domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) does not want the message, 
    * and the event is discarded.

    ---
    <br/>

1. **What if a Subscriber returns a 429 Too Many Requests?**

    Upon receiving a 429 Too Many Requests from a [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>), 
    * [Streamer 🌬️ domains](<🌬️🎭 Streamer role.md>) conclude that the [Buffer ⏳ domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) is failing to do its one and only job, 
    * and the event is discarded nonetheless.

    ---
    <br/>

1. **How to prevent Buffers from spoofing the events?**

    To avoid spoofing, [Streamer 🌬️ domains](<🌬️🎭 Streamer role.md>) encrypt the event content with the [DKIM public key 📨](<../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) of the [Subscriber 🔔 domain](<../Subscribers 🔔/🔔🎭 Subscriber role.md>) before sending it to the Subscriber's [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>).

    ---
    <br/>
