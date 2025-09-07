🪢 NLWeb Ecosystem
===

![](<.📎 Assets/Ecosystem.png>)

The NLWeb ecosystem aims to simplify everyday business transactions by streamlining interactions between users, organizations, and things, while ensuring security and performance at a global scale.

* Users interact with [Domains 👥](<../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) using their [Wallet 🧑‍🦰 apps](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    * A [Wallet 🧑‍🦰](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) is an NLWeb-compatible mobile app from any vendor (e.g., `any-wallet.org`).
  
    * Each app depends on a [Notifier 📣 domain](<../20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) for device-specific communications (e.g., WebSockets, MQTT).
    
    * Each [Notifier 📣 domain](<../20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) depends on a [Broker 🤵 domain](<../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) for [Chat 💬](<../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) orchestration with [Host 🤗 domains](<../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>). 

* Users store their data in [Vault 🗄️ domains](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>).
  
    * These are [Domains 👥](<../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) that can share user data with [Consumer 💼 domains](<../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>).
    
    * [Vault 🗄️ domains](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) may allow users to edit their data through the user's [Folder 🗂️ editor](<../20 🧑‍🦰 UI/26 🗂️ Folders/01 🗂️ Folder editor.md>).

* Users designate [Agents 🫥 domains](<../30 🫥 Agents/00 Entities/🫥 Agent vault.md>) to handle specific well-defined roles in [Chats 💬](<../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with [Host 🤗 domains](<../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) (e.g., payments).

    * These [Agents 🫥](<../30 🫥 Agents/00 Entities/🫥 Agent vault.md>) are [Vault 🗄️ domains](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) that the user told their [Broker 🤵 domain](<../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to invoke by default when a role is required.



- Users use their Wallets or their wearables (e.g., [Userables 💍](<../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>), [Tapbands ⌚](<../70 🌳 Ambient/76 ⌚ Brand Tapbands/01 ⌚💠 Tapband thing.md>)) to interact with [Padlocks 🔒](<../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>), [Robots 🤖](<../70 🌳 Ambient/72 🤖 Brand Robots/01 🤖💠 Robot thing.md>), and other smart [Things 💠](<../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>).

- Organizations interact with an email-like inbox API behind a domain name, and can assume a multitude of roles in parallel - e.g.:
    * session [Host 🤗](<../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>), 
    * business [Seller 💵](<../30 🫥 Agents/04 💳 Payers/02 💵🎭 Seller role.md>),
    * data [Consumer 💼](<../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>), 
    * user-bound [Vault 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>), 
    * event [Streamer 🌬️](<../40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>), 
    * and asynchronous service [Supplier 🏭](<../30 🫥 Agents/06 🛎️ Concierges/02 🏭🎭 Supplier role.md>). 

- Domains are extended by helper domains, e.g.:
    * [Buffer ⏳](<../40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) for global ingestion and throttling, 
    * [Collector 🏦](<../30 🫥 Agents/04 💳 Payers/03 🏦🛠️ Collector helper.md>) for payments, 
    * [Biller 🤝](<../30 🫥 Agents/04 💳 Payers/04 🤝🛠️ Biller helper.md>) for financial contracts, 
    * [Advertiser 👀](<../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) for ads.

- Data integration and structural validation is assured via [Schema Codes 🧩](<../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) that domains and [Authorities 🏛️](<../40 👥 Domains/43 👍 Trusts/02 🏛️🛠️ Authority helper.md>) can define on their domain [Manifests 📜](<../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) 
    - these codes are the foundation of resource [Locators 🔆](<../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>), physical [Things 💠](<../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>), and verifiable offline [Tokens 🎫](<../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).

- Domains interact directly with humans with edge devices that exhibit well-known behaviors - e.g.:
    * locator [Scanners ✨](<../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>), 
    * biometric [Palmists 🖐️](<../60 🧰 Edge/63 🖐️ Palmists/01 🖐️🔌 Palmist device.md>) and [Selfies 📸](<../60 🧰 Edge/64 📸 Selfies/01 📸🔌 Selfie device.md>), 
    * and circuit [Relays 🎬](<../60 🧰 Edge/65 🎬 Relayers/04 🎬🔌 Relay device.md>).

- Device integration is assured by natural language [Relayer 🛰️](<../60 🧰 Edge/61 🔌 Pluggables/04 🛰️🏭 Relayer supplier.md>) domains that communicate with local [Antenna 📡](<../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) hubs that aggregate [Pluggable 🔌](<../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>) devices and [Wi-Fier 🛜](<../60 🧰 Edge/61 🔌 Pluggables/03 🛜🔀 Wi-Fier router.md>) routers. 

- Security is assured by a [Trust 👍](<../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) framework, digital signatures for [Messages 📨](<../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) and [files](<../30 🫥 Agents/05 🆔 Identities/08 🆔🔏 User Signature.md>), global [Firewalls 🔥](<../40 👥 Domains/43 👍 Trusts/03 🔥🛠️ Firewall helper.md>) that actively monitor the ecosystem, [Identity 🆔](<../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) domains that authenticate users on behalf of other domains while maintaining privacy and legal compliance, and [Ephemeral 🦋](<../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>) devices that dynamically rotate QR and NFC locators to prevent fraud.

- Performance at a global scale is assured by a distributed cluster of domain [Listeners 👂](<../40 👥 Domains/44 📜 Manifests/02 👂👥 Listener helper.md>) that propagate domain schemas and trusts in near-real time, and domain [Graphs 🕸](<../40 👥 Domains/44 📜 Manifests/03 🕸👥 Graph helper.md>) that cache them to support high-performant queries from any domain.