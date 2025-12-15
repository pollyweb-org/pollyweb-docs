<!-- 
🗄️🐌 https://quip.com/oSzpA7HRICjq/-Broker-Binds#temp:C:DSD3f7309f961e24f0ebb5897e2f 
🗄️🐌 https://quip.com/IZapAfPZPnOD#temp:C:PDZf81764583b31439f999550159  
-->

# 🤵🐌🗄️ Bound @ Vault

> About
* Implemented by the [`Bound` 📃 script](<🗄️ Bound 📃 handler.md>)
* Part of the [`Bind` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind vault ⏩ flow.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-vault.dom
    Subject: Bound@Vault

Body:
    Bind: <bind-uuid>
    Answer: ACCEPTED|DECLINED
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Bind@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
||`To`|text| [Vault 🗄️](<../../🗄️ Vault/🗄️🎭 Vault role.md>)  | [`Bind@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
|| `Subject` |text| `Bound@Vault`
|Body|  `Bind` | uuid | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID | [`Bind@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
|       | `Answer` | enum | `ACCEPTED` `DECLINED` |
|
