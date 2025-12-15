# 💼 Receive 📃 handler

> Purpose

* [`Script`](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Receive@Consumer` 🐌 msg](<💼 Receive 🐌 msg.md>)

<br/>

## Flow

![alt text](<💼 Receive ⚙️ uml.png>)

## Script

```yaml
📃 Receive@Consumer:

# Assert the message
- ASSERT $.Msg:
    AllOf: Query

# Resolve the callback
- READ >> $query:
    Set: Consumer.Queries
    Key: $.Msg.Query

# Save the received token
- SAVE $query:
    State: RECEIVED
    Token: $.Msg.Shared
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)  [`REEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|