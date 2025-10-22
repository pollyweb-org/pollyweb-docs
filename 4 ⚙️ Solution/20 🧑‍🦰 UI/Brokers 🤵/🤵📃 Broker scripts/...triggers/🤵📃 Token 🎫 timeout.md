# 🤵📃 Token 🎫 timeout

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) to execute when a soft delete of [`Tokens` 🪣 table](<../../🤵🪣 Broker tables/🤵🪣 Tokens table.md>) times out.


## Script

```yaml
📃 TokenTimeout:

# Assert the inputs
- ASSERT|!Item:
    AllOf: Path, Wallet
    Texts: Path
    UUIDs: Wallet

# Get the Wallet 🧑‍🦰
- GET >> $wallet:
    Pool: Wallets@Broker
    Key: !Item.Wallet

# Remove from Wallet
- SEND:
    To: $wallet.Notifier
    Subject: Remove@Notifier
    Wallet: !Item.Wallet
    Path: !Item.Path
```

|Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<../../🤵🪣 Broker tables/🤵🪣 Tokens table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Remove@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/3 🤵🐌📣 Remove.md>)
|