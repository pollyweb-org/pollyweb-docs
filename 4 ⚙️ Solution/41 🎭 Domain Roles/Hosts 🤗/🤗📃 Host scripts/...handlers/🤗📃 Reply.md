<!-- TODO -->

# 🤗📃 Reply

> Implements the [`Reply@Host` 🅰️ method](<../../🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>)

## Script

```yaml
# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Prompt, Result 
    UUIDs: Prompt
    # Answer may be empty
    # Answer has any structure

# Get the prompt
- GET >> $prompt:
    Pool: Prompts@Host
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
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/GET ⏬ item.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/SAVE 💾 item.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)
|