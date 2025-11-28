# 🤵 OnSchemaAltered 📃 handler

> About
* Part of the [`Broker.Schemas` 🪣 table](<../🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>)
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that projects the [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    * of a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    * into the [`Broker.Frontend` 🪣 table](<../../Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>).



<br/>

## Diagram

![alt text](<🤵 OnSchemaAltered ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnSchemaAltered:

# Assert the inputs
- ASSERT|$Schema:
    AllOf: Wallet
    UUIDs: Wallet

# Get the Wallet 🧑‍🦰
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $Schema.Wallet

# Get the Wallet's Frontend
- READ >> $frontend:
    Set: Broker.Frontend
    Key: $wallet.ID

# Prepare the response:
- PUT|$wallet.Schemas >> $schemas:
    Code, Title, Description

# Replace only the Frontend Tokens.
- SAVE|$frontend:
    Schemas: $schemas
```


|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) |  [`Frontend`](<../../Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>) [`Schemas`](<../🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) 
|