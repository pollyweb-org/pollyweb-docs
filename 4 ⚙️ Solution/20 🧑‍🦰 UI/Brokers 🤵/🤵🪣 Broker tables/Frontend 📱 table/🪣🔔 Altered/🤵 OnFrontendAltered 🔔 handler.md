# 🤵 OnFrontendAltered 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to inform a [Notifier 📣 domain](<../../../../Notifiers 📣/📣/📣 Notifier 👥 domain.md>) 
    * that the UI need to be refreshed 
    * on the [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)


<br/>

## Diagram

![alt text](<🤵 OnFrontendAltered ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnFrontendAltered:

# Assert the inputs
- ASSERT $Item:
    AllOf: Wallet, Frontend
    UUIDs: Wallet

# Tell the Notifier to perform updates
- SEND:
    Header:
        To: $wallet.Notifier.Require
        Subject: Updated@Notifier
    Body:
        Wallet: $Item.Wallet.Require
        New: $New
        Old: $Old
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Frontend` 🪣 table](<../🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Updated@Notifier` 🐌 msg](<../../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|