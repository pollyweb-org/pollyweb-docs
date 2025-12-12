# 💼 OnInviteValid 🔔 handler

> About
* Part of the [`Consumer.Invites` 🪣 table](<../🪣 Invites/💼 Consumer.Invites 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnValid ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnInviteValid:

# Continue the WAIT
- RACE $Invite.ID:
    $Invite.Help
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`RACE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/RACE 🏁/🏁 RACE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Invites`](<../🪣 Invites/💼 Consumer.Invites 🪣 table.md>)