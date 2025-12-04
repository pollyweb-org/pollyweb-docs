# 💼 OnInviteInvited 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../../Queries 🗄️ table/🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnInviteInvited ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnInviteInvited:

# Verify if the Helper is trusted
- TRUSTS >> $trusted:
    Trusted: $Invite.Helper
    Schema: $Invite.Schema
    Role: VAULT

# Progress the state
- IF|$trusted:
    Then: 
        SAVE|$Query:
            .State: TRUSTED
    Else:
        SAVE|$Query:
            .State: UNTRUSTED
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRUSTS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Invites`](<../🪣 Invites/💼 Consumer.Invites 🪣 table.md>)