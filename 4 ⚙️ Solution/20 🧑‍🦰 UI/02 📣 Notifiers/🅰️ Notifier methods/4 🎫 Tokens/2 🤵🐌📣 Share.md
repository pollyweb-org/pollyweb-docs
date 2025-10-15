# 🤵💼🐌📣 Share @ Notifier

> Sends [Tokens 🎫](<../../../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) to a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>).

> Part of [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>) flow:
> <br/>• triggers [`Receive@Consumer`](<../../../../../6 🅰️ APIs/30 💼🅰️ Consumer/03 🧑‍🦰🐌💼 Receive.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Share@Notifier
Body: 
    WalletID: <wallet-id>
    ChatID: <chat-uuid>
    Consumer: any-consumer.com
    Tokens: 
      - /storage/nlweb/tokens/any-issuer.com/<token-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | [Broker 🤵 domain](<../../../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) name
| | `To`| string | [Notifier 📣 domain](<../../📣 Notifier domain.md>) name
| | `Subject`| string | `Share@Notifier`
| Body | `WalletID`| uuid | [Wallet 🧑‍🦰](<../../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) ID from [`Onboard@Broker`](<../1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|| `ChatID` | string | [Chat 💬](<../../../12 💬 Chats/$ 💬 Chat.md>) ID from [`Query@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>)
|| `Consumer` | string | [Consumer 💼](<../../../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) from [ `Query@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>)
| | `Tokens`  | string[] | Paths from [`Saved@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/53 🧑‍🦰🐌🤵 Saved.md>)
|