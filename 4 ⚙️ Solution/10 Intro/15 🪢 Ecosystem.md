🪢 PollyWeb Ecosystem
===

![](<.📎 Assets/Ecosystem.png>)

The PollyWeb ecosystem aims to simplify everyday business transactions by streamlining interactions between users, organizations, and things, while ensuring security and performance at a global scale.

* Users interact with [Domains 👥](<../40 👥 Domains/👥 Domain/👥 Domain.md>) using their [Wallet 🧑‍🦰 apps](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).

    * A [Wallet 🧑‍🦰](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) is a PollyWeb-compatible mobile app from any vendor (e.g., `any-wallet.dom`).
  
    * Each app depends on a [Notifier 📣 domain](<../20 🧑‍🦰 UI/Notifiers 📣/📣/📣 Notifier 👥 domain.md>) for device-specific communications (e.g., WebSockets, MQTT).
    
    * Each [Notifier 📣 domain](<../20 🧑‍🦰 UI/Notifiers 📣/📣/📣 Notifier 👥 domain.md>) depends on a [Broker 🤵 domain](<../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) for [Chat 💬](<../35 💬 Chats/Chats 💬/💬 Chat.md>) orchestration with [Host 🤗 domains](<../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>). 

* Users store their data in [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>).
  
    * These are [Domains 👥](<../40 👥 Domains/👥 Domain/👥 Domain.md>) that can share user data with [Consumer 💼 domains](<../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>).
    
    * [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) may allow users to edit their data through the user's [Editor 🧑‍💻 agent](<../50 🫥 Agent domains/Editors 🧑‍💻/🧑‍💻🫥 Editor agent.md>).

* Users designate [Agents 🫥 domains](<../50 🫥 Agent domains/$/🫥🗄️ Agent vault.md>) to handle specific well-defined roles in [Chats 💬](<../35 💬 Chats/Chats 💬/💬 Chat.md>) with [Host 🤗 domains](<../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) (e.g., payments).

    * These [Agents 🫥](<../50 🫥 Agent domains/$/🫥🗄️ Agent vault.md>) are [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) that the user told their [Broker 🤵 domain](<../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) to invoke by default when a role is required.



- Users use their Wallets or their wearables (e.g., [Userables 💍](<../25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>), [Tapbands ⌚](<../25 🔆 Locators/Tapbands ⌚/⌚💠 Tapband thing.md>)) to interact with [Padlocks 🔒](<../70 🌳 Ambient/75 🔒 Padlocks/$ 🔒 Padlock device.md>), [Robots 🤖](<../25 🔆 Locators/Robots 🤖/🤖💠 Robot thing.md>), and other smart [Things 💠](<../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>).

- Organizations interact with an email-like inbox API behind a domain name, and can assume a multitude of roles in parallel - e.g.:
    * session [Host 🤗](<../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>), 
    * business [Seller 💵](<../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>),
    * data [Consumer 💼](<../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>), 
    * user-bound [Vault 🗄️](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>), 
    * event [Streamer 🌬️](<../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>), 
    * and asynchronous service [Supplier 🏭](<../41 🎭 Domain Roles/Suppliers 🏭/🏭 Supplier/🏭🎭 Supplier role.md>). 

- Domains are extended by helper domains, e.g.:
    * [Buffer ⏳ helper domains](<../45 🤲 Helper domains/Buffers ⏳/⏳ Buffer/⏳🤲 Buffer helper.md>) for global ingestion and throttling, 
    * [Collector 🏦 helper domains](<../45 🤲 Helper domains/Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>) for payments, 
    * [Biller 🤝 helper domains](<../45 🤲 Helper domains/Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>) for financial contracts, 
    * [Advertiser 👀 helper domains](<../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) for ads.

- Data integration and structural validation is assured via:
    - [Schema Codes 🧩](<../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) that domains and [Authority 🏛️ helper domains](<../45 🤲 Helper domains/Authorities 🏛️/🏛️🤲 Authority helper.md>) can define on their [domain Manifests 📜](<../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) 
    - these codes are the foundation of resource [Locators 🔆](<../25 🔆 Locators/Locators 🔆/🔆 Locator.md>), physical [Things 💠](<../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>), and verifiable offline [Tokens 🎫](<../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).

- Domains interact directly with humans with edge devices that exhibit well-known behaviors - e.g.:
    * locator [Scanners ✨](<../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>), 
    * biometric [Palmists 🖐️](<../60 🧰 Edge/63 🖐️ Palmists/01 🖐️🔌 Palmist device.md>) and [Selfies 📸](<../60 🧰 Edge/64 📸 Selfies/01 📸🔌 Selfie device.md>), 
    * and circuit [Relays 🎬](<../60 🧰 Edge/65 🎬 Relayers/04 🎬🔌 Relay device.md>).

- Device integration is assured by:
    - natural language [Relayer 🛰️](<../45 🤲 Helper domains/Relayers 🛰️/🛰️🤲 Relayer helper.md>) domains;
    - that communicate with local [Antenna 📡](<../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) hubs;
    - that aggregate [Pluggable 🔌](<../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>) devices and [Wi-Fier 🛜](<../60 🧰 Edge/61 🔌 Pluggables/03 🛜🔀 Wi-Fier router.md>) routers. 

- Security is assured by:
    * a [Trust 🫡](<../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) framework; 
    * digital signatures for [Messages 📨](<../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) and [files](<../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/5 Verify Signatures 🆔⏩🔏/🆔⏩ Verify Signatures 🔏.md>);
    * global [Firewall 🔥 helper domains](<../45 🤲 Helper domains/Firewalls 🔥/🔥🤲 Firewall helper.md>) that actively monitor the ecosystem;
    * user [Identifier 🆔 vault domains](<../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) that authenticate users on behalf of other [domains 👥](<../40 👥 Domains/👥 Domain/👥 Domain.md>) while maintaining privacy and legal compliance;
    * and [Ephemeral 🦋 devices](<../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>) that dynamically rotate QR and NFC [Locators 🔆](<../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to prevent fraud.

- Performance at a global scale is assured by:
  * a distributed cluster of [Listener 👂 helper domains](<../45 🤲 Helper domains/Listeners 👂/👂 Listener helper/👂🤲 Listener helper.md>) that propagate [Schema Codes 🧩](<../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) and [Trusts 🫡](<../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) from [domain Manifests 📜](<../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) in near-real time;
  * and [Graph 🕸 helper domains](<../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>) that cache them to support high-performant queries from any [domain 👥](<../40 👥 Domains/👥 Domain/👥 Domain.md>).

  ---