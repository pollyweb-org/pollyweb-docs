# 🤵 OnSchemaLocalized 📃 handler

> About
* Part of the [`Broker.Schemas` 🪣 table](<../🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>)
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a change in the language of a [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)'s Domain.
* Part of the [🤵 `Broker.Wallets.Localize` ⏩ flow](<../../Wallets 🧑‍🦰 table/🪣🧱 20 Localize ⏩ flow/🤵 Broker.Wallets.Localize ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnSchemaLocalized ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnSchemaLocalized:

# Assert the Domain
- ASSERT|$Schema:
    AllOf: Code, Language
    Texts: Code, Language

# Translate the schema info
- TRANSLATE >> $graph:
    Schema: $Schema.Code
    To: $Schema.Language
    
# Save the translation
- SAVE|$Schema:
    Title: $graph.Schema.Title
    Description: $graph.Schema.Description
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Schemas`](<../🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>)
|