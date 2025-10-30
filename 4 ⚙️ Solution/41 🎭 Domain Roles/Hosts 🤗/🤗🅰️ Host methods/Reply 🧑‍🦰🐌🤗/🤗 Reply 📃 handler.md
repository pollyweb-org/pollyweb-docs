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
- GET >> $prompt:
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

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|