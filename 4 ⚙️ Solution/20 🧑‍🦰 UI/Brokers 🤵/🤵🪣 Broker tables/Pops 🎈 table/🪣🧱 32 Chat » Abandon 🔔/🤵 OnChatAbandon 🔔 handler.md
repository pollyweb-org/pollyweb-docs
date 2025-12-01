# 🤵 OnPopChatAbandon 📃 handler

> Part of the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a Pop to abandon a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

<br/>

## Diagram

![alt text](<🤵 OnChatAbandon ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPopAbandon:

# Assert the Pop
- ASSERT|$Pop:
    AllOf: Chat

# Load the chat
- CHAT|$Pop.Chat

# Ignore if not active
- IF|$Pop.Chat.State.IsNot(ACTIVE):
    - FAIL|The chat is not active.
    - RETURN

# Confirm before abandoning
- CONFIRM|Abandon this chat?

# Process the user's option
- SAVE|$Pop.Chat:
    .State: ABANDONED

# Inform success
- DONE|Chat abandoned!
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`FAIL`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>)  [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`DONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Pops`](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsNot`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsNot ⓕ.md>)
|