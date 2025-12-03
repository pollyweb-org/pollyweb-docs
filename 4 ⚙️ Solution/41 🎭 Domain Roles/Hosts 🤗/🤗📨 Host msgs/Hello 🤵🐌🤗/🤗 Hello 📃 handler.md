# 🤗 Hello 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Hello@Host` 🐌 msg](<🤗 Hello 🐌 msg.md>)

## Diagram

![alt text](<🤗 Hello ⚙️ uml.png>)

## Handler

```yaml
📃 Hello@Host:

# Verify the message
- VERIFY|$.Msg

# Check if the Broker is trustworthy
- TRUSTS|$.Msg.From:
    Schema: .HOST/HELLO

# Assert the message
- ASSERT|$.Msg:
    AllOf: Chat
    UUIDs: Chat

# Set the chat
- CHAT:
    Broker: $.Msg.From
    Chat: $.Msg.Chat

# Start a Chat for the locator
- TALK
```


Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CHAT`](<../../🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`TALK`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/TALK 😃/😃 TALK ⌘ cmd.md>) [`TRUSTS`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|