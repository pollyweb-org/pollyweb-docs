# 🤵 OnBindOffered 📃 handler

> Purpose
* Translates a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) offered by a [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)
* Reacting to the [`Bind@Broker` 🅰️ method](<../../../🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)

## Flow

![alt text](<🤵 OnBindOffered ⚙️ uml.png>)

## Script

```yaml
📃 OnBindOffered:
    
# Rename for readability
- PUT|$Item >> $bind

# Translate 
- TRANSLATE >> $graph:
    Domain: $bind.Vault
    Schema: $bind.Schema
    Language: $bind.Language

# Save the bind
- SAVE|$bind:
    .State: DETAILED
    VaultTitle: $graph.Domain.Title
    SchemaTitle: $graph.Schema.Title
    Description: $graph.Schema.Description
```

Uses||
|-|-
[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) 
|

