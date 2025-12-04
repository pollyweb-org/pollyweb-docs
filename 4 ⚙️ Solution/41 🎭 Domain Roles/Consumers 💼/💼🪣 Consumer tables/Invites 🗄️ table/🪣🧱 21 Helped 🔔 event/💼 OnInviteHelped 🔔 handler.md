# 💼 OnInviteHelped 🔔 handler

> About
* Part of the [`Consumer.Invites` 🪣 table](<../../Invites 🗄️ table/🪣 Invites/💼 Consumer.Invites 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnInviteHelped ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnInviteHelped:

# Verify if the Vault is trusted
- TRUSTS >> $trusted:
    Trusted: $Query.Vault
    Schema: $Query.Schema
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

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRUSTS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) |
