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

# Prompt the user for the region
- ONE|To what region? >> $lang:
    Options:
        - ID: pt-pt
          Title: 🇵🇹 Portugal
        - ID: pt-br
          Title: 🇧🇷 Brazil

# Remember the previous region for undo
- PUT|$Pop.Wallet.Language >> $prevLang

# Ignore if already on that language
- IF|$prevLang == $lang.ID:
    - SUCCESS|Already set to {$lang.Title}!
    - RETURN

# Confirm before changing
- CONFIRM|Set to {$lang.Title}?

# Process the user's option
- SAVE|$Pop.Wallet:
    Language: $lang

# Inform success, but allow an undo
- SUCCESS|Done! >> $success:
    Options: 
        - ↩️ /Undo set region

# Process undo request
- CASE|$success:
    Undo: 
    
        # Save back the previous language
        - SAVE|$Pop.Wallet:
            Language: $prevLang

        # Inform success of reversal
        - SUCCESS|Region reverted.
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
|