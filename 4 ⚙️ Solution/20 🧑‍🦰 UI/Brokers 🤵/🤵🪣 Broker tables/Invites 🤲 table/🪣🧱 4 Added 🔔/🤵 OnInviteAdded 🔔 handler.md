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
        Inviter: $Invite.Inviter
        Invite: $Invite.ID

# Mark as done
- RETURN|DONE
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Broker.Invites`](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>)