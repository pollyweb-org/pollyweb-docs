# 😃📃 `.BIND` script

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`BIND`](<🔗 BIND ⌘ cmd.md>) command.
* Part of the [🧑‍🦰 `Bind Vault` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind Vault ⏩ flow.md>)



<br/>

## Diagram

![alt text](<🔗 BIND ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN|.BIND:
    Schema: schema-1
    Reference: my-user
    Internals:
        extra: data
```
Uses: [`RUN`](<../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)

<br/>

## Script

```yaml
📃 .BIND:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Schema
    Texts: Schema, Reference

# Save the bind
- SAVE|Vault.Binds >> $bind:
    
    # From $.Inputs
    Schema: $Schema
    Reference: $Reference
    Internals: $Internals
    
    # From $.Chat
    Broker: $.Chat.Broker
    Chat: $.Chat.ID
    
# Wait for the bound schema
- WAIT >> $bound:
    Hook: $bind.ID

# Return the schema
- RETURN:
    $bound
```



|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`WAIT`](<../../⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds` 🪣 table](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|