# 🤵🐌🤗 Abandoned @ Host

> About
* Part of the [Abandon session 🧑‍🦰👉🤗](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Chats 💬/Abandon 💬🤵/🧑‍🦰 Abandon chat ⏩ flow.md>) flow.
* Tells all [Host 🤗 domains](<../../🤗 Host role/🤗🎭 Host role.md>) in a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) that the user abandoned it.

<br/>


## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-host.dom
    Subject: Abandoned@Host

Body: 
    Chat: <chat-uuid>
```

|Object|Property|Type|Description | Origin 
|-|-|-|-|-
| Header    |`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Pop@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>)
|           |`To`|text| [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) | [`Hello@`](<../Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) <br/> [`Invited@`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>) <br/>  [`Disclose@`](<../../../Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)
|           | `Subject`     | string    | `Abandoned@Host`
| Body      | `Chat`      | uuid      | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Hello@`](<../Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|

<br/>


