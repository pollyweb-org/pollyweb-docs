# 🤵 OnBindRemoved 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that informs a [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) that a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) was removed.
  
## Diagram

![alt text](<🤵 OnBindRemoved ⚙️ uml.png>)

## Script

```yaml
📃 OnBindRemoved:

# Assert the inputs
- ASSERT|$Item:
    AllOf: Vault, ID
    Texts: Vault
    UUIDs: ID
    
# Inform the Vault
- SEND:
    Header:
        To: $Item.Vault
        Subject: Unbound@Vault
    Body:
        Bind: $Item.ID
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Unbound@Vault` 🅰️ method](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Unbound 🤵🐌🗄️/🗄️ Unbound 🐌 msg.md>) 
|