# 🗄️ OnCollectReady 📃 handler

## Diagram

![alt text](<🗄️ OnCollectReady ⚙️ uml.png>)

## Script

```yaml
📃 OnCollectReady:

# Send the Collect message
- SEND:
    Header:
        To: $Collect.Consumer
        Subject: Collect@Consumer
    Body:
        Collect: $Collect.ID
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
|