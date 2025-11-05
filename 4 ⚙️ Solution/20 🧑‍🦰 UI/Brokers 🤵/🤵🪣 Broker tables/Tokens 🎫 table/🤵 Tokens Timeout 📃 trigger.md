# 🤵📃 Token 🎫 timeout

> Purpose: 

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to execute when a soft delete of [`Tokens` 🪣 table](<🤵 BrokerTokens 🪣 table.md>) times out.
* Triggered by the [`Triggered@Talker` 🅰️ method](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Triggered.md>)

## How to call

```yaml
- RUN|TokenTimeout:
    Item: 
        ID: <token-uuid>
        Wallet: <wallet-id>
```

## Script

```yaml
📃 TokenTimeout:

# Assert the inputs
- ASSERT|$Item:
    AllOf: ID, Wallet
    UUIDs: ID, Wallet

# Get the Wallet 🧑‍🦰
- READ >> $wallet:
    Set: BrokerWallets
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
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<🤵 BrokerTokens 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Remove@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>)
|