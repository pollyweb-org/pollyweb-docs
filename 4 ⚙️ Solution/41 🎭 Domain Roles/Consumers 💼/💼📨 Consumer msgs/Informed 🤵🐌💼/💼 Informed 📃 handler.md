# 💼 Informed 📃 handler

> Purpose

* [`Script`](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Informed@Consumer` 🐌 msg](<💼 Informed 🐌 msg.md>)
<br/>

## Flow

![alt text](<💼 Informed ⚙️ uml.png>)

## Script

```yaml
📃 Informed@Consumer:

# Verify the message
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg.Hook

# Continue the chat
- RACE|$.Msg.Hook
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RACE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/RACE 🏁/🏁 RACE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|