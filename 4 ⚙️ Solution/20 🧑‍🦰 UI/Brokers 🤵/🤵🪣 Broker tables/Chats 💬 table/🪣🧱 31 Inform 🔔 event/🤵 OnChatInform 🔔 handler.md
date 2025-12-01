# 🤵 OnChatInform 🔔 handler

> About
* Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
* Part of the [🤵 `Broker.Chats.Inform` ⏩ flow](<../🪣🧱 30 Inform ⏩ flow/🤵 Broker.Chats.Inform ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnChatInform ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnChatInform:


# Progress the state
- SAVE|$Chat:
    .State: INFORMED
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
|