# 🤵 OnWalletAltered 📃 handler

> About
* Part of the [`Broker.Wallets` 🪣 table](<../🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that projects the [`Broker.Wallets` 🪣 table](<../🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
    * into the [`Broker.Frontend` 🪣 table](<../../Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>).



<br/>

## Diagram

![alt text](<🤵 OnWalletAltered ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnWalletAltered:

# Assert the Wallet item
- ASSERT|$Wallet:
    AllOf: ID, Language, PublicKey
    UUIDs: ID
    Texts: Language, PublicKey

# Insert or update the Frontend
- SAVE|Broker.Frontend:
    Wallet: $Wallet.ID
    Language: $Wallet.Language
    PublicKey: $Wallet.PublicKey
```


|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) |  [`Frontend`](<../../Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)  [`Wallets`](<../🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) 
|