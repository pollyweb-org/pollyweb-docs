# 🧑‍🦰🐌💼 Shared @ Consumer

> List of [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) sent by a [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to a [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>).

> Used in the [💼⏩🧑‍🦰 Share Token @ Consumer](<../../5 ⏩ Flows/20 💼⏩ Consumers/03 💼⏩🧑‍🦰 Share Token.md>) flow.

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.com
    To: any-consumer.com
    Subject: Shared@Consumer
Body: 
    ChatID: <chat-uuid>
    Tokens: 
      - Code: airlines.any-igo.org/SSR/WCH:1 
        Issuer: any-issuer.com
        Key: ANY-TOKEN-KEY
        ...
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
| | `To`| string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
| | `Subject`| string | `Shared@Consumer`
| Body | `ChatID` | string | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
| | `Tokens`  | list | List of Token objects
| Token | `Code`| string | [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
| | `Issuer` | string | [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
| | `Key`| string | Resource key on the [Issuer 🎴](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>)
| | ... | ... | Other [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) fields
    

---
<br/>

## FAQ

1. **Why does the From has the Broker name instead of the Wallet's?**

    `Privacy` [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) should not be able to track returning users, so [Wallet 🧑‍🦰 apps](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) hide their identity behind the [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) for privacy.

    ---
    <br/>