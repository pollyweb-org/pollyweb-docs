# ⏰ Export 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Script 📃/📃 Script.md>) that implements the [`Export@Alarm` 🅰️ method](<⏰ Export 🚀 request.md>).

## Script

```yaml
📃 Export@Alarm:

# Verify the message
- VERIFY|$.Msg

# Get all the alarms
- GET >> $alarms:
    Set: AlarmDomain
    Key: $.Msg.Domain

# Format the list
- EVAL|$alarms >> $ret:
    - When
    - Hook

# Return the list
- RETURN|$ret
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Command ⌘/⌘ Command.md>) |[`EVAL`](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 for datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/Scripts 📃/📃 for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`AlarmDomains` 🪣 table](<../../⏰🪣 Alarm tables/⏰ AlarmDomains 🪣 table.md>)
|