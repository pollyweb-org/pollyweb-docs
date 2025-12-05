# 🤵 OnInviteVerified 📃 handler

> About
* Part of the [`Broker.Invites` 🪣 table](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>)


<br/>

## Diagram

![alt text](<🤲 OnAskVerified ⚙️ uml.png>)
  
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

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| [Dataset 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Invites`](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>)