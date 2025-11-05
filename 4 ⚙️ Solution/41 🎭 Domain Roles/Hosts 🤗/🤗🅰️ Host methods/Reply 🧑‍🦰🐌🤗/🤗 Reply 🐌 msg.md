# 🧑‍🦰🐌🤗 Reply @ Host

> Flow
* Part of the [`Prompt` ⏩ flow](<../../🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>).

> Purpose

* A [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    * replies to a [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) 
    * of a [Host 🤗 domain](<../../🤗 Host role/🤗🎭 Host role.md>) 
    * in a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).



> Signature of the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
* signed with the `PrivateKey` from [`Converse@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) 🅰️ method
* verified with the `PublicKey` from [`Hello@Host`](<../Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) 🅰️ method


<br/>

## Async Message 🐌

```yaml
Header:
    From: Anonymous
    To: any-host.dom
    Subject: Reply@Host
    
Body: 
    Prompt: <prompt-uuid>
    Result: OK # Default
    Answer: [Starter, Main, Coffee]
```


|Object|Property|Type|Description | Origin
|-|-|-|-|-
| Header    |`From`|domain| `Anonymous`
|           |`To`|domain| [Sender 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) | [`Prompt@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Prompt 🤵🐌📣/📣 Prompt 🐌 msg.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `Prompt`    | uuid      | [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) ID | [`Prompt@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Prompt 🤵🐌📣/📣 Prompt 🐌 msg.md>)
|| `Result`| enum | `OK` `CANCEL` `YES` `NO` 
|| `Answer` | any | Answer to the [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)
|
