📜 Domain Manifests FAQ
===

![](<./📎 Assets/📜 Manifest.png>)

1. **How do domains publicize their identity?**

    In NLWeb, [Domains 👥](<00 ✅ 👥 Domain.md>) publish their metadata in the form a Manifest 📜.

    ---

1. **How do domains publish Manifests?**

    A domain's Manifest 📜 content is sent in parts or in full to [Listeners 👂](<02 ✅ 👂👥 Listener helper.md>), who then propagate it to [Graphs 🕸](<03 ✅ 🕸👥 Graph helper.md>).

    ---

1. **How can a domain inspect another domain's Manifest?**

    Domains leverage Manifest 📜 caches, called [Graphs 🕸](<03 ✅ 🕸👥 Graph helper.md>), that keep up-to-date representations of NLWeb domain Manifests 📜.
    * Manifest queries to these [Graphs 🕸](<03 ✅ 🕸👥 Graph helper.md>) are synchronous and expected to have millisecond latency.
    * This is similar to what DNS records do for Web 2.0, but with a more complex data schema. 

    ---

1. **What information can be added to a Manifest?**

    Manifests can include the following sections:
    - 🤗 [Host Identity](<../../20 ✅ 🧑‍🦰 UI/23 ✅ 💬 Chats/03 ✅ 🤗🎭 Host role.md>): domain identification (mandatory)
    - 👍 [Domain Trusts](<../43 ✅ 👍 Trusts/01 ✅ 👍 Domain Trust.md>): trusted domains, Codes, and roles
    - 🧩 [Schema Codes](<../../20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>): defined by the domain
    - 🧩 [Delegate Codes](<../../20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>): Codes delegated to other domains
    - 🔌 [Integrations](<../../20 ✅ 🧑‍🦰 UI/23 ✅ 💬 Chats/06 ✅ 🔌🎭 Integrator role.md>): synchronous datasets, asynchronous supplies, and streaming endpoints.

    ---

1. **How to implement a domain Manifest in AWS?**

    ![](<./📎 Assets/📜 Manifest@AWS.png>)

    This solution relies on the following [📨 Messaging](<../41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>) components:
    - 📨 **Inbox**: an API endpoint with CDN that verifies the sender's signature.
    - 📮 **Async Post**: an async message outbound component that signs messages. 

    Architecture features: 
    * allows large Manifest files (up to 1 GB) to be published in its entirety.
    * allows changes in small Manifest parts (up to 100 KB) to be published with low latency, which is the recommendation for large Manifests that change often.
    * allows for drift detection when the Manifest is updated in parts.

    ---
