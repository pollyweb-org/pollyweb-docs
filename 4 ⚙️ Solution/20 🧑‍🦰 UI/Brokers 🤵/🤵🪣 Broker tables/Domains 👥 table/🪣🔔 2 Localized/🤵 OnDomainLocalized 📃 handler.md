# 🤵 OnDomainLocalized 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a change in the language of a [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)'s Domain.

<br/>

## Diagram

![alt text](<🤵 OnDomainLocalized ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnDomainLocalized:

# Assert the Domain
- ASSERT|$Domain:
    AllOf: Name, Language
    Texts: Name, Language

# Translate the domain info
- TRANSLATE >> $graph:
    To: $Domain.Language
    Domain: $Domain.Name
    
# Save the translation
- SAVE|$Domain:
    Title: $graph.Domain.Title
    Description: $graph.Domain.Description
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domains`](<../🪣 Domains/🤵 Broker.Domain 🪣 table.md>)
|