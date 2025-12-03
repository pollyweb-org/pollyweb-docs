# 😃📃 .ALARM ⏰ script

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`ALARM`](<⏰ ALARM ⌘ cmd.md>) command 

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
- ASSERT|$.Inputs:
    AllOf: When, Call, With
    Times: When
    Texts: Call

# Set the alarm
- SEND:
    Header:
        To: $.Hosted.Alarm
        Subject: Trigger@Alarm
    Body:
        When: $When
        Hook: 
            Call: $Call
            With: $With
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Trigger@Alarm` 📨 msg](<../../../../45 🤲 Helper domains/Alarms ⏰/⏰📨 Alarm msgs/Trigger 👥🐌⏰/⏰ Trigger 🐌 msg.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)  [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|

## Event handler

```yaml
📃 Triggered@Alarm:

# Verify the hook
- VERIFY|$.Msg

# Assert if it's the right helper
- ASSERT|$.Msg:
    From: $.Hosted.Alarm

# Call the method
- RUN|$.Msg.Hook.Call:
    $Hook.With
```