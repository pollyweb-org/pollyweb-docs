# 🤵📃 OnPopped handler


## Diagram

![alt text](<🤵 OnPopInserted ⚙️ uml.png>)


## Script


```yaml
📃 OnPopped: 

# Request the Wallet to open a chat
- SEND:
    Header:
        To: $Pop.Notifier
        Subject: Open@Notifier
    Body:
        Wallet: <wallet-uuid>
        Hook: <hook-uuid>
        Chat: <chat-uuid>
        Host: another-domain.dom
        HostTitle: Any Other Domain, Inc.
        SmallIcon: <base64>
        BigIcon: <base46>
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`REGISTER`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/REGISTER 🔆/🔆 REGISTER ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds` 🪣 table](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Assess@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Assess 🤵🐌📣/📣 Assess 🐌 msg.md>)
|