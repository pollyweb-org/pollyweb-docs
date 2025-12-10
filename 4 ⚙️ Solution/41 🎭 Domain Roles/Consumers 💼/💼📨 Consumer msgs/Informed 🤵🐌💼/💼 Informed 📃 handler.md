# 💼 Informed 📃 handler

> Purpose

* [`Script`](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Informed@Consumer` 🐌 msg](<💼 Informed 🐌 msg.md>)
<br/>

## Flow

![alt text](<💼 Informed ⚙️ uml.png>)

## Script

```yaml
📃 Informed@Consumer:



# Assert the message
- ASSERT|$.Msg:
    AllOf: Hook
    UUIDs: Hook

# Resolve the callback
- READ >> $invite:
    Set: Consumer.Invites
    Key: $.Msg.Invite

# Save the received token
- SAVE|$invite:
    .State: HELPED
    Token: $.Msg.Help
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)  [`REEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|