<!-- TODO: -->

# 🤗📃 Prompted

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/📃 Script.md>) that implements 

> Triggered by the [`Prompt@Host` 📃 script](<../...procedures/🤗📃 Prompt 🤔 script.md>)

## Script

```yaml
📃 Prompted@Host: 

# Get the prompt
- GET >> $prompt:
    Pool: Prompts@Host
    Key: $.Msg.Prompt

# Verify the message
- VERIFY|$.Msg:
    Key: $prompt.PublicKey

# Verify the cache TTL
- ASSERT:
    - $prompt.TTL > .Now

# Returned the cached response
- RETURN:
    prompt.Prompted
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/GET ⏬ item.md>) [`RETURN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/RETURN ⤴️.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...functions/{Function} 🐍.md>) | {.Now}
|