# 🤵 OnPopChat 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a Pop in a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

<br/>

## Diagram

![alt text](<🤵 OnPopChat ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPopChat:

# Load the chat
- CHAT|$Pop.Chat

# Prompt the user for options
- ONE|What do you need? >> $option:
    Options:
        - 🏃 /Abandon chat

# Process the user's option
- CASE|$option:
    region: 
        SAVE|$Pop:
            .State: LOCALIZE
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Pops`](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>) 
|