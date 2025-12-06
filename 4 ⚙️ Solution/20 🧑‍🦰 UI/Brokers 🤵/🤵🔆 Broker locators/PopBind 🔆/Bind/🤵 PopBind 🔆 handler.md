# 🤵 OnPopBind 🔔 handler

> About
* Part of the [`Broker.Pops` 🪣 table](<../../../🤵🪣 Broker tables/Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
* Asks the user if they want do remove the [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>).


<br/>

## Script

```yaml
📃 OnPopBind:

# Get the Bind
- SELECT >> $bind:
    From: Broker.Binds
    Where: 
        ID: $.Chat.Inputs.Bind
        Wallet: $.Chat.Wallet
        .State: ACTIVE
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds`](<../../../🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)