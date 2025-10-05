# 🎫 Talker OFFER command

> Part of [Talker 😃](<01 😃 Talker.md>)

  
<br/>

1. **What is an OFFER message command?**

    An `OFFER`
    * is a message [Command ⌘](<10 ⌘ Command.md>) 
    * that invokes the [Save Token @ Wallet ⏩](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow.

    ---
    <br/>


2. **What does a Chat look like?**

    
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🎴 [Issuer](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | ℹ️ Issuing your token...
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save token? [Yes, No]  | > Yes
    | 🎴 [Issuer](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.

    ---
    <br/>

3. **What's the OFFER syntax?**

    ```yaml
    OFFER|{function} >> $accepted
    ```

   
    | Argument| Purpose
    |-|-
    | `{function}`  | [{Function}](<12 🐍 {Function}.md>) that issues the [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID.
    | `<accepted>`| Boolean placeholder for [Accepted @ Issuer](<../../../6 🅰️ APIs/55 🎴🅰️ Issuer/02 🤵🐌🎴 Accepted.md>).

    ---
    <br/>

4. **What does a Talker look like for static codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Offer:
   - INFO|Issuing your token...
   - OFFER|{GetTokenID} >> $accepted
   - IF|{$accepted}:
       Then: SUCCESS|Saved to your wallet.
       Else: FAILURE|You rejected the token.
   ```

   | [Command ⌘](<10 ⌘ Command.md>) | Purpose
   |-|-
   | ⤵️ [`IF`](<21 ⤵️ IF flow.md>) | To verify the result.  
   
   ---
   <br/>

