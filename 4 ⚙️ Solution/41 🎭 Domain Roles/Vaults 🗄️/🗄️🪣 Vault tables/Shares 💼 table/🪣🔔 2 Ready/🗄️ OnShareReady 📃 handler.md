# 🗄️ OnShareReady 📃 handler

## Diagram

![alt text](<🗄️ OnShareReady ⚙️ uml.png>)

## Script

```yaml
📃 OnShareReady:

# Send the Collect message
- SEND:
    Header:
        To: $Share.Consumer
        Subject: Collect@Consumer
    Body:
        Hook: $Share.ID
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | {{Collect@Consumer}}
|