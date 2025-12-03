# 🤵 OnPopInserted 🔔 event

> Part of the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the [`Pop@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🤵 OnPopInserted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPopped: 

# Assert the Pop
- ASSERT|$Pop:
    AllOf: Wallet, Hook, Key, Context
    UUIDs: Wallet, Hook
    Texts: Context, Key

# Add the Chat
- SAVE|Broker.Chats:
    .State: ASKED
    Pop: $Pop.ID
    Hook: $Pop.Hook
    Wallet: $Pop.Wallet
    Host: $.Hosted.Domain
    Key: POP
    Inputs:
        $Pop.Context
        $Pop.Key
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Pops`](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted` 🧠 holder](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|