# 🤵🐌📣 Share @ Notifier

> Implementations
* Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)

> Purpose
* Sends [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) to a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>).

> Flow
* Part of [`Share Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Token 🎫.md>) 
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
    Chat: <chat-uuid>
    Consumer: any-consumer.dom
    Tokens: 
      - Key: <token-key> 
        Path: /storage/nlweb/tokens/<token-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | [Broker 🤵 domain](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) name
| | `To`| string | [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) name
| | `Subject`| string | `Share@Notifier`
| Body | `Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID from [`Onboard@Broker`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|| `Chat` | string | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Query@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|| `Consumer` | string | [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) from [ `Query@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| Tokens | `Key`| uuid | `Key` from [`Offer@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
|| `Path`  | string | `Path` from [`Saved@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>)
|