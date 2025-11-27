# 🤵 OnBindLocalized 🔔 handler
  
> About
* Part of the [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
* Part of the [🤵 `Broker.Binds.Localize` ⏩ flow](<../🪣🧱 50 Localize ⏩ flow/🤵 Broker.Binds.Localize ⏩ flow.md>)
* Part of the [🤵 `Broker.Wallets.Localize` ⏩ flow](<../../Wallets 🧑‍🦰 table/🪣🧱 20 Localize ⏩ flow/🤵 Broker.Wallets.Localize ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnBindLocalized ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindLocalized:

# Get the translation
- TRANSLATE >> $graph:
    Domain: $Bind.Vault
    Schema: $Bind.Schema
    To: $Bind.Language

# Save the bind
- SAVE|$Bind:
    VaultTitle: $graph.Domain.Title
    SchemaTitle: $graph.Schema.Title
    Description: $graph.Schema.Description
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
|

