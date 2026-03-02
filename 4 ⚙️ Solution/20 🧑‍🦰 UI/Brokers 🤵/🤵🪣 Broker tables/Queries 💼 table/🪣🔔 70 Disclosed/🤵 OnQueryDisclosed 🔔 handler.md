# 🤵 OnQueryDisclosed 🔔 handler

> About
* Part of the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnQueryDisclosed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryDisclosed:

# Send the message to the vault
- SEND:
    Header:
        To: $Query.Vault.Require
        Subject: Disclose@Vault
    Body:
        Bind: $Query.Bind.Require
        Chat: $Query.Chat.Require
        Query: $Query.Query.Require
        Consumer: $Query.Consumer.Require
        Language: $Query.Chat.Language.Require
```

Used ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Disclose@Vault` 🐌 msg](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)