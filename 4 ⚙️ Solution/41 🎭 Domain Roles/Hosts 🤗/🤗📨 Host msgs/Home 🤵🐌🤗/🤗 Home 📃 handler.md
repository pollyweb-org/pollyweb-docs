# 🤗 Home@Host 📃 handler

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Home@Host` 🐌 msg](<🤗 Home 🐌 msg.md>).


## Script

```yaml
📃 Home@Host: 

# Verify the message
- VERIFY $.Msg

# Assert the message
- ASSERT $.Msg:
    AllOf: Chat
    UUIDs: Chat

# Assert the Chat exists for the Broker
- READ >> $chat:
    Set: Host.Chats
    Key: 
        Chat: $.Msg.Chat
        Broker: $.Msg.From

# Start the default talker
- TALK
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`TALK`](<../../🤗⌘ Host cmds/TALK 😃/😃 TALK ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤗🪣 Host tables/Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|