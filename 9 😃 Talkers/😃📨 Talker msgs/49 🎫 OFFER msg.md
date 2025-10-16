# 🎫 Talker OFFER command

> Part of [Talker 😃](<../10 😃 Talker.md>)

  
<br/>

1. **What is an OFFER message command?**

    An `OFFER`
    * is a message [Command ⌘](<../😃🌊 Talker flow/10 ⌘ Command.md>) 
    * that invokes the [Save Token @ Wallet ⏩](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow.

    ---
    <br/>


1. **What does a [Chat 💬](<../../4 ⚙️ Solution/35 Chats/12 💬 Chats/💬 Chat.md>) look like?**

    
    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../4 ⚙️ Solution/35 Chats/20 🤔 Prompts/🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🎴 [Issuer](<../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>) | ℹ️ Issuing your token...
    | 🤵 [Broker](<../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Save token? [Yes, No]  | > Yes
    | 🎴 [Issuer](<../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.

    ---
    <br/>

1. **What's the OFFER syntax?**

    ```yaml
    OFFER|{function} >> $accepted
    ```

   
    | Argument| Purpose
    |-|-
    | `{function}`  | [{Function}](<../😃🗃️ Talker data/12 🐍 {Function}.md>) that issues the [Token 🎫](<../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>) ID.
    | `<accepted>`| Boolean placeholder for [Accepted @ Issuer](<../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>).

    ---
    <br/>

1. **What does a Talker look like for static codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Offer:
   - INFO|Issuing your token...
   - OFFER|{GetTokenID} >> $accepted
   - IF|$accepted:
       Then: SUCCESS|Saved to your wallet.
       Else: FAILURE|You rejected the token.
   ```

   | [Command ⌘](<../😃🌊 Talker flow/10 ⌘ Command.md>) | Purpose
   |-|-
   | ⤵️ [`IF`](<../😃🌊 Talker flow/21 ⤵️ IF flow.md>) | To verify the result.  
   
   ---
   <br/>

