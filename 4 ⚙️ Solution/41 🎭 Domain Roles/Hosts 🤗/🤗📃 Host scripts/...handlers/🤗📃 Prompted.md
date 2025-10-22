<!-- TODO: -->

# 🤗📃 Prompted

## Script

```yaml
# Get the prompt
- GET|Prompts@Host|$.Msg.Prompt >> $prompt

# Verify the message
- VERIFY|$.Msg|$prompt.PublicKey


```