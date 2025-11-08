# 😃🔗 Talker `BIND` command

> Implemented by the [`.BIND` 📃 script](<🔗 BIND 📃 script.md>)

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>

1. **What is a BIND message command?**

    A `BIND`
    * is a message [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that invokes the [Bind @ Vault ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind vault ⏩ flow.md>).

    ---
    <br/>


1. **What does a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) look like for required binds?**

    > It's an all-or-nothing, where `No` stops the flow.

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ]  | > Bind
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 [Bind?](<🔗 BIND ⌘ cmd.md>) [Yes, No] <br/> -  Some schema 🧩 <br/> - Some other schema 🧩 | > Yes
    | 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ [Done!](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>



1. **What does a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) look like for optional binds?**

    > There are checkboxes for the user to select, and `No` continues.

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ]  | > Bind
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 [Bind?](<🔗 BIND ⌘ cmd.md>) [All, No] <br/> - [ ] Some schema 🧩 <br/> - [ ] Some other schema 🧩 | > All
    | 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ [Done!](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>


1. **What's the BIND syntax?**


    ```yaml
    # For a single required schema.
    - BIND|<schema> 
    - SUCCESS|Bound!
    ```

    | Input| Purpose 
    |-|-
    | `<schema>` | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) from [`Bindable@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>) 

    ```yaml
    # For a single optional schema.
    - BIND|schema >> $bound
    - IF|$bound:
        Then: SUCCESS|Bound.
        Else: FAILURE|Not bound.
    ```

    | Input| Purpose
    |-|-
    | `$bound`  | Boolean confirmation of acceptance.

    ```yaml
    # For multiple optional static codes.
    BIND >> $bound:
        - <schema-1>
        - <schema-n>
    ```

   
    | Input| Purpose
    |-|-
    | `<schema-n>` | Array of [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) sent on [`Bindable@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)
    | `$bound`  | Array of [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) received on [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)


   ```yaml
   # For holder codes
   BIND|{bindable} >> $bound
   ```

   
    | Input| Purpose
    |-|-
    | `{bindable}` | [{Function}](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) to get the [Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [Bindable @ Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>).


    ---
    <br/>

1. **What does the dot mean in a schema?**

    Given that the [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) defined by `nlweb.dom` will be widely used, 
    * [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) accept a dot as a prefix of `nlweb.dom/`.
    * Consider the following equal examples.

        ```yaml
        BIND|.IDENTITY/OVER21
        ```
        ```yaml
        BIND|nlweb.dom/IDENTITY/OVER21
        ```

    ---
    <br/>

1. **What does a Talker look like for static codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Bind:

   # Offer multiple binds.
   - BIND >> $bound:
       - some-authority.dom/SOME-CODE
       - another-authority.dom/ANOTHER-CODE

   # Verify it any was bound.
   - IF|$bound:
       Then: SUCCESS|Your wallet is bound.
       Else: FAILURE|Not bounded.
   ```

   Uses: [`BIND`](<🔗 BIND ⌘ cmd.md>) [`IF`](<../../⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>)

   ---
   <br/>




1. **What does a Talker look like for holder codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Bind:

   # Calculate the schemas in code
   - EVAL|GetBindables >> $bindable

   # Offer the binds
   - BIND|$bindable >> $bound

   # Check if any was bound
   - IF|$bound:
       Then: SUCCESS|Your wallet is bound.
       Else: FAILURE|Not bounded.
   ```

   Uses: [`BIND`](<🔗 BIND ⌘ cmd.md>) [`EVAL`](<../../⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`IF`](<../../⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>)
   
   ---
   <br/>

