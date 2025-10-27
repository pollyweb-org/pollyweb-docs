# 😃🔗 Talker `BIND` command

> Implemented by the [`.BIND` 📃 script](<BIND 📃 script.md>)

> Part of [Talker 😃](<../../../😃 Talker role.md>)

<br/>

1. **What is a BIND message command?**

    A `BIND`
    * is a message [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) 
    * that invokes the [Bind @ Vault ⏩ flow](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🗄️ Bind 🔗.md>).

    ---
    <br/>


1. **What does a [Chat 💬](<../../../../💬 Chats/💬 Chat.md>) look like for required binds?**

    > It's an all-or-nothing, where `No` stops the flow.

    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ]  | > Bind
    | 🤵 [Broker](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 [Bind?](<BIND 🔗 cmd.md>) [Yes, No] <br/> -  Some schema 🧩 <br/> - Some other schema 🧩 | > Yes
    | 🗄️ [Vault](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ [Done!](<../../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>



1. **What does a [Chat 💬](<../../../../💬 Chats/💬 Chat.md>) look like for optional binds?**

    > There are checkboxes for the user to select, and `No` continues.

    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ]  | > Bind
    | 🤵 [Broker](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 [Bind?](<BIND 🔗 cmd.md>) [All, No] <br/> - [ ] Some schema 🧩 <br/> - [ ] Some other schema 🧩 | > All
    | 🗄️ [Vault](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ [Done!](<../../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>


1. **What's the BIND syntax?**


    ```yaml
    # For a single required schema.
    - BIND|<schema> 
    - SUCCESS|Bound!
    ```

    | Argument| Purpose 
    |-|-
    | `<schema>` | [Schema 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) from [`Bindable@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>) 

    ```yaml
    # For a single optional schema.
    - BIND|schema >> $bound
    - IF|$bound:
        Then: SUCCESS|Bound.
        Else: FAILURE|Not bound.
    ```

    | Argument| Purpose
    |-|-
    | `$bound`  | Boolean confirmation of acceptance.

    ```yaml
    # For multiple optional static codes.
    BIND >> $bound:
        - <schema-1>
        - <schema-n>
    ```

   
    | Argument| Purpose
    |-|-
    | `<schema-n>` | Array of [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) sent on [`Bindable@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)
    | `$bound`  | Array of [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) received on [`Bound@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)


   ```yaml
   # For placeholder codes
   BIND|{bindable} >> $bound
   ```

   
    | Argument| Purpose
    |-|-
    | `{bindable}` | [{Function}](<../../...functions 🐍/{Function} 🐍.md>) to get the [Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [Bindable @ Broker](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>).


    ---
    <br/>

1. **What does the dot mean in a schema?**

    Given that the [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) defined by `nlweb.dom` will be widely used, 
    * [Talkers 😃](<../../../😃 Talker role.md>) accept a dot as a prefix of `nlweb.dom/`.
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
       - some-authority.com/SOME-CODE
       - another-authority.com/ANOTHER-CODE

   # Verify it any was bound.
   - IF|$bound:
       Then: SUCCESS|Your wallet is bound.
       Else: FAILURE|Not bounded.
   ```

   Commands: [`BIND`](<BIND 🔗 cmd.md>) [`IF`](<../../...control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>)

   ---
   <br/>




1. **What does a Talker look like for placeholder codes?**
    
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

   Commands: [`BIND`](<BIND 🔗 cmd.md>) [`EVAL`](<../../...placeholders 🧠/EVAL ⬇️/EVAL ⬇️ flow.md>) [`IF`](<../../...control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>)
   
   ---
   <br/>

