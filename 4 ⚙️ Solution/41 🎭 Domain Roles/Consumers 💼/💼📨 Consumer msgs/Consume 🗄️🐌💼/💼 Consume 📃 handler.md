# 🗄️ Consume 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Consume@Consumer` 📨 msg](<💼 Consume 🐌 msg.md>).

## Flow

![alt text](<💼 Consume ⚙️ uml.png>)

## Script

```yaml
📃 Consumer@Consumer:

# Verify the message
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Query, Collect, Schema
    UUIDs: Query, Collect
    Schema.IsSchema:
    
# Get the query
- READ >> $query:
    Set: Consumer.Queries
    Key: $.Msg.Query
    Assert: 
        # Is it the expected vault?
        Vault: $.Msg.From
        # Is it one of the queried schemas?
        Schemas.Contains: $.Msg.Schema

# Save the collect hook
- SAVE|$query:
    .State: CONSUME
    Collect: $.Msg.Collect
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks` 🪣 table](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsSchema`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Collect@Vault` 📨 msg](<../../../Vaults 🗄️/🗄️📨 Vault msgs/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>)
|