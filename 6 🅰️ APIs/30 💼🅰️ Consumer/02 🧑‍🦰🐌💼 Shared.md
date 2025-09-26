# 🧑‍🦰🐌💼 Shared @ Consumer

> Asynchronous message sent directly by a Wallet to a [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>).

> Contains the shared [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).

> Used in [💼⏩🧑‍🦰 Query token](<../../5 ⏩ Flows/24 💼⏩ Consumers/03 💼⏩🧑‍🦰 Query token.md>).

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.org
    Subject: Shared@Consumer
Body: 
    ChatID: <chat-uuid>
    Tokens: 
      - Code: airlines.any-igo.org/SSR/WCH:1 
        Issuer: any-issuer.com
        TokenID: <token-uuid>
        ...
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | Wallet's [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
| | `Subject`| string | `Shared@Consumer`
| Body | `ChatID` | string | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
| | `Tokens`  | list | List of Token objects
| Token | `Code`| string | [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
| | `Issuer` | string | [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>)
| | `TokenID`| string | [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID on the Issuer
| | ... | ... | Other properties
    

---
<br/>