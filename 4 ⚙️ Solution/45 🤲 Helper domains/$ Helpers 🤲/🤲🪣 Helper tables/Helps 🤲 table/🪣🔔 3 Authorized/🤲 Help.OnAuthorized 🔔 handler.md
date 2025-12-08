# 🤲 Help.OnAuthorized 🔔 handler

> About
* Part of the [`Helper.Helps` 🪣 table](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 


## Diagram

![alt text](<🤲 Help.OnAuthorized ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Help.OnAuthorized:

# Get the context
- SEND >> $context:
    Header:
        To: $Invite.Consumer
        Subject: Invited@Consumer
    Body: 
        Invite: $Invite.Invite

# Verify the schema of the context
- VERIFY|$context >> $valid:
    Schema: "{$Invite.Schema}/CONTEXT"

# Fail if not valid
- IFNOT|$valid:
    RETURN|BROKEN

# Progress if valid
- SAVE|$Invite:
    .State: VALID
    Context: $context
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`IFNOT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IFNOT ⤵️/⤵️ IFNOT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Helper.Helps`](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Invited@Consumer` 🚀 call](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Invited 🤲🚀💼/💼 Invited 🚀 call.md>)