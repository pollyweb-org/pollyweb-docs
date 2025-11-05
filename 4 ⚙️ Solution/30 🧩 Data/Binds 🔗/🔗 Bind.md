🔗 Binds
===

1. **What is a Bind?**

    A [Bind 🔗](<🔗 Bind.md>) is 
    * a relationship between a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) and a [Vault 🗄️ domain](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) 
    * for a given [Schema 🧩](<../Codes 🧩/🧩 Schema Code.md>).

    ---
    <br/>

1. **How can users bind to Vaults?**

    ![](<🔗 Bind ⚙️ uml.png>)

    |#|Step|Interface|Step
    |-|-|-|-
    | 1| `Hello`| [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | Open a [💬 Chat](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) with the [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) and select `Bind`
    | 1| `Hello`| Browser | Login to the website of the [Vault 🗄️ ](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) and click `Bind`
    | 2|  `Bind`|[Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | On the [💬 Chat](<../../35 💬 Chats/Chats 💬/💬 Chat.md>), follow the steps detailed below

    ---
    <br/>


1. **How to bind to a new simple Vault domain?**
    
    Using their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>):
    1. a user initiates a [💬 Chat](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>);
    2. selects an option that requires a [bind 🔗](<🔗 Bind.md>);
    4. accepts the bind.

    The [💬 Chat](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) may look similar to the following.
    
    | [Domain](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    |-|-|-
    | 🗄️ Vault | 😃 Hi! What do you need? <br/>- [ Bla ] | > Bla
    | [🤵 Broker](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Flow: Bla, bla, bla [+] 
    | [🤵 Broker](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Any Schema Code 🧩](<../Codes 🧩/🧩 Schema Code.md>) | > Yes 
    | 🗄️ Vault | ✅ Done! 
    |

    The Vault's [Script 📃](<../../35 💬 Chats/Scripts 📃/Script 📃.md>) may look like the following.

    ```yaml
    💬|[Bla]:
    - INFORM|bla
    - BIND|any-authority.org/ANY-SCHEMA-CODE
    - SUCCESS|Done!
    ```

    The `Flow` section of the [Vault's Manifest 📜](<../Manifests 📜/📜 Manifest/📜 Manifest.md>) may look like the following.

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
    
    Using their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>):
    1. a user (e.g., Alice) initiates a [💬 Chat](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>);
    2. selects the option to [bind 🔗](<🔗 Bind.md>) to the [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>);
    3. provides the authentication data required by the [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) (e.g., login and password);
    4. selects one or more [Schema Codes 🧩](<../Codes 🧩/🧩 Schema Code.md>) to [bind 🔗](<🔗 Bind.md>) to, from the list of available [Binds 🔗](<🔗 Bind.md>) provided to the user by the [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>).

    The [💬 Chat](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) may look similar to the following.
    
    | [Domain](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    |-|-|-
    | 🗄️ Vault | 😃 Hi! What do you need? <br/>- [ Bind ] to this Vault <br/>- [ Something else ] | > Bind
    | [🤵 Broker](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Flow: Bind on app [+] || The [Host 🤗 role](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) changed the context.
    | 🗄️ Vault | 😃 Type your Vault ID. | `my-id`
    | 🗄️ Vault | 😃 Type your Secret. | `*******`
    | 🗄️ Vault | ℹ️ Hi, Alice! [+] |
    | 🗄️ Vault | 😃 What to bind? [All] <br/> - [ [ Schema Code 🧩](<../Codes 🧩/🧩 Schema Code.md>) #1 ] <br/> - [ [ Schema Code 🧩](<../Codes 🧩/🧩 Schema Code.md>) #2 ] | > All
    | [🤵 Broker](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Schema Code 🧩](<../Codes 🧩/🧩 Schema Code.md>) #1  <br/> - [Schema 🧩](<../Codes 🧩/🧩 Schema Code.md>) #2 | > Yes | 
    | 🗄️ Vault | ✅ Done! [+]


    ---
    <br/>

1. **How to bind to an existing Vault domain with a web browser?**

    Using the domain's mobile website or mobile app:
    1. a user (e.g., Alice) initiates a session in the target [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>);
    2. clicks on a `bind wallet` button provided by the [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>);
    3. a QR code [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) is presented to the user;
    4. the user scans the QR code with their mobile device;
    5. the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) opens with a new [💬 Chat](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) with the [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>).

    The [💬 Chat](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) may look similar to the following.

    | [Domain](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    |-|-|-
    | | | 🔆 [scan](<../../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰✨ Wallet QR scan.md>)
    | 🔎 [Finder](<../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Vault (4.3 ⭐)  [+] || The [Broker 🤵](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) informed the user.
    | 🗄️ Vault | ℹ️ Hi, Alice! Let's bind. || The [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) had a [Host 🤗](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)  callback.
    | [🤵 Broker](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Flow: Web bind [+] || The [Host 🤗 role](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) changed the context.
    | 🗄️ Vault | 😃 What to bind? [All] <br/> - [ Data Set #1 ] <br/> - [ Data Set #2 ] | > All
    | [🤵 Broker](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 Bind [Yes, No, +]<br/>- [ Schema Code 🧩](<../Codes 🧩/🧩 Schema Code.md>) #1  <br/> - [Schema 🧩](<../Codes 🧩/🧩 Schema Code.md>) #2 | > Yes | The [Broker 🤵](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) protected the user.
    | 🗄️ Vault | ✅ Done! [+]

    ---
    <br/>


<!-- 

TODO: Workflows

## Workflows

| Workflow | Notes 
|-|-
| [ 🤵⏩🗄️ Bind Vault @ Broker ](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵⏩ Broker flows/Bind vault 🗄️⏩🤵/Bind vault ⏩ flow.md>) ||
||

-->