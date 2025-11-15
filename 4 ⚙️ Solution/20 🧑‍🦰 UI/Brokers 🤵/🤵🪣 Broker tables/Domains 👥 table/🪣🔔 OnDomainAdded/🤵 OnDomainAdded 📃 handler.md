# 🤵 OnDomainAdded 📃 handler

> Purpose
* Calls the [`Domain@Graph` 🅰️ method](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Domain/🕸 Domain 🚀 call.md>) for new domains.

## How to call

```yaml
- RUN|OnDomainAdded:
    Name: <domain-name>
```

Inputs | Purpose | Examples
|-|-|-
| `Name` | Domain identifier | `any-domain.dom` 


## Script

```yaml
📃 OnDomainAdded:

# Ensure the parameters are given
- ASSERT|$Item:
    AllOf: Name
    Texts: Name

# Change the translation
- SET|$domain:
    Title: $Title

# Update the table
- SAVE|$Item
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>): [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CALL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>): [`Domains` 🪣](<../🪣 Domains/🤵 Broker.Domains 🪣 table.md>)
|