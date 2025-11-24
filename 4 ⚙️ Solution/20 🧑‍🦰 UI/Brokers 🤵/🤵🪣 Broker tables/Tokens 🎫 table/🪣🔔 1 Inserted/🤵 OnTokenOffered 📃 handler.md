# 🤵 OnTokenOffered 📃 handler
  
<br/>

## Diagram

![alt text](<🤵 OnTokenOffered ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenOffered:

# Assert the Token
- ASSERT|$Token:
    AllOf: Issuer, Schema
    Texts: Issuer, Schema

# Get the translation
- TRANSLATE >> $graph:
    Domain: $Token.Issuer
    Schema: $Token.Schema
    Text: {$Schema.Title}, by {$Domain.Title}
    To: $Token.Wallet.Language
        
# Save the token
- SAVE|$Token:
    .State: DETAILED
    Language: $Token.Wallet.Language
    Title: $graph.Text
    IssuerTitle: $graph.Domain.Title
    SchemaTitle: $graph.Schema.Title
    Description: $graph.Schema.Description
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
|

