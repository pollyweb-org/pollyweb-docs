# 🤵 OnChatterHelper 🔔 handler

> Part of the [`Broker.Chatters` 🪣 table](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls the [`Help@Helper` 🐌 msg](<../../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Help 🐌 msg.md>)
  
<br/>

## Diagram

![alt text](<🤵 OnChatterHelper ⚙️ uml.png>)


## Script

```yaml
📃 OnChatterHelper:

# Assert the inputs for invites
- ASSERT $.Chatter:
    AllOf: Schema, Invite

# Invite the helper to the chat
- SEND:
    Header:
        To: $Chatter.Domain
        Subject: Help@Helper
    Body:
        Chat: $Chatter.Chat
        Consumer: $Chatter.Chat.Host
        Schema: $Chatter.Schema
        Invite: $Chatter.Invite
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Broker.Chatters`](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Help@Helper`](<../../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Help 🐌 msg.md>)
|