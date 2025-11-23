# 🤵 OnTokenLocalized 📃 handler
  
<br/>

## Diagram

![alt text](<🤵 OnTokenLocalized ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenLocalized:

# Get the translation
- TRANSLATE >> $graph:
    Domain: $Token.Vault
    Schema: $Token.Schema
    Language: $Token.Language

# Save the token
- SAVE|$Token:
    IssuerTitle: $graph.Domain.Title
    SchemaTitle: $graph.Schema.Title
    Description: $graph.Schema.Description
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
|

