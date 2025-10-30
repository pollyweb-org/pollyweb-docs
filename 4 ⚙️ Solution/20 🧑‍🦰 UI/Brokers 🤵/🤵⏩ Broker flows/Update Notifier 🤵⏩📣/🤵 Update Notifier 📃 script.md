# 🤵📃 Update Notifier

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/📃 Script.md>) that calls [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>).

<br/>

## How to call

```yaml
RUN|Updated@Notifier:
    Wallet: <wallet-uuid>
    Updates: [ CHATS, BINDS, TOKENS ]
```

## Script

```yaml
📃 Updated@Notifier:

# Assert required inputs
- ASSERT|$.Inputs:
    OneOf: Wallet, Updates
    UUIDs: Wallet
    Lists: Updates

# Assert the options
- ASSERT|$:Updates:
    Enum: CHATS, BINDS, TOKENS

# Get the Wallet
- GET >> $wallet:
    Set: BrokerWallets
    Key: $:Wallet
    
# Tell the Notifier to perform updates
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: $wallet.Wallet
        Updates: $:Updates
```


Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Updated@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|