# 🪵 Log 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Log@Logger` 🅰️ method](<🪵 Log 🐌 msg.md>)

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
    AllOf: Thread, Text
    UUIDs: Thread
    Texts: Level, Text, Group, Blame

# Assert the level
- ASSERT|$.Msg.Level:
    Enum: INFO, WARNING, ERROR

# Get the thread
- READ >> $thread:
    Set: LoggerThreads
    Key: $.Msg.Thread

# Assert the sender
- ASSERT|$.Msg:
    From: $thread.Domain

# Discard by group filter, if set
- IF|$thread.Groups:
    IF|$.Msg.Group.NotIn($thread.Groups):
      RETURN

# Save the log entry
- SAVE|LoggerEntry:
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
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DEFAULT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) [`READ`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Threads`](<../../🪵🪣 Logger tables/🪵 LoggerThreads 🪣 table.md>)  [`Entries`](<../../🪵🪣 Logger tables/🪵 LoggerEntries 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Function 🐍.md>) | [`.NotIn`](<../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.IsNotIn}.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|