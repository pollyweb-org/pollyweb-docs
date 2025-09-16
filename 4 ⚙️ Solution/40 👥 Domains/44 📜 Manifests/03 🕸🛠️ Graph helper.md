🕸 Graph helper domains FAQ
===

![](<.📎 Assets/📜 Graphs.png>)

1. **What is a Graph domain in NLWeb?**

    A [Graph 🕸 domain](<03 🕸🛠️ Graph helper.md>) is 
    * a [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) 
    * that builds network representations of [trust 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>) relationships between [domains 👥](<00 👥 Domain.md>). 

    ---
    <br/>

2. **Are Graphs like a self-sovereign identity (SSI) ledger?**

    No. NLWeb doesn't use ledgers nor [decentralized identifiers (DIDs) 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>). 
    * Instead of DIDs, NLWeb uses DNS and the web's Public Key Infrastructure (PKI) to identify domains — thus, it doesn't need an additional database for registration and discovery. 
    * [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) are cached representations of the NLWeb, contributing to maximizing performance, resilience, and onboarding.

    ---
    <br/>

3. **How are NLWeb Graphs updated?**

    [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) subscribe to changes in [domain Manifests 📜](<01 📜 Domain Manifest.md>). 

    - Domains have the responsibility to raise an event every time they publish a new version of their [domain Manifest 📜](<01 📜 Domain Manifest.md>) or [📨 DKIM](<../41 📨 Comms/01 📨 Domain Message.md>). 
    
    - To allow any graph to subscribe to changes in any [domain Manifests 📜](<01 📜 Domain Manifest.md>), NLWeb provides a cluster of [Listener 👂 nodes](<02 👂🛠️ Listener helper.md>) for [domains 👥](<00 👥 Domain.md>) to publish change notifications to, and for [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) to receive notifications from. 
    
    - Upon receiving a notification, [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) update their graph representations. 

    ---
    <br/>

4. **How can domains reset their Manifest representation on Graphs?**

    [Domains 👥](<00 👥 Domain.md>) can send a RESET event that [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) will interpret as the need to start from scratch.

    ---
    <br/>

5. **What if an event references an unknown Schema Code?**

    [Domains 👥](<00 👥 Domain.md>) will place the change on hold until the referenced [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) is available.

    ---
    <br/>

6. **How can domains know about Manifest events placed on hold?**

    [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>) raise alert events. 
    - Interested domains should [subscribe 🔔](<../41 📨 Comms/04 🔔🎭 Subscriber role.md>) to the Graph's [Streamer 🌬️ role](<../41 📨 Comms/02 🌬️🎭 Streamer role.md>), filtering the [domains 👥](<00 👥 Domain.md>) they're interested in receiving alert notifications about. 
    - For privacy reasons, some security alerts may only be pushed to the [Subscriber 🔔 domain](<../41 📨 Comms/04 🔔🎭 Subscriber role.md>) that is referenced in the alert.

    ---
    <br/>

7. **How is a new NLWeb trust graph populated?**

    Whenever a new [Graph 🕸 domain](<03 🕸🛠️ Graph helper.md>) is "born", it can ask a [Listener 👂 domain](<02 👂🛠️ Listener helper.md>) to replay the last change notification of every domain since the beginning of time in order to (re)build its graph representations. 

    ---
    <br/>

8. **How do Graphs support the verification of Tokens?**

    [Issuer 🎴 domains](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) sign [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with their active [📨 DKIM](<../41 📨 Comms/01 📨 Domain Message.md>) key-pair. 
    
    * When [Issuer 🎴 domains](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) rotate their [📨 DKIM](<../41 📨 Comms/01 📨 Domain Message.md>), it is no longer possible for [Consumer 💼 domains](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to validate old [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with the new [📨 DKIM](<../41 📨 Comms/01 📨 Domain Message.md>).

    * Instead, [Consumer 💼 domains](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) should ask a [Graph 🕸 domain](<03 🕸🛠️ Graph helper.md>) for the Issuer's [📨 DKIM](<../41 📨 Comms/01 📨 Domain Message.md>) at the time the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) was issued.

    ---
    <br/>