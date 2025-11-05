# 🤵📃 Set Language 

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Language@Broker`](<🤵 Language 🐌 msg.md>) method.

## Flow

![alt text](<🤵 Language ⚙️ uml.png>)

## Script

```yaml
📃 Language@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Language
    Texts: Language

# Get the Wallet from the message
- RUN|Get-Wallet >> $wallet

# Exit if language not changed
- CASE|$wallet.Language:
    $.Msg.Language: RETURN

# Translate domains and schemas
- RUN|Translate-All >> $translated:
    $wallet

# Save the new translations
- PARALLEL:
    - RUN|Save-Chats($wallet, $translated)
    - RUN|Save-Binds($wallet, $translated)
    - RUN|Save-Tokens($wallet, $translated)

# Change the Wallet
- SAVE|$wallet:
    Language: .Msg.Language

# Inform the Notifier
- RUN|Updated@Notifier:
    Wallet: $wallet
    Updates: [CHATS, BINDS, TOKENS]
```


|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`PARALLEL`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>)  [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)  [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)  
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) | [`Get Wallet` 📃 script](<scripts/🤵 Get Wallet 📃 script.md>)<br/>[`Translate All` 📃 script](<scripts/🤵 Translate All 📃 script.md>)<br/>[`Save Binds` 📃 script](<scripts/🤵 Save Binds 📃 script.md>)<br/>[`Save Chats` 📃 script](<scripts/🤵 Save Chats 📃 script.md>)<br/>[`Save Tokens` 📃 script](<scripts/🤵 Save Tokens 📃 script.md>)<br/>[`Update Notifier` 📃 script](<../../🤵⏩ Broker flows/Update Notifier 🤵⏩📣/🤵 Update Notifier 📃 script.md>) 
|
