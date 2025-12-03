# 🤵 OnChatterHost 🔔 handler

> Part of [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

<br/>

## Diagram

![alt text](<🤵 OnChatterHost ⚙️ uml.png>)


## Script

```yaml
📃 OnChatterHost:

# Invite the Host to the chat
- SEND:
    Header:
        To: $Chatter.Domain
        Subject: Hello@Host
    Body:
        Chat: $Chatter.Chat.Require
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) |  [`Chatters`](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Hello@Host` 🐌 msg](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|