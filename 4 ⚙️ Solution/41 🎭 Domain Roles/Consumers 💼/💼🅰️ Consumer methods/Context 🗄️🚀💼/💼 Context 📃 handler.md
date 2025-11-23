# 💼 Context 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Context@Consumer` 🅰️ method](<💼 Context 🚀 call.md>)

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
    Set: Talker.Hooks
    Key: $.Msg.Hook

# Assert the schemas
- ASSERT|$.Msg:
    Schema.IsIn($hook.Schemas)

# Check the trust
- TRUSTS|$.Msg.From:
    Schema: $.Msg.Schema
    Role: VAULT

# Return the context
- RETURN|$hook.Context
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`TRUSTS`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks` 🪣 table](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|