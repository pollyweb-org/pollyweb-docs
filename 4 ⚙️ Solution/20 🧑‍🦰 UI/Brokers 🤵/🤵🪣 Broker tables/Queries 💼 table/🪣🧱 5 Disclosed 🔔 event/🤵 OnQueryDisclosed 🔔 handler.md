# 🤵 OnQueryDisclosed 🔔 handler

> About
* Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnQueryDisclosed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryDisclosed:

# Assert the Query
- ASSERT|$Query:
    AllOf: Bind, Vault

# Send the message to the vault
- SEND:
    Header:
        To: $Query.Vault
        Subject: Disclose@Vault
    Body:
        Chat: $Query.Chat
        Consumer: $Query.Domain
        Language: $Query.Chat.Language
        Bind: $Query.Bind
```

Used ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Disclose@Vault` 🅰️ method](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)