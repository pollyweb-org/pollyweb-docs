🗄️ Vault domain role
===

1. **What is a Vault domain role in NLWeb?**

    A [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) with a [Vault 🗄️ role](<🗄️🎭 Vault role.md>) 
    * is any [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) that stores user data,
    * has a [Bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) with the user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>), 
    * and shares it with [Consumer 💼 domains](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>). 

    ---
    <br/>

1. **What are examples of Vault domains?**

    |Example|Details
    |-|-
    | `Banks` | These hold and revoke customers' bank accounts.
    | `Hospitals` | These hold and control patients' medical records.
    | `Governments` | These hold and revoke citizens' identity documents.
    |[🫥 `Agents`](<../../50 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) | These are [Vaults 🗄️](<🗄️🎭 Vault role.md>) with well-known NLWeb APIs.
    

    ---
    <br/>


1. **How are Vault domains configured on a Wallet?**

    For a [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) to be listed as a [Vault 🗄️ domain](<🗄️🎭 Vault role.md>) in the [user's Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>), the user first needs to [bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) the [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) to the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>).

    | | Workflow |  Description
    |-|-|-
    | | [👉 Binds ](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/01 🧑‍🦰👉🤵 List binds.md>) | List the user's [Binds 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>)
    || [👉 Bind](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind 🔗.md>) | [Bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) the [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) to a [Vault 🗄️](<🗄️🎭 Vault role.md>)
    || [👉 Unbind](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/03 🧑‍🦰👉🗄️ Unbind.md>) | Remove a [Bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) from a [Vault 🗄️](<🗄️🎭 Vault role.md>)
    
    ---
    <br/>

1. **What are default Vaults?**

    To streamline user onboarding, [Broker 🤵 domains](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) may automatically [bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) new [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) to default [Agent 🫥 vault domains](<../../50 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>).
        
    | | Workflow |  Description
    |-|-|-
    ||[👉 Onboard](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/11 🧑‍🦰👉🤵 Onboard.md>) | Register the [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) on a [Broker 🤵](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)

    ---
    <br/>

1. **Can users ask Vaults to share data with other Hosts?**

    Yes. 
    - Upon a share request with the [Consumer 💼 host](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>) in a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>), users can authorize their [Vault 🗄️ domains](<🗄️🎭 Vault role.md>) to disclose a data set with that [Consumer 💼 domain](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>). 
    - This requires both [Vault 🗄️](<🗄️🎭 Vault role.md>) and [Consumer 💼 host](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>) domains to [trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) one another for the [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) of the dataset to be shared.

    | | Workflow |  Description
    |-|-|-
    ||[👉 Share](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>) | Shares a [Bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) with a [Consumer 💼](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>)
    || [💼 Consume](<🗄️⏩ Vault flows/🗄️⏩💼 Consume 🔗.md>) | Tells a [Consumer 💼](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>) to collect data
    

    ---
    <br/>

1. **Can users ask Vaults to download data to the device?**

    No. 
    * That is covered by the [Issuer 🎴 domain](<../40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) role. 

    ---
    <br/>

1. **How can Vaults comply with data residency?**

    [Vault 🗄️ domains](<🗄️🎭 Vault role.md>) 
    * can ask users to share their [Storage 📦 vault](<../../50 🫥 Agents/80 📦 Storage/$ 📦🫥 Storage agent.md>), 
    * then store the user data there.

    ---
    <br/>

1. **Do users have private vaults, like the Solid Project?**

    No. 
    * Unlike the [Solid Project 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/05 📺 Berners-Lee vaults.md>), by Sir Tim Berners-Lee, NLWeb users don't have a private repository (a.k.a. [Vault 🗄️](<🗄️🎭 Vault role.md>)) for all their data, so they don't effectively own their data. 
    * Instead, a user's data is scattered across a number of [Vault 🗄️ domains](<🗄️🎭 Vault role.md>) managed by different providers who decide how much of the user's data is accessible and by whom.
  
    This is a better representation of reality as we know it - e.g., 
    * a person's bank history is with banks, 
    * their medical records are with hospitals,
    * their birth certificates are with governments,
    * and their location history is with Google Maps (or at least was, until 2024).

    ---
    <br/>

1. **Why can't users control their Vaults, like in the Solid project?**

    Let's take Google Mail as an example:
    - users open and close their accounts;
    - users export their data to a laptop;
    - users allow 3rd-party apps to read their email.

    It feels like users "control" their mailbox.

    * However, Google is the one legally bounded to keep the service up-and-running, and Google may be fined by the European Union if it abruptly ends the service or causes economical harm to a significant number of EU users. 
    * Users have little to no legal responsibility to Google. 
    * Google is also the one who receives direct economic benefit from the service, and drives the feature roadmap. 
    * Finally, Google owns the infrastructure, and all that comes with it. 
    * Thus, Google is in control, yes, in a way that most users would not want to be, and would probably not be able to be without a proper enterprise backing them up.

    Google is able to provide Gmail as free service to users because it is able to  monetize it indirectly and at scale via: 
    - integrated adds in the free web version; 
    - Gmail Enterprise licenses for corporations; 
    - and OS licenses for Samsung and other smartphone manufacturers running Android with the Google Play and Google Suite features.

    In other words, the vast majority of users (~99% likely) 
    * don't have the economical means to maintain it, 
    * the legal framework to be responsible for it, 
    * and the knowledge to manage it;
    * and that is not expected to change any time soon.
  
    Conversely, our global society is built on the trust that we have in the ability of corporations to deliver, and the ability of public institutions to regulate them — NLWeb aims to replicate our modern society with the following mechanisms:
    * [Vault 🗄️ domains](<🗄️🎭 Vault role.md>) controlled by corporations;
    * [Trusts 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) in [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) to represent partnerships;
    * [Authority 🏛️ domains](<../../45 🛠️ Helper domains/14 🏛️ Authorities/$ 🏛️🛠️ Authority helper.md>) for intergovernmental agreements;
    * [Broker 🤵 domains](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) to protect users from bad corporate actors;
    * [Reviewer ⭐ domains](<../../50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>) to collect social feedback on corporations;
    * [Firewall 🔥 domains](<../../45 🛠️ Helper domains/40 🔥 Firewalls/$ 🔥🛠️ Firewall helper.md>) to monitor and penalize bad corporate actors.
    
    ---
    <br/>

1. **How about a central place for user preferences?**

    Exceptionally, NLWeb advocates for the use of [Persona 🧢 vault](<../../50 🫥 Agents/70 🧢 Personas/$ 🧢🫥 Persona agent.md>) aimed for preference-based personalization 
    - e.g., nicknames, seat preferences, film genres;
    - but, even here, users rent storage on [Persona 🧢 vault](<../../50 🫥 Agents/70 🧢 Personas/$ 🧢🫥 Persona agent.md>) as a service that is owned and managed by a company.

    ---
    <br/>


1. **What if the user only wants to have one Vault?**

    A single [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) can, in theory, implement all existing [Schema Codes 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) and establish [trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) relationships with all existing [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>).

    * Thus, a user may wish to [bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) to that single [Vault 🗄️ domain](<🗄️🎭 Vault role.md>) with all [Schema Codes 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) the user is interested in sharing, and is [trusted 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) buy all the [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) the user is interested in interacting with. 
  
    * However, this solution doesn't seem scalable, if at all realistic.

    ---
    <br/>

1. **How is data residency solved by vaults?**

    Where nations require their citizens' data to be stored within nation's borders, [Vault 🗄️ domains](<🗄️🎭 Vault role.md>) can leverage the user's [Storage 📦 vault](<../../50 🫥 Agents/80 📦 Storage/$ 📦🫥 Storage agent.md>) to store their data. 
    
    - [Storage vaults 📦](<../../50 🫥 Agents/80 📦 Storage/$ 📦🫥 Storage agent.md>) are multi-tenant cloud repositories rented by users, where users can allow bound vaults to write their data into. 
    
    - The [Storage vault 📦](<../../50 🫥 Agents/80 📦 Storage/$ 📦🫥 Storage agent.md>) will comply with the user's [data-residency 🏔️](<../../../2 🏔️ Landscape/1 💼 Business landscape/02 🏳️ Sovereignty landscape/00 🏳️ Sovereignty index.md>) requirements by choosing in which region to store the user's data. 
    
    - This solution also allows for free services to offload the cost of storage to the user.

    ---
    <br/>


1. **How are users protected from tracking by Vault consortiums?**

    User tracking is typically done by a consortium of domains crossing information about a user's interaction with each one of them, allowing them to reconstruct the user's journey. 
    
    - To avoid this, each [Vault 🗄️ domain](<🗄️🎭 Vault role.md>) is bounded to a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) using a unique key-pair, so that there are no common properties between two [Vault Binds 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) of the same user, thus no way to cross the interactions with the [Vault 🗄️ domain](<🗄️🎭 Vault role.md>).

    ---
    <br/>

1. **How are users protected from stalking from vaults?**

    [Vault 🗄️ domains](<🗄️🎭 Vault role.md>) are [Host 🤗 domains](<../30 🤗 Hosts/$ 🤗🎭 Host role.md>) that store user data. 
    
    * When a user [binds 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) to a [Host 🤗 domain](<../30 🤗 Hosts/$ 🤗🎭 Host role.md>), the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) passes a unique [bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) ID to the [Host 🤗](<../30 🤗 Hosts/$ 🤗🎭 Host role.md>) to be able to identify the user across sessions, turning the [Host 🤗 domain](<../30 🤗 Hosts/$ 🤗🎭 Host role.md>) into a [Vault 🗄️ domain](<🗄️🎭 Vault role.md>).
    
    * While the [Vault 🗄️ domain](<🗄️🎭 Vault role.md>) is now able to track the user across [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>), it cannot track the user across [Host 🤗 domains](<../30 🤗 Hosts/$ 🤗🎭 Host role.md>) because the [Bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) ID is unique for the relationship between that user and that [Host 🤗](<../30 🤗 Hosts/$ 🤗🎭 Host role.md>).

    ---
    <br/>

1. **How do Vaults protect user data from Consumers?**

    [Consumer 💼 domains](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>) can't request user data directly to [Vault 🗄️ domains](<🗄️🎭 Vault role.md>). 
    
    * Instead, [Consumer 💼 domains](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>) request such data directly to the user. 

    * When prompted, the user selects the preferred [Vault 🗄️ domain](<🗄️🎭 Vault role.md>) to answer the Consumer's 💼 request, then signs and sends a disclose request to the selected [Vault 🗄️ domain](<🗄️🎭 Vault role.md>), asking it to disclose the requested data to the [Consumer 💼 domain](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>). 
    
    * At that point, the [Vault 🗄️ domain](<🗄️🎭 Vault role.md>) may ask the user for additional data (e.g., which credit card to use on a payment) or perform additional validations (e.g., a one-time-password via SMS to approve a bank transfer). 
    
    * Finally, the [Vault 🗄️ domain](<🗄️🎭 Vault role.md>) sends the data directly to the [Consumer 💼 domain](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>) who requested it.

    ---
    <br/>
    
1. **How can users do selective disclosure?**

    [Selective disclosure 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/07 📺 SSI selective disclosure.md>) (i.e., the ability for a user to select which fields to disclose from a given schema code) is not allowed by design on NLWeb. 
    
    * Instead, NLWeb advocates for purpose-driven datasets that are self-contained and requested under the principle of least-privilege, e.g.:
        - a hotel should not ask for all passport fields for a check-in; 
        - instead, it should ask only for required booking data like first/last name, check-in/out dates, and PNR.

    ---
    <br/>


1. **What flows are initiated by Vaults?**

    |Flow ⏩| Details
    |-|-
    | [💼 Consume](<🗄️⏩ Vault flows/🗄️⏩💼 Consume 🔗.md>) | Tells a [Consumer 💼](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>) to collect data
    | [🧑‍🦰 Engage](<🗄️⏩ Vault flows/🗄️⏩🧑‍🦰 Engage 💬.md>) | Opens a new [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with a [Bound 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) user
    

    ---
    <br/>

1. **What API methods does a Vault exposes?**
   
    | [From 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Subject 📨](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>) | Description |
    |-|--------|-------------|
    | [🤵 Broker](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | [`Bound`](<🗄️🅰️ Vault methods/🤵🐌🗄️ Bound.md>) | Add a [Bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) |
    |  | [`Unbind`](<🗄️🅰️ Vault methods/🤵🐌🗄️ Unbind.md>) | Remove a [Bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) |
    | | [`Disclose`](<🗄️🅰️ Vault methods/🤵🐌🗄️ Disclose.md>) | Disclose the data of a [Bind 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) |
    | | [`Suppress`](<🗄️🅰️ Vault methods/🤵🐌🗄️ Suppress.md>) | Suppress [🖐️ Palm scans](<../../50 🫥 Agents/45 🆔 Identities/22 🆔🖐️ Palm scan.md>) |
    | [💼 Consumer](<../27 💼 Consumers/$ 💼🎭 Consumer role.md>) | [`Collect`](<🗄️🅰️ Vault methods/💼🚀🗄️ Collect.md>) | Return the data disclosed
    
    ---
    <br/>

