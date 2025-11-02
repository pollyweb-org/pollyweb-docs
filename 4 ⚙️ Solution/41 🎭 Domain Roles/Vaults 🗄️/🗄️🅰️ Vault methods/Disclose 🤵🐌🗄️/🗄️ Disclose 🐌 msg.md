<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZa3f3ba7f94154a2fbd520e931 -->


# 🧑‍🦰🐌🗄️ Disclose @ Vault

> Purpose

* Request for a [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>) 
    * to share user data 
    * with a [Consumer 💼 domain](<../../../Consumers 💼/💼🎭 Consumer role.md>).

> Used by
* [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-broker.dom
    Subject: Disclose@Vault
    
Body:
    Chat: <chat-uuid>
    Consumer: any-coffee-shop.dom
    Language: en-us
    Bind: <bind-uuid>
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header|`From`|domain| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Bound@`](<../Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
||`To`|domain| [Vault 🗄️](<../../🗄️🎭 Vault role.md>) | [`Bound@`](<../Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|| `Subject` | string | `Disclose@Vault`
|Body| `Chat`| uuid | [Chat 💬 ID](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)  | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|| `Consumer` | string | [Consumer 💼](<../../../Consumers 💼/💼🎭 Consumer role.md>) | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|| `Language` | enum | ISO code | [`Language@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Language 🧑‍🦰🐌🤵/🤵 Language 🐌 msg.md>)
|| `Bind` | uuid | [Bind 🔗 ID](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) | [`Bound@`](<../Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|
