# 🤵 OnBindOffered 🔔 handler


> About
* Part of the [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
* Translates a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) offered by a [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>)
* Reacts to the [`Bind@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
* The item may already exist in the `REJECTED` or `REMOVED` state.

<br/>

## Flow

![alt text](<🤵 OnBindOffered ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindOffered:

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
[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) 
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds`](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
|

