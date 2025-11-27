# 🤵 OnBindRemoved 🔔 handler

> Part of the [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that plans the [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to be deleted in a random future.
  
<br/>

## Diagram

![alt text](<🤵 OnBindRemoved ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindRemoved:
    
# Assert the inputs
- ASSERT|$Bind:
    AllOf: Vault
    Texts: Vault

# Notify the Vault
- SEND:
    Header:
        To: $Bind.Vault
        Subject: Unbound@Vault
    Body:
        Bind: $Bind.ID
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds`](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Unbound@Vault` 🅰️ method](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Unbound 🤵🐌🗄️/🗄️ Unbound 🐌 msg.md>)
|