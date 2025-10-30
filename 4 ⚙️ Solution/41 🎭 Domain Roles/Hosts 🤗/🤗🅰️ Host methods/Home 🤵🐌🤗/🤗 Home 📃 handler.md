# 🤗📃 Home

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/📃 Script.md>) that implements the [`Home@Host` 🅰️ method](<🤗 Home 🐌 msg.md>).


## Script

```yaml
📃 Home@Host: 

# Get the Chat
- GET >> $chat:
    Set: HostChats
    Key: $.Msg.Chat

# Start a Chat for the locator
- TALK|$.Msg.Chat|$chat.Locator
```

Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/⌘ Command.md>) | [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`TALK`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/TALK 😃/😃 TALK ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤗🪣 Host tables/Chats 💬 table/🤗 HostChats 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|