# 🤵🐌📣 Updated @ Notifier

> Implements the [Notifier 📣 domain](<../../📣/📣 Notifier 👥 domain.md>)

> Purpose
* The [Broker 🤵 domain](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) 
    * tells the [Notifier 📣 domain](<../../📣/📣 Notifier 👥 domain.md>) 
    * that there was an update 
    * and they need to refresh the user experience.

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Updated@Notifier
    
Body:
    Wallet: <wallet-uuid>
    Old: {...}
    New: {...}
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`|text| [Broker 🤵](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Brokers 🤵/🤵📨 Broker msgs/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>)
||`To`|text| [Notifier 📣](<../../📣/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../../../Brokers 🤵/🤵📨 Broker msgs/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>)
||`Subject`|text|`Updated@Notifier`
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID | [`Onboard@`](<../../../Brokers 🤵/🤵📨 Broker msgs/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>)
|      |`Updates`   |enum  | `CHATS` `BINDS` `TOKENS`
|