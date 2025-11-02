# 🧑‍🦰🐌🤵 Join @ Broker

> Purpose: 
* Asks the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * to join a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) to help.

> Used in:
* [🧑‍🦰👉🤵 Host Home](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Chats 💬/Host home 💬🤵/🧑‍🦰 Host home ⏩ flow.md>) flow
* [🧑‍🦰👉🤵 Abandon Chat](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Chats 💬/Abandon 💬🤵/🧑‍🦰 Abandon chat ⏩ flow.md>) flow

<br/>

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
...
| 🤗 [Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Continue [Yes, No] 
| | | > Broker 🤵 |
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 What do you need? <br/> - [ Home ] menu  <br/> - [ Abandon ] Chat <br/> - [ Something else ] 
|

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Join@Broker

Body:
    Chat: <chat-uuid>
    Host: any-host.dom
    Token: <token-uuid>
    Issuer: any-issuer.dom
    Bind: <bind-uuid>
    Vault: any-vault.dom
```

| Object | Property | Type |Description|Origin
|-|-|-|-|-
| Header |`From`|domain| [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`To`|domain| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|| `Subject` | string | `Join@Broker`
| Body | `Chat`  | uuid   | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)  | [`Converse@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>)
|