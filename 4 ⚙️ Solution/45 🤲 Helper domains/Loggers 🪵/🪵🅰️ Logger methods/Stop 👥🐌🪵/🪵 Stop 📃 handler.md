# 🪵 Stop 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Stop@Logger` 🅰️ method](<🪵 Stop 🐌 msg.md>)

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
- GET >> $thread:
    Set: LoggerThreads
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
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Threads`](<../../🪵🪣 Logger tables/🪵 LoggerThreads 🪣 table.md>) 
|