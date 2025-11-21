# 🤵 OnChatAbandoned 📃 handler


## Diagram

![alt text](<🤵 OnChatAbandoned ⚙️ uml.png>)


## Script

```yaml
📃 OnChatAbandoned:

# Inform the Host.
- SEND:
    Header:
        To: $Chat.Host
        Subject: Abandoned@Host
    Body:
        Chat: $Chat.ID
```