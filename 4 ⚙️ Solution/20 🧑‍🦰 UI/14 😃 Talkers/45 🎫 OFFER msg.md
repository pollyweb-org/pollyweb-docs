# 🎫 Talker ISSUE command

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What is an OFFER message command?**

    An `OFFER`
    * is a message [Command](<10 Command.md>) 
    * that invokes the [Offer Token @ Issuer ⏩](<../../../5 ⏩ Flows/60 🎴⏩ Issuers/01 🎴⏩🧑‍🦰 Offer token.md>) flow.

    ---
    <br/>


2. **What does a Chat look like?**

    
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🎴 [Issuer](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | ℹ️ Issuing your token...
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save Token? [Yes, No]  | > Yes
    | 🎴 [Issuer](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.

    ---
    <br/>

3. **What's the OFFER syntax?**

    ```yaml
    OFFER|<code>|{tokenID}
    ```

   
    | Argument| Purpose
    |-|-
    | `<code>` | The [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) sent on [Bindable @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>).
    | `<bound>`  | Array of [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) received on [Bound @ Vault](<../../../6 🅰️ APIs/95 🗄️🅰️ Vault/02 🤵🐌🗄️ Bound.md>).

    ---
    <br/>

4. **What does a Talker look like for static codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Offer:
   - INFO|Issuing your token...
   - OFFER|nlweb.org/HOST/BOOKING/SELF|{bookingUUID}
   - SUCCESS|Saved to your wallet.
   ```

   | Command | Purpose
   |-|-
   | ⤵️ [IF](<21 ⤵️ IF flow.md>) | To verify the result.  
   
   ---
   <br/>



5. **What's the BIND syntax for placeholder codes?**

   ```yaml
   BIND|{bindable} >> <bound> 
   ```

   
    | Argument| Purpose
    |-|-
    | `{bindable}` | [{Function}](<11 {Function}.md>) to get the [Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) for [Bindable @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>).
    | `<bound>`  | Array of [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) received on [Bound @ Vault](<../../../6 🅰️ APIs/95 🗄️🅰️ Vault/02 🤵🐌🗄️ Bound.md>).

    ---
    <br/>

6. **What does a Talker look like for placeholder codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Bind:
   - INFO|Let's bind you.
   - EVAL|{GetBindableCodes} >> bindable
   - BIND|{$bindable} >> bound
   - IF|{$bound}:
       Then: SUCCESS|Your wallet is bound.
       Else: FAILURE|Not bounded.
   ```

   | Command | Purpose
   |-|-
   | ⏏️ [EVAL](<20 ⏏️ EVAL flow.md>) | To put the bindable array into a placeholder.
   | ⤵️ [IF](<21 ⤵️ IF flow.md>) | To verify the result.
   
   ---
   <br/>