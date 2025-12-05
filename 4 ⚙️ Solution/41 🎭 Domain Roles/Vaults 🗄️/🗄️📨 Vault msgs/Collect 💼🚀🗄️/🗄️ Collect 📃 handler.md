# 🗄️ Collect@Vault 📃 handler

> About
* Implements the [Vault 🗄️ domain](<../../🗄️ Vault/🗄️🎭 Vault role.md>)
* Part of the [`Consume` ⏩ flow](<../../🗄️⏩ Vault flows/Consume 🗄️⏩💼/🗄️ Consume ⏩ flow.md>)
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Collect@Vault` 🚀 call](<🗄️ Collect 🚀 call.md>)

<br/>

## Diagram

![alt text](<🗄️ Collect ⚙️ uml.png>)

<br/>

## Script

```yaml
# Verify the signature
- VERIFY|$.Msg

# Get the share
- READ >> $share:
    Set: Vault.Shares
    Key: $.Msg.Collect
    Assert:
        Consumer: $.Msg.From
        Expires.IsFuture:

# Return the response
- RETURN:
    $share.Data
```


|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Shares`](<../../🗄️🪣 Vault tables/Discloses 💼 table/🪣 Collects/🗄️ Vault.Collects 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsFuture`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>) |
| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|