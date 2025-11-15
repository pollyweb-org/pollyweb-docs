# 🤵🐌📣 Frozen @ Notifier 

> Implementation
* Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)

> Flow
* Part of the [`Freeze` ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Freeze 🤗⏩❄️/🤗 Freeze ⏩ flow.md>)
* Called by [`Freeze@Broker` 🅰️ method](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Freeze 🤗🐌🤵/🤵 Freeze 🐌 msg.md>) 

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Frozen@Notifier
    
Body:
    Wallet: <wallet-uuid>
    Chat: <chat-uuid>
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`|string|[Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) name|[`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>)
||`To`|string|[Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) name|[`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>)
||`Subject`|string|`Frozen@Notifier`
|Body|`Wallet`|uuid|[Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID|[`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>)
||`Chat`|uuid|[Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID|[`Open@Notifier`](<../Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
|