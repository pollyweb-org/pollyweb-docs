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
Uses: [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)

<br/>

## Script

```yaml
📃 .BIND:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Schema
    Texts: Schema, Reference

# See if already bound
- PUT >> $bind:
    $.Chat.Binds.Where:
        Schema: $.Inputs.Schema

# Return if found
- IF|$bind:
    RETURN|$bind

# Save the bind
- SAVE|Vault.Binds >> $bind:
    .State: OFFERED

    # From $.Inputs
    Schema: $Schema
    Reference: $Reference
    Internals: $Internals
    
    # From $.Chat
    Broker: $.Chat.Broker
    Chat: $.Chat.Chat
    
# Wait for the bound schema
- WAIT >> $bound:
    Hook: $bind.ID

# Return the schema
- RETURN:
    $bound
```


|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`WAIT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Inputs`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|