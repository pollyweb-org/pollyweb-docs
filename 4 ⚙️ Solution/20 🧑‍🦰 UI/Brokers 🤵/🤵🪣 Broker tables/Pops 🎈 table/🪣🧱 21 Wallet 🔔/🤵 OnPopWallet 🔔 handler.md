# 🤵 OnPopWallet 📃 handler

> Part of the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a Pop in a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).

<br/>

## Diagram

![alt text](<🤵 OnPopWallet ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPopWallet:

# Load the chat
- CHAT|$Pop.Chat

# Prompt the user for options
- ONE|What do you need? >> $option:
    Options:
        - 🈯 Set /region

# Process the user's option
- CASE|$option:
    region: 
        SAVE|$Pop:
            .State: LOCALIZE
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
|