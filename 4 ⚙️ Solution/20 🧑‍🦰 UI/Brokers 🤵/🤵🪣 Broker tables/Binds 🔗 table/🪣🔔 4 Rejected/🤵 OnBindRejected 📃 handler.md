# 🤵 OnBindRejected 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that informs a [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) that a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) was rejected.
  
## Diagram

![alt text](<🤵 OnBindRejected ⚙️ uml.png>)

## Script

```yaml
📃 OnBindRejected:
    
# Inform the Vault
- SEND:
    Header:
        To: $Bind.Vault
        Subject: Bound@Vault
    Body:
        Hook: $Bind.Hook
        Bind: $Bind.ID
        Accepted: False
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Bound@Vault` 🅰️ method](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|