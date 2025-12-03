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

# Validate the Token
- ASSERT|$Query.Token >> $valid:
    AllOf: Starts, Issuer
    Starts.IsFuture:
    Expires.IsPast:
    Schema.IsIn: $Query.Schemas

# Exit if invalid
- IFNOT|$valid:
    - SAVE|$Query:
        .State: INVALID
    - RETURN

# Verify the Token signature and schema
- VERIFY|$Query.Token >> $valid

# Exit if corrupted
- IFNOT|$valid:
    - SAVE|$Query:
        .State: CORRUPTED
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
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IFNOT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IFNOT ⤵️/⤵️ IFNOT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)  [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRUSTS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) 
|[{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsPast`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsPast ⓕ.md>) [`.IsFuture`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>) [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>)
|