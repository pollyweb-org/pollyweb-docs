# 🤵 OnChatLocated 🔔 handler

> Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls the [`Open@Notifier` 📨 msg](<../../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>).

<br/>

## Diagram

![alt text](<🤵 OnChatDetailed ⚙️ uml.png>)


## Script

```yaml
📃 OnChatLocated:

# Open the Chat in the Wallet app
- SEND:
    Header:
        To: $Chat.Wallet.Notifier
        Subject: Open@Notifier
    Body:
        Chat: $Chat.ID.Require
        Wallet: $Chat.Wallet.Require
        Hook: $Chat.Hook
        Host: $Chat.Host.Require
        HostTitle: $Chat.HostTitle.Require
        SmallIcon: $Chat.SmallIcon
        BigIcon: $Chat.BigIcon
        ChatEmoji: $Chat.ChatEmoji
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Open@Notifier`](<../../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) 
|