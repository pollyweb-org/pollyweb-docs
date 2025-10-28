# 😃📃 .ALARM ⏰ script

> [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) that implements the [`ALARM`](<⏰ ALARM ⌘ cmd.md>) command 

## How to run

```yaml
- RUN|.ALARM:
    When: 1 day
    Call: MyMethod
    With: {A:, B:2}
```

## Script

```yaml
📃 .ALARM:

# Assert parameters
- ASSERT|.Inputs:
    .AllOf: When, Call, With
    .Times: When
    .Texts: Call

# Set the alarm
- SEND:
    Header:
        To: $.Settings.Alarm
        Subject: Trigger@Alarm
    Body:
        When: $:When
        Hook: 
            Call: $:Call
            With: $:With
```

Needs||
|-|-
| [Commands ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Trigger@Alarm` 🅰️ method](<../../../../../45 🤲 Helper domains/Alarms ⏰/⏰🅰️ Alarm methods/Trigger 👥🐌⏰/⏰ Trigger 🐌 msg.md>)
| [Placeholders 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Settings`](<../../...messages 📨/$.Settings 🎛️.md>)
|

## Event handler

```yaml
📃 Triggered@Alarm:

# Verify the hook
- VERIFY|$.Msg

# Assert if it's the right helper
- ASSERT|$.Msg:
    From: $.Settings.Alarm

# Call the method
- RUN|$.Msg.Hook.Call:
    $:Hook.With
```