# ⏰ Export 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Export@Alarm` 🅰️ method](<⏰ Export 🚀 request.md>).

## Script

```yaml
📃 Export@Alarm:

# Verify the message
- VERIFY|$.Msg

# Get all the alarms
- GET >> $alarms:
    Set: AlarmTriggers
    Where:
        Domain: $.Msg.Domain
```