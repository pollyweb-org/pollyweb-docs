# 🤵 OnPopChat 📃 handler

> Part of the [`Broker.Pops` 🪣 table](<../../../🤵🪣 Broker tables/Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a Pop in a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

<br/>

## Diagram

![alt text](<🤵 PopChat ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPopChat:

- READ >> $chat:
    Set: Broker.Chats
    Key: $.Chat.Parameters.Chat
    Assert:
        Wallet: $.Msg.From

# Load the chat
- CHAT|$.Chat

# Prompt the user for options
- ONE|What do you need? >> $option:
    Options:
        - 🏃 /Abandon chat

# Process the user's option
- CASE|$option:
    Abandon: 
        RUN|PopChatAbandon
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Pops`](<../../../🤵🪣 Broker tables/Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>) 
|