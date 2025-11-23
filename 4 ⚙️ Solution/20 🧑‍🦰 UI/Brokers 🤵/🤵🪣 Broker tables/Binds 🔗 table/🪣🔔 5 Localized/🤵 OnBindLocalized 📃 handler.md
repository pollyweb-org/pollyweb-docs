# 🤵 OnBindLocalized 📃 handler
  
## Diagram

![alt text](<🤵 OnBindLocalized ⚙️ uml.png>)

## Script

```yaml
📃 OnBindLocalized:

# Get the translation
- TRANSLATE >> $graph:
    Domain: $Bind.Vault
    Schema: $Bind.Schema
    Language: $Bind.Language

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

