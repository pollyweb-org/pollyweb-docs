# 🤵 OnBindBound 🔔 handler

> Part of the [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that informs a [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) that a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) was accepted.

<br/>
  
## Diagram

![alt text](<🤵 OnBindBound ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindBound:

# Inform the Vault
- SEND:
    Header:
        To: $Bind.Vault.Require
        Subject: Bound@Vault
    Body:
        Bind: $Bind.ID.Require
        Answer: ACCEPTED
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds`](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Bound@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|