<!-- 
🗄️🐌 https://quip.com/oSzpA7HRICjq/-Broker-Binds#temp:C:DSD3f7309f961e24f0ebb5897e2f 
🗄️🐌 https://quip.com/IZapAfPZPnOD#temp:C:PDZf81764583b31439f999550159  
-->

# 🤵🐌🗄️ Bound @ Vault

> Implementation
* Implemented by the [`Bound` 📃 script](<🗄️ Bound 📃 handler.md>)


> Used by

* [`Bind` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind vault ⏩ flow.md>)


## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-vault.dom
    Subject: Bound@Vault

Body:
    Offer: <bind-uuid>
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Bindable@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)
||`To`|text| [Vault 🗄️](<../../🗄️🎭 Vault role.md>)  | [`Bindable@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)
|| `Subject` |text| `Bound@Vault`
|Body|  `Offer` | uuid |  [Vault 🗄️](<../../🗄️🎭 Vault role.md>)  hook| [`Bindable@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)
|
