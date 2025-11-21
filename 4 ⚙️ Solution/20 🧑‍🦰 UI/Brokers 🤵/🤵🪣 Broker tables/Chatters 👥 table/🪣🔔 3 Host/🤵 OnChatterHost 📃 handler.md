# 🤵 OnChatterHost 📃 handler

> Part of [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

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
        Chat: $Chatter.Chat
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) |  [`Chatters`](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Hello@Host` 🅰️ method](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|