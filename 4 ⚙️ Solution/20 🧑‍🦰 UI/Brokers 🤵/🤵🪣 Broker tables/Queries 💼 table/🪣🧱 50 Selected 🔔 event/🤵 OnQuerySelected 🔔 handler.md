# 🤵 OnQueryTrusted 🔔 handler



<br/>

## Diagram

![alt text](<🤵 OnQuerySelected ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryTrusted:

# Load the Chat
- CHAT|$Query.Chat

# See if there is only one trust
- IF|$Query.Trusted.IsOne:
    PUT >> $trust:
        $Query.Trusted.First

# Ask to select if there are many trusts
- IF|$Query.Trusted.AreMany:
    ONE >> $trust:
        Text: What to share?
        Select: 
            From: $Query.Trusted
            AllOf: ID, Title
            Translate: No

# Exit if no trust was selected
- UNLESS|$trust:
    - SAVE|$Query:
        .State: REJECTED
    - RETURN

# Load the Schema details
- READ >> $schema:
    Set: Broker.Schemas
    Key: 
        Schema: $trust.Schema
        Wallet: $Query.Wallet

# Confirm the share
- CONFIRM >> $confirm:
    Text: > 
        Send this data?
        Send: ´{$trust.Title}´
        To: ´{$Query.Chat.HostTitle}´
    Details:
        ´$schema.Details´

# Exit if no trust was selected
- UNLESS|$confirm:
    - SAVE|$Query:
        .State: REJECTED
    - RETURN

# Assign the trust data to the Query
- CASE|$trust.Type:
    BIND: 
        SAVE|$Query:
            .State: DISCLOSED
            Bind: $trust.ID
            Vault: $trust.Domain
    TOKEN:
        SAVE|$Query:
            .State: SHARED
            Token: $trust.ID
            Vault: $trust.Domain 
```

Uses ||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`UNLESS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/UNLESS ⤵️/⤵️ UNLESS ⌘ cmd.md>)  |
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>) [`Broker.Schemas`](<../../Schemas 🧩 table/🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>)  |
|[{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsOne`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsOne ⓕ.md>) [`.AreMany`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/AreMany ⓕ.md>)