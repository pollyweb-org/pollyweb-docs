🫥 Agent vault domain FAQ
===

1. **What is an Agent vault?**

    Agents 🫥 are any [Vault 🗄️ domains](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) with well-known features that are linked to a user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    * They behave like the default apps for smartphones, where the operating system (e.g., Android, iOS) asks the user to select default apps for each role - e.g.:
        * internet browsing: Chrome, Firefox, or Safari;
        * email messaging: Gmail, Outlook, Apple Mail.

    * While in a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), a [Host 🤗 domain](<../23 💬 Chats/04 🤗🎭 Host role.md>) asks the user's [Broker 🤵 domain](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to invoke user Agents 🫥 by role - e.g.:

        * `any-host.com` asks `any-broker.com` to invoke the user's [Persona 🧢 agent](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>), 
        * then `any-broker.com` invokes the domain `any-persona.com`.

    ---
    <br/>


2. **What are examples of Agent roles?**

    | |Agent 🫥 | Example | Responsibilities 
    |-|-|-|-
    | 🛎️| [Concierge](<../../30 🫥 Agents/06 🛎️ Concierges/01 🛎️🫥 Concierge agent.md>) | TaskRabbit | Orchestrates tasks with 3rd parties (e.g., deliveries, repairs).
    |🧚| [Curator](<../../30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | ChatGPT | Filters options sent by [Host 🤗 domains](<../23 💬 Chats/04 🤗🎭 Host role.md>).
    |🧳| [Custodian](<../../70 🌳 Ambient/71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) | FindMy | Manages the user's [Things 💠](<../../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>), including [Userables 💍](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) and [⌚ Tapbands](<../../70 🌳 Ambient/76 ⌚ Brand Tapbands/01 ⌚💠 Tapband thing.md>).
    |🔎| [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | Google | Searches for [Host 🤗 domains](<../23 💬 Chats/04 🤗🎭 Host role.md>), and  introduces them when they start a new [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>).
    |🆔|[Identity](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | IDOne | Confirms that the user is physically present behind the remote screen.
    |🌼| [Keybox](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/04 🌼🗄️ Keybox vault.md>) | FindMy | Stores and manages the user's [Padlock 🔒](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>) keys.
    |📇| [Mingler](<../../30 🫥 Agents/08 📇 Minglers/01 📇🫥 Mingler agent.md>) | WhatsApp | Connects multiple users in a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), allowing them to exchange [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).
    |🧭| [Navigator](<../../30 🫥 Agents/07 🧭 Navigators/01 🧭🫥 Navigator agent.md>) | G.Maps | Helps users going from point A to B.
    |💳| [Payer](<../../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | Paypal | Performs payments to [Collector 🏦 domains](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>).
    |🧢| [Persona](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | Facebook | Stores and shares user preferences and personally identifiable information (PII).
    |⭐| [Reviewer](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | TrustPilot | Collects and shares user feedback from [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) experiences.
    |🗓️| [Scheduler](<../../30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | Outlook | Monitors and manages the user's agenda.
    |📦| [Storage](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) | Dropbox | Stores user data for other [Vault 🗄️ domains](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>), for data residency compliance.
    |🕓| [Timeline](<../../30 🫥 Agents/38 🕓 User Timeline/01 🕓🗄️ Timeline agent.md>) | G.Photos | Collects and fans out user-related events.
    |💖| [Vitalogist](<../../30 🫥 Agents/09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) | GoogleFit | Monitors the user's health events and provides feedback.

    ---
    <br/>


2. **Are Agents singletons?**

    Yes and no.

    * Yes, Agents 🫥 are singletons from the perspective that:

        * [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) typically assign one (and only one) default user Agents 🫥 for each role, and; 
  
        * [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) allow users to replace each default Agent 🫥 to any other of the user's [Vault 🗄️ domains](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) that are [bound 🔗](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) by the role's [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>).

    * And no, Agents 🫥 are not singletons from the perspective [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) allow roles not to have a default Agent 🫥 when there are more than one [Vault 🗄️ domains](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) that support the role's [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>).

        * One use case where this is important is when a user has two nationalities (e.g., French and Japanese), and each nation needs its own [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>).

        * When this happens, the user's [Broker 🤵 domain](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) will ask the user to select which of the two [Identity 🆔 agents](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) should receive the [Host 🤗 domain](<../23 💬 Chats/04 🤗🎭 Host role.md>) request.

    ---
    <br/>


1. **How can users chat with an Agent?**

    To open an [Agent 🫥 vault](<04 🫥🗄️ Agent vault.md>), users can ask their [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>);
    * e.g., by stating what they're trying to accomplish;
    * as in the following example, from the [Trip Return 🤝 use case](<../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/2 🧭 @ Destination/21 🧭 Return.md>).

    | Service | Prompt  | User 
    | - | - | - 
    | | | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>)
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 😃 Hi! What do you need? | `return to` <br/> `hotel`
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 💬 How can I help? <br/> - Open [ 🧭 Navigator ] <br/> - [ Something else ] | > 🧭 Navigator 
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | ✅ Over to 🧭 Navigator.
    | [ new chat ]
    | 🔎 [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Navigator (4.4 ⭐) [+]
    | 🧭 [Navigator](<../../30 🫥 Agents/07 🧭 Navigators/01 🧭🫥 Navigator agent.md>) | ℹ️ Request: return to hotel [+]
    | 🧭 [Navigator](<../../30 🫥 Agents/07 🧭 Navigators/01 🧭🫥 Navigator agent.md>) | 😃 Go to `Any Hotel`? [Yes, No]| > Yes
    | ...
    
    ---
    <br/>