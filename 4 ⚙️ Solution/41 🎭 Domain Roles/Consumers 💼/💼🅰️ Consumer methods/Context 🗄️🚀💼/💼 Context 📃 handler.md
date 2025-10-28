# 💼 Context 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Context@Consumer` 🅰️ method](<💼 Context 🚀 request.md>)

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
- GET >> $hook
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

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`TRUSTS`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks` 🪣 table](<../../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 TalkerHooks 🪝 table.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>)
|