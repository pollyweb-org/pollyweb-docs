# 🤵 PopWalletLocalize 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a Pop to change the language.

<br/>

## Diagram

![alt text](<🤵 PopWalletLocalize ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 PopWalletLocalize:

# Assert the Wallet
- ASSERT $wallet:
    AllOf: Language, Region
    Texts: Language, Region

# Remember the previous region for undo
- PUT >> $old:
    $wallet.Language
    $wallet.Region

# Inform current region
- INFO: Your current region is {$old.Region}.

# Get the regions
- SELECT >> $regions:
    All: ID, Title
    From: .Hosted.Assets.Regions

# Prompt the user for the region
- ONE Change to what region? >> $new:
    Options: $regions

# Ignore if already on that language
- IF:
    $old.Language: $new.ID
- THEN:
    - DONE: Already set to {$new.Title}!
    - RETURN

# Confirm before changing
- CONFIRM: Set to {$new.Title}?

# Process the user's option
- SAVE $wallet:
    Language: $new.ID
    Region: $new.Title

# Inform success, but allow an undo
- DONE >> $options:
    Text: Done!
    Options: 
        - ↩️ /Revert to {$old.Region}

# Process undo request
- CASE $options:
    Revert: 
    
        # Save back the previous language
        - SAVE $wallet:
            Language: $old.Language
            Region: $old.Region

        # Inform success of reversal
        - DONE: Region reverted.
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/1️⃣ ONE ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`DONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats`](<../../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Broker.Wallets`](<../../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) 
|