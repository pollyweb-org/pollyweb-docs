👥 Domains
===

1. **What is a Domain in NLWeb?**

    In NLWeb, a [domain 👥](<00 👥 Domain.md>) is any public web service that
    * sends and receives domain [Messages 📨](<01 📨 Domain Message.md>)
    * and publishes a [domain Manifest 📜](<../44 📜 Manifests/$ 📜 Domain Manifest.md>).


    ---
    <br/>


1. **What does a domain DNS look like?**
    
    Consider the following sample DNS configuration for the domain name [`any-domain.com`]().
    
    
    | Record Name | Type | Value 
    |-|-|-|
    | 👉 Name servers from the DNS register
    | [`any-domain.com`]() | `NS` | `{name servers}`
    | 👉 Endpoint for inbound [messages 📨](<01 📨 Domain Message.md>)  
    | `nlweb`.[`any-domain.com`]() | `A` | `1234.any-api.com`
    | 👉 [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) for outbound and [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>)
    | `pk6`.`_domainkey`.[`any-domain.com`]() | `TXT` | `v=DKIM1;k=rsa;p=...` 
    | 👉 Old [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) for old [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>)
    | `pk5`.`_domainkey`.[`any-domain.com`]() | `TXT` | `v=DKIM1;k=rsa;p=...` 

    

    ---
    <br/>

1. **What API methods does a Domain need to expose?**

    Supported API methods differ based on the number roles assumed by the [domain 👥](<00 👥 Domain.md>), from none to many.
    * The following list enumerates the possible roles a [domain 👥](<00 👥 Domain.md>) can assume.


    | Role 🎭&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Responsibility
    |-|-
    | [🍏 Brand](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>) | Bundles and sells physical products as [Things 💠](<../../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>)
    | [💼 Consumer](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) | Consumes data from [Vaults 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) and [Issuers 🎴](<../../41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>)
    | [🪣 Dataset](<../../41 🎭 Domain Roles/28 🪣 Datasets/$ 🪣🎭 Dataset role.md>) | Exposes that exposes a synchronous data API
    | [🛠️ Helper](<../../45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) | Offloads undifferentiated logic from [domains 👥](<00 👥 Domain.md>)
    | [🤗 Host](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | Hosts [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) for [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) via [Brokers 🤵](<../../20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>)
    | [🪢 Integrator](<../../41 🎭 Domain Roles/35 🪢 Integrators/$ 🪢🎭 Integrator role.md>) |  [Manifests 📜](<../44 📜 Manifests/$ 📜 Domain Manifest.md>)  endpoints for [Finders 🔎](<../../30 🫥 Agents/40 🔎 Finders/02 🔎🫥 Finder vault.md>) to index
    | [🎴 Issuer](<../../41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) | Issues [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) to be saved on users' [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | [🌬️ Streamer](<../../41 🎭 Domain Roles/75 🌬️ Streamers/$ 🌬️🎭 Streamer role.md>) | Pushes and replays domain events to [Subscribers 🔔](<../../41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>)
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>) | Subscribes to domain events from a [Streamers 🌬️](<../../41 🎭 Domain Roles/75 🌬️ Streamers/$ 🌬️🎭 Streamer role.md>)
    | [🗄️ Vault](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) | Stores user data and shares it with [Consumers 💼](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>)
    | [🏭 Supplier](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>) | Accept async order requests from [domains 👥](<00 👥 Domain.md>)
    
    ---
    <br/>

1. **What flows are implemented by domains?**

    |Flow| Description
    |-|-
    |[👥⏩🕸 Manifest](<../../../5 ⏩ Flows/30 👥⏩ Domains/04 👥⏩🕸 Manifest 📜.md>) | Publish [domain Manifest 📜](<../44 📜 Manifests/$ 📜 Domain Manifest.md>) changes
    | [👥⏩🤝 Subscribe](<../../../5 ⏩ Flows/07 🤝⏩ Billers/02 👥⏩🤝 Domain Subscription.md>) | Sign subscriptions on [Biller 🤝 domains](<../../45 🛠️ Helper domains/15 🤝 Billers/$ 🤝🛠️ Biller helper.md>)


    ---
    <br/>