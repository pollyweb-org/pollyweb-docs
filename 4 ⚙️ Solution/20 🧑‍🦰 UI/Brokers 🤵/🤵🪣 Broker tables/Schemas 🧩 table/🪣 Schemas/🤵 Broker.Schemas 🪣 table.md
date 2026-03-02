# 🤵🪣 Broker.Schemas table

> About
* Implements the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>)
* [Propagated 🛢](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) by [`Binds` ](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Tokens`](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) tables
* Localized by the [🤵 `Broker.Wallets.Localize` ⏩ flow](<../../Wallets 🧑‍🦰 table/🪣🧱 20 Localize ⏩ flow/🤵 Broker.Wallets.Localize ⏩ flow.md>)

<br/>

## Lifecycle

![alt text](<🤵 Broker.Schemas ⚙️ uml.png>)

<br/>

## Data access

|Actor| [🛢 Propagate](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) | [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
|-|:-:|:-:|:-:
|[`Broker.Binds` 🪣](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) | X
|[`Broker.Chats` 🪣](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) | X
|[`Broker.Tokens` 🪣](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) | X
|[`OnWalletLocalized` 🔔](<../../Wallets 🧑‍🦰 table/🪣🧱 21 Localized 🔔/🤵 OnWalletLocalized 🔔 handler.md>) |  |X| X |

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Schemas
Item: Schema
Key: Code, Wallet
```

<br/>

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.

```yaml
Handlers:
    INSERTED >> OnSchemaInserted:  # Calls Schema@Graph
    UPDATED >> OnSchemaLocalized:  # Calls Translate@Graph
        Assert: New.Language
    ALTERED >> OnSchemaAltered:    # Updates Broker.Frontend
```
Handlers:
* [`OnSchemaInserted` 📃 handler](<../🪣🔔 Inserted/🤵 OnSchemaInserted 🔔 handler.md>)
* [`OnSchemaLocalized` 📃 handler](<../🪣🔔 Localized/🤵 OnSchemaLocalized 🔔 handler.md>)
* [`OnSchemaAltered` 📃 handler](<../🪣🔔 Altered/🤵 OnSchemaAltered 🔔 handler.md>)

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Bind,Token propagation
Code: any-authority.dom/ANY-SCHEMA:1.0
Wallet: <wallet-uuid>

# From OnSchemaAdded, OnPopLocalize
Language: en-US
Title: Any Schema
Description: bla, bla...
```