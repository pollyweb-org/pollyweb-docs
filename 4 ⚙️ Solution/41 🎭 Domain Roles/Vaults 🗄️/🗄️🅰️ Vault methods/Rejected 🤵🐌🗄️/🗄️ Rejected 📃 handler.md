# 🗄️ Rejected 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Rejected@Vault` 🅰️ method](<🗄️ Rejected 🐌 msg.md>).

<br/>

## Diagram

![alt text](<🗄️ Rejected ⚙️ uml.png>)

<br/>

## Script
```yaml
📃 Rejected@Vault:

# Verify the message
- VERIFY|$.Msg

# Assert required fields
- ASSERT|$.Msg:
    AllOf: Hook

# Resolve the bind
- READ >> $bind:
    Set: Vault.Binds
    Key: $.Msg.Hook
    Assert: 
        Broker: $.Msg.From

# Update the state
- SAVE|$bind:
    .State: REJECTED
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds`](<../../🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>) |
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) |
|