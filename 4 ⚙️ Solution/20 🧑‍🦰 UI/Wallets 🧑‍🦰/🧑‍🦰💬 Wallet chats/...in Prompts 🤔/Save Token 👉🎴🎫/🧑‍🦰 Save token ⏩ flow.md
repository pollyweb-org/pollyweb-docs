# 🧑‍🦰 `Save Token` ⏩ flow

> Purpose
* On the [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>), 
    * a user accepts a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) 
    * offered by an [Issuer 🎴 domain](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>).

> Implementation
* Implemented by the [🎴 `Issuer.Tokens.Issue` ⏩ flow](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🪣 Issuer tables/Tokens 🎫 table/🪣⏩ Issued flow/🎴 Issuer.Tokens.Issued ⏩ flow.md>)
* Implemented by the [🤵 `Broker.Tokens.Issue` ⏩ flow](<../../../../Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>)

<br/>

## 💬 Chat 

Consider the following excerpt from the [Book restaurant table 🤝 use case](<../../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>).

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🎴 [Issuer](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) | ℹ️ Issuing your token...
| 🤵 [Broker](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Save token? [Yes, No]  | > Yes
| 🎴 [Issuer](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.

<br/>

## 😃 Talker 

The associated [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) uses the [`ISSUE`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴⌘ Issuer cmds/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>) command.

```yaml
- INFO: Issuing your token...
- ISSUE: .HOST >> $token

- IF $token:
    DONE: Saved to your wallet.
- ELSE:
    FAIL: You declined the token.
```
Uses: [`FAIL`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`INFO`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`ISSUE`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴⌘ Issuer cmds/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>) [`DONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`.HOST`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)

<br/>

## ⏩ Flow diagram 

![Accept](<🧑‍🦰 Save Token ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
|1| [🤗⏩🧑‍🦰 Prompt](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | ℹ️ Issuing your token...
|2| [🎴🐌🤵 `Issue@Broker`](<../../../../Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | In the [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>), [Issuers 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) offer a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|3| [🤗⏩🧑‍🦰 Prompt](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | 🫥 Save token? [Yes, No]
|4| [🤵🐌📣 `Save@Notifier`](<../../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>) | [Brokers 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) send the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID
|5| [🧑‍🦰🚀🎴 `Issued@Issuer`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 call.md>) | [Wallets 🧑‍🦰](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) download it and save it
|6| [🧑‍🦰🐌🤵 `Saved@Broker`](<../../../../Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) | [Wallets 🧑‍🦰](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) tell [Brokers 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) it's saved
|7| [🤵🐌🎴 `Offered@Issuer`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>) | [Brokers 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) tell [Issuers 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) of acceptance
|8| [🤗⏩🧑‍🦰 Prompt](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | ✅ Saved to your wallet.
|

<br/>

## FAQ

1. **Why the extra step to download the Token?**

    `Privacy` [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) are not proxied via the [Broker 🤵 domain](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) to protect user's privacy.    
    * Instead, [Wallet 🧑‍🦰 apps](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) download the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) directly from [Issuer 🎴 domain](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>).
    * Accepted [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) are stored locally, and only the path is sent to the [Broker 🤵 domain](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>).

    ---
    <br/>