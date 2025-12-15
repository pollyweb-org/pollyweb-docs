# 🤗 Abandoned@Host 📃 handler

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Abandoned@Host` 🐌 msg](<🤗 Abandoned 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🤗 Abandoned ⚙️ uml.png>)

<br/>

## Handler

```yaml
📃 Abandoned@Host:

# Assert the message
- ASSERT $.Msg:
    AllOf: Chat
    UUIDs: Chat

# Verify the message
- VERIFY $.Msg

# Read the chat
- READ >> $chat:
    Set: Host.Chats
    Key: 
        Chat: $.Msg.Chat
        Broker: $.Msg.From

# Mark the chat as abandoned
- SAVE $chat:
    State: ABANDONED
```

Uses ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Chats`](<../../🤗🪣 Host tables/Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)