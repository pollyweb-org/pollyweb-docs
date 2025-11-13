# 🤵 OnChatChanges 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to inform a [Notifier 📣 domain](<../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) 
    * that [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) need to be updated 
    * on the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)

> Flow 

* Triggered by the [`Raised@Itemizer` 🔔 event](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Raised.md>)


## Diagram

![alt text](<🤵 OnFrontendAltered ⚙️ uml.png>)

## How to call

```yaml
- RUN|OnChatChanges:
    Item: 
        ID: <chat-uuid>
        Wallet: <wallet-id>
```

## Script

```yaml
📃 OnChatChanges:

# Assert the inputs
- ASSERT|$Item:
    AllOf: ID, Wallet
    UUIDs: ID, Wallet

# Get the Wallet 🧑‍🦰
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $Item.Wallet

# Tell the Notifier to perform updates
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: $Item.Wallet
        Updates: [CHATS]
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Wallets` 🪣 table](<../Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Updated@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|