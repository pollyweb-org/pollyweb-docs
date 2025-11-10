# 🧑‍🦰🐌🤵 PopToken @ Broker

* Opens a new [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) 
    * with the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
    * for a given [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).

<br/>

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | > Token 🎫 |
| | | > Broker 🤵 |
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ℹ️ Context: Token bla, bla
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🤗 Hi! What do you need? <br/> - [ Tag ] Token  <br/> - [ Remove ] Token 
|

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Pop@Broker

Body:
    Hook: <hook-uuid>
    Token: <token-uuid>
```

| Object | Property | Type |Description|Origin|Purpose
|-|-|-|-|-|-
| Header |`From`|domain| [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`To`|domain| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|| `Subject` | string | `PopToken@Broker`
| Body | `Hook` | uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) hook || [`Converse@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>)
|       | `Token` | uuid   | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID
|

