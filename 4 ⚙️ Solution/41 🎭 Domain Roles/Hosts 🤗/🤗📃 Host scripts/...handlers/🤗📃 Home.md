# 🤗📃 Home

[Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Home@Host` 🅰️ method](<../../🤗🅰️ Host methods/🤵🐌🤗 Home.md>).


## Script

```yaml
# Get the Chat
- GET|Chats@Host|$.Msg.Chat >> $chat

# Start a Chat for the locator
- TALK|$.Msg.Chat|$chat.Locator
```

Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/⌘ Command.md>) | [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/GET ⏬ item.md>) [`TALK`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/TALK 😃.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤗🪣 Host tables/🤗🪣 Chats 💬.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>)
|