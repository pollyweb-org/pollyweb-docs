# 🤵 OnPopLocalize 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a Pop to change the language.

<br/>

## Diagram

![alt text](<🤵 OnPopLocalize ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPopLocalize:

# Load the chat
- CHAT|$Pop.Chat

# Prompt the user for options
- ONE|What do you need? >> $option:
    Options:
        - 🈯 Set /language

# Process the user's option
- CASE|$option:
    /language: 
        SAVE|$Pop:
            .State: LOCALIZE
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
|