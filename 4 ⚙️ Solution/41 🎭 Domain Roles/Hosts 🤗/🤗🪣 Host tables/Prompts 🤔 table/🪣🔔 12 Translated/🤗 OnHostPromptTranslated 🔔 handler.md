# 🤗 OnHostPromptTranslated 🔔 handler

## Diagram

![alt text](<🤗 OnHostPromptTranslated ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPromptTranslated:


# Call the Prompt@Broker
- SEND|$hook:
    Header:
        To: Broker
        Subject: Prompt@Broker
    Body:
        Chat: Chat
        Hook: Hook
        Emoji: $Emoji
        Format: $Format
        Expires: Expires
```