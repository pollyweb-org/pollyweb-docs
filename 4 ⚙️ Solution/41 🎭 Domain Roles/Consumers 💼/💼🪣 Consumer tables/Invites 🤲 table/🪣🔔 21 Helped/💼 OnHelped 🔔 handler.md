# 💼 OnInviteHelped 🔔 handler

> About
* Part of the [`Consumer.Invites` 🪣 table](<../🪣 Invites/💼 Consumer.Invites 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnHelped ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnInviteHelped:

# Verify the help schema
- VERIFY $Invite.Help >> $valid:
    Schema: $Invite.Schema

# Progress the state
- IF $valid:
    RETURN: VALID
- ELSE:
    RETURN: INVALID
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Invites`](<../🪣 Invites/💼 Consumer.Invites 🪣 table.md>)