# 🗄️📃 Collect handler

> Implementation
* Implements the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> Flow
* Part of the [`Consume` ⏩ flow](<../../🗄️⏩ Vault flows/Consume 🗄️⏩💼/🗄️ Consume ⏩ flow.md>)


> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Script 📃/📃 Script.md>) that implements the [`Collect@Vault` 🅰️ method](<🗄️ Collect 🚀 request.md>)

<br/>

# Flow

![alt text](<🗄️ Collect ⚙️ uml.png>)


## Script


```yaml
# Verify the signature
- VERIFY|$.Msg

# Get the collect
- GET >> $collect:
    Set: VaultCollects
    Key: $.Msg.Collect

# Assert the Consumer
- ASSERT|$.Msg:
    From: $collect.Consumer

# Return the response
- RETURN:
    $collect.Data
```


|Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 for datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/Scripts 📃/📃 for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Collects` 🪣 table](<../../🗄️🪣 Vault tables/Collects 💼 table/🗄️ VaultCollects 🪣 table.md>)
| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|