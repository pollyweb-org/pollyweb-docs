🌬️ Streamer domain role FAQ
===

![](<.📎 Assets/📨 Streamer.png>)

1. **What is a Streamer domain role in NLWeb?**

    A Streamer is an [Integrator 🪢 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🪢🎭 Integrator role.md>) that pushes events to subscriber [Domains 👥](<../44 📜 Manifests/00 👥 Domain.md>).

    ---

2. **What are examples of event streams?**

    - [Graph 🕸 domains](<../44 📜 Manifests/03 🕸👥 Graph helper.md>) subscribe to Manifest updates from [Listeners 👂](<../44 📜 Manifests/02 👂👥 Listener helper.md>) to build their graph databases.
    - [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) subscribe to [Graph 🕸 domains](<../44 📜 Manifests/03 🕸👥 Graph helper.md>), [Advertiser 👀 domains](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>), and [Reviewer ⭐ domains](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) to build their search index.
    - [Firewall 🔥 domains](<../43 👍 Trusts/03 🔥🛠️ Firewall helper.md>) subscribe to [Listener 👂 domains](<../44 📜 Manifests/02 👂👥 Listener helper.md>) and [Graphs 🕸 domains](<../44 📜 Manifests/03 🕸👥 Graph helper.md>) to ensure domain compliance.

    ---

3. **Do Streamers push messages?**

    Yes. NLWeb advocates for subscribers to bind to a [⏳ Buffer](<03 ⏳🛠️ Buffer helper.md>) for increased resilience.

    ---

4. **What if a push fails with a timeout or 5XX error?**

    Streamers will retry to push events to subscribers with exponential back-off for up to 2 days. After that, the event is discarded.

    ---

5. **What if a push fails with a 4XX HTTP error?**

    The event is discarded - Streamers assume that the subscriber does not want the message.

    ---

6. **What if a subscriber returns a 429 Too Many Requests?**

    The event is discarded nonetheless - subscribers are responsible to ensure ingestion capacity, or should otherwise delegate it to Buffer domains.

    ---

7. **How can subscribers delegate to a Buffer domain?**

    When subscribing, subscribers can assign a Buffer.

    ---

8. **How to prevent Buffers from spoofing the events?**

    When using a Buffer, Streamers encrypt the event content with the public key of the subscriber. For details, see Buffer domains.

    ---
