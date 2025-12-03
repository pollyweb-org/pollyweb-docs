# 🤵 Goodbye 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Goodbye@Broker`](<🤵 Goodbye 🐌 msg.md>) method.

## Diagram

![alt text](<🤵 Goodbye ⚙️ uml.png>)

## Script

```yaml
📃 Goodbye@Broker:

# Verify the message
- VERIFY|$.Msg

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Chat
    UUIDs: Chat

# Read the chatter
- READ >> $chatter:
    Set: Broker.Chatters
    Key: 
        Domain: $.Msg.From
        Chat: $.Msg.Chat
    Assert:
        Role: HOST

# Process the Chat state
- SAVE|$chatter.Chat:
    .State: CLOSED
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSESS`](<../../🤵⏩ Broker flows/Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>)  [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|