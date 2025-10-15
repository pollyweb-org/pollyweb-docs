🌬️ Streamer domain role
===

1. **What is a Streamer domain role in NLWeb?**

    A Streamer 🌬️ is any [domain 👥](<../41 📨 Messages/00 👥 Domain.md>) that 
    * pushes and replays events to [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) 
    * via the Subscribers' [Buffer ⏳ helper domains](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>).

    ---
    <br/>

1. **How do Streamer domains work?**

    ![](<../41 📨 Messages/.📎 Assets/📨🌬️ Streamer-simple.png>)

    |Steps|Description
    |-|-
    |0| [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) first need to subscribe to a [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>) by providing their [Buffer ⏳ helper domain](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>).
    |1, 2, 3| [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) then publish events at any time to the [Buffer ⏳ helper domain](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>).
    |4| [Buffer ⏳ helper domains](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>) deliver the events to [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) according to a set delivery policy.

    ---
    <br/>

1. **What are examples of domain event streams?**

    * [Listener 👂 domains](<../../42 Backbone/10 👂 Listeners/02 👂🛠️ Listener helper.md>) and [Graph 🕸 domains](<../../42 Backbone/20 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) stream domain [Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>) updates.
    * [Advertiser 👀 domains](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) and [Reviewer ⭐ domains](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) stream feedbacks about [Host 🤗 domain](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>).
    * [Persona 🧢 agent domains](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) stream changes performed by the user.

    ---
    <br/>

1. **Do Streams guarantee unique delivery?**

    No. 
    * The same event may be delivered more than once.
    * [Buffer ⏳ helper domains](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>) are responsible for deduping when necessary.

    ---
    <br/>

1. **Do Streams guarantee ordered delivery?**

    No. 
    * While events have timestamps, they may be delivered out of order.
    * [Buffer ⏳ helper domains](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>) are responsible for ordering events when necessary.

    ---
    <br/>

1. **What if a push fails with a timeout or 5XX error?**

    Upon receiving a timeout or 5XX error from a [Buffer ⏳ helper domain](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>), 
    * [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) will retry to push events with exponential back-off for up to 24 hours. 
    * After that, the event is discarded.

    ---
    <br/>

1. **What if a push fails with a 4XX HTTP error?**

    Upon receiving a non-authorized 4XX error from a [Buffer ⏳ helper domain](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>), 
    * [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) assume that the [Buffer ⏳ domain](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>) does not want the message, 
    * and the event is discarded.

    ---
    <br/>

1. **What if a Subscriber returns a 429 Too Many Requests?**

    Upon receiving a 429 Too Many Requests from a [Buffer ⏳ helper domain](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>), 
    * [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) conclude that the [Buffer ⏳ domain](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>) is failing to do its one and only job, 
    * and the event is discarded nonetheless.

    ---
    <br/>

1. **How to prevent Buffers from spoofing the events?**

    To avoid spoofing, [Streamer 🌬️ domains](<02 🌬️🎭 Streamer role.md>) encrypt the event content with the [DKIM public key 📨](<../41 📨 Messages/01 📨 Domain Message.md>) of the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) before sending it to the Subscriber's [Buffer ⏳ helper domain](<../../45 Helpers/10 ⏳ Buffers/03 ⏳🛠️ Buffer helper.md>).

    ---
    <br/>
