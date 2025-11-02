<!-- Docs: https://quip.com/PCunAKUqSObO/-Notifier#temp:C:UKE27bcb1e6dd3e493f88b36b695 -->
<!-- Source: -->
<!-- Test: -->

# 🤵🐌📣 Translated @ Notifier

> Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)

> Purpose
* [Broker 🤵 domains](<../../../Brokers 🤵/🤵 Broker helper/🤵🤲 Broker helper.md>) call [Notifier 📣 domains](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) to re-render translated contented.


> Used by 
* [🧑‍🦰👉🤵 Translate](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Set Language 💬🤵/🧑‍🦰 Set Language ⏩ flow.md>) 

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Translated@Notifier
Body:
    Wallet: <wallet-uuid>
    Language: en-us
```

|Object|Property|Type|Description | Origin
|-|-|-|-|-
|Header|`From`|domain| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵🤲 Broker helper.md>) | [`Onboard@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 request.md>)
||`To`|domain| [Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 request.md>)
||`Subject`|string|`Translated@Notifier`
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID | [`Onboard@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 request.md>)
|      |`Language` |enum  | ISO code | [`Language@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Language 🧑‍🦰🐌🤵/🤵 Language 🐌 msg.md>)
|