# 🎫 Talker OFFER command

> Part of [Talker 😃](<../😃 Talker.md>)

  
<br/>

1. **What is an OFFER message command?**

    An `OFFER`
    * is a message [Command ⌘](<../😃⚙️ Talker cmds/⌘ Command.md>) 
    * that invokes the [Save Token @ Wallet ⏩](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Prompts 🤔/👉🎴 Save token.md>) flow.

    ---
    <br/>


1. **What does a [Chat 💬](<../../💬 Chats/💬 Chat.md>) look like?**

    
    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🎴 [Issuer](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) | ℹ️ Issuing your token...
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Save token? [Yes, No]  | > Yes
    | 🎴 [Issuer](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.

    ---
    <br/>

1. **What's the OFFER syntax?**

    ```yaml
    OFFER|{function} >> $accepted
    ```

   
    | Argument| Purpose
    |-|-
    | `{function}`  | [{Function}](<../😃💾 Talker data/12 🐍 {Function}.md>) that issues the [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) ID.
    | `<accepted>`| Boolean placeholder for [Accepted @ Issuer](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>).

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

   | [Command ⌘](<../😃⚙️ Talker cmds/⌘ Command.md>) | Purpose
   |-|-
   | ⤵️ [`IF`](<../😃⚙️ Talker cmds/IF ⤵️.md>) | To verify the result.  
   
   ---
   <br/>

