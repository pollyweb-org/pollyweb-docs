# 👥🎭 Domain Role

> Part of [domain 👥](<👥 Domain.md>)

## FAQ

1. **What are domain roles?**

    Supported API methods differ based on the number roles assumed by the [domain 👥](<👥 Domain.md>), from none to many.

    ---
    <br/>

1. **What API methods does a Domain need to expose?**

    | Role 🎭&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Responsibility
    |-|-
    | [🍏 Brand](<../../41 🎭 Domain Roles/Brands 🍏/🍏🎭 Brand role.md>) | Bundles and sells physical products as [Things 💠](<../../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>)
    | [💼 Consumer](<../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) | Consumes data from [Vaults 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) and [Issuers 🎴](<../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)
    | [🪣 Dataset](<../../41 🎭 Domain Roles/Datasetters 🪣/🪣🎭 Datasetter role.md>) | Exposes that exposes a synchronous data API
    | [🤲 Helper](<../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) | Offloads undifferentiated logic from [domains 👥](<👥 Domain.md>)
    | [🤗 Host](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | Hosts [Chats 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) for [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) via [Brokers 🤵](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>)
    | [🪢 Integrator](<../../41 🎭 Domain Roles/Integrators 🪢/🪢🎭 Integrator role.md>) |  [Manifests 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>)  endpoints for [Finders 🔎](<../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) to index
    | [🎴 Issuer](<../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) | Issues [Tokens 🎫](<../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) to be saved on users' [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | [🌬️ Streamer](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) | Pushes and replays domain events to [Subscribers 🔔](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔 Subscriber/🔔🎭 Subscriber role.md>)
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔 Subscriber/🔔🎭 Subscriber role.md>) | Subscribes to domain events from a [Streamers 🌬️](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>)
    | [🗄️ Vault](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | Stores user data and shares it with [Consumers 💼](<../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>)
    | [🏭 Supplier](<../../41 🎭 Domain Roles/Suppliers 🏭/🏭 Supplier/🏭🎭 Supplier role.md>) | Accept async order requests from [domains 👥](<👥 Domain.md>)
    
    ---
    <br/>
