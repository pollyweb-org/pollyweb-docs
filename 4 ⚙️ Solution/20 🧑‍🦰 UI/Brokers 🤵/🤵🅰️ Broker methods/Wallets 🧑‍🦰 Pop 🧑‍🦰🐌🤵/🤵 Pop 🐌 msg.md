# 🧑‍🦰🐌🤵 PopBind @ Broker

> Implemented by [`PopBind@Broker` 📃 script](<🤵 Pop 📃 handler.md>)

* Opens a new [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) 
    * with the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
    * with a given context.

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | > Token 🎫 |
| | | > Broker 🤵 |
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ℹ️ Context: Token bla, bla
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🤗 Hi! What do you need? <br/> - [ Remove ] Token <br/> - [ Something else ] 
|


## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Pop@Broker

Body:
    Hook: <hook-uuid>
    Bind: <bind-uuid>
```

| Object | Property | Type |Description|Origin|Purpose
|-|-|-|-|-|-
| Header |`From`|domain| [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`To`|domain| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|| `Subject` | string | `Pop@Broker`
| Body | `Hook` | uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) hook || [`Converse@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>)
|| `Bind` | uuid   | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID
|

