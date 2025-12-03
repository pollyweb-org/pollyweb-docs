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
VERIFY|$Query.Token >> $valid:

IFNOT|$valid:
        - SAVE|$Query:
            .Status: CORRUPTED
    - RETURN

```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`UNLESS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/UNLESS ⤵️/⤵️ UNLESS ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
|