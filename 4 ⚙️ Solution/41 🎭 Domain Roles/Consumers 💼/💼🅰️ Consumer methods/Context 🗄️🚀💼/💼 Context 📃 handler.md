# 💼 Context 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Context@Consumer` 🅰️ method](<💼 Context 🚀 request.md>)

## Flow

![alt text](<💼 Context ⚙️ uml.png>)

## Script

```yaml
📃 Context@Consumer:

# Verify the message
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Hook, Schema
    UUIDs: Hook
    Texts: Schema

# Get the hook
- READ >> $hook
    Set: TalkerHooks
    Key: $.Msg.Hook

# Assert the schemas
- ASSERT|$.Msg:
    Schema.In($hook.Schemas)

# Check the trust
- TRUSTS|$.Msg.From:
    Schema: $.Msg.Schema
    Role: VAULT

# Return the context
- RETURN|$hook.Context
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`TRUSTS`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks` 🪣 table](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 TalkerHooks 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|