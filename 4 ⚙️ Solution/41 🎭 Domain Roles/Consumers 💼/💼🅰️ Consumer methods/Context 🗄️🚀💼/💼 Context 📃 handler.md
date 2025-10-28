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
- ASSERT:
    $.Msg.Schema.In($hook.Schemas)

# Check the trust
- TRUSTS|$.Msg.From:
    Schema: $.Msg.Schema
    Role: VAULT

# Return the context
- RETURN|$hook.Context
```