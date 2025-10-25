# 🧑‍🦰🐌🤵 Pop @ Broker

> Implemented by [`Pop@Broker` 📃 script](<Pop 📃 handler.md>)

* Opens a new [Chat 💬](<../../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
    * with the [Broker 🤵 domain](<../../../🤵🤲 Broker helper.md>)
    * with a given context.

<br/>

## Chat

| [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | > Token 🎫 |
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../🤵🤲 Broker helper.md>) | ℹ️ Context: Token bla, bla
| 🤵 [Broker](<../../../🤵🤲 Broker helper.md>) | 🤗 Hi! What do you need? <br/> - [ Remove ] Token <br/> - [ Something else ] 
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
    Context: TOKEN
    Key: <token-uuid>
```

| Object | Property | Type |Description
|-|-|-|-
| Header | `From`    | string | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/🧑‍🦰🚀📣 Onboard.md>)
|| `To`      | string | [Broker 🤵](<../../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/🧑‍🦰🚀📣 Onboard.md>)
|| `Subject` | string | `Pop@Broker`
| Body | `Hook` | uuid | `Hook` for [`Converse@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/🤵🐌📣 Converse.md>)
|       | `Context`  | enum | `HOST` `ISSUER` `VAULT` `BIND` `TOKEN` 
|       | `Key` | uuid   | Optional index for the context
|

