# 😃🎫 Talker `ISSUE` command

> Part of [Talker 😃](<../../😃 Talker role.md>)

  
<br/>

1. **What is an ISSUE message command?**

    An `ISSUE`
    * is a message [Command ⌘](<../...commands ⌘/⌘ Command.md>) 
    * that invokes the [Save Token @ Wallet ⏩](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🎴 Save token.md>) flow
    * to save a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>).

    ---
    <br/>


1. **What does a [Chat 💬](<../../../💬 Chats/💬 Chat.md>) look like?**

    
    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🎴 [Issuer](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) | ℹ️ Issuing your token...
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Save token? [Yes, No]  | > Yes
    | 🎴 [Issuer](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.

    ---
    <br/>

1. **What's the ISSUE syntax?**

    ```yaml
    ISSUE|<schema> >> $token:
        Schema: <schema>
        Starts: <iso-utc-date>
        Expires: <iso-utc-date>
        Properties: 
            {properties}
        Internals:
            {internals}
    ```

   
    | Argument| Purpose | Example
    |-|-|-
    | `$token`| The [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) issued | `{Token:X, Schema:Y}`| `Schema`  | The [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | `.TOKEN:1.0`
    | `Starts` | Optional ISO UTC date | `2024-09-21T12:34:00Z`
    | `Expires` | Optional ISO UTC date | `2024-09-21T12:34:00Z`
    | `Properties`| User public properties | `{A:1, B:2}`
    | `Properties`| [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) internal notes | `{A:1, B:2}`

    ---
    <br/>

1. **What does a Talker look like?**
    
   ```yaml
   # 😃 Talker 
   💬 Offer:

   - INFO|Issuing your token...

   - ISSUE >> $token:
        Schema: any-authority.dom/ANY-SCHEMA:1.0
        Properties: 
            Number: 123456789

   - IF|$token:
        Then: SUCCESS|Saved to your wallet.
        Else: FAILURE|You rejected the token.
   ```
   Commands: [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️ prompt.md>) [`IF`](<../...control ▶️/IF ⤵️.md>)  
   
   ---
   <br/>

