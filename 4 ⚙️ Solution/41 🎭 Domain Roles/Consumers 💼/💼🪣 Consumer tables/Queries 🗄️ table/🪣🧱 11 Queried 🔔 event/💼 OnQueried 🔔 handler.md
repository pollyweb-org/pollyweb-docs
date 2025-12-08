# 💼 OnQueryQueried 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnQueried ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryQueried:

# Query the Broker
- SEND:
    Header:
        To: $Query.Broker
        Subject: Query@Broker
    Body: 
        Chat: $Query.Chat
        Query: $Query.ID
        Schemas: $Query.Schemas
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Queries`](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)