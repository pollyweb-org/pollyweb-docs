# 🤵 OnInviteAdded 📃 handler

> About
* Part of the [`Broker.Invites` 🪣 table](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>)



<br/>

## Diagram

![alt text](<🤵 OnInviteAdded ⚙️ uml.png>)
  
<br/>

## Script

```yaml
📃 OnAdded:

# Invite the helper to the chat
- SEND:
    Header:
        To: $Invite.Helper
        Subject: Help@Helper
    Body:
        Chat: $Invite.Chat
        Schema: $Invite.Schema
        Consumer: $Invite.Consumer
        Invite: $Invite.Invite

# Mark as done
- RETURN DONE
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) |  [`Broker.Invites`](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>)