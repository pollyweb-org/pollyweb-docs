<!-- TODO: -->

# 🤗📃 Prompted

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements 

> Triggered by the [`Prompt@Host` 📃 script](<../...procedures/🤗📃 Prompt 🤔 script.md>)

## Script

```yaml
📃 Prompted@Host: 

# Get the prompt
- GET|Prompts@Host|$.Msg.Prompt >> $prompt

# Verify the message
- VERIFY|$.Msg|$prompt.PublicKey

# Returned the cached response
- RETURN|prompt.Prompted
```