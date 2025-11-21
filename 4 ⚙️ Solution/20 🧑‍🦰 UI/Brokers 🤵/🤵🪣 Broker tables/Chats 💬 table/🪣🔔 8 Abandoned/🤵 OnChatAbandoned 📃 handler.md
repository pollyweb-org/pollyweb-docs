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

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|