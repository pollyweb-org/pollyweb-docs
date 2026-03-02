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
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Save token? [Yes, No]  | > Yes
    | 🎴 [Issuer](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.

    ---
    <br/>

1. **What's the ISSUE syntax?**

    ```yaml
    ISSUE >> $token:
        Token: <token-uuid>
        Schema: <schema>
        Starts: <iso-utc-date>
        Expires: <iso-utc-date>
        Context: {A:1,B:2}
    ```

   
    | Input| Purpose | Example
    |-|-|-
    | `$token`| The [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) issued | `{Token:X, Schema:Y}`| `Schema`  | The [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | `.TOKEN:1.0`
    | `Token` | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID | `<token-uuid>`
    || Defaults to [`.UUID`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/UUID ⓕ.md>)
    | `Starts` | Optional ISO UTC date | `2024-09-21T12:34:00Z`
    |           | Defaults to [`.Now`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>)
    | `Expires` | Optional ISO UTC date | `2024-09-21T12:34:00Z`
    | `Context`| User public properties | `{A:1,B:2}`

    ---
    <br/>

1. **What are alternative syntaxes?**

    ```yaml
    ISSUE: <schema> >> $token
    ```

    ```yaml
    ISSUE: <schema>
    ```

    ```yaml
    ISSUE >> $token:
        Schema: <schema>
    ```

    ---
    <br/>
   
1. **What does a Talker look like?**
    
    ```yaml
    💬 Offer:

    - INFO: Issuing your token...

    - ISSUE >> $token:
        Schema: any-authority.dom/ANY-SCHEMA:1.0
        Context: 
            Number: 123456789

    - IF $token:
        DONE: Saved to your wallet.
    - ELSE: 
        FAIL: You declined the token.
    ```
    Uses: [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`FAIL`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>)
   
    ---
    <br/>

