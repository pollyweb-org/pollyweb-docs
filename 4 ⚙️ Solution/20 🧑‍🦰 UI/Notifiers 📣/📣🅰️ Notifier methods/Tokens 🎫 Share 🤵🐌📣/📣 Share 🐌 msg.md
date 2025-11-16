# 🤵🐌📣 Share @ Notifier

> Implementations
* Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)

> Purpose
* Sends [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) to a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>).

> Flow
* Part of [`Share Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>) 
* triggers the [`Receive@Consumer` 🅰️ method](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Share@Notifier
Body: 
    Wallet: <wallet-id>
    Hook: <hook-uuid>
    Consumer: any-consumer.dom
    Tokens: 
      - Token: <token-uuid>
        Key: token-1234
```

|Object|Property|Type|Description|Origin |Purpose
|-|-|-|-|-|-
| Header|`From`|text| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
| |`To`|text| [Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
| | `Subject`|text| `Share@Notifier`
| Body | `Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|| `Hook` | uuid | [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) Hook | [`Query@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|| `Consumer` |text| [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | [ `Query@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
| Tokens | `Token`|uuid | [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) key | [`Save@`](<../Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|| `Key`|text| [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) key | [`Offer@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|