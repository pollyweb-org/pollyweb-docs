# 🤵📃 Update Domain 🪣

> Used by:
* [`Offer` 📃 script](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 📃 handler.md>)

<br/>

## How to call

```yaml
- RUN|Update-Domain:
    Name: <domain-identifier>
    Title: <domain-translation>
```

Inputs | Purpose | Examples
|-|-|-
| `Name` | Domain identifier | `any-domain.dom` 
| `Title` | Domain translation | `Any Domain`
|

## Script

```yaml
📃 Update-Domain:

# Ensure the parameters are given
- ASSERT|$.Inputs:
    AllOf: Name, Title
    Texts: Name, Title

# Try to get the domain, if it exists
- READ >> $domain:
    Set: Broker.Domains
    Key: $Name
    Default: 
        Domain: $Name

# Change the translation
- SET|$domain:
    Title: $Title

# Update the table
- SAVE|$domain
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>): [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>): [`Domains` 🪣](<🤵 BrokerDomains 🪣 table.md>)
|