<!-- TODO 

[`Reply handler`](<🤗 Reply 📃 handler.md>)
[`Reply@Host` 🅰️ method](<🤗 Reply 🐌 msg.md>)
[`Prompt@Host`](<../../🤗🧩 Host schemas/🧩 HOST.md>)
-->

# 🤗📃 Reply

> Implements the [`Reply@Host` 🅰️ method](<🤗 Reply 🐌 msg.md>)

## Script

```yaml
📃 Reply@Host:

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Prompt, Result 
    UUIDs: Prompt
    # Answer may be empty
    # Answer has any structure

# Get the prompt
- READ >> $prompt:
    Set: HostPrompts
    Key: $.Msg.Prompt

# Verify the message
- VERIFY|$.Msg:
    Key: $prompt.PublicKey

# Set the result
- SAVE|$prompt:
    Result: $.Msg.Result
    Answer: $.Msg.Answer 
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|