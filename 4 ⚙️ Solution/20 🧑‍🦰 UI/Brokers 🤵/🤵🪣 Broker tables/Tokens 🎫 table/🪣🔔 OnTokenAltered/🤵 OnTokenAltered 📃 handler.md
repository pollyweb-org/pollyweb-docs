# 🤵 OnTokenAltered 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that projects the [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    * of a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    * into the [`Broker.Frontend` 🪣 table](<../../Frontend 📱 table/🤵 Broker.Frontend 🪣 table.md>).

> Flow 

* Triggered by the [`Raised@Itemizer` 🔔 event](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Raised.md>)


## Diagram

![alt text](<🤵 OnTokenAltered ⚙️ uml.png>)

## How to call

```yaml
- RUN|OnTokenAltered:
    Item: 
        Wallet: <wallet-id>
```

## Script

```yaml
📃 OnTokenAltered:

# Assert the inputs
- ASSERT|$Item:
    AllOf: Wallet
    UUIDs: Wallet

# Get the Wallet 🧑‍🦰
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $Item.Wallet

# Get the Wallet's Frontend
- READ >> $frontend:
    Set: Broker.Frontend
    Key: $wallet.ID
    Default: 
        PublicKey: $wallet.PublicKey

# Prepare the response:
- PUT|$wallet.Tokens >> $tokens:
    Issuer, Issuer$, Schema, Schema$, 
    Key, Status, Token

# Replace only the Frontend Tokens.
- SAVE|$frontend:
    Tokens: $tokens
```


|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Frontend`](<../../Frontend 📱 table/🤵 Broker.Frontend 🪣 table.md>) [`Tokens` ](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>) 
|