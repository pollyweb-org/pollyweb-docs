# 🤵 OnTokenLocalized 📃 handler
  
> About
* Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
* Part of the [🤵 `Broker.Tokens.Localize` ⏩ flow](<../🪣🧱 20 Localize ⏩ flow/🤵 Broker.Tokens.Localize ⏩ flow.md>)
* Part of the [🤵 `Broker.Wallets.Localize` ⏩ flow](<../../Wallets 🧑‍🦰 table/🪣🧱 20 Localize ⏩ flow/🤵 Broker.Wallets.Localize ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnTokenLocalized ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenLocalized:

# Assert the Token
- ASSERT|$Token:
    AllOf: Issuer, Schema, Language
    Texts: Issuer, Schema, Language, Tag

# Get the translation
- TRANSLATE >> $graph:
    Domain: $Token.Issuer
    Schema: $Token.Schema
    Text: "{$Schema.Title}, by {$Domain.Title}"
    To: $Token.Language
        
# Save the token
- SAVE|$Token:
    Title: Tag.Default($graph.Text)     # Use the tag if set
    IssuerTitle: $graph.Domain.Title
    SchemaTitle: $graph.Schema.Title
    Description: $graph.Schema.Description
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Default`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Default ⓕ.md>)
|

