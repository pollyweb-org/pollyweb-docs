# 💼 Receive 📃 handler

> Purpose

* [`Script`](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Receive@Consumer` 🅰️ method](<💼 Receive 🐌 msg.md>)

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
- GET >> $hook
    Set: TalkerHooks
    Key: $.Msg.Hook

# Verify the Wallet signature
- VERIFY|$.Msg:
    Key: $hook.PublicKey

# Continue the Chat
- REEL|$hook:
    $.Msg.Tokens
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>)  [`REEL`](<../../../../35 💬 Chats/Scripts 📃/...control ▶️/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|