# 🪵 Start 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Start@Logger` 🅰️ method](<🪵 Start 🚀 request.md>)

## Script

```yaml
📃 Start@Logger:

# Verify the message
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    Texts: Delete
    Lists: Groups

# Save the thread
- SAVE|LoggerThreads >> $thread:
    ID: .UUID
    Started: $.Msg.Header.Timestamp 
    Domain: $.Msg.Header.From
    Groups: $.Msg.Groups
    .Delete: $.Msg.Delete

# Return the thread ID
- RETURN:
    Thread: $thread.ID
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Threads`](<../../🪵🪣 Logger tables/🪵 LoggerThreads 🪣 table.md>) 
|