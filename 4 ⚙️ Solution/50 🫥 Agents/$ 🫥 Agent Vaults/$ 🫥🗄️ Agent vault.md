🫥 Agent vault domain
===

1. **What is an Agent vault?**

    Agents 🫥 are any [Vault 🗄️ domains](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) with well-known features that are linked to a user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>).

    * They behave like the default apps for smartphones, where the operating system (e.g., Android, iOS) asks the user to select default apps for each role - e.g.:
        * internet browsing: Chrome, Firefox, or Safari;
        * email messaging: Gmail, Outlook, Apple Mail.

    * While in a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>), a [Host 🤗 domain](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) to invoke user Agents 🫥 by role - e.g.:

        * `any-host.com` asks `any-broker.com` to invoke the user's [Persona 🧢 agent](<../70 🧢 Personas/$ 🧢🫥 Persona agent.md>), 
        * then `any-broker.com` invokes the domain `any-persona.com`.

    ---
    <br/>


1. **What are examples of Agent roles?**

    | |Agent 🫥 | Example | Responsibilities 
    |-|-|-|-
    | 🛎️| [Concierge](<../25 🛎️ Concierges/$ 🛎️🫥 Concierge agent.md>) | TaskRabbit | Orchestrates tasks with 3rd parties (e.g., deliveries, repairs).
    |🧚| [Curator](<../30 🧚 Curators/$ 🧚🫥 Curator agent.md>) | ChatGPT | Filters options sent by [Host 🤗 domains](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>).
    |🧳| [Custodian](<../35 🧳 Custodians/$ 🧳🫥 Custodian agent.md>) | FindMy | Manages the user's [Things 💠](<../../70 🌳 Ambient/71 💠 Brand Things/$ 💠 Thing.md>), including [Userables 💍](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) and [⌚ Tapbands](<../../70 🌳 Ambient/76 ⌚ Brand Tapbands/$ ⌚💠 Tapband thing.md>).
    |🔎| [Finder](<../40 🔎 Finders/$ 🔎🫥 Finder agent.md>) | Google | Searches for [Host 🤗 domains](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>), and  introduces them when they start a ../05 💬 Chats/01 💬 Chat.mds/01 💬 Chat.md>).
    |🆔|[Identity](<../45 🆔 Identities/$ 🆔🫥 Identity agent.md>) | IDOne | Confirms that the user is physically present behind the remote screen.
    |🌼| [Keybox](<../48 🌼 Keyboxes/$ 🌼🫥 Keybox agent.md>) | FindMy | Stores and manages the user's [Padlock 🔒](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>) keys.
    |📇| [Mingler](<../50 📇 Minglers/$ 📇🫥 Mingler agent.md>) | WhatsApp | Connects multiple users in a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>), allowing them to exchange [Tokens 🎫](<../../30 🧩 Data/30 🎫 Tokens/$ 🎫 Token.md>).
    |🧭| [Navigator](<../55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | G.Maps | Helps users going from point A to B.
    |💳| [Payer](<../60 💳 Payers/03 💳🎭 Payer role.md>) | Paypal | Performs payments to [Collector 🏦 domains](<../../45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>).
    |🧢| [Persona](<../70 🧢 Personas/$ 🧢🫥 Persona agent.md>) | Facebook | Stores and shares user preferences and personally identifiable information (PII).
    |⭐| [Reviewer](<../73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>) | TrustPilot | Collects and shares user feedback from [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) experiences.
    |🗓️| [Scheduler](<../75 🗓️ Schedulers/$ 🗓️🫥 Scheduler agent.md>) | Outlook | Monitors and manages the user's agenda.
    |📦| [Storage](<../80 📦 Storage/$ 📦🫥 Storage agent.md>) | Dropbox | Stores user data for other [Vault 🗄️ domains](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>), for data residency compliance.
    |🕓| [Timeline](<../90 🕓 Timeline/$ 🕓🗄️ Timeline agent.md>) | G.Photos | Collects and fans out user-related events.
    |💖| [Vitalogist](<../95 💖 Vitalogists/$ 💖🫥 Vitalogist agent.md>) | GoogleFit | Monitors the user's health events and provides feedback.

    ---
    <br/>


1. **Are Agents singletons?**

    Yes and no.

    * Yes, Agents 🫥 are singletons from the perspective that:

        * [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) typically assign one (and only one) default user Agents 🫥 for each role, and; 
  
        * [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) allow users to replace each default Agent 🫥 to any other of the user's [Vault 🗄️ domains](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) that are [bound 🔗](<../../30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) by the role's [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>).

    * And no, Agents 🫥 are not singletons from the perspective [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) allow roles not to have a default Agent 🫥 when there are more than one [Vault 🗄️ domains](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) that support the role's [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>).

        * One use case where this is important is when a user has two nationalities (e.g., French and Japanese), and each nation needs its own [Identity 🆔 agent](<../45 🆔 Identities/$ 🆔🫥 Identity agent.md>).

        * When this happens, the user's [Broker 🤵 domain](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) will ask the user to select which of the two [Identity 🆔 agents](<../45 🆔 Identities/$ 🆔🫥 Identity agent.md>) should receive the [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) request.

    ---
    <br/>


1. **How can users chat with an Agent?**

    To open an [Agent 🫥 vault](<$ 🫥🗄️ Agent vault.md>), users can ask their [Broker 🤵 domain](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>);
    * e.g., by stating what they're trying to accomplish;
    * as in the following example, from the [Trip Return 🤝 use case](<../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/02 🧭 Return @ Destination.md>).

    | [Domain](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - 
    | | | 🤵 [Broker](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)
    | 🤵 [Broker](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | 😃 Hi! What do you need? | `return to` <br/> `hotel`
    | 🤵 [Broker](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | 💬 How can I help? <br/> - Open [ 🧭 Navigator ] <br/> - [ Something else ] | > 🧭 Navigator 
    | 🤵 [Broker](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | ✅ Over to 🧭 Navigator.
    | [ new chat ]
    | 🔎 [Finder](<../40 🔎 Finders/$ 🔎🫥 Finder agent.md>) | ⓘ Any Navigator (4.4 ⭐) [+]
    | 🧭 [Navigator](<../55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ℹ️ Request: return to hotel [+]
    | 🧭 [Navigator](<../55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | 😃 Go to `Any Hotel`? [Yes, No]| > Yes
    | ...
    
    ---
    <br/>