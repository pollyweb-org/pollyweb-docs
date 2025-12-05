# 🤵 OnInviteVerified 📃 handler

> About
* Part of the [`Broker.Invites` 🪣 table](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>)


<br/>

## Diagram

![alt text](<🤵 OnInviteVerified ⚙️ uml.png>)
  
<br/>

## Script

```yaml
📃 OnInviteVerified:

# Load the chat
- CHAT:
    Chat: $Invite.Chat
    Broker: $.Hosted.Domain

# Get the Helper title
- TRANSLATE >> $translation:
    Domain: $Invite.Helper

# Confirm with the Wallet
- CONFIRM >> $confirmed:
    Text: Allow {$translation.Domain}?

# Progress the chat
- IF|$confirmed:
    Then: 
        SAVE|$Invite:
            .State: CONFIRMED
    Else:
        SAVE|$Invite:
            .State: REJECTED
```

Uses: [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
