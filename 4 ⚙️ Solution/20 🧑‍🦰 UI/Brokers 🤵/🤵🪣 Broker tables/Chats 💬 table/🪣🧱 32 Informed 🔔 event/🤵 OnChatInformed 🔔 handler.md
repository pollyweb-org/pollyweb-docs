# 🤵 OnChatInformed 🔔 handler

> About
* Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
* Part of the [🤵 `Broker.Chats.Inform` ⏩ flow](<../🪣🧱 30 Inform ⏩ flow/🤵 Broker.Chats.Inform ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnChatInformed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnChatInformed:

# Tell the consumer to proceed
- SEND:
    Header: 
        To: $Chat.Host
        Subject: Informed@Consumer
    Body:
        Hook: $Chat.Informed
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats`](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Informed@Consumer`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Informed 🤵🐌💼/💼 Informed 🐌 msg.md>)
|