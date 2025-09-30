# 🧑‍🦰🐌💼 Receive @ Consumer

> [Wallet 🧑‍🦰 apps](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) sends [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to a [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>).



> Part of the [💼⏩🧑‍🦰 Share Token @ Consumer](<../../5 ⏩ Flows/20 💼⏩ Consumers/03 💼⏩🧑‍🦰 Share Token.md>) flow:
> <br/>• succeeds [Share @ Notifier](<../65 📣🅰️ Notifier/02 📣💬🅰️ Chats/22 🤵🐌📣 Share.md>)

> List of [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>):
> <br/>• content from the response of [Issued @ Issuer](<../55 🎴🅰️ Issuer/01 🧑‍🦰🚀🎴 Issued.md>)
> <br/>• stored in local files during [ Saved @ Broker](<../15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/53 🧑‍🦰🐌🤵 Saved.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: Anonymous
    To: any-consumer.com
    Subject: Receive@Consumer
Body: 
    ChatID: <chat-uuid>
    Tokens: 
      - Issuer: any-issuer.com
        TokenID: ANY-TOKEN-KEY
        Code: airlines.any-igo.org/SSR/WCH:1 
        ...
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | `Anonymous`
| | `To`| string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
| | `Subject`| string | `Receive@Consumer`
| Body | `ChatID` | string | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
| | `Tokens`  | list | List of `Token` objects
| Token |  `Issuer` | string | [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
| | `TokenID`| string | Resource key on the [Issuer 🎴](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>)
||`Code`| string | [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
| | ... | ... | Other [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) fields
|
