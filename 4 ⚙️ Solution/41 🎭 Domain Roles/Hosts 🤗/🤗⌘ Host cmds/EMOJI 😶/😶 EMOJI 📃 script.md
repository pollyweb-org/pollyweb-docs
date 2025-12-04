# 😃📃 .EMOJI 💬 script

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`EMOJI` 💬 command](<😶 EMOJI ⌘ cmd.md>).


## Diagram

![alt text](<😶 EMOJI ⚙️ uml.png>)

<br/>

## How to run

```yaml
RUN|.EMOJI: 
    Emoji: 😶
```

<br/>

## Script

```yaml
📃 .EMOJI:

# Assert the required fields
- ASSERT:
    $Emoji.IsNotEmpty:
    $.Chat.IsNotEmpty:

# Get the Chat item
- READ >> $chat:
    Set: Host.Chats
    Key: 
        Broker: $.Chat.Broker
        Chat: $.Chat.Chat

# Set the emoji on the item
- SAVE|$chat:
    Emoji: $Emoji

# Set the emoji on the holder
- SET|$.Chat:
    Emoji: $Emoji
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SET`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Chats`](<../../🤗🪣 Host tables/Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |  [`.IsNotEmpty`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsNotEmpty ⓕ.md>)
[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 
|
