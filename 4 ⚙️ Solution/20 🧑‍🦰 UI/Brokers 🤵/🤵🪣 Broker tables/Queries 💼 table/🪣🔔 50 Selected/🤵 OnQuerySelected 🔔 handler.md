# 🤵 OnQueryTrusted 🔔 handler

> About
* Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnQuerySelected ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQuerySelected:

# Load the Chat
- CHAT $Query.Chat

# Load the Schema details
- READ >> $schema:
    Set: Broker.Schemas
    Key: 
        Schema: $Query.Selected.Schema
        Wallet: $Query.Wallet

# Confirm the share
- CONFIRM:
    Text: > 
        Send this data?
        Send: ´{$Query.Selected.Title.Require}´
        To: ´{$Query.Chat.HostTitle.Require}´
    Details:
        ´$schema.Details´

# Exit if no trust was selected
- ELSE:
    RETURN: REJECTED

# Assign the trust data to the Query
- CASE $Query.Selected.Type:
    BIND: 
        SAVE $Query:
            .State: DISCLOSED
            Bind: $Query.Selected.ID.Require
            Vault: $Query.Selected.Domain.Require
    TOKEN:
        SAVE $Query:
            .State: SHARED
            Token: $Query.Selected.ID.Require
            Issuer: $Query.Selected.Domain.Require
```

Uses ||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>)  [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`IFNOT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IFNOT ⤵️/⤵️ IFNOT ⌘ cmd.md>)  |
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>) [`Broker.Schemas`](<../../Schemas 🧩 table/🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>)  |
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)