🕸 Graph helper domains
===

1. **What is a Graph domain in NLWeb?**

    A [Graph 🕸 domain](<03 🕸🛠️ Graph helper.md>) is 
    * any [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) 
    * that subscribes to [domain Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>) change events from [Listener 👂 domains](<02 👂🛠️ Listener helper.md>)
    * then builds network representations of [Trust 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>) relationships between [domains 👥](<../41 📨 Msgs/00 👥 Domain.md>)
    * including indirect relationships via [Authority 🏛️ domains](<../43 👍 Trusts/02 🏛️🛠️ Authority helper.md>). 

    ---
    <br/>

1. **What can domains use Graphs for?**

    [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) can answer the following questions synchronously from any [domain 👥](<../41 📨 Msgs/00 👥 Domain.md>).

    |Scope&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Question
    |-|-
    |[👥 Identity](<../41 📨 Msgs/00 👥 Domain.md>)| What's the identity of [domain 👥](<../41 📨 Msgs/00 👥 Domain.md>) `D`?
    |[👍 Trusts](<../43 👍 Trusts/01 👍 Domain Trust.md>) | Can I trust the data of [Schema 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) `S` sent by [domain 👥](<../41 📨 Msgs/00 👥 Domain.md>) `D`?
    |[👍 Trusts](<../43 👍 Trusts/01 👍 Domain Trust.md>) | Can I trust my data of [Schema 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) `S` to a [domain 👥](<../41 📨 Msgs/00 👥 Domain.md>) `D`?
    | [🧩 Schemas](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) | What's the schema definition of [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) `S`?
    | [🎫 Tokens](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) | What's the historical public [📨 DKIM](<../41 📨 Msgs/01 📨 Domain Message.md>) key of [🎫 Token](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) `T`?
    | [🪣 Datasets](<../../20 🧑‍🦰 UI/12 💬 Chats/07 🪣🎭 Dataset role.md>) | What are the synchronous [Datasets 🪣](<../../20 🧑‍🦰 UI/12 💬 Chats/07 🪣🎭 Dataset role.md>) of [domain 👥](<../41 📨 Msgs/00 👥 Domain.md>) `D`?
    | [🏭 Supplies](<../../30 🫥 Agents/06 🛎️ Concierges/02 🏭🎭 Supplier role.md>) | What are the asynchronous [Supplies 🏭](<../../30 🫥 Agents/06 🛎️ Concierges/02 🏭🎭 Supplier role.md>) of [domain 👥](<../41 📨 Msgs/00 👥 Domain.md>) `D`?
    | [🌬️ Streams](<../42 🌬️ Streams/02 🌬️🎭 Streamer role.md>) | What are the event [Streams 🌬️](<../42 🌬️ Streams/02 🌬️🎭 Streamer role.md>) of [domain 👥](<../41 📨 Msgs/00 👥 Domain.md>) `D`?
    
    ---
    <br/>


1. **How are NLWeb Graphs updated?**

    ![](<.📎 Assets/📜 Graphs.png>)

    [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) subscribe to changes in [domain Manifests 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>). 

    - Domains have the responsibility to raise an event every time they publish a new version of their [domain Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>) or [📨 DKIM](<../41 📨 Msgs/01 📨 Domain Message.md>). 
    
    - To allow any graph to subscribe to changes in any [domain Manifests 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>), NLWeb provides a cluster of [Listener 👂 nodes](<02 👂🛠️ Listener helper.md>) for [domains 👥](<../41 📨 Msgs/00 👥 Domain.md>) to publish change notifications to, and for [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) to receive notifications from. 
    
    - Upon receiving a notification, [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) update their graph representations. 

    ---
    <br/>

1. **Are Graphs like a self-sovereign identity (SSI) ledger?**

    No. NLWeb doesn't use ledgers nor [decentralized identifiers (DIDs) 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>). 
    * Instead of DIDs, NLWeb uses DNS and the web's Public Key Infrastructure (PKI) to identify domains — thus, it doesn't need an additional database for registration and discovery. 
    * [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) are cached representations of the NLWeb, contributing to maximizing performance, resilience, and onboarding.

    ---
    <br/>


1. **How can domains reset their Manifest representation on Graphs?**

    To reset their [domain Manifests 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>):
    * a [domain 👥](<../41 📨 Msgs/00 👥 Domain.md>) can send a RESET event to their [Listener 👂 helper domain](<02 👂🛠️ Listener helper.md>);
    * subscribed [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) will interpret it as the need to start from scratch.

    ---
    <br/>

1. **What if an event references an unknown Schema Code?**

    [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) will place the change on hold until the referenced [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) is available.

    ---
    <br/>

1. **How can domains know about Manifest events placed on hold?**

    [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) raise alert events. 
    - Interested domains should [subscribe 🔔](<../42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) to the Graph's [Streamer 🌬️ role](<../42 🌬️ Streams/02 🌬️🎭 Streamer role.md>), filtering the [domains 👥](<../41 📨 Msgs/00 👥 Domain.md>) they're interested in receiving alert notifications about. 
    - For privacy reasons, some security alerts may only be pushed to the [Subscriber 🔔 domain](<../42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) that is referenced in the alert.

    ---
    <br/>

1. **How is a new NLWeb trust graph populated?**

    Whenever a new [Graph 🕸 domain](<03 🕸🛠️ Graph helper.md>) is "born", 
    * it can ask a [Listener 👂 domain](<02 👂🛠️ Listener helper.md>) 
    * to replay the last change notification 
    * of every domain path
    * since the beginning of time 
    * in order to (re)build its graph representations. 

    ---
    <br/>

1. **How do Graphs support the verification of Tokens?**

    [Issuer 🎴 domains](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) sign [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with their active [📨 DKIM](<../41 📨 Msgs/01 📨 Domain Message.md>) key-pair. 
    
    * When [Issuer 🎴 domains](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) rotate their [📨 DKIM](<../41 📨 Msgs/01 📨 Domain Message.md>), it is no longer possible for [Consumer 💼 domains](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to validate old [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with the new [📨 DKIM](<../41 📨 Msgs/01 📨 Domain Message.md>).

    * Instead, [Consumer 💼 domains](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) should ask a [Graph 🕸 domain](<03 🕸🛠️ Graph helper.md>) for the Issuer's [📨 DKIM](<../41 📨 Msgs/01 📨 Domain Message.md>) at the time the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) was issued.

    ---
    <br/>


1. **What API methods are exposed by Graphs?**

    |Method|Description
    |-|-
    |[👥🚀 Trusted](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/02 👥🚀🕸 Trusted.md>) | Can I trust that other domain?
    |[👥🚀 Trusts](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>) | Do these  domains trust each other? 
    |[👥🚀 Identity](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/04 👥🚀🕸 Identity.md>) | Return the identity of a domain.
    |[👥🚀 Queryable](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/05 👥🚀🕸 Queryable.md>) | Select only the trustable codes.
    |[👥🚀 Translate](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | Translate these domains and codes.
    |[👥🚀 Public Key](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/07 👥🚀🕸 Public Key.md>) | What was the DKIM at this date?
    |[👥🚀 Schema](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>) | What's the schema of this code?
    |[👥🚀 Offer](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/09 👥🚀🕸 Offer.md>) | Detail this domain offer.
    
    ---
    <br/>