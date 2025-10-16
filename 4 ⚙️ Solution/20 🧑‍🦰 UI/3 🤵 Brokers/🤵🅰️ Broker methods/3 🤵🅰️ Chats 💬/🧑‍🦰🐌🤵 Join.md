# 🧑‍🦰🐌🤵 Join @ Broker

> Asks the [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) to join a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) to help.

> Used in:
> <br/> • [🧑‍🦰👉🤵 Host Home](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Chats 💬/💬🤵 Host home.md>) flow
> <br/> • [🧑‍🦰👉🤵 Abandon Chat](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Chats 💬/💬🤵 Abandon 💬.md>) flow

<br/>

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
...
| 🤗 [Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Continue [Yes, No] 
| | | > Broker 🤵 |
| 🤵 [Broker](<../../🤵🤲 Broker helper.md>) | 🫥 What do you need? <br/> - [ Home ] menu  <br/> - [ Abandon ] Chat <br/> - [ Something else ] 
|

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Join@Broker

Body:
    ChatID: <chat-uuid>
    Host: any-host.dom
    TokenID: <token-uuid>
    Issuer: any-issuer.dom
    BindID: <bind-uuid>
    Vault: any-vault.dom
```

| Object | Property | Type |Description
|-|-|-|-
| Header | `From`    | string | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|| `To`      | string | [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|| `Subject` | string | `Join@Broker`
| Body | `ChatID`  | uuid   | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>)  from [`Converse@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|