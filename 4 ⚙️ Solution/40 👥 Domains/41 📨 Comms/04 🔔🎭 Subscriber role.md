🔔 Subscriber domain role FAQ
===

1. **What is a Subscriber domain role in NLWeb?**

    A Subscriber 🔔 role is a [domain 👥](<../44 📜 Manifests/00 👥 Domain.md>) that leverage a [Buffer ⏳ helper](<03 ⏳🛠️ Buffer helper.md>) to subscribe to events from a [Streamer 🌬️ domain](<02 🌬️🎭 Streamer role.md>).

    ---

2. **What are examples of event subscribers?**

    * [Graph 🕸 domains](<../44 📜 Manifests/03 🕸👥 Graph helper.md>) build their graph databases with subscriptions to [Manifest](<../44 📜 Manifests/01 📜 Domain Manifest.md>) updates from [Listener 👂 streams](<../44 📜 Manifests/02 👂👥 Listener helper.md>).
  
    * [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) build their search index with subscriptions to [Graph 🕸](<../44 📜 Manifests/03 🕸👥 Graph helper.md>), [Advertiser 👀](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>), and [Reviewer ⭐](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) streams.
    
    * [Firewall 🔥 domains](<../43 👍 Trusts/03 🔥🛠️ Firewall helper.md>) subscribe to [Listener 👂](<../44 📜 Manifests/02 👂👥 Listener helper.md>) and [Graph 🕸](<../44 📜 Manifests/03 🕸👥 Graph helper.md>) streams to ensure domain compliance.

    ---