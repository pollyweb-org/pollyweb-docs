# 🤵 OnBindBound 📃 handler

> Part of the [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that informs a [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) that a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) was accepted.
  
## Diagram

![alt text](<🤵 OnBindBound ⚙️ uml.png>)

## Script

```yaml
📃 OnBindBound:

# Inform the Vault
- SEND:
    Header:
        To: $Bind.Vault
        Subject: Bound@Vault
    Body:
        Hook: $Bind.Hook
        Bind: $Bind.ID
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Bound@Vault` 🅰️ method](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|