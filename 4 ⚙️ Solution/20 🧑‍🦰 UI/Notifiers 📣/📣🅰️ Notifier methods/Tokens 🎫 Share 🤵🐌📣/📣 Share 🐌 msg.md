# 🤵🐌📣 Share @ Notifier

> Implementations
* Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)

> Purpose
* Sends [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) to a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>).

> Flow
* Part of [`Share Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🎫 Share Token ⏩ flow.md>) 
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
      - Key: <token-key> 
        Path: /storage/nlweb/tokens/<token-uuid>
```

|Object|Property|Type|Description|Origin |Destination
|-|-|-|-|-|-
| Header| `From`    | string | [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) | [`Onboard@Broker`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
| | `To`| string | [Notifier 📣](<../../📣👥 Notifier domain.md>) | [`Onboard@Broker`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
| | `Subject`| string | `Share@Notifier`
| Body | `Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  | [`Onboard@Broker`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|| `Hook` | uuid | [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) Hook | [`Query@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Receive@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|| `Consumer` | string | [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | [ `Query@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Receive@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
| Tokens | `Key`| uuid | `Key` | [`Offer@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [`Receive@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|| `Path`  | string | `Path` | [`Saved@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>)
|