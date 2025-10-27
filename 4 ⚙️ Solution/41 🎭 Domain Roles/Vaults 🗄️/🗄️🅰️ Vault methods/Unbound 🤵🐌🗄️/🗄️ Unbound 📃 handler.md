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
- GET >> $bind:
    Set: Binds@Vault
    Key: $.Bind

# Confirm it's the same Broker
- ASSERT:
    $.Msg.From: $bind.Broker

# Remove the bind
- DELETE|$bind
```

|Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`DELETE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/DELETE/DELETE 🗑️ item.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬/GET ⏬ item.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [Binds 🪣](<../../🗄️🪣 Vault tables/Binds 🔗 table/🗄️ VaultBinds 🪣 table.md>)
|