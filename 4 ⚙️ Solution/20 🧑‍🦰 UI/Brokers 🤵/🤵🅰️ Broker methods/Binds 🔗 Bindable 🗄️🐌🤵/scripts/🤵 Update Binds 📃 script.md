# 🤵 Update Binds 📃 script


## Script

```yaml
📃 Update-Binds:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: wallet
   
# Tell the Notifier to perform updates
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: $wallet.ID
        Updates: $Updates
```


Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Updated@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|