# 🤵 OnTokenOffered 📃 handler
  
> Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the [`Issue@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>).
* Part of the [🤵 Broker.Tokens.Insert ⏩ flow](<../🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnTokenIssued ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenOffered:

# Assert the Token
- ASSERT|$Token:
    AllOf: Issuer, Schema, Language
    Texts: Issuer, Schema, Language

# Get the translation
- TRANSLATE >> $graph:
    Domain: $Token.Issuer
    Schema: $Token.Schema
    Text: "{$Schema.Title}, by {$Domain.Title}"
    To: $Token.Language
        
# Save the token
- SAVE|$Token:
    .State: DETAILED
    Title: $graph.Text
    IssuerTitle: $graph.Domain.Title
    SchemaTitle: $graph.Schema.Title
    Description: $graph.Schema.Description
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
|

