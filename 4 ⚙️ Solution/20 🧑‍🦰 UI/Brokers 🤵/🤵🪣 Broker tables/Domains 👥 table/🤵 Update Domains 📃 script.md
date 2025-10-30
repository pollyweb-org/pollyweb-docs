# 🤵📃 Update Domain 🪣

> Used by:
* [`Offer` 📃 script](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 📃 handler.md>)

<br/>

## How to call

```yaml
- RUN|UpdateDomain:
    Domain: <domain-identifier>
    Domain$: <domain-translation>
```

Inputs | Purpose | Examples
|-|-|-
| `Domain` | Domain identifier | `any-domain.dom` 
| `Domain$` | Domain translation | `Any Domain`
|

## Script

```yaml
📃 UpdateDomain:

# Ensure the parameters are given
- ASSERT|$.Inputs:
    AllOf: Domain, Domain$
    Texts: Domain, Domain$

# Try to get the domain, if it exists
- GET >> $domain:
    Set: BrokerDomains
    Key: $:Domain
    Default: 
        Domain: $:Domain

# Change the translation
- EVAL|$domain:
    Domain$: $:Domain$

# Update the table
- SAVE|$domain
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃⌘ commands/Command ⌘/⌘ Command.md>): [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>): [`Domains` 🪣](<🤵 BrokerDomains 🪣 table.md>)
|