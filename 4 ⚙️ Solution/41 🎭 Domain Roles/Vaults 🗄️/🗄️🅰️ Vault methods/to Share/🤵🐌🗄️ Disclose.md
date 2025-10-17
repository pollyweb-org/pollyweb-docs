<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZa3f3ba7f94154a2fbd520e931 -->


# 🧑‍🦰🐌🗄️ Disclose @ Vault

> Request for a [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>) to share user data with a [Consumer 💼 domain](<../../../Consumers 💼/💼🎭 Consumer role.md>).

> Used by [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Prompts 🤔/👉💼 Share Bind 🔗.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-broker.dom
    Subject: Disclose@Vault
    
Body:
    ChatID: <chat-uuid>
    Consumer: any-coffee-shop.com
    Language: en-us
    BindID: <bind-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From` | string | [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) from [`Bound@Vault`](<../to Bind/🤵🐌🗄️ Bound.md>)
|| `To` | string | [Vault 🗄️](<../../🗄️🎭 Vault role.md>) from [`Bound@Vault`](<../to Bind/🤵🐌🗄️ Bound.md>)
|| `Subject` | string | `Disclose@Vault`
|Body| `ChatID`| uuid | [Chat 💬 ID](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>)  from [`Query@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Query.md>)
|| `Consumer` | string | [Consumer 💼](<../../../Consumers 💼/💼🎭 Consumer role.md>) from [`Query@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Query.md>)
|| `Language` | enum | ISO code from [`Translate@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/🧑‍🦰🐌🤵 Translate.md>)
|| `BindID` | uuid | [Bind 🔗 ID](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) from [`Bound@Vault`](<../to Bind/🤵🐌🗄️ Bound.md>)
|
