# 🤵 OnFrontendAltered 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to inform a [Notifier 📣 domain](<../../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) 
    * that the UI need to be refreshed 
    * on the [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)

> Flow 

* Triggered by the [`Raised@Itemizer` 🔔 event](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Raised.md>)


## Diagram

![alt text](<🤵 OnFrontendAltered ⚙️ uml.png>)

## How to call

```yaml
- RUN|OnFrontendAltered:
    Item: 
        Wallet: <wallet-uuid>
        Chats: {...}
        Binds: {...}
        Tokens: {...}
    New: {...}
    Old: {...}
```

## Script

```yaml
📃 OnFrontendAltered:

# Assert the inputs
- ASSERT|$Item:
    AllOf: Wallet, Frontend
    UUIDs: Wallet

# Tell the Notifier to perform updates
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: $Item.Wallet
        #Chats: $Item.Chats
        #Binds: $Item.Binds
        #Tokens: $Item.Tokens
        #New: $New
        #Old: $Old
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Frontend` 🪣 table](<../🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Updated@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|