# 🤵 OnTokenChanged 📃 trigger

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to inform a [Notifier 📣 domain](<📣👥 Notifier domain.md>) that [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) need to be updated on the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)

> Flow 

* Triggered by the [`Triggered@Talker` 🅰️ method](<../../../../45 🤲 Helper domains/Alarms ⏰/⏰🔔 Alarm events/⏰🔔 Triggered.md>)

## How to call

```yaml
- RUN|OnTokenTimeout:
    Item: 
        ID: <token-uuid>
        Wallet: <wallet-id>
```

## Script

```yaml
📃 OnTokenTimeout:

# Assert the inputs
- ASSERT|$Item:
    AllOf: ID, Wallet
    UUIDs: ID, Wallet

# Get the Wallet 🧑‍🦰
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $Item.Wallet

# Remove from Wallet
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Remove@Notifier
    Body:
        Wallet: $Item.Wallet
        Token: $Item.ID
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<🤵 Broker.Tokens 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Remove@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>)
|