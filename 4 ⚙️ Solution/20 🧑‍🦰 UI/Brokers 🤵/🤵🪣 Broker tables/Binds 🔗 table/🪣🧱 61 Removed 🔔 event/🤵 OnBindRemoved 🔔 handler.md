# 🤵 OnBindRemoved 🔔 handler

> About
* Part of the [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
* Part of the [🤵 `Broker.Binds.Remove` ⏩ flow](<../🪣🧱 60 Remove ⏩ flow/🤵 Broker.Binds.Remove ⏩ flow.md>)
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that plans the [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to be deleted in a random future.
  
<br/>

## Diagram

![alt text](<🤵 OnBindRemoved ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindRemoved:

# Notify the Vault
- SEND:
    Header:
        To: $Bind.Vault.Require
        Subject: Unbound@Vault
    Body:
        Bind: $Bind.ID.Require
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds`](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Unbound@Vault` 📨 msg](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Unbound 🤵🐌🗄️/🗄️ Unbound 🐌 msg.md>)
|