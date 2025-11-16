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
    Context: TOKEN
    Key: <token-uuid>
```

| Object | Property | Type |Description|Origin|Purpose
|-|-|-|-|-|-
| Header |`From`|text| [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`To`|text| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|| `Subject` |text| `Pop@Broker`
| Body | `Hook` | uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) hook || [`Open@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
|       | `Context`  | enum | `HOST` `ISSUER` `VAULT` `BIND` `TOKEN` 
|       | `Key` | uuid   | Optional context index
|

