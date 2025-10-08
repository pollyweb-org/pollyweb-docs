# 🔗 Talker BIND command

> Part of [Talker 😃](<../../33 😃 Talkers/01 😃 Talker.md>)

<br/>

1. **What is a BIND message command?**

    A `BIND`
    * is a message [Command ⌘](<../20 🌊 Talker Flows/10 ⌘ Command.md>) 
    * that invokes the [Bind @ Vault ⏩ flow](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind.md>).

    ---
    <br/>



1. **What does a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) look like for optional binds?**

    > There are checkboxes for the user to select, and `No` continues.

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
    | 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Bind to Any Vault?](<44 🔗 BIND msg.md>) [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
    | 🗄️ [Vault](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | ✅ [Done! Your wallet is bound.](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/23 ✅ SUCCESS prompt.md>)

    ---
    <br/>


1. **What does a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) look like for required binds?**

    > It's an all-or-nothing, where `No` stops the flow.

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
    | 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Bind to Any Vault?](<44 🔗 BIND msg.md>) [Yes, No] <br/> -  Some schema code 🧩 <br/> - Some other schema code 🧩 | > Yes
    | 🗄️ [Vault](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | ✅ [Done! Your wallet is bound.](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/23 ✅ SUCCESS prompt.md>)

    ---
    <br/>


1. **What's the BIND syntax?**


    ```yaml
    # For a single required code.
    - BIND|<code> 
    - SUCCESS|Bound!
    ```

    | Argument| Purpose 
    |-|-
    | `<code>` | [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) from [`Bindable@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>) 

    ```yaml
    # For a single optional code.
    - BIND|code >> $bound
    - IF|{$bound}:
        Then: SUCCESS|Bound.
        Else: FAILURE|Not bound.
    ```

    | Argument| Purpose
    |-|-
    | `$bound`  | Boolean confirmation of acceptance.

    ```yaml
    # For multiple optional static codes.
    BIND >> $bound:
        - <code-1>
        - <code-n>
    ```

   
    | Argument| Purpose
    |-|-
    | `<code-n>` | Array of [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) sent on [`Bindable@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>)
    | `$bound`  | Array of [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) received on [`Bound@Vault`](<../../6 🅰️ APIs/95 🗄️🅰️ Vault/02 🤵🐌🗄️ Bound.md>)


   ```yaml
   # For placeholder codes
   BIND|{bindable} >> $bound
   ```

   
    | Argument| Purpose
    |-|-
    | `{bindable}` | [{Function}](<../30 💾 Talker Data/12 🐍 {Function}.md>) to get the [Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) for [Bindable @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>).


    ---
    <br/>

1. **What does the `@` character mean in a code?**

    Given that the [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) defined by `nlweb.org` will be widely used, 
    * [Talkers 😃](<../../33 😃 Talkers/01 😃 Talker.md>) accept the character `@` as a prefix of `nlweb.org/`.
    * Consider the following equal examples.

        ```yaml
        BIND|@IDENTITY/OVER21
        BIND|nlweb.org/IDENTITY/OVER21
        ```

    ---
    <br/>

1. **What does a Talker look like for static codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Bind:
   - BIND >> $bound:
       - some-authority.com/SOME-CODE
       - another-authority.com/ANOTHER-CODE
   - IF|{$bound}:
       Then: SUCCESS|Your wallet is bound.
       Else: FAILURE|Not bounded.
   ```

   | [Command ⌘](<../20 🌊 Talker Flows/10 ⌘ Command.md>) | Purpose
   |-|-
   | ⤵️ [IF](<../20 🌊 Talker Flows/21 ⤵️ IF flow.md>) | To verify the result.  
   
   ---
   <br/>




1. **What does a Talker look like for placeholder codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Bind:
   - EVAL|{GetBindableCodes} >> $bindable
   - BIND|{$bindable} >> $bound
   - IF|{$bound}:
       Then: SUCCESS|Your wallet is bound.
       Else: FAILURE|Not bounded.
   ```

   | [Command ⌘](<../20 🌊 Talker Flows/10 ⌘ Command.md>) | Purpose
   |-|-
   | ⬇️ [`EVAL`](<../30 💾 Talker Data/20 ⬇️ EVAL flow.md>) | To put the bindable array into a placeholder.
   | ⤵️ [`IF`](<../20 🌊 Talker Flows/21 ⤵️ IF flow.md>) | To verify the result.
   
   ---
   <br/>