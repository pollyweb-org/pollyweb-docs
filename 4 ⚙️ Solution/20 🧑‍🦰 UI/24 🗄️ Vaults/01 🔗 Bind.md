🔗 Binds FAQ
===

1. **What is a Bind?**

    A [Bind 🔗](<01 🔗 Bind.md>) is a relationship between a [Wallet 🧑‍🦰 app](<../23 💬 Chats/02 🧑‍🦰💬 Wallet chats.md>) and [Vault 🗄️ domains](<03 🗄️🎭 Vault role.md>) for a given [Schema Code 🧩](<02 🧩 Schema Code.md>).

    ---

2. **How can users bind to Vaults?**

    For a [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to be listed as a [Vault 🗄️ domain](<03 🗄️🎭 Vault role.md>) in the [user's Wallet 🧑‍🦰 app](<../23 💬 Chats/02 🧑‍🦰💬 Wallet chats.md>), the user first needs to bind the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to the [Wallet 🧑‍🦰 app](<../23 💬 Chats/02 🧑‍🦰💬 Wallet chats.md>). 
    * To streamline user onboarding, [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) may automatically [bind 🔗](<01 🔗 Bind.md>) new [Wallet 🧑‍🦰 apps](<../23 💬 Chats/02 🧑‍🦰💬 Wallet chats.md>) to default [Agent 🫥 vault domains](<04 🫥🗄️ Agent vault.md>).
    
    ---


1. **How to bind to a Vault domain with a Wallet app?**
    
    Using their [Wallet 🧑‍🦰 app](<../23 💬 Chats/02 🧑‍🦰💬 Wallet chats.md>):
    1. a user (e.g., Alice) initiates a [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    2. selects the option to [Bind 🔗](<01 🔗 Bind.md>) to the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    3. provides the authentication data required by the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) (e.g., login and password);
    4. selects one or more [Schema Codes 🧩](<02 🧩 Schema Code.md>) to [bind 🔗](<01 🔗 Bind.md>) to, from the list of available [Binds 🔗](<01 🔗 Bind.md>) provided to the user by the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).


    The [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) may look similar to the following.
    
    | Service | Prompt  | User | What happened?
    |-|-|-|-|
    | 🗄️ Vault | 😃 Hi! What do you need? <br/>- [ Bind ] to this Vault <br/>- [ Something else ] | > Bind
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Input form: Bind [+] || The [Host 🤗 role](<../23 💬 Chats/03 🤗🎭 Host role.md>) changed the context.
    | 🗄️ Vault | 😃 Type your Vault ID. | `my-id`
    | 🗄️ Vault | 😃 Type your Secret. | `*******`
    | 🗄️ Vault | ℹ️ Hi, Alice! [+] || The [Vault 🗄️ role](<03 🗄️🎭 Vault role.md>)  authenticated the user.
    | 🗄️ Vault | 😃 What to bind? [All] <br/> - [ [ Schema Code 🧩](<02 🧩 Schema Code.md>) #1 ] <br/> - [ [ Schema Code 🧩](<02 🧩 Schema Code.md>) #2 ] | > All
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Schema Code 🧩](<02 🧩 Schema Code.md>) #1  <br/> - [Schema Code 🧩](<02 🧩 Schema Code.md>) #2 | > Yes | The [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) protected the user.
    | 🗄️ Vault | ✅ Done! [+]


    ---
    <br/>

2. **How to bind to a Vault domain with a web browser?**

    Using the domain's mobile website or mobile app:
    1. a user (e.g., Alice) initiates a session in the target [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    2. clicks on a `bind wallet` button provided by the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    3. a QR code [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) is presented to the user;
    4. the user scans the QR code with their mobile device;
    5. the [Wallet 🧑‍🦰 app](<../23 💬 Chats/02 🧑‍🦰💬 Wallet chats.md>) opens with a new [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

    The [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) may look similar to the following.

    | Service | Prompt  | User | What happened?
    |-|-|-|-
    | | | 🔆 [scan](<../22 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>)
    | 🔎 [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Vault (4.3 ⭐)  [+] || The [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) informed the user.
    | 🗄️ Vault | ℹ️ Hi, Alice! Let's bind. || The [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) had a [Host 🤗](<../23 💬 Chats/03 🤗🎭 Host role.md>)  callback.
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Input form: Bind [+] || The [Host 🤗 role](<../23 💬 Chats/03 🤗🎭 Host role.md>) changed the context.
    | 🗄️ Vault | 😃 What to bind? [All] <br/> - [ Data Set #1 ] <br/> - [ Data Set #2 ] | > All
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Schema Code 🧩](<02 🧩 Schema Code.md>) #1  <br/> - [Schema Code 🧩](<02 🧩 Schema Code.md>) #2 | > Yes | The [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) protected the user.
    | 🗄️ Vault | ✅ Done! [+]

    ---


<!-- 

TODO: Workflows

## Workflows

| Workflow | Notes 
|-|-
| [ 🤵⏩🗄️ Bind Vault @ Broker ](<../../../5 ⏩ Flows/08 🤵⏩ Brokers/02 🤵⏩🗄️ Bind vault.md>) ||
||

-->