# 🧑‍🦰🐌🤵 Saved @ Broker

> Implementation
* Implements the [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Saved` 📃 script](<🤵 Saved 📃 handler.md>)

> Purpose
* [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    * inform [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>) 
    * where the file with the [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) details 
    * was stored locally on the device.

> Flow
* Part of the [`Save Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>)
* Triggered by [`Save@Notifier`](<../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Saved@Broker

Body:
    Issuer: any-issuer.dom
    Token: <token-uuid>
    Path: /local/path/to/token/file
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>) | 
||`To`|text| [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>) | 
||`Subject`|text|`Saved@Broker` 
|Body  |`Issuer`| text | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) domain | [`Save@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>) | 
||`Token` |uuid  | [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>) key | [`Save@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>) | 
|  |`Path` |text  | Local saved path  |  | [`Remove@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>)
|