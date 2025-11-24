# 🤵 OnTokenOffered 📃 handler

> Purpose
* Translates a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) offered by an [Issuer 🎴 domain](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)
* Reacts to the [`Offer@Broker` 🅰️ method](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)

## Flow

![alt text](<🤵 OnTokenOffered ⚙️ uml.png>)
## Script

```yaml
📃 OnTokenOffered:

# Assert the Token
- ASSERT|$Token:
    AllOf: Schema, Issuer, Language
    Texts: Schema, Issuer, Language

# Translate 
- TRANSLATE >> $graph:
    Domain: $Token.Issuer
    Schema: $Token.Schema
    Language: $Token.Language

# Save the token
- SAVE|$Token:
    .State: DETAILED
    IssuerTitle: $graph.Domain.Title
    SchemaTitle: $graph.Schema.Title
    Description: $graph.Schema.Description
```

Uses||
|-|-
[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) 
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
|

