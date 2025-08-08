🌬️ Streamer domain role FAQ
===

![](<./📎 Assets/📨 Streamer.png>)

1. **What is a Streamer domain role in NLWeb?**

    A Streamer is an [🪢 Integrator](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🔌🎭 Integrator role.md>) domain that pushes events to subscriber domains.

    ---

1. **What are examples of streams?**

    - [Graphs 🕸](<../44 📜 Manifests/03 🕸👥 Graph helper.md>) subscribe to Manifest updates from [Listeners 👂](<../44 📜 Manifests/02 👂👥 Listener helper.md>) to build their graph databases.
    - [Finders 🔎](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) subscribe to [Graphs 🕸](<../44 📜 Manifests/03 🕸👥 Graph helper.md>), [Advertisers 👀](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>), and [Reviewers ⭐](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) to build their search index.
    - [Firewalls 🔥](<../43 👍 Trusts/03 🔥👥 Firewall helper.md>) subscribe to [Listeners 👂](<../44 📜 Manifests/02 👂👥 Listener helper.md>) and [Graphs 🕸](<../44 📜 Manifests/03 🕸👥 Graph helper.md>) to ensure domain compliance.

    ---

1. **Do Streamers push messages?**

    Yes. NLWeb advocates for subscribers to bind to a [⏳ Buffer](<03 ⏳👥 Buffer helper.md>) for increased resilience.

    ---

1. **What if a push fails with a timeout or 5XX error?**

    Streamers will retry to push events to subscribers with exponential back-off for up to 2 days. After that, the event is discarded.

    ---

1. **What if a push fails with a 4XX HTTP error?**

    The event is discarded - Streamers assume that the subscriber does not want the message.

    ---

1. **What if a subscriber returns a 429 Too Many Requests?**

    The event is discarded nonetheless - subscribers are responsible to ensure ingestion capacity, or should otherwise delegate it to Buffer domains.

    ---

1. **How can subscribers delegate to a Buffer domain?**

    When subscribing, subscribers can assign a Buffer.

    ---

1. **How to prevent Buffers from spoofing the events?**

    When using a Buffer, Streamers encrypt the event content with the public key of the subscriber. For details, see Buffer domains.

    ---
