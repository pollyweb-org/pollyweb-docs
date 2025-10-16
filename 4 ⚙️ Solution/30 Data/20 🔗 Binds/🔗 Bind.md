🔗 Binds
===

1. **What is a Bind?**

    A [Bind 🔗](<🔗 Bind.md>) is 
    * a relationship between a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) and a [Vault 🗄️ domain](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) 
    * for a given [Schema Code 🧩](<../10 🧩 Schema Codes/🧩 Schema Code.md>).

    ---
    <br/>

1. **How can users bind to Vaults?**

    ![](<.📎 Assets/🔗 Bind.png>)

    |#|Step|Interface|Step
    |-|-|-|-
    | 1| `Hello`| [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) | Open a [💬 Chat](<../../35 Chats/12 💬 Chats/$ 💬 Chat.md>) with the [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) and select `Bind`
    | 1| `Hello`| Browser | Login to the website of the [Vault 🗄️ ](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) and click `Bind`
    | 2|  `Bind`|[Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) | On the [💬 Chat](<../../35 Chats/12 💬 Chats/$ 💬 Chat.md>), follow the steps detailed below

    ---
    <br/>


1. **How to bind to a new simple Vault domain?**
    
    Using their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>):
    1. a user initiates a [💬 Chat](<../../35 Chats/12 💬 Chats/$ 💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>);
    2. selects an option that requires a [bind 🔗](<🔗 Bind.md>);
    4. accepts the bind.

    The [💬 Chat](<../../35 Chats/12 💬 Chats/$ 💬 Chat.md>) may look similar to the following.
    
    | [Domain](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    |-|-|-
    | 🗄️ Vault | 😃 Hi! What do you need? <br/>- [ Bla ] | > Bla
    | [🤵 Broker](<../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | ⓘ Flow: Bla, bla, bla [+] 
    | [🤵 Broker](<../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Any Schema Code 🧩](<../10 🧩 Schema Codes/🧩 Schema Code.md>) | > Yes 
    | 🗄️ Vault | ✅ Done! 
    |

    The [Vault's Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) may look like the following.

    ```yaml
    💬|[Bla]:
    - INFORM|bla
    - BIND|any-authority.org/ANY-SCHEMA-CODE
    - SUCCESS|Done!
    ```

    The `Flow` section of the [Vault's Manifest 📜](<../../40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>) may look like the following.

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

1. **How to bind to an existing Vault domain with a Wallet app?**
    
    Using their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>):
    1. a user (e.g., Alice) initiates a [💬 Chat](<../../35 Chats/12 💬 Chats/$ 💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>);
    2. selects the option to [bind 🔗](<🔗 Bind.md>) to the [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>);
    3. provides the authentication data required by the [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) (e.g., login and password);
    4. selects one or more [Schema Codes 🧩](<../10 🧩 Schema Codes/🧩 Schema Code.md>) to [bind 🔗](<🔗 Bind.md>) to, from the list of available [Binds 🔗](<🔗 Bind.md>) provided to the user by the [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>).

    The [💬 Chat](<../../35 Chats/12 💬 Chats/$ 💬 Chat.md>) may look similar to the following.
    
    | [Domain](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    |-|-|-
    | 🗄️ Vault | 😃 Hi! What do you need? <br/>- [ Bind ] to this Vault <br/>- [ Something else ] | > Bind
    | [🤵 Broker](<../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | ⓘ Flow: Bind on app [+] || The [Host 🤗 role](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) changed the context.
    | 🗄️ Vault | 😃 Type your Vault ID. | `my-id`
    | 🗄️ Vault | 😃 Type your Secret. | `*******`
    | 🗄️ Vault | ℹ️ Hi, Alice! [+] |
    | 🗄️ Vault | 😃 What to bind? [All] <br/> - [ [ Schema Code 🧩](<../10 🧩 Schema Codes/🧩 Schema Code.md>) #1 ] <br/> - [ [ Schema Code 🧩](<../10 🧩 Schema Codes/🧩 Schema Code.md>) #2 ] | > All
    | [🤵 Broker](<../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Schema Code 🧩](<../10 🧩 Schema Codes/🧩 Schema Code.md>) #1  <br/> - [Schema Code 🧩](<../10 🧩 Schema Codes/🧩 Schema Code.md>) #2 | > Yes | 
    | 🗄️ Vault | ✅ Done! [+]


    ---
    <br/>

1. **How to bind to an existing Vault domain with a web browser?**

    Using the domain's mobile website or mobile app:
    1. a user (e.g., Alice) initiates a session in the target [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>);
    2. clicks on a `bind wallet` button provided by the [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>);
    3. a QR code [Locator 🔆](<../15 🔆 Locators/$ 🔆 Locator.md>) is presented to the user;
    4. the user scans the QR code with their mobile device;
    5. the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) opens with a new [💬 Chat](<../../35 Chats/12 💬 Chats/$ 💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>).

    The [💬 Chat](<../../35 Chats/12 💬 Chats/$ 💬 Chat.md>) may look similar to the following.

    | [Domain](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    |-|-|-
    | | | 🔆 [scan](<../15 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>)
    | 🔎 [Finder](<../../50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) | ⓘ Any Vault (4.3 ⭐)  [+] || The [Broker 🤵](<../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) informed the user.
    | 🗄️ Vault | ℹ️ Hi, Alice! Let's bind. || The [Locator 🔆](<../15 🔆 Locators/$ 🔆 Locator.md>) had a [Host 🤗](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>)  callback.
    | [🤵 Broker](<../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | ⓘ Flow: Web bind [+] || The [Host 🤗 role](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) changed the context.
    | 🗄️ Vault | 😃 What to bind? [All] <br/> - [ Data Set #1 ] <br/> - [ Data Set #2 ] | > All
    | [🤵 Broker](<../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Schema Code 🧩](<../10 🧩 Schema Codes/🧩 Schema Code.md>) #1  <br/> - [Schema Code 🧩](<../10 🧩 Schema Codes/🧩 Schema Code.md>) #2 | > Yes | The [Broker 🤵](<../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) protected the user.
    | 🗄️ Vault | ✅ Done! [+]

    ---
    <br/>


<!-- 

TODO: Workflows

## Workflows

| Workflow | Notes 
|-|-
| [ 🤵⏩🗄️ Bind Vault @ Broker ](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/05 🤵⏩🗄️ Bind vault.md>) ||
||

-->