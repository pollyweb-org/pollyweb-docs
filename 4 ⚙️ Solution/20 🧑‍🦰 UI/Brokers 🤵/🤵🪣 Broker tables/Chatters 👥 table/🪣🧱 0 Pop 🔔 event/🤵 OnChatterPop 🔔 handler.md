# 🤵 OnChatterPop 🔔 handler.md

> Part of the [`Broker.Chatters` 🪣 table](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)

<br/>
  
## Diagram

![alt text](<🤵 OnChatterPop ⚙️ uml.png>)


## Script

```yaml
📃 OnChatterPop:

# Update the Pop
- SAVE|$Chatter.Chat.Pop:
    .State: POPPED
    Chat: $Chatter.Chat
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Pops`](<../../Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
|