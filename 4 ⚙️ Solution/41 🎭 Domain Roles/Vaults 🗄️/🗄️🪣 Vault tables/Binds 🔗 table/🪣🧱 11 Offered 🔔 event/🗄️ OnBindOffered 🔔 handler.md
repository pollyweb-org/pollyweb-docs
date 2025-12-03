# 🗄️ OnBindOffered 🔔 handler

> About
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that reacts to the [`BIND` command](<../../../🗄️⌘ Vault commands/BIND 🔗/🔗 BIND ⌘ cmd.md>), 
    * which is implemented by the [`BIND` 📃 script](<../../../🗄️⌘ Vault commands/BIND 🔗/🔗 BIND 📃 script.md>).
* Part of the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>)
* Part of the [🗄️ `Vault.Binds.Bind` ⏩ flow](<../🪣🧱 10 Bind ⏩ flow/🗄️ Vault.Binds.Bind ⏩ flow.md>)



<br/>

## Diagram

![alt text](<🗄️ OnBindOffered ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindOffered:

# Send the message to the Broker
- SEND:
    Header:
        To: $Bind.Broker
        Subject: Bind@Broker
    Body:
        Chat: $Bind.Chat.Require
        Bind: $Bind.ID.Require
        Schema: $Bind.Schema.Require
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds`](<../🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Bind@Broker` 🅰️ method](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
|