# 🔗 Talker BIND command

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What is a BIND message command?**

    A `BIND`
    * is a message [Command ⌘](<10 ⌘ Command.md>) 
    * that invokes the [Bind @ Vault ⏩ flow](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind.md>).

    ---
    <br/>


3. **What does a Chat look like for static codes?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Bind to Any Vault?](<42 🔗 BIND msg.md>) [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
    | 🗄️ [Vault](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | ✅ [Done! Your wallet is bound.](<../31 🤔 Prompts/13 ✅ SUCCESS prompt.md>)

    ---
    <br/>

2. **What's the BIND syntax for static codes?**

   ```yaml
   BIND >> $bound:
       - <code-1>
       - <code-2>
   ```

   
    | Argument| Purpose
    |-|-
    | `<code-n>` | Array of [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) sent on [Bindable @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>).
    | `<bound>`  | Array of [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) received on [Bound @ Vault](<../../../6 🅰️ APIs/95 🗄️🅰️ Vault/02 🤵🐌🗄️ Bound.md>).

    ---
    <br/>

3. **What does a Talker look like for static codes?**
    
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

   | [Command ⌘](<10 ⌘ Command.md>) | Purpose
   |-|-
   | ⤵️ [IF](<21 ⤵️ IF flow.md>) | To verify the result.  
   
   ---
   <br/>



4. **What's the BIND syntax for placeholder codes?**

   ```yaml
   BIND|{bindable} >> $bound
   ```

   
    | Argument| Purpose
    |-|-
    | `{bindable}` | [{Function}](<12 🐍 {Function}.md>) to get the [Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) for [Bindable @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>).
    | `<bound>`  | Array of [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) received on [Bound @ Vault](<../../../6 🅰️ APIs/95 🗄️🅰️ Vault/02 🤵🐌🗄️ Bound.md>).

    ---
    <br/>

5. **What does a Talker look like for placeholder codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Bind:
   - EVAL|{GetBindableCodes} >> $bindable
   - BIND|{$bindable} >> $bound
   - IF|{$bound}:
       Then: SUCCESS|Your wallet is bound.
       Else: FAILURE|Not bounded.
   ```

   | [Command ⌘](<10 ⌘ Command.md>) | Purpose
   |-|-
   | ⬇️ [`EVAL`](<20 ⬇️ EVAL flow.md>) | To put the bindable array into a placeholder.
   | ⤵️ [`IF`](<21 ⤵️ IF flow.md>) | To verify the result.
   
   ---
   <br/>