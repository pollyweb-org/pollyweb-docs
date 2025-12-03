# 🪵 Stop 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Stop@Logger` 📨 msg](<🪵 Stop 🐌 msg.md>)

## Script

```yaml
📃 Stop@Logger:

# Verify the message
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Thread
    UUIDs: Thread

# Get the thread
- READ >> $thread:
    Set: Logger.Threads
    Key: $.Msg.Thread

# Assert the sender
- ASSERT|$.Msg:
    From: $thread.Domain

# Update the thread
- SAVE|$thread:
    Stopped: $.Msg.Header.Timestamp
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Threads`](<../../🪵🪣 Logger tables/🪵 LoggerThreads 🪣 table.md>) 
|