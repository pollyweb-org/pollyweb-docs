# 🗄️ Consume 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Consume@Consumer` 🅰️ method](<💼 Consume 🐌 msg.md>).

## Flow

![alt text](<💼 Consume ⚙️ uml.png>)

## Script

```yaml
📃 Consumer@Consumer:

# Verify the message
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Hook, Collect, Schema
    UUIDs: Hook, Collect
    Texts: Schema
    
# Get the hook
- READ >> $hook:
    Set: Talker.Hooks
    Key: $.Msg.Hook

# Is it the expected vault?
- ASSERT|$.Msg:
    From: $hook.Vault

# Is it one of the queried schemas?
- ASSERT|$.Msg:
    Schema.IsIn($hook.Schemas)

# Verify if the Vault is trusted
- TRUSTS|$.Msg.From:
    Schema: $.Msg.Schema$
    Role: VAULT

# Get the data
- SEND >> $data:
    Header: 
        To: $.Msg.From
        Subject: Collect@Vault
    Body:
        Collect: $.Msg.Collect

# Assert the schema
- ASSERT|$data:
    Schema: $.Msg.Schema

# Continue the talker 
- REEL|$.Msg.Hook:
    $data
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`TRUSTS`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks` 🪣 table](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 TalkerHooks 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Collect@Vault` 🅰️ method](<../../../Vaults 🗄️/🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 request.md>)
|