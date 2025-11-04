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
    Set: VaultBinds
    Key: $.Bind

# Confirm it's the same Broker
- ASSERT|$.Msg:
    From: $bind.Broker

# Remove the bind
- DELETE|$bind
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DELETE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) [`READ`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [Binds 🪣](<../../🗄️🪣 Vault tables/Binds 🔗 table/🗄️ VaultBinds 🪣 table.md>)
|