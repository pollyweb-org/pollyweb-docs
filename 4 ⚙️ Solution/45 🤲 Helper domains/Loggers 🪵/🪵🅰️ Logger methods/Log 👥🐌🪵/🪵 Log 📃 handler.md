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
- GET >> $thread:
    Set: LoggerThreads
    Key: $.Msg.Thread

# Assert the sender
- ASSERT|$.Msg:
    From: $thread.Domain

# Save the log entry
- SAVE|LoggerEntry:
    Domain: $thread.Domain
    Thread: $thread.ID
    Sent: $.Msg.Sent
    Group: $.Msg.Group
    Blame: $.Msg.Blame
    Level: $.Msg.Level
    Text: $.Msg.Text
    Details: $.Msg.Details
```