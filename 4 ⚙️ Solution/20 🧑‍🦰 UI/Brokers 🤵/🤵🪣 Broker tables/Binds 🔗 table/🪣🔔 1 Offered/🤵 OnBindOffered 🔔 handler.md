# 🤵 OnBindOffered 📃 handler

> Part of the [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)

> Purpose
* Translates a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) offered by a [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)
* Reacts to the [`Bind@Broker` 🅰️ method](<../../../🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
* The item may already exist in the `REJECTED` or `REMOVED` state.

## Flow

![alt text](<🤵 OnBindOffered ⚙️ uml.png>)

## Script

```yaml
📃 OnBindOffered:

# Assert the Bind
- ASSERT|$Bind:
    AllOf: Schema, Vault, Language
    Texts: Schema, Vault, Language

# Translate 
- TRANSLATE >> $graph:
    Domain: $Bind.Vault
    Schema: $Bind.Schema
    To: $Bind.Language

# Save the bind
- SAVE|$Bind:
    .State: DETAILED
    VaultTitle: $graph.Domain.Title
    SchemaTitle: $graph.Schema.Title
    Description: $graph.Schema.Description
```

Uses||
|-|-
[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) 
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Binds`](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
|

