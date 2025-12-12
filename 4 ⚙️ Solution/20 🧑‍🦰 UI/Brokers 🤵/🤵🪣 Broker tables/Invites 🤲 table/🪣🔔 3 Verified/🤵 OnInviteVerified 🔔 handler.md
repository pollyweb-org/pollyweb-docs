# 🤵 OnInviteVerified 📃 handler

> About
* Part of the [`Broker.Invites` 🪣 table](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>)


<br/>

## Diagram

![alt text](<🤵 OnInviteVerified ⚙️ uml.png>)
  
<br/>

## Script

```yaml
📃 OnVerified:

# Load the chat
- CHAT:
    Chat: $Invite.Chat
    Broker: $.Hosted.Domain

# Get the Helper title
- TRANSLATE >> $translation:
    Domain: $Invite.Helper

# Confirm with the Wallet
- CONFIRM: Allow {$translation.Domain}?
- ELSE: 
    RETURN: REJECTED

# Add the chat participant, if not already added
- SAVE Broker.Chatters:
    Chat: $Invite.Chat
    Domain: $Invite.Helper
    Role: HELPER

# Progress the chat
- RETURN: ADDED
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) [`ELSE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/ELSE ⤵️/⤵️ ELSE ⌘ cmd.md>) [`IFNOT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IFNOT ⤵️/⤵️ IFNOT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) 
| [Dataset 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Invites`](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>)