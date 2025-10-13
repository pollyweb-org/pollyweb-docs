# 🧑‍🦰🐌🤵 Help @ Broker

> Asks the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to join a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) to help.

> Used in:
> <br/> • [🧑‍🦰👉🤵 Host Home](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/02 🧑‍🦰👉🤵 Host home.md>) flow
> <br/> • [🧑‍🦰👉🤵 Abandon Chat](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>) flow

<br/>

## Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
...
| 🤗 [Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Continue [Yes, No] 
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 What do you need? <br/> - [ Home ] menu  <br/> - [ Abandon ] Chat <br/> - [ Something else ] 
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
| Header | `From`    | string | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|| `To`      | string | [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|| `Subject` | string | `Help@Broker`
| Body | `ChatID`  | uuid   | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)  from [`Assessed@Notifier`](<../../65 📣🅰️ Notifier/02 📣💬🅰️ Chats/21 🤵🐌📣 Assessed.md>)
|