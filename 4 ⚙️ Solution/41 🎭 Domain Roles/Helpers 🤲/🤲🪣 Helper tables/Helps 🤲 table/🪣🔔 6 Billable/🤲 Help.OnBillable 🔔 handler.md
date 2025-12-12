# 🤲 Help.OnBillable 🔔 handler

> About
* Part of the [`Helper.Helps` 🪣 table](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 


## Diagram

![alt text](<🤲 Help.OnBillable ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Help.OnBillable:

# Return the data to the consumer
- SEND:
    Header:
        To: $.Hosted.Biller
        Subject: Bill@Biller
    Body: 
        Bill: $Help.Bill

# Progress the state
- RETURN: BILLED
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Helper.Helps`](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 
| 
