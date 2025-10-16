<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZa3f3ba7f94154a2fbd520e931 -->


# 🧑‍🦰🐌🗄️ Disclose @ Vault

> Request for a [Vault 🗄️ domain](<../🗄️🎭 Vault role.md>) to share user data with a [Consumer 💼 domain](<../../Consumers 💼/💼🎭 Consumer role.md>).

> Used by [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet chats/in Prompts 🤔/🧑‍🦰👉💼 Share Bind 🔗.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-broker.com
    To: any-broker.com
    Subject: Disclose@Vault
    
Body:
    ChatID: <chat-uuid>
    Consumer: any-coffee-shop.com
    Language: en-us
    BindID: <bind-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From` | string | [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>)
|| `To` | string | [Vault 🗄️ domain](<../🗄️🎭 Vault role.md>) name
|| `Subject` | string | `Disclose@Vault`
|Body| `ChatID`| uuid | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID
|| `Consumer` | string | [Consumer 💼 domain](<../../Consumers 💼/💼🎭 Consumer role.md>) name
|| `Language` | enum | ISO language code
|| `BindID` | uuid | [Bind 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) ID
|
