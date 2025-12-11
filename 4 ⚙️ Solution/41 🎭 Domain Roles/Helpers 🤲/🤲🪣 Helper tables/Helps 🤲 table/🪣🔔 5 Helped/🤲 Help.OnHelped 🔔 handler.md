# 🤲 Help.OnHelped 🔔 handler

> About
* Part of the [`Helper.Helps` 🪣 table](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 


## Diagram

![alt text](<🤲 Help.OnHelped ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Help.OnHelped:

# Return the data to the consumer
- SEND:
    Header:
        To: $Help.Consumer
        Subject: Helped@Consumer
    Body: 
        Helped: $Help.Helped
        Invite: $Help.Invite

# Progress the state
- RETURN BILLABLE
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Helper.Helps`](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 
| 
