
<!-- Docs: https://quip.com/PCunAKUqSObO/-Notifier -->
<!-- Source: -->
<!-- Test: -->


# 🤵🐌📣 Updated @ Notifier

> Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)

> Purpose
* The [Broker 🤵 domain](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) 
    * tells the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) 
    * that there was an update 
    * and they need to refresh the user experience.

> Used in
* [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../Brokers 🤵/🤵⏩ Broker flows/Update Binds 🤵⏩🔗/Update Binds ⏩ flow.md>)
* [🤵⏩🧑‍🦰 Update tokens](<../../../Brokers 🤵/🤵⏩ Broker flows/Update Tokens 🤵⏩🎫/Update Tokens ⏩ flow.md>)
* [🤵⏩🧑‍🦰 Update chats 💬](<../../../Brokers 🤵/🤵⏩ Broker flows/Update Chats 🤵⏩💬/Update Chats ⏩ flow.md>)

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

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) name
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) from [`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/...for Wallets 🧑‍🦰/Onboard/📣🚀🤵 Onboard.md>)
||`Subject`|string|`Updated@Notifier`
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID from [`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/...for Wallets 🧑‍🦰/Onboard/📣🚀🤵 Onboard.md>)
|      |`Updates`   |enum  | `CHATS` `BINDS` `TOKENS`
|