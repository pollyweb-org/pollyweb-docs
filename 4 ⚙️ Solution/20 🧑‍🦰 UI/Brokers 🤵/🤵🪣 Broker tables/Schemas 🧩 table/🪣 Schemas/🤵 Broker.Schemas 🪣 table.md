# 🤵🪣 Broker.Schemas table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Schemas
Item: Schema
Key: Code, Wallet

Handlers:
    OnSchemaInserted:       # Call Schema@Graph
        Events: INSERTED 
    OnSchemaLocalized:      # Call Translate@Graph
        Events: UPDATED
        Assert: New.Language
```

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