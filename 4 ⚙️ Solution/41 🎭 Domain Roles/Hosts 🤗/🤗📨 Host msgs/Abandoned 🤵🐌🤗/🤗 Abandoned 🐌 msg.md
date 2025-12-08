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
| Header    |`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Locate@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)
|           |`To`|text| [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) | [`Hello@Host`](<../Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) <br/> [`Invited@Helper`](<../../../Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Help 🐌 msg.md>) <br/>  [`Disclose@Vault`](<../../../Vaults 🗄️/🗄️📨 Vault msgs/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)
|           | `Subject`     | string    | `Abandoned@Host`
| Body      | `Chat`      | uuid      | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Hello@Host`](<../Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|

<br/>


