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
- TRY >> $error:
    - VERIFY $Invite.Help:
        Schema: $Invite.Schema

# Progress the state
- IF: $error
- THEN: RETURN INVALID
- ELSE: RETURN VALID
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`ELSE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/ELSE ⤵️/⤵️ ELSE ⌘ cmd.md>) [`THEN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/THEN ⤵️/⤵️ THEN ⌘ cmd.md>) [`TRY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/TRY 🧪/🧪 TRY ⌘ cmd.md>) [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Invites`](<../🪣 Invites/💼 Consumer.Invites 🪣 table.md>)