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

Params | Purpose | Examples
|-|-|-
| `Domain` | Domain identifier | `any-domain.dom` 
| `Domain$` | Domain translation | `Any Domain`
|

## Script

```yaml
📃 UpdateDomain:

# Ensure the parameters are given
- ASSERT:
    AllOf: $:Domain, $:Domain$
    Texts: $:Domain, $:Domain$

# Try to get the domain, if it exists
- GET >> $domain:
    Set: Domains@Broker
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
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>): [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/EVAL ⬇️ flow.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) 
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>): [`Domains` 🪣](<🤵 BrokerDomains 🪣 table.md>)
|