# 🤵 OnDomainLocalized 📃 handler

> About
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a change in the language of a [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)'s Domain.
* Part of the [🤵 `Broker.Wallets.Localize` ⏩ flow](<../../Wallets 🧑‍🦰 table/🪣🧱 20 Localize ⏩ flow/🤵 Broker.Wallets.Localize ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnDomainLocalized ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnDomainLocalized:

# Assert the Domain
- ASSERT $Domain:
    AllOf: Name, Language
    Texts: Name, Language

# Translate the domain info
- TRANSLATE >> $graph:
    Domain: $Domain.Name
    To: $Domain.Language
    
# Save the translation
- SAVE $Domain:
    Title: $graph.Domain.Title
    Description: $graph.Domain.Description
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domains`](<../🪣 Domains/🤵 Broker.Domains 🪣 table.md>)
|