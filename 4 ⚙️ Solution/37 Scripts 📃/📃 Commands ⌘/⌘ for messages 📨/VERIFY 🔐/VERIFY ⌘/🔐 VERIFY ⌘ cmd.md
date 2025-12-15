# 🔐 Talker `VERIFY` command

> About
* Part of [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Implemented by the [`VERIFY` 📃 script](<🔐 VERIFY 📃 script.md>)

## FAQ

1. **What is a VERIFY message command?**

    [`VERIFY`](<🔐 VERIFY ⌘ cmd.md>)
    * is a [Command ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that checks if a given content was signed by the sender.

    ---
    <br/>

1. **What type of content can be verified?**

    | Assert | Sender | Verification
    |-|-|-
    | [`.IsMessage`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsMessage ⓕ.md>) | [Domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | Was a [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) signed by the [domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | Was a [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) signed by the [Wallet 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?
    | [File 📄](<../../../../../30 🧩 Data/Files 📄/📄 File.md>) |  [Domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | Was a [File 📄](<../../../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | Was a [File 📄](<../../../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [Wallet 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?
    |[`.IsToken`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsToken ⓕ.md>) | [Wallet 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | Was a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) signed by the [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)?
    ||| and does it comply with the [Schema Code 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)

    ---
    <br/>

