# 💼 Receive 📃 handler

> Purpose

* [`Script`](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Receive@Consumer` 🅰️ method](<💼 Receive 🐌 msg.md>)

<br/>

## Flow

![alt text](<💼 Receive ⚙️ uml.png>)

## Script

<!-- TODO
Confirm the trust of the received tokens.
It's true that the Broker already did it, 
but it may have been compromised.
-->

```yaml
📃 Receive@Consumer:

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Tokens, Hook
    UUIDs: Hook
    Lists: Tokens

# Resolve the callback
- READ >> $hook
    Set: Talker.Hooks
    Key: $.Msg.Hook

# Verify the Wallet signature
- VERIFY|$.Msg:
    Key: $hook.PublicKey

# Continue the Chat
- REEL|$hook:
    $.Msg.Tokens
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)  [`REEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|