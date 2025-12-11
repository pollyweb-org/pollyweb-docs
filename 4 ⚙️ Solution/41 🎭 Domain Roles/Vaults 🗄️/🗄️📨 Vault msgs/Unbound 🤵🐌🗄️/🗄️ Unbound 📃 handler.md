<!-- TODO -->

# 🗄️📃 Unbound handler

> Part of the [Vault 🗄️ domain](<../../🗄️ Vault/🗄️🎭 Vault role.md>)

> Implements the [`Unbound@Vault` 🐌 msg](<🗄️ Unbound 🐌 msg.md>)


## Script

```yaml
🗄️📃 Unbound@Vault:

# Verify the inputs
- ASSERT $.Msg:
    AllOf: Bind
    UUIDs: Bind

# Verify the domain signature
- VERIFY $.Msg

# Check if the Broker is still trustworthy
- TRUSTS|$.Msg.From:
    Schema: .BROKER

# Resolve the bind
- READ >> $bind:
    Set: Vault.Binds
    Key: $.Bind
    Assert: 
        Broker: $.Msg.From
        .State: BOUND

# Remove the bind
- SAVE $bind:
    .State: UNBOUND
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DELETE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [Binds 🪣](<../../🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
|