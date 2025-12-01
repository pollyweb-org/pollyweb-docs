# 🤵 OnQueryAbrupt 🔔 handler


> About
* Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnQueryAbrupt ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryAbrupt:

# Load the Chat
- CHAT|$Query.Chat

# Fail the Chat due to ABRUPT Query
- FAIL|Unannounced request blocked.
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`FAIL`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>) |