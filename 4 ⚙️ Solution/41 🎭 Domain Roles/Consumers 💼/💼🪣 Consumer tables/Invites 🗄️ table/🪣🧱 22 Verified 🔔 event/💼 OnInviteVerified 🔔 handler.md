# 💼 OnInviteVerified 🔔 handler

> About
* Part of the [`Consumer.Invites` 🪣 table](<../../Invites 🗄️ table/🪣 Invites/💼 Consumer.Invites 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnInviteVerified ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnInviteVerified:

# Continue the WAIT
- RACE|$Invite.ID:
    $Invite.Help
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`RACE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/RACE 🏁/🏁 RACE ⌘ cmd.md>)
