# 🤵 OnFormInformed 🔔 handler

> About
* Part of the [`Broker.Forms` 🪣 table](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)


<br/>

## Diagram

![alt text](<🤵 OnFormInformed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnFormInformed:

# Tell the consumer to proceed
- SEND:
    Header: 
        To: $Form.Consumer
        Subject: Informed@Consumer
    Body:
        Hook: $Form.Hook
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Forms`](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Informed@Consumer`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Informed 🤵🐌💼/💼 Informed 🐌 msg.md>)
|