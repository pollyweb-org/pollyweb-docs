🌬️ Streamer domain role FAQ
===

1. **What is a Streamer domain role in NLWeb?**

    A Streamer 🌬️ is any [domain 👥](<../44 📜 Manifests/00 👥 Domain.md>) that pushes and replays events to [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) via their [Buffer ⏳ helpers](<03 ⏳🛠️ Buffer helper.md>).

    ---

1. **How do Streamer domains work?**

    ![](<.📎 Assets/📨🌬️ Streamer-simple.png>)

    |Step|Description
    |-|-
    |0| [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) first need to subscribe to a Streamer 🌬️ by providing their [Buffer ⏳ helper](<03 ⏳🛠️ Buffer helper.md>).
    |1, 2, 3| Streamers 🌬️ then publish events at any time to the [Buffer ⏳ helper](<03 ⏳🛠️ Buffer helper.md>).
    |4| [Buffer ⏳ helpers](<03 ⏳🛠️ Buffer helper.md>) deliver the events to [Subscriber 🔔 domains](<04 🔔🎭 Subscriber role.md>) according to a set delivery policy.

    ---

1. **What are examples of domain event streams?**

    * [Listener 👂 domains](<../44 📜 Manifests/02 👂👥 Listener helper.md>) and [Graph 🕸 domains](<../44 📜 Manifests/03 🕸👥 Graph helper.md>) stream domain [Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>) updates.
    * [Advertiser 👀 domains](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) and [Reviewer ⭐ domains](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) stream feedbacks about [Host 🤗 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>).
    * [Persona 🧢 agents](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) stream changes performed by the user.

    ---

2. **Do Streams guarantee unique delivery?**

    No. 
    * The same event may be delivered more than once.
    * [Buffer ⏳ helpers](<03 ⏳🛠️ Buffer helper.md>) are responsible for deduping when necessary.

    ---

2. **Do Streams guarantee ordered delivery?**

    No. 
    * While events have timestamps, they may be delivered out of order.
    * [Buffer ⏳ helpers](<03 ⏳🛠️ Buffer helper.md>) are responsible for ordering events when necessary.

    ---

3. **What if a push fails with a timeout or 5XX error?**

    Upon receiving a timeout or 5XX error from a [Buffer ⏳ helper](<03 ⏳🛠️ Buffer helper.md>), 
    * Streamers 🌬️ will retry to push events with exponential back-off for up to 24 hours. 
    * After that, the event is discarded.

    ---

4. **What if a push fails with a 4XX HTTP error?**

    Upon receiving a non-authorized 4XX error from a [Buffer ⏳ helper](<03 ⏳🛠️ Buffer helper.md>), 
    * Streamers 🌬️ assume that the [Buffer ⏳ helper](<03 ⏳🛠️ Buffer helper.md>) does not want the message, 
    * and the event is discarded.

    ---

5. **What if a Subscriber returns a 429 Too Many Requests?**

    Upon receiving a 429 Too Many Requests from a [Buffer ⏳ helper](<03 ⏳🛠️ Buffer helper.md>), 
    * Streamers 🌬️ conclude that the [Buffer ⏳ helper](<03 ⏳🛠️ Buffer helper.md>) is failing to do its one and only job, 
    * and the event is discarded nonetheless.

    ---

6. **How to prevent Buffers from spoofing the events?**

    To avoid spoofing, Streamers 🌬️ encrypt the event content with the public key of the [Subscriber 🔔 domain](<04 🔔🎭 Subscriber role.md>) before sending it to the Subscriber's [Buffer ⏳ helper](<03 ⏳🛠️ Buffer helper.md>).

    ---
