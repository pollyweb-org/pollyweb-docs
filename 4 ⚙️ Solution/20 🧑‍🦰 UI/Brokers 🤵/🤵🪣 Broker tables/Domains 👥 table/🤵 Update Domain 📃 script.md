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
- GET >> $domain:
    Set: BrokerDomains
    Key: $:Name
    Default: 
        Domain: $:Name

# Change the translation
- EVAL|$domain:
    Title: $:Title

# Update the table
- SAVE|$domain
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>): [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>): [`Domains` 🪣](<🤵 BrokerDomains 🪣 table.md>)
|