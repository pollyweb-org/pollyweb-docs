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

# Trust all invites from the Broker itself
#   this is to allow intros to Chats by Finders
- IF $Invite.Consumer.Is($.Hosted.Domain):   
    RETURN: TRUSTED

# Assert rules
- ASSERT >> $valid:
    Chat.Host: $Invite.Consumer   # Only from the host
    Chat.State: ACTIVE   # While the chat is active

# Exit if invalid
- IFNOT $valid: 
    RETURN: INVALID

# The invited is a trusted Vault?
- TRUSTS >> $trusted:
    Truster: $Invite.Consumer
    Trusted: $Invite.Helper
    Schema: $Invite.Schema
    Role: VAULT

# Exit if not a trusted VAULT
- IFNOT $trusted:
    RETURN: UNTRUSTED

# The inviter is a trusted Consumer?
- TRUSTS >> $trusted:
    Truster: $Invite.Helper
    Trusted: $Invite.Consumer
    Schema: $Invite.Schema
    Role: CONSUMER

# Exit if not a trusted CONSUMER
- IFNOT $trusted:
    RETURN: UNTRUSTED

# Progress the state
- RETURN: TRUSTED
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`IFNOT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IFNOT ⤵️/⤵️ IFNOT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`TRUSTS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Invites`](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>) [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

