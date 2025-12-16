# 😃📃 `.GOODBYE` script

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`GOODBYE`](<👋 GOODBYE ⌘ cmd.md>) command.


<br/>

## Diagram

![alt text](<../GOODBYE 👋/👋 GOODBYE ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .GOODBYE:
    Message: Optional message
```
Uses: [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)

<br/>

## Script

```yaml
📃 .GOODBYE:

# Assert the message
- ASSERT:
    Texts: $Message

# Show the goodbye message, if any
- IF $Message:
    DONE: $Message

# Save the chat
- SAVE $.Chat.Item:
    STATE: GOODBYE    
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Chats`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🪣 Host tables/Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 
|