# 🤵📃 Pop handler

> Purpose
* [Script 📃](<🤵 PopBind 🐌 msg.md>) that implements the [`Pop@Broker` 🅰️ method](<🤵 PopBind 🐌 msg.md>)


## Script

<!-- TODO: Finish the code -->

```yaml
📃 PopBind: 

# Assert $.Msg
- ASSERT|$.Msg:
    - AllOf: Hook, Bind
    - UUIDs: Hook, Bind

# Get the Bind
- READ >> $bind:
    Set: Broker.Binds
    Key: $.Msg.Bind

# Verify the Message
- VERIFY|$.Msg:
    Key: $bind.Wallet.PublicKey

```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds` 🪣 table](<../../🤵🪣 Broker tables/Binds 🔗 table/🤵 Broker.Binds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|