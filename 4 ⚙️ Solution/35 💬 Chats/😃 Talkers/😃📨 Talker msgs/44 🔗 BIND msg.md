# 🔗 Talker BIND command

> Part of [Talker 😃](<../😃 Talker.md>)

<br/>

1. **What is a BIND message command?**

    A `BIND`
    * is a message [Command ⌘](<../😃⚙️ Talker cmds/10 ⌘ Command.md>) 
    * that invokes the [Bind @ Vault ⏩ flow](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/30 👉🔗 Binds/🧑‍🦰👉🗄️ Bind 🔗.md>).

    ---
    <br/>


1. **What does a [Chat 💬](<../../💬 Chats/💬 Chat.md>) look like for required binds?**

    > It's an all-or-nothing, where `No` stops the flow.

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ]  | > Bind
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 [Bind?](<44 🔗 BIND msg.md>) [Yes, No] <br/> -  Some schema code 🧩 <br/> - Some other schema code 🧩 | > Yes
    | 🗄️ [Vault](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ [Done!](<../../🤔 Prompts/🤔📢 Prompt status/23 ✅ SUCCESS prompt.md>)

    ---
    <br/>



1. **What does a [Chat 💬](<../../💬 Chats/💬 Chat.md>) look like for optional binds?**

    > There are checkboxes for the user to select, and `No` continues.

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ]  | > Bind
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 [Bind?](<44 🔗 BIND msg.md>) [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
    | 🗄️ [Vault](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ [Done!](<../../🤔 Prompts/🤔📢 Prompt status/23 ✅ SUCCESS prompt.md>)

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
    | `<code>` | [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) from [`Bindable@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>) 

    ```yaml
    # For a single optional code.
    - BIND|code >> $bound
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
        - <code-1>
        - <code-n>
    ```

   
    | Argument| Purpose
    |-|-
    | `<code-n>` | Array of [Schema Codes 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) sent on [`Bindable@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)
    | `$bound`  | Array of [Schema Codes 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) received on [`Bound@Vault`](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/🤵🐌🗄️ Bound.md>)


   ```yaml
   # For placeholder codes
   BIND|{bindable} >> $bound
   ```

   
    | Argument| Purpose
    |-|-
    | `{bindable}` | [{Function}](<../😃💾 Talker data/12 🐍 {Function}.md>) to get the [Codes 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) for [Bindable @ Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>).


    ---
    <br/>

1. **What does the dot mean in a code?**

    Given that the [Schema Codes 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) defined by `nlweb.org` will be widely used, 
    * [Talkers 😃](<../😃 Talker.md>) accept a dot as a prefix of `nlweb.org/`.
    * Consider the following equal examples.

        ```yaml
        BIND|.IDENTITY/OVER21
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
   - IF|$bound:
       Then: SUCCESS|Your wallet is bound.
       Else: FAILURE|Not bounded.
   ```

   | [Command ⌘](<../😃⚙️ Talker cmds/10 ⌘ Command.md>) | Purpose
   |-|-
   | ⤵️ [IF](<../😃⚙️ Talker cmds/21 ⤵️ IF flow.md>) | To verify the result.  
   
   ---
   <br/>




1. **What does a Talker look like for placeholder codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Bind:
   - EVAL|GetBindableCodes >> $bindable
   - BIND|$bindable >> $bound
   - IF|$bound:
       Then: SUCCESS|Your wallet is bound.
       Else: FAILURE|Not bounded.
   ```

   | [Command ⌘](<../😃⚙️ Talker cmds/10 ⌘ Command.md>) | Purpose
   |-|-
   | ⬇️ [`EVAL`](<../😃💾 Talker data/20 ⬇️ EVAL flow.md>) | To put the bindable array into a placeholder.
   | ⤵️ [`IF`](<../😃⚙️ Talker cmds/21 ⤵️ IF flow.md>) | To verify the result.
   
   ---
   <br/>