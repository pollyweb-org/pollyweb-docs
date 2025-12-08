# 🤲 OnHelperTrusted 🔔 handler

> About
* Part of the [`Helper.Helps` 🪣 table](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 


## Diagram

![alt text](<🤲 Help.OnTrusted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Help.OnTrusted:

# Check if authorized for billing
- SEND >> $response:
    Header:
        To: $.Hosted.Biller
        Subject: Authorize@Biller
    Body: 
        Domain: $Invite.Consumer
        Schema: $Invite.Schema

# Progress the state
- IF|$response.Result.Is(AUTHORIZED):
    Then: RETURN|AUTHORIZED
    Else: RETURN|BLOCKED
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Helper.Helps`](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Authorize@Biller`](<../../../../Billers 🤝/🤝📨 Biller msgs/🤲🚀🤝 Authorize/🤝 Authorize 🚀 call.md>)