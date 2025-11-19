# 🤵 OnBindDeleted 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that informs a [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) that a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) was removed.
  
## Diagram

![alt text](<🤵 OnBindDeleted ⚙️ uml.png>)

## Script

```yaml
📃 OnBindDeleted:
    
# Inform the Vault
- SEND:
    Header:
        To: $Bind.Vault
        Subject: Unbound@Vault
    Body:
        Bind: $Bind.ID
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Unbound@Vault` 🅰️ method](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Unbound 🤵🐌🗄️/🗄️ Unbound 🐌 msg.md>) 
|