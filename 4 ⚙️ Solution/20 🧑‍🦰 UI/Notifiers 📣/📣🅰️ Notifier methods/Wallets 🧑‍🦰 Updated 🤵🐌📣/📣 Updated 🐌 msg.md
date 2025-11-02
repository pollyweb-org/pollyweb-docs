
<!-- Docs: https://quip.com/PCunAKUqSObO/-Notifier -->
<!-- Source: -->
<!-- Test: -->


# 🤵🐌📣 Updated @ Notifier

> Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)

> Purpose
* The [Broker 🤵 domain](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * tells the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) 
    * that there was an update 
    * and they need to refresh the user experience.

> Used in
* [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../Brokers 🤵/🤵⏩ Broker flows/Update Binds 🤵⏩🔗/🤵 Update Binds ⏩ flow.md>)
* [🤵⏩🧑‍🦰 Update tokens](<../../../Brokers 🤵/🤵⏩ Broker flows/Update Tokens 🤵⏩🎫/🤵 Update Tokens ⏩ flow.md>)
* [🤵⏩🧑‍🦰 Update chats 💬](<../../../Brokers 🤵/🤵⏩ Broker flows/Update Chats 🤵⏩💬/🤵 Update Chats ⏩ flow.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Updated@Notifier
    
Body:
    Wallet: <wallet-uuid>
    Updates: [ CHATS, BINDS ]
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`|domain| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 request.md>)
||`To`|domain| [Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 request.md>)
||`Subject`|string|`Updated@Notifier`
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID | [`Onboard@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 request.md>)
|      |`Updates`   |enum  | `CHATS` `BINDS` `TOKENS`
|