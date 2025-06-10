🕸 Graph Domain Development FAQ
===

![](<./📎 Assets/📜 Graphs.png>)

1. **What is a Graph domain in NLWeb?**

    Graphs are domains that build network representations of [trust 👍](<../43 ✅ 👍 Trusts/01 ✅ 👍 Domain Trust.md>) relationships between domains. 

    ---

1. **Are Graphs like a self-sovereign identity (SSI) ledger?**

    No. NLWeb doesn't use ledgers nor decentralized identifiers (DIDs). 
    * Instead of DIDs, NLWeb uses DNS and PKI to identify domains - thus, it doesn't need an additional database for registration and discovery. 
    * Graphs are cached representations of the NLWeb, contributing to maximizing performance, resilience, and onboarding.

    ---

1. **How are NLWeb Graphs updated?**

    NLWeb Graphs subscribe to changes in domain [Manifests 📜](<01 ✅ 📜 Domain Manifest.md>). 

    - Domains have the responsibility to raise an event every time they publish a new version of their Manifest or [📨 DKIM](<../41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>). 
    
    - To allow any graph to subscribe to changes in any domain Manifests, NLWeb provides a cluster of [Listeners 👂](<02 ✅ 👂👥 Listener helper.md>) for domains to publish change notifications to, and for Graphs to receive notifications from. 
    
    - Upon receiving a notification, Graphs update their graph representations. 

    ---

1. **How can domains reset their Manifest representation on Graphs?**

    Domains can send a RESET event that Graphs will interpret as the need to start from scratch.

    ---

1. **What if an event references an unknown Schema Code?**

    Domains will place the change on hold until the referenced [Schema Code 🧩](<../../20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>) is available.

    ---

1. **How can domains know about Manifest events placed on hold?**

    Graphs raise alert events. 
    - Interested domains should subscribe to that [🌬️ Streamer](<../41 ✅ 📨 Comms/02 ✅ 🌬️🎭 Streamer role.md>), filtering the domains they're interested in receiving alert notifications about. 
    - For privacy reasons, some alerts are only pushed to the subscriber domain that is referenced in the alert.

    ---

1. **How is a new NLWeb trust graph populated?**

    Whenever a new Graph is "born", it can ask a [Listener 👂](<02 ✅ 👂👥 Listener helper.md>) to replay the last change notification of every domain since the beginning of time in order to (re)build its graph representations. 

    ---

1. **How do Graphs support the verification of Tokens?**

    [Issuers 🎴](<../../20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/02 ✅ 🎴🎭 Issuer role.md>) sign [Tokens 🎫](<../../20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>) with their active DKIM key-pair. 
    - When Issuers rotate their DKIM, it is no longer possible to validate old Tokens with the new DKIM;
    - instead, domains should ask a Graph for the Issuer's DKIM at the time the Token was issued.

    ---

1. **How to implement a Graph on AWS?**

    ![](<./📎 Assets/📜 Graphs@AWS.png>)

    Graphs rely on the following components for domain [📨 Messaging](<../41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>):
    - 📨 **Inbox**: the combination of the Distributer plus the Endpoint;
    - 📮 **Async Post**: an async message outbound that signs messages.

    For throttled consumption of high-throughput events, Graphs rely on [⏳ Buffers](<../41 ✅ 📨 Comms/03 ✅ ⏳👥 Buffer helper.md>).

    Regarding Lambdas:
    - the drift handler needs can accept files of up to 1 GB.
    - there should be a distinct table handler per table.
    - there should be a distinct synchronous handler per request type.

    ---
