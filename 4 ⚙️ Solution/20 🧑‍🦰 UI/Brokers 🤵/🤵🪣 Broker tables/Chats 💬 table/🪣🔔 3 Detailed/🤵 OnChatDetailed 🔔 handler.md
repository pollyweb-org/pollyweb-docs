# 🤵 OnChatLocated 🔔 handler

> Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls the [`Open@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>).

<br/>

## Diagram

![alt text](<🤵 OnChatDetailed ⚙️ uml.png>)


## Script

```yaml
📃 OnChatLocated:

# Rename for legibility
- PUT|$Item >> $chat

# Open the Chat in the Wallet app
- SEND:
    Header:
        To: $chat.Wallet.Notifier
        Subject: Open@Notifier
    Body:
        Wallet: $chat.Wallet
        Hook: $chat.Hook
        Chat: $chat.ID
        PrivateKey: $chat.PrivateKey
        Host: $chat.Host
        HostTitle: $chat.HostTitle
        SmallIcon: $chat.SmallIcon
        BigIcon: $chat.BigIcon
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Open@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) 
|