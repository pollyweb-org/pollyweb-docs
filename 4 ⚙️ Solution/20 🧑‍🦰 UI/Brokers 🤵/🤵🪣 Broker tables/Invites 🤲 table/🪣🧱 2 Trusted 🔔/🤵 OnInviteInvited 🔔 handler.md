# 🤵 OnInviteInvited 📃 handler

> About
* Part of the [`Broker.Invites` 🪣 table](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>)
* Reacts to the [`Invite@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)


<br/>

## Diagram

![alt text](<🤵 OnInviteInvited ⚙️ uml.png>)
  
<br/>

## Script

```yaml
📃 OnInvited:

# Find the chatter
- SELECT >> $exists:
    Exists:
    From: Broker.Chatters
    Where: 
        Chat: $Invite.Chat
        Domain: $Invite.Helper
        Role: HELPER

# Progress the state
- IF|$exists:
    Then: RETURN|ADDED
    Else: RETURN|VERIFIED
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Invites`](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>) [`Broker.Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)

