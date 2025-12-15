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
📃 Collect@Vault:

# Verify the inputs
- ASSERT $.Msg:
    AllOf: Disclose
    UUIDs: Disclose

# Verify the signature
- VERIFY $.Msg

# Get the disclose
- READ >> $disclose:
    Set: Vault.Discloses
    Key: $.Msg.Disclose
    Assert:
        Consumer: $.Msg.From
        Expires.IsFuture:

# Return the response
- RETURN:
    $disclose.Data
```


|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Discloses`](<../../🗄️🪣 Vault tables/Discloses 💼 table/🪣 Discloses/🗄️ Vault.Discloses 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsFuture`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>) |
| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|