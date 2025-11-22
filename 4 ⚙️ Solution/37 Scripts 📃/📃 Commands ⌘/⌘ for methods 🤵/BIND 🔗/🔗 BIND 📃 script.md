# 😃📃 `.BIND` script

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`BIND`](<🔗 BIND ⌘ cmd.md>) command.

<br/>

## Diagram

![alt text](<🔗 BIND ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN|.BIND:
    User: my-user
    Schemas:
      - schema-1
      - schema-n
```
Uses: [`RUN`](<../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)

<br/>

## Script

```yaml
📃 .BIND:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Schemas, User
    Lists: Schemas

# Save the bind
- SAVE|Vault.Binds >> $bind:
    Broker: $.Chat.Broker
    Chat: $.Chat.ID
    Schemas: $Schemas
    User: $User

# Wait for the bound schema
- WAIT >> $schema:
    Hook: $bind.ID

# Return the schema
- RETURN:
    $schema
```



|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`WAIT`](<../../⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds` 🪣 table](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>)
|