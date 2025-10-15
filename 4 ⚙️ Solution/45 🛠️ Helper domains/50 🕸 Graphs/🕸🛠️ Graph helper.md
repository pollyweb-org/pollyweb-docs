🕸 Graph helper domains
===

1. **What is a Graph domain in NLWeb?**

    A [Graph 🕸 domain](<🕸🛠️ Graph helper.md>) is 
    * any [Helper 🛠️ domain](<../$ 🛠️ Helpers/🛠️👥 Helper domain.md>) 
    * that subscribes to [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) change events from [Listener 👂 domains](<../60 👂 Listeners/👂🛠️ Listener helper.md>)
    * then builds network representations of [Trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) relationships between [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>)
    * including indirect relationships via [Authority 🏛️ domains](<../14 🏛️ Authorities/$ 🏛️🛠️ Authority helper.md>). 

    ---
    <br/>

1. **What can domains use Graphs for?**

    [Graph 🕸 domains](<🕸🛠️ Graph helper.md>) can answer the following questions synchronously from any [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>).

    |Scope&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Question
    |-|-
    |[👥 Identity](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>)| What's the identity of [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) `D`?
    |[👍 Trusts](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) | Can I trust the data of [Schema 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) `S` sent by [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) `D`?
    |[👍 Trusts](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) | Can I trust my data of [Schema 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) `S` to a [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) `D`?
    | [🧩 Schemas](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) | What's the schema definition of [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) `S`?
    | [🎫 Tokens](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) | What's the historical public [📨 DKIM](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>) key of [🎫 Token](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) `T`?
    | [🪣 Datasets](<../../41 🎭 Domain Roles/28 🪣 Datasets/$ 🪣🎭 Dataset role.md>) | What are the synchronous [Datasets 🪣](<../../41 🎭 Domain Roles/28 🪣 Datasets/$ 🪣🎭 Dataset role.md>) of [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) `D`?
    | [🏭 Supplies](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>) | What are the asynchronous [Supplies 🏭](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>) of [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) `D`?
    | [🌬️ Streams](<../../41 🎭 Domain Roles/75 🌬️ Streamers/🌬️🎭 Streamer role.md>) | What are the event [Streams 🌬️](<../../41 🎭 Domain Roles/75 🌬️ Streamers/🌬️🎭 Streamer role.md>) of [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) `D`?
    
    ---
    <br/>


1. **How are NLWeb Graphs updated?**

    ![](<.📎 Assets/📜 Graphs.png>)

    [Graph 🕸 domains](<🕸🛠️ Graph helper.md>) subscribe to changes in [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>). 

    - Domains have the responsibility to raise an event every time they publish a new version of their [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) or [📨 DKIM](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>). 
    
    - To allow any graph to subscribe to changes in any [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>), NLWeb provides a cluster of [Listener 👂 nodes](<../60 👂 Listeners/👂🛠️ Listener helper.md>) for [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) to publish change notifications to, and for [Graph 🕸 domains](<🕸🛠️ Graph helper.md>) to receive notifications from. 
    
    - Upon receiving a notification, [Graph 🕸 domains](<🕸🛠️ Graph helper.md>) update their graph representations. 

    ---
    <br/>

1. **Are Graphs like a self-sovereign identity (SSI) ledger?**

    No. NLWeb doesn't use ledgers nor [decentralized identifiers (DIDs) 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>). 
    * Instead of DIDs, NLWeb uses DNS and the web's Public Key Infrastructure (PKI) to identify domains — thus, it doesn't need an additional database for registration and discovery. 
    * [Graph 🕸 domains](<🕸🛠️ Graph helper.md>) are cached representations of the NLWeb, contributing to maximizing performance, resilience, and onboarding.

    ---
    <br/>


1. **How can domains reset their Manifest representation on Graphs?**

    To reset their [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>):
    * a [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) can send a RESET event to their [Listener 👂 helper domain](<../60 👂 Listeners/👂🛠️ Listener helper.md>);
    * subscribed [Graph 🕸 domains](<🕸🛠️ Graph helper.md>) will interpret it as the need to start from scratch.

    ---
    <br/>

1. **What if an event references an unknown Schema Code?**

    [Graph 🕸 domains](<🕸🛠️ Graph helper.md>) will place the change on hold until the referenced [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) is available.

    ---
    <br/>

1. **How can domains know about Manifest events placed on hold?**

    [Graph 🕸 domains](<🕸🛠️ Graph helper.md>) raise alert events. 
    - Interested domains should [subscribe 🔔](<../../41 🎭 Domain Roles/76 🔔 Subscribers/🔔🎭 Subscriber role.md>) to the Graph's [Streamer 🌬️ role](<../../41 🎭 Domain Roles/75 🌬️ Streamers/🌬️🎭 Streamer role.md>), filtering the [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) they're interested in receiving alert notifications about. 
    - For privacy reasons, some security alerts may only be pushed to the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/76 🔔 Subscribers/🔔🎭 Subscriber role.md>) that is referenced in the alert.

    ---
    <br/>

1. **How is a new NLWeb trust graph populated?**

    Whenever a new [Graph 🕸 domain](<🕸🛠️ Graph helper.md>) is "born", 
    * it can ask a [Listener 👂 domain](<../60 👂 Listeners/👂🛠️ Listener helper.md>) 
    * to replay the last change notification 
    * of every domain path
    * since the beginning of time 
    * in order to (re)build its graph representations. 

    ---
    <br/>

1. **How do Graphs support the verification of Tokens?**

    [Issuer 🎴 domains](<../../41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>) sign [Tokens 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) with their active [📨 DKIM](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>) key-pair. 
    
    * When [Issuer 🎴 domains](<../../41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>) rotate their [📨 DKIM](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>), it is no longer possible for [Consumer 💼 domains](<../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) to validate old [Tokens 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) with the new [📨 DKIM](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>).

    * Instead, [Consumer 💼 domains](<../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) should ask a [Graph 🕸 domain](<🕸🛠️ Graph helper.md>) for the Issuer's [📨 DKIM](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>) at the time the [Token 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) was issued.

    ---
    <br/>


1. **What API methods are exposed by Graphs?**

    |Method|Description
    |-|-
    |[👥🚀 Trusted](<🕸🅰️ Graph methods/👥🚀🕸 Trusted.md>) | Can I trust that other domain?
    |[👥🚀 Trusts](<🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>) | Do these  domains trust each other? 
    |[👥🚀 Identity](<🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) | Return the identity of a domain.
    |[👥🚀 Queryable](<🕸🅰️ Graph methods/👥🚀🕸 Queryable.md>) | Select only the trustable codes.
    |[👥🚀 Translate](<🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | Translate these domains and codes.
    |[👥🚀 Public Key](<🕸🅰️ Graph methods/👥🚀🕸 Public Key.md>) | What was the DKIM at this date?
    |[👥🚀 Schema](<🕸🅰️ Graph methods/👥🚀🕸 Schema.md>) | What's the schema of this code?
    |[👥🚀 Offer](<🕸🅰️ Graph methods/👥🚀🕸 Offer.md>) | Detail this domain offer.
    
    ---
    <br/>