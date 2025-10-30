👥 Domains
===

1. **What is a Domain in NLWeb?**

    In NLWeb, a [domain 👥](<👥 Domain.md>) is any public web service that
    * sends and receives domain [Messages 📨](<../30 🧩 Data/Messages 📨/📨 Message.md>)
    * and publishes a [domain Manifest 📜](<../30 🧩 Data/Manifests 📜/📜 Manifest.md>).


    ---
    <br/>



1. **What API methods does a Domain need to expose?**

    Supported API methods differ based on the number roles assumed by the [domain 👥](<👥 Domain.md>), from none to many.
    * The following list enumerates the possible roles a [domain 👥](<👥 Domain.md>) can assume.


    | Role 🎭&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Responsibility
    |-|-
    | [🍏 Brand](<../41 🎭 Domain Roles/Brands 🍏/🍏🎭 Brand role.md>) | Bundles and sells physical products as [Things 💠](<../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>)
    | [💼 Consumer](<../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | Consumes data from [Vaults 🗄️](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) and [Issuers 🎴](<../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)
    | [🪣 Dataset](<../41 🎭 Domain Roles/Datasetters 🪣/🪣🎭 Datasetter role.md>) | Exposes that exposes a synchronous data API
    | [🤲 Helper](<../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | Offloads undifferentiated logic from [domains 👥](<👥 Domain.md>)
    | [🤗 Host](<../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | Hosts [Chats 💬](<../35 💬 Chats/Chats 💬/💬 Chat.md>) for [Wallet 🧑‍🦰 apps](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) via [Brokers 🤵](<../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>)
    | [🪢 Integrator](<../41 🎭 Domain Roles/Integrators 🪢/🪢🎭 Integrator role.md>) |  [Manifests 📜](<../30 🧩 Data/Manifests 📜/📜 Manifest.md>)  endpoints for [Finders 🔎](<../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) to index
    | [🎴 Issuer](<../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) | Issues [Tokens 🎫](<../30 🧩 Data/Tokens 🎫/🎫 Token.md>) to be saved on users' [Wallets 🧑‍🦰](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | [🌬️ Streamer](<../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) | Pushes and replays domain events to [Subscribers 🔔](<../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>)
    | [🔔 Subscriber](<../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) | Subscribes to domain events from a [Streamers 🌬️](<../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>)
    | [🗄️ Vault](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | Stores user data and shares it with [Consumers 💼](<../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)
    | [🏭 Supplier](<../41 🎭 Domain Roles/Suppliers 🏭/🏭🎭 Supplier role.md>) | Accept async order requests from [domains 👥](<👥 Domain.md>)
    
    ---
    <br/>

1. **What flows are implemented by domains?**

    |Flow| Description
    |-|-
    |[👥⏩🌐 DNS config](<👥⏩ Domain flows/DNS config 👥🌐/👥 DNS config ⏩ flow.md>) | Configure the domain [DKIM 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>)
    |[👥⏩👥 Request Sync 🚀](<👥⏩ Domain flows/Send Sync 👥🚀👥 /👥 Sync Request ⏩ flow.md>) | Send requests that wait for a response
    |[👥⏩👥 Send Async 🐌](<👥⏩ Domain flows/Send Async 👥🐌👥/👥 Async Message ⏩ flow.md>) | Send event-driven commands or events
    |[👥⏩🕸 Manifest](<👥⏩ Domain flows/Manifest 👥📜🕸/👥 Manifest ⏩ flow.md>) | Publish [domain Manifest 📜](<../30 🧩 Data/Manifests 📜/📜 Manifest.md>) changes
    | [👥⏩🤝 Subscribe](<../45 🤲 Helper domains/Billers 🤝/🤝⏩ Biller flows/👥⏩🤝 Domain Subscription.md>) | Sign subscriptions on [Biller 🤝 domains](<../45 🤲 Helper domains/Billers 🤝/🤝🤲 Biller helper.md>)


    ---
    <br/>