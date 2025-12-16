# 💼 OnQueryTrusted 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnTrusted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryTrusted:

# Get the data
- SEND >> $data:
    Header: 
        To: $Query.Vault
        Subject: Collect@Vault
    Body:
        Collect: $Query.Collect.Require

# Verify the schema
- VERIFY $data.valid:
    Schema: $Query.Schema

# Progress the state
- SAVE $Query:
    STATE: COLLECTED
    Data: $data
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`TRY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/TRY 🧪/🧪 TRY ⌘ cmd.md>) [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Queries`](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)