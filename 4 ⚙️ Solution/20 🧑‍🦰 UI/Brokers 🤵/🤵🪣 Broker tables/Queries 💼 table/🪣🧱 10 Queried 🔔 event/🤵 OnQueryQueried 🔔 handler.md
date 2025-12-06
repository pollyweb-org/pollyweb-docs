# 🤵 OnQueryQueried 🔔 handler

> About
* Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnQueryQueried ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryQueried:

# Get the queried schemas
- PUT >> $queried:
    $Query.Schemas

# Get the informed schemas
- PUT >> $informed:
    $Query.Chat.FormSchemas

# Check if only informed schemas were queried
- IF|$queried.IsIn($informed):
    Then: RETURN|INFORMED   # Continue
    Else: RETURN|ABRUPT     # Stop
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>)  |   
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>) [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) |
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) |
|