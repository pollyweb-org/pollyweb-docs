# 💼 OnQueryTokened 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnQueryTokened ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryTokened:

# Continue the talker 
- RACE|$Query.ID:
    $Query.Token
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`RACE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/RACE 🏁/🏁 RACE ⌘ cmd.md>)