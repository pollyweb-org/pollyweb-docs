# ⏰ Export 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Export@Alarm` 🚀 call](<⏰ Export 🚀 call.md>).

## Script

```yaml
📃 Export@Alarm:

# Verify the message
- VERIFY $.Msg

# Get all the alarms
- READ >> $alarms:
    Set: Alarm.Domains
    Key: $.Msg.Domain

# Format the list
- PUT $alarms >> $ret:
    - When
    - Hook

# Return the list
- RETURN: $ret
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |[`CALL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`AlarmDomains` 🪣 table](<../../⏰🪣 Alarm tables/⏰ AlarmDomains 🪣 table.md>)
|