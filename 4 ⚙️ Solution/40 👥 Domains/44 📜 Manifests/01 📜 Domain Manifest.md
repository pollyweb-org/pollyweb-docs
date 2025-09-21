📜 Domain Manifests FAQ
===


1. **How do domains publicize their identity?**

    In NLWeb, [domains 👥](<00 👥 Domain.md>) publish their metadata in the form a [domain Manifest 📜](<01 📜 Domain Manifest.md>).

    ---
    <br/>


2. **How can a domain inspect another domain's Manifest?**

    [Domains 👥](<00 👥 Domain.md>) leverage Manifest 📜 caches, called [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>), that keep up-to-date representations of NLWeb [domain Manifests 📜](<01 📜 Domain Manifest.md>).
    * Manifest queries to these [Graphs 🕸](<03 🕸🛠️ Graph helper.md>) are synchronous and expected to have millisecond latency.
    * This is similar to what DNS records do for Web 2.0, but with a more complex data schema. 

    ---
    <br/>


1. **How does it work?**

    ![](<.📎 Assets/📜 Manifest.png>)

    Each [domain 👥](<00 👥 Domain.md>) sends the content of their [domain Manifests 📜](<01 📜 Domain Manifest.md>) in parts or in full to a [Listener 👂 helper domain](<02 👂🛠️ Listener helper.md>), who then propagates it to [Graph 🕸 domains](<03 🕸🛠️ Graph helper.md>).

    |Step|Description
    |-|-
    |A| When a [domain 👥](<00 👥 Domain.md>) sends a request to another
    |B| the recipient queries a [Graph 🕸 helper domain](<03 🕸🛠️ Graph helper.md>) for information about the sender to assess its [trustworthiness 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>)
    |C| and only then responds successfully.
    

    ---
    <br/>

2. **What information can be added to a Manifest?**

    Manifests can include the following sections.

    |Section|Purpose | Schemas
    |-|-|-
    | 🤗 [Host Identity](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) | Domain identification (mandatory). | • [/MANIFEST 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 Manifest.md>) <br/>• [/MANIFEST/IDENTITY 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestIdentity.md>) <br/>• [/MANIFEST/TRANSLATION 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestTranslation.md>)
    | 👍 [Domain Trusts](<../43 👍 Trusts/01 👍 Domain Trust.md>) | Trusted domains, Codes, and roles. | • [/MANIFEST/TRUST 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestTrust.md>)
    |  🧩 [Schema Codes](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) | Defined by the domain. | • [/MANIFEST/CODE 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestCode.md>) <br/>• [/MANIFEST/CODE/SCHEMA 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestCodeSchema.md>) | Schema validation of a Code
    |  🧩 [Delegated Codes](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) | Codes delegated to other domains. | • [/MANIFEST/DELEGATE 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestDelegate.md>)
    | 🪢 [Integrations](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🪢🎭 Integrator role.md>) |Synchronous datasets, <br/>asynchronous supplies, <br/>and streaming endpoints. | • [/MANIFEST/OFFER 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestOffer.md>)

    ---
    <br/>

1. **What are examples of manifests?**

    | Category | Example
    |-|-
    | `Business` | [Coffee shop 📜](<../../../8 📜 Manifests/🌐 Businesses/📜 cafe.any-business.com.md>)
    || [Car Park 📜](<../../../8 📜 Manifests/🌐 Businesses/📜 carpark.any-business.org.md>)
    || [Casino](<../../../8 📜 Manifests/🌐 Businesses/📜 casino.any-business.org.md>)
    || [Hairdresser](<../../../8 📜 Manifests/🌐 Businesses/📜 hairdresser.any-business.org.md>)
    || [Restaurant](<../../../8 📜 Manifests/🌐 Businesses/📜 restaurant.any-business.org.md>)
    || [Utility](<../../../8 📜 Manifests/🌐 Businesses/📜 utility.any-business.org.md>)
    || [Vending](<../../../8 📜 Manifests/🌐 Businesses/📜 vending.any-business.org.md>)