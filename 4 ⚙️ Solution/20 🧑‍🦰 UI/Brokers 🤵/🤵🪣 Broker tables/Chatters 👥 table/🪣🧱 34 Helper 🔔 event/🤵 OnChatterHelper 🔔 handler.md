# 🤵 OnChatterHelper 🔔 handler

> Part of the [`Broker.Chatters` 🪣 table](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls the [`Invited@Helper` 🐌 msg](<../../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>)
  
<br/>

## Diagram

![alt text](<🤵 OnChatterHelper ⚙️ uml.png>)


## Script

```yaml
📃 OnChatterHelper:

# Assert the inputs for invites
- ASSERT|$.Chatter:
    AllOf: Schema, Invite

# Invite the helper to the chat
- SEND:
    Header:
        To: $Chatter.Domain
        Subject: Invited@Helper
    Body:
        Chat: $Chatter.Chat
        Inviter: $Chatter.Chat.Host
        Schema: $Chatter.Schema
        Invite: $Chatter.Invite
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Invited@Helper` 🐌 msg](<../../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>)
|