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

# Assert rules
- ASSERT|$Invite >> $valid:
    Chat.Host: Inviter   # Only from the host
    Chat.State: ACTIVE   # While the chat is active
- IFNOT|$valid: 
    RETURN|INVALID

# The invited is a trusted Vault?
- TRUSTS >> $trusted:
    Truster: $Invite.Inviter
    Trusted: $Invite.Helper
    Schema: $Invite.Schema
    Role: VAULT
- IFNOT|$trusted:
    RETURN|UNTRUSTED

# The inviter is a trusted Consumer?
- TRUSTS >> $trusted:
    Truster: $Invite.Helper
    Trusted: $Invite.Inviter
    Schema: $Invite.Schema
    Role: CONSUMER
- IFNOT|$trusted:
    RETURN|UNTRUSTED

# Progress the state
- RETURN|CONFIRMED
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Invites`](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>) [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

