# 🪵 Log 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Log@Logger` 🅰️ method](<🪵 Log 🐌 msg.md>)

## Script

```yaml
📃 Log@Logger:

# Verify the message
- VERIFY|$.Msg

# Default inputs
- DEFAULT|$.Msg:
    Level: INFO

# Assert the inputs
- ASSERT|$.Msg:
    - AllOf: Thread, Text
    - UUIDs: Thread
    - Texts: Level, Text, Group, Blame
    - Level.IsIn(INFO, WARNING, ERROR)

# Get the thread
- READ >> $thread:
    Set: Logger.Threads
    Key: $.Msg.Thread

# Assert the sender
- ASSERT|$.Msg:
    From: $thread.Domain

# Discard by group filter, if set
- IF|$thread.Groups:
    IF|$.Msg.Group.NotIn($thread.Groups):
      RETURN

# Save the log entry
- SAVE|Logger.Entry:
    Domain: $thread.Domain
    Thread: $thread.ID
    Sent: $.Msg.Header.Timestamp
    Group: $.Msg.Group
    Blame: $.Msg.Blame
    Level: $.Msg.Level
    Text: $.Msg.Text
    Details: $.Msg.Details
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DEFAULT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Threads`](<../../🪵🪣 Logger tables/🪵 LoggerThreads 🪣 table.md>)  [`Entries`](<../../🪵🪣 Logger tables/🪵 LoggerEntries 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.NotIn`](<../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/IsNotIn ⓕ any.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|