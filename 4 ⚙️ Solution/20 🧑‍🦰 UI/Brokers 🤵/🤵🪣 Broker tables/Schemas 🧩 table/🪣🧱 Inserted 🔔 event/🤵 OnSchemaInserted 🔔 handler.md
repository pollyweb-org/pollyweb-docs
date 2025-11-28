# 🤵 OnSchemaInserted 📃 handler

> About
* Part of the [`Broker.Schemas` 🪣 table](<../🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>)
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the insertion of a new [`Schema`](<../🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>) item.

<br/>

## Diagram

![alt text](<🤵 OnSchemaInserted ⚙️ uml.png>)

<br/>

## Script 

```yaml
📃 OnSchemaInserted:

# Assert the Schema
- ASSERT|$Schema:
    AllOf: Code, Wallet
    Texts: Code
    UUIDs: Wallet

# Get the Schema details from the Graph
- SEND >> $schema:
    Header:
        To: $.Hosted.Graph
        Subject: Schema@Graph
    Body:
        Schema: $Schema.Name
        Language: $Schema.Wallet.Language

# Save the Schema info
- SAVE|$Schema:
    Language: $Schema.Wallet.Language
    Title: $schema.Title
    Description: $schema.Description
    Emoji: $schema.Emoji
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Schemas`](<../🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) |  [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Schema@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Schema/🕸 Schema 📃 handler.md>)
|