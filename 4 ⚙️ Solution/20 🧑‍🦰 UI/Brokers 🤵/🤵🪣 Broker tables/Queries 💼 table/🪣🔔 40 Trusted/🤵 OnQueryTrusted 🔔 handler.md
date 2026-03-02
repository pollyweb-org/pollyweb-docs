# 🤵 OnQueryTrusted 🔔 handler


> About
* Part of the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)


<br/>

## Diagram

![alt text](<🤵 OnQueryTrusted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryTrusted:

# See if there is only one trust
- IF $Query.Trusted.IsOne:
    PUT >> $selected:
        $Query.Trusted.First

# Ask to select if there are many trusts
- IF $Query.Trusted.AreMany:

    # Load the Chat
    - CHAT $Query.Chat

    # Ask to select one of the trusts
    - ONE >> $selected:
        Text: What to share?
        Select: 
            From: $Query.Trusted
            AllOf: ID, Title
            Translate: No

# Exit if no trust was selected
- IFNOT $selected:
    RETURN: UNSELECTED

# Save the selected trust and mark as SELECTED
- SAVE $Query:
    STATE: SELECTED
    Selected: $selected
```

Uses ||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>)  [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/1️⃣ ONE ⌘ cmd.md>)  [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)   |
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)   |
|[{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsOne`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsOne ⓕ.md>) [`.AreMany`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/AreMany ⓕ.md>)