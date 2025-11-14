<!-- TODO -->

# 🗄️📃 Unbound handler

> Part of the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> Implements the [`Unbound@Vault` 🅰️ method](<🗄️ Unbound 🐌 msg.md>)


## Script

```yaml
🗄️📃 Unbound@Vault:

# Verify the domain signature
- VERIFY|$.Msg

# Resolve the bind
- READ >> $bind:
    Set: Vault.Binds
    Key: $.Bind

# Confirm it's the same Broker
- ASSERT|$.Msg:
    From: $bind.Broker

# Remove the bind
- DELETE|$bind
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DELETE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [Binds 🪣](<../../🗄️🪣 Vault tables/Binds 🔗 table/🗄️ Vault.Binds 🪣 table.md>)
|