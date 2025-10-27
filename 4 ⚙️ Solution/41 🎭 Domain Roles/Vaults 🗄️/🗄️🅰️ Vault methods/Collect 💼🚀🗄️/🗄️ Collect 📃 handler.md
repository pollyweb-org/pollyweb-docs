# 🗄️📃 Collect handler

> Part of the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Collect@Vault` 🅰️ method](<🗄️ Collect 🚀 request.md>)

## Script


```yaml
# Verify the signature
- VERIFY|$.Msg

# Get the collect
- GET >> $collect:
    Set: Collects@Vault
    Key: $.Msg.Collect

# Assert the Consumer
- ASSERT:
    $.Msg.From: $collect.Consumer

# Return the response
- RETURN:
    $collect.Data
```


|Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬/GET ⏬ item.md>) [`RETURN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RETURN ⤴️/RETURN ⤴️.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Collects` 🪣 table](<../../🗄️🪣 Vault tables/Collects 💼 table/🗄️ VaultCollects 🪣 table.md>)
| [Placeholder 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>)
|