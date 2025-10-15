📦 Storage vault domains
===

![](<00 📎 Assets/📦 Storage.png>)

1. **What is a Storage domain in NLWeb?**

    A Storage 📦 domain is a shared repository [Vault 🗄️](<../../25 Data/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) that users can subscribe to keep their data in the cloud, similar to Dropbox and Google Drive, with the intent of being shared with other services. 

    ---
    
1. **Why are Storage domains important for other domains?**

    Storage 📦 domains allow other services to store the user's data in a repository controlled and paid by the user, offloading the cost while complying with data residency requirements.

    ---

1. **How does it help with data residency compliance?**

    Storage 📦 domains align with the [NLWeb Sovereignty pledge 🦅](<../../../1 🎯 Mission/3 🦅 Sovereignty.md>) - e.g.:
    - to ensure data privacy compliance, a U.S. service can store the data of a German citizen in a Storage service hosted in the [AWS European Sovereign Cloud 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/02 🏳️ Sovereignty landscape/10 📺 Sovereignty @ AWS.md>), which is managed by European staff and located within German borders.

    ---

1. **How does it help low-cost services?**

    To keep costs low, a free video streaming service may offload the cost of storage to the user, by storing the user's video files on the user's Storage 📦 service.

    ---

1. **How do Storage vaults keep data secure?**

    This is a shared responsibility.

    - Storage 📦 vaults fully segregate each user-domain section, so that no domain can see user data from another domain, and no users can see data from other users. 

    - In parallel, NLWeb advocates for domains writing to a Storage 📦 service to encrypt their data. 

    ---

1. **How can users set up a Storage Vault?**

    Wallets typically onboard users with a default Storage 📦 service, allowing users to immediately taking advantage of a free tier.

    Nonetheless, users can find and bind into another Storage 📦 service, like they do with any other Vault.

    ---

1. **Can users change to a different Storage domain?**

    Yes. 
    - The NLWeb protocol includes a mechanism from transfer between Storage 📦 domains. 
    - Failure to comply causes [Firewalls 🔥](<../../45 🛠️ Helper domains/21 🔥 Firewalls/$ 🔥🛠️ Firewall helper.md>) to block the domain.

    ---

1. **How can users pay for Storage?**

    Typically, with a [subscription 🤝](<../04 💳 Payers/06 🤝🛠️ Biller helper.md>), like Google Drive.

    ---

1. **How can users increase the available Storage space?**

    Typically, by upgrading the [subscription 🤝](<../04 💳 Payers/06 🤝🛠️ Biller helper.md>), like Google Drive.

    ---

1. **Do users need to approve each Storage access to others domains?**

    No. Once the access if first granted, domains can access their allocated space anytime.

    ---

1. **Can users limit the storage space used by a given domain?**

    Yes. 
    - Storage 📦 services allow users to define maximum allocation space per domain.

    ---

1. **How do users clean up a domain's allocated space?**

    - **Option 1:** delete all data from that domain - this is the easiest, quickest, and more destructive way.

    - **Option 2:** chose to delete only the cache and/or data from that domain, but not the settings - this is similar to how Android OS allows users to clean data from mobile apps.

    - **Option 3:** initiate a chat with that domain, and clean the storage from there - this option allows users to exclude specific files that only that domain can read (e.g., large video files). 

    ---

1. **How to implement a Storage vault on AWS?**

    ![](<00 📎 Assets/📦 Storage$Vault @AWS.png>)

    This solution requires the following components:
    - 📜 **Manifester**: to expose its [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>); 
    - 📨 **Inbox**: a combination of the Distributer plus the Endpoint for domain [📨 Messaging](<../../40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>).

    Design decisions:
    - Storage 📦 vaults write asynchronously, meaning that a read after a write may return the old value and not the one just written 
        - Storage 📦 clients should cache their writes in order to have read-after-write consistency;
    - reads don't return items bigger than 100KB 
        - instead, Storage 📦 vaults return a temporary link where clients can download the content from;
    - the Downloader Lambda is separated to be set with 10 GB of memory 
        - this is required to be able to download and uncompress items of up to 1 GB;
    - items bigger than 1 GB are rejected 
        - this is verified in a property in the write payload, which needs to match the size of the item even when smaller than 1 GB.

    ---

1. **How to implement a Storage client cache on AWS?**

    ![](<00 📎 Assets/📦 Storage$Client @AWS.png>)

    Storage clients rely on the following components for domain [📨 Messaging](<../../40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>):
    - 📨 **Inbox**: the combination of the Distributer plus the Endpoint;
    - 🚀 **Sync Call**: a synchronous request outbound that signed requests;
    - 📮 **Async Post**: an async message outbound that signs messages.

    Design decisions:
    - data sent to Storage 📦 vaults is first compressed and encrypted;
    - each user is assigned a different encryption key;
    - large items are stored on S3 but referenced by DynamoDB;
    - every time an item is written, the TTL is updated;
    - replication to the Storage 📦 vault is done in delayed (periodic) batches.

    ---