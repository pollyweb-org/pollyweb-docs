🔗 Binds FAQ
===

1. **What is a Bind?**

    A [Bind 🔗](<01 🔗 Bind.md>) is 
    * a relationship between a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and a [Vault 🗄️ domain](<03 🗄️🎭 Vault role.md>) 
    * for a given [Schema Code 🧩](<02 🧩 Schema Code.md>).

    ---
    <br/>

2. **How can users bind to Vaults?**

    ![](<.📎 Assets/🗄️ Vault.png>)

    |#|Category|Interface|Step
    |-|-|-|-
    | 1| `Hello`| [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) | Open a [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) with the [Vault 🗄️ domain](<03 🗄️🎭 Vault role.md>), and select "Bind".
    | 1| `Hello`| Web browser | Login to the website of the [Vault 🗄️ domain](<03 🗄️🎭 Vault role.md>) , and click "Bind".
    | 2|  `Bind`|[Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) | On the [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>), follow the steps detailed below.

    ---
    <br/>


3. **How to bind to a new simple Vault domain?**
    
    Using their [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>):
    1. a user initiates a [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    2. selects an option that requires a [bind 🔗](<01 🔗 Bind.md>);
    4. accepts the bind.

    The [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) may look similar to the following.
    
    | Service | Prompt  | User 
    |-|-|-
    | 🗄️ Vault | 😃 Hi! What do you need? <br/>- [ Bla ] | > Bla
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Flow: Bla, bla, bla [+] 
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Any Schema Code 🧩](<02 🧩 Schema Code.md>) | > Yes 
    | 🗄️ Vault | ✅ Done! 
    |

    The [Vault's Talker 😃](<../23 💬 Chats/03 😃 Talker.md>) may look like the following.

    ```yaml
    💬|[Bla]:
    - FLOW|bla
    - BIND|any-authority.org/ANY-SCHEMA-CODE
    - SUCCESS|Done!
    ```

    The `Flow` section of the [Vault's Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) may look like the following.

    ```yaml
    Flows:
      bla: 
        Title: Bla, bla, bla
        Steps:
        - Input: BIND|any-authority.org/ANY-SCHEMA-CODE
          Details: <detailed reasoning for the user>
    ```

    ---
    <br/>

4. **How to bind to an existing Vault domain with a Wallet app?**
    
    Using their [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>):
    1. a user (e.g., Alice) initiates a [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    2. selects the option to [bind 🔗](<01 🔗 Bind.md>) to the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    3. provides the authentication data required by the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) (e.g., login and password);
    4. selects one or more [Schema Codes 🧩](<02 🧩 Schema Code.md>) to [bind 🔗](<01 🔗 Bind.md>) to, from the list of available [Binds 🔗](<01 🔗 Bind.md>) provided to the user by the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

    The [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) may look similar to the following.
    
    | Service | Prompt  | User 
    |-|-|-
    | 🗄️ Vault | 😃 Hi! What do you need? <br/>- [ Bind ] to this Vault <br/>- [ Something else ] | > Bind
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Flow: Bind on app [+] || The [Host 🤗 role](<../23 💬 Chats/04 🤗🎭 Host role.md>) changed the context.
    | 🗄️ Vault | 😃 Type your Vault ID. | `my-id`
    | 🗄️ Vault | 😃 Type your Secret. | `*******`
    | 🗄️ Vault | ℹ️ Hi, Alice! [+] |
    | 🗄️ Vault | 😃 What to bind? [All] <br/> - [ [ Schema Code 🧩](<02 🧩 Schema Code.md>) #1 ] <br/> - [ [ Schema Code 🧩](<02 🧩 Schema Code.md>) #2 ] | > All
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Schema Code 🧩](<02 🧩 Schema Code.md>) #1  <br/> - [Schema Code 🧩](<02 🧩 Schema Code.md>) #2 | > Yes | 
    | 🗄️ Vault | ✅ Done! [+]


    ---
    <br/>

5. **How to bind to an existing Vault domain with a web browser?**

    Using the domain's mobile website or mobile app:
    1. a user (e.g., Alice) initiates a session in the target [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    2. clicks on a `bind wallet` button provided by the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    3. a QR code [Locator 🔆](<../04 🔆 Locators/01 🔆 Locator.md>) is presented to the user;
    4. the user scans the QR code with their mobile device;
    5. the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) opens with a new [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

    The [💬 Chat](<../23 💬 Chats/01 💬 Chat.md>) may look similar to the following.

    | Service | Prompt  | User 
    |-|-|-
    | | | 🔆 [scan](<../04 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>)
    | 🔎 [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Vault (4.3 ⭐)  [+] || The [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) informed the user.
    | 🗄️ Vault | ℹ️ Hi, Alice! Let's bind. || The [Locator 🔆](<../04 🔆 Locators/01 🔆 Locator.md>) had a [Host 🤗](<../23 💬 Chats/04 🤗🎭 Host role.md>)  callback.
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Flow: Web bind [+] || The [Host 🤗 role](<../23 💬 Chats/04 🤗🎭 Host role.md>) changed the context.
    | 🗄️ Vault | 😃 What to bind? [All] <br/> - [ Data Set #1 ] <br/> - [ Data Set #2 ] | > All
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Schema Code 🧩](<02 🧩 Schema Code.md>) #1  <br/> - [Schema Code 🧩](<02 🧩 Schema Code.md>) #2 | > Yes | The [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) protected the user.
    | 🗄️ Vault | ✅ Done! [+]

    ---
    <br/>


<!-- 

TODO: Workflows

## Workflows

| Workflow | Notes 
|-|-
| [ 🤵⏩🗄️ Bind Vault @ Broker ](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/02 🤵⏩🗄️ Bind vault.md>) ||
||

-->