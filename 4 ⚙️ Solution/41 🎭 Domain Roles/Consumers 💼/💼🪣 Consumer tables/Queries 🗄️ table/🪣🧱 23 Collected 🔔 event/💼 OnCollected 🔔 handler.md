# 💼 OnQueryCollected 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnCollected ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryCollected:

# Continue the talker 
- RACE $Query.ID:
    $Query.Collected
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`RACE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/RACE 🏁/🏁 RACE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Queries`](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)