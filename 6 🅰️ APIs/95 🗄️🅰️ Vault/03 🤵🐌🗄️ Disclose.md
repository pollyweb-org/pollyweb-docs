<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZa3f3ba7f94154a2fbd520e931 -->


# 🧑‍🦰🐌🗄️ Disclose @ Vault

> Request for a [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) to share user data with a [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>).

> Used by [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../5 ⏩ Flows/20 💼⏩ Consumers/02 💼⏩🧑‍🦰 Query vault.md>)

<br/>

## 🐌 Async Message


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
| Header| `From` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
|| `To` | string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) name
|| `Subject` | string | `Disclose@Vault`
|Body| `ChatID`| uuid | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
|| `Consumer` | string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
|| `Language` | enum | ISO language code
|| `BindID` | uuid | [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) ID
|
