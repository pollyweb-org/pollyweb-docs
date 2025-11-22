# 🗄️ OnShareAsked 📃 handler

## Diagram

![alt text](<🗄️ OnShareAsked ⚙️ uml.png>)

## Script

```yaml
📃 OnShareAsked:

# Assert the Share
- ASSERT|$Share:
    AllOf: Chat, Consumer, Language, Bind.Schema, Bind.User
    Texts: Language, Consumer, Bind.Schema, Bind.User
    UUIDs: Chat

# Execute the handler
- ASYNC|OnDisclosure >> $hook:
    $Share.Chat
    $Share.Consumer
    $Share.Language
    $Share.Bind.Schema
    $Share.Bind.User

# Wait for the shared data
- WAIT >> $data:
    Hook: $hook

# Save the data for collection
- SAVE|$Share:
    .State: READY
    Data: $data
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`WAIT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
|