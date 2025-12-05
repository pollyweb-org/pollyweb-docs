# 🤵 OnInviteConfirmed 📃 handler

> About
* Part of the [`Broker.Invites` 🪣 table](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>)



<br/>

## Diagram

![alt text](<🤵 OnInviteConfirmed ⚙️ uml.png>)
  
<br/>

## Script

```yaml
📃 OnInviteConfirmed:

# Add the participant to the chat
- SAVE|Broker.Chatters:
    Chat: $Invite.Chat
    Domain: $Invite.Helper
    Role: HELPER
```

Uses:  [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
