# 🤵💼🐌📣 Share @ Notifier

> Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)

> Sends [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) to a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>).

> Part of [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Token 🎫.md>) flow:
> <br/>• triggers [`Receive@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/🧑‍🦰🐌💼 Receive.md>)

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
      - /storage/nlweb/tokens/any-issuer.dom/<token-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | [Broker 🤵 domain](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) name
| | `To`| string | [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) name
| | `Subject`| string | `Share@Notifier`
| Body | `Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID from [`Onboard@Broker`](<../1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|| `Chat` | string | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Query@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/6 ...for Share 💼/💼🐌🤵 Query.md>)
|| `Consumer` | string | [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) from [ `Query@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/6 ...for Share 💼/💼🐌🤵 Query.md>)
| | `Tokens`  | string[] | Paths from [`Saved@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/5 ...for Tokens 🎫/🧑‍🦰🐌🤵 Saved.md>)
|