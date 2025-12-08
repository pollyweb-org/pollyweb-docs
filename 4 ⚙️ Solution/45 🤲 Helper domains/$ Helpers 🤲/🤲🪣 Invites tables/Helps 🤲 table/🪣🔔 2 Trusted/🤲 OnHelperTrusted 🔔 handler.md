# 🤲 OnHelperTrusted 🔔 handler

> About
* Part of the [`Helper.Helps` 🪣 table](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 


## Diagram

![alt text](<🤲 OnHelperTrusted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnHelperTrusted:

# Check if authorized for billing
- SEND >> $authorized:
    Header:
        To: $.Hosted.Biller
        Subject: Authorize@Biller
    Body: 
        Domain: $Invite.Consumer
        Schema: $Invite.Schema

# Progress the state
- IF|$authorized:
    Then: RETURN|AUTHORIZED
    Else: RETURN|BLOCKED
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) {{SEND}}
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Helper.Helps`](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 
| {{Messages}} | {{Authorize@Biller}}