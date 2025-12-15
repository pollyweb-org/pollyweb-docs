# 💼 OnQueryReceived 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnReceived ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryReceived:

# Validate the Schema
- ASSERT $Query.Token:
    Error: Unexpected schema
    Schema.IsIn: $Query.Schemas

# Verify the Token signature and schema
- VERIFY: $Query.Token

# Otherwise, progress
- RETURN: TOKENED
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)   [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>) 
|[{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsPast`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsPast ⓕ.md>) [`.IsFuture`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>) [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Queries`](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)