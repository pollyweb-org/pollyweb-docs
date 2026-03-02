# 🧑‍🦰🐌🤵 Opened @ Broker

> Purpose

* A [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    * informs the [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>) 
    * that a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) 
    * is ready to receive [Prompts 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>).


## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Opened@Broker

Body:
    Chat: <chat-uuid>
    PublicKey: <public-key>
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header |`From`|text| [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | [`Open@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
|        |`To`|text| [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>)  | [`Open@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) |
|        | `Subject` |text| `Opened@Broker` | 
| Body   | `Chat`  | uuid   | [Chat 💬 ID](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Open@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
|| `PublicKey`|string  | To verify messages || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>) [`Reply@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) [`Download@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Download 🧑‍🦰🚀🤗/🤗 Download 🚀 call.md>)
|