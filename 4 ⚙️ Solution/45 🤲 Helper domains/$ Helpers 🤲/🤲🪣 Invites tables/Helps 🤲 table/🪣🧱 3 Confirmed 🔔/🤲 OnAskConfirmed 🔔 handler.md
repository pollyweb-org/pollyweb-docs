# 🤵 OnInviteConfirmed 📃 handler

> About
* Part of the [`Broker.Invites` 🪣 table](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>)



<br/>

## Diagram

![alt text](<🤲 OnAskConfirmed ⚙️ uml.png>)
  
<br/>

## Script

```yaml
📃 OnInviteConfirmed:

# Add the chat participant, if not already added
- SAVE|Broker.Chatters:
    Chat: $Invite.Chat
    Domain: $Invite.Helper
    Role: HELPER

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
- SAVE|$Invite:
    .State: DONE
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chatters`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Broker.Invites`](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>)