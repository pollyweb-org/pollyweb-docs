# 😃📃 .EMOJI 😶 script

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`EMOJI` ⌘ command](<😶 EMOJI ⌘ cmd.md>)


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

# Wait for the Broker to change it
- SEND >> $wait:
    Header: 
        To: $.Chat.Broker
        Subject: Emoji@Broker
    Body:
        Chat: $.Chat.Chat
        Emoji: $Emoji
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |  [`.IsNotEmpty`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsNotEmpty ⓕ.md>)
[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 
|
