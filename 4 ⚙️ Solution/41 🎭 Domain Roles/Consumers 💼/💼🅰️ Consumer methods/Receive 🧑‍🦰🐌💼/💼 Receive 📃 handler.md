# 💼 Receive 📃 handler

> Purpose

* [`Script`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Receive@Consumer` 🅰️ method](<💼 Receive 🐌 msg.md>)

<br/>

## Flow

![alt text](<💼 Receive ⚙️ uml.png>)

## Script

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
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>)  [`REEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|