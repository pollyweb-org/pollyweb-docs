# 🧑‍🦰🐌🤵 Help @ Broker

> Asks the [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) to join a [Chat 💬](<../../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) to help.

> Used in:
> <br/> • [🧑‍🦰👉🤵 Host Home](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/02 🧑‍🦰👉🤵 Host home.md>) flow
> <br/> • [🧑‍🦰👉🤵 Abandon Chat](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>) flow

<br/>

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
...
| 🤗 [Host](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 😃 Continue [Yes, No] 
| | | > Broker 🤵 |
| 🤵 [Broker](<../../🤵🤲 Broker helper.md>) | 🫥 What do you need? <br/> - [ Home ] menu  <br/> - [ Abandon ] Chat <br/> - [ Something else ] 
|

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Help@Broker

Body:
    ChatID: <chat-uuid>
```

| Object | Property | Type |Description
|-|-|-|-
| Header | `From`    | string | [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|| `To`      | string | [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|| `Subject` | string | `Help@Broker`
| Body | `ChatID`  | uuid   | [Chat 💬](<../../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)  from [`Converse@Notifier`](<../../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|