# 🤵 OnQueryShared 🔔 handler

> About
* Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnQueryShared ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryShared:

# Assert the Query
- ASSERT|$Query:
    AllOf: Token, Issuer

# Send the message to the Notifier
- SEND:
    Header:
        To: $Query.Wallet.Notifier
        Subject: Share@Notifier
    Body:
        Chat: $Query.Chat
        Consumer: $Query.Domain
        Language: $Query.Chat.Language
        Bind: $Query.Bind
```

Used ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Share@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>) 
