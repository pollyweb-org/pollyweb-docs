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

# Assert the Pop
- ASSERT|$Pop:
    AllOf: Chat, Wallet

# Assert the Wallet
- ASSERT|$Pop.Wallet:
    AllOf: Language, Region
    Texts: Language, Region

# Load the chat
- CHAT|$Pop.Chat

# Remember the previous region for undo
- PUT >> $old:
    $Pop.Wallet.Language
    $Pop.Wallet.Region

# Inform current region
- INFO|Your current region is {$old.Region}.

# Prompt the user for the region
- ONE|Change to what region? >> $new:
    Options:
        - ID: pt-pt
          Title: 🇵🇹 Portugal
        - ID: pt-br
          Title: 🇧🇷 Brazil

# Ignore if already on that language
- IF|$old.Language.Is($new.ID):
    - SUCCESS|Already set to {$new.Title}!
    - RETURN

# Confirm before changing
- CONFIRM|Set to {$new.Title}?

# Process the user's option
- SAVE|$Pop.Wallet:
    Language: $new.ID
    Region: $new.Title

# Inform success, but allow an undo
- SUCCESS|Done! >> $success:
    Options: 
        - ↩️ /Revert to {$old.Region}

# Process undo request
- CASE|$success:
    Revert: 
    
        # Save back the previous language
        - SAVE|$Pop.Wallet:
            Language: $old.Language
            Region: $old.Region

        # Inform success of reversal
        - SUCCESS|Region reverted.
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SUCCESS`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Pops`](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) 
|