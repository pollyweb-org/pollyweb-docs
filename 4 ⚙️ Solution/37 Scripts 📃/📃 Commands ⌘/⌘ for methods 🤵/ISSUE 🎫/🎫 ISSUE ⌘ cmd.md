# 😃🎫 Talker `ISSUE` command

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* To be used with an [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) role

> Implementation
* Implemented by the [`ISSUE` 📃 script](<🎫 ISSUE 📃 script.md>)
* Part of the [🧑‍🦰 `Save Token` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>)
* Part of the [🎴 `Issuer.Tokens.Issue` ⏩ flow](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🪣 Issuer tables/Tokens 🎫 table/🪣⏩ Issued flow/🎴 Issuer.Tokens.Issued ⏩ flow.md>)

  
<br/>

## FAQ

1. **What is an ISSUE message command?**

    An `ISSUE`
    * is a message [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that invokes the [`Save Token` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>)
    * to save a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).

    ---
    <br/>


1. **What does a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) look like?**

    
    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🎴 [Issuer](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) | ℹ️ Issuing your token...
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 Save token? [Yes, No]  | > Yes
    | 🎴 [Issuer](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.

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

   
    | Input| Purpose | Example
    |-|-|-
    | `$token`| The [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) issued | `{Token:X, Schema:Y}`| `Schema`  | The [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | `.TOKEN:1.0`
    | `Starts` | Optional ISO UTC date | `2024-09-21T12:34:00Z`
    | `Expires` | Optional ISO UTC date | `2024-09-21T12:34:00Z`
    | `Properties`| User public properties | `{A:1, B:2}`
    | `Properties`| [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) internal notes | `{A:1, B:2}`

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
        Else: FAILURE|You declined the token.
   ```
   Uses: [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`IF`](<../../⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>)  
   
   ---
   <br/>

