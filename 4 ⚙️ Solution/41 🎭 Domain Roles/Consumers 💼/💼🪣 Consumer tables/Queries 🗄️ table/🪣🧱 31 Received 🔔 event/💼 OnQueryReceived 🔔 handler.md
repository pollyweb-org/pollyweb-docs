# 💼 OnQueryReceived 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnQueryReceived ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryReceived:

# Verify the Token signature
- VERIFY|$Query.Token >> $valid

# Exit if corrupted
- IFNOT|$valid:
    - SAVE|$Query:
        .State: INVALID
    - RETURN

# Check the trust
- TRUSTS >> $trusted:
    Trusted: $Query.Token.Issuer
    Schema: $Query.Token.Schema
    Role: VAULT

# Exit if untrusted
- IFNOT|$trusted:
    - SAVE|$Query:
        .State: UNTRUSTED
    - RETURN

# Otherwise, progress
- SAVE|$Query:
    .State: TOKENED
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`IFNOT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IFNOT ⤵️/⤵️ IFNOT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)  [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRUSTS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) 
|