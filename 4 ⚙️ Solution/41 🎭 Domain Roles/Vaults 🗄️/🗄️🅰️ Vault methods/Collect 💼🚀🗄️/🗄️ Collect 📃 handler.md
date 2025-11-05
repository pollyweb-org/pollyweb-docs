# 🗄️📃 Collect handler

> Implementation
* Implements the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> Flow
* Part of the [`Consume` ⏩ flow](<../../🗄️⏩ Vault flows/Consume 🗄️⏩💼/🗄️ Consume ⏩ flow.md>)


> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Collect@Vault` 🅰️ method](<🗄️ Collect 🚀 request.md>)

<br/>

# Flow

![alt text](<🗄️ Collect ⚙️ uml.png>)


## Script


```yaml
# Verify the signature
- VERIFY|$.Msg

# Get the collect
- READ >> $collect:
    Set: VaultCollects
    Key: $.Msg.Collect

# Assert the Consumer
- ASSERT|$.Msg:
    From: $collect.Consumer

# Return the response
- RETURN:
    $collect.Data
```


|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Collects` 🪣 table](<../../🗄️🪣 Vault tables/Collects 💼 table/🗄️ VaultCollects 🪣 table.md>)
| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|