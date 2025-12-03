# 🤵🐌📣 Share @ Notifier

> About
* Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)
* Sends [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) to a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>).
* Part of [`Share Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>) 
* triggers the [`Receive@Consumer` 🅰️ method](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Share@Notifier
Body: 
    Wallet: <wallet-id>
    Query: <query-uuid>
    Consumer: any-consumer.dom
    Token: <token-uuid>
    Issuer: any-issuer.dom
```

|Object|Property|Type|Description|Origin |Purpose
|-|-|-|-|-|-
| Header|`From`|text| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
| |`To`|text| [Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
| | `Subject`|text| `Share@Notifier`
| Body | `Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|| `Query` | uuid | [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) Query | [`Query@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|| `Consumer` |text| [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) | [ `Query@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
| | `Token`|uuid | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID | [`Save@`](<../Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|| `Issuer`|text| [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name | [`Issue@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|