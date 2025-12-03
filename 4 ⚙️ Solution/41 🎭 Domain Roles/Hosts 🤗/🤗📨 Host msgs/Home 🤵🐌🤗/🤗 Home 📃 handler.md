# 🤗📃 Home

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Home@Host` 🐌 msg](<🤗 Home 🐌 msg.md>).


## Script

```yaml
📃 Home@Host: 

# Get the Chat
- READ >> $chat:
    Set: Host.Chats
    Key: $.Msg.Chat

# Start a Chat for the locator
- TALK|$.Msg.Chat|$chat.Locator
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`TALK`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/TALK 😃/😃 TALK ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤗🪣 Host tables/Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|