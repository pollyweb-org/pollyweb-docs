# 💼 OnQueryQueried 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

## Diagram

![alt text](<💼 OnQueryQueried ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryQueried:

# Query the Broker
- SEND:
    Header:
        To: $Query.Broker.Require
        Subject: Query@Broker
    Body: 
        Chat: $Query.Chat.Require
        Hook: $Query.ID
        Schemas: $Query.Schemas.Require
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)