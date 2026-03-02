# 🤵🐌🗄️ Disclose @ Vault

> Purpose

* Request for a [Vault 🗄️ domain](<../../🗄️ Vault/🗄️🎭 Vault role.md>) 
    * to share user data 
    * with a [Consumer 💼 domain](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>).

> Used by
* [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-vault.dom
    Subject: Disclose@Vault
    
Body:
    Bind: <bind-uuid>   # Vault Bind
    Chat: <chat-uuid>   # Broker Chat
    Query: <query-uuid>   # Consumer Hook
    Language: en-us     # Shared data language
    Consumer: any-consumer.dom
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header|`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | [`Bound@`](<../Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
||`To`|text| [Vault 🗄️](<../../🗄️ Vault/🗄️🎭 Vault role.md>) | [`Bound@`](<../Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|| `Subject` |text| `Disclose@Vault`
|Body|  `Bind` | uuid | [Bind 🔗 ID](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) | [`Bound@`](<../Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|| `Chat`| uuid | [Chat 💬 ID](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)  | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|| `Query` | uuid| [Consumer 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>)  hook | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) 
|| `Consumer` |text| [Consumer 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|| `Language` | enum | ISO code | 
|
