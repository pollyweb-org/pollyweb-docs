# 🤵 OnFormInformed 🔔 handler

> About
* Part of the [`Broker.Forms` 🪣 table](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
* Part of the [`Inform` ⏩ flow](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)


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
        Wait: $Form.Wait.Require
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Forms`](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Informed@Consumer`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Informed 🤵🐌💼/💼 Informed 🐌 msg.md>)
|