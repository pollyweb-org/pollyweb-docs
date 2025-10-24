# 🤵📃 Token 🎫 timeout

> Purpose: 

* [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/📃 Script.md>) to execute when a soft delete of [`Tokens` 🪣 table](<../../🤵🪣 Broker tables/🤵🪣 Tokens table.md>) times out.
* Triggered by the [`Trigger@Talker` 🅰️ method](<../../../../35 💬 Chats/😃 Talkers/😃🅰️ Talker methods/🛢🐌😃 Deleted.md>)

## How to call

```yaml
- RUN|TokenTimeout:
    Item: 
        Path: /path/to
        Wallet: <wallet-uuid>
```

## Script

```yaml
📃 TokenTimeout:

# Assert the inputs
- ASSERT|$:Item:
    AllOf: Path, Wallet
    Texts: Path
    UUIDs: Wallet

# Get the Wallet 🧑‍🦰
- GET >> $wallet:
    Set: Wallets@Broker
    Key: $:Item.Wallet

# Remove from Wallet
- SEND:
    To: $wallet.Notifier
    Subject: Remove@Notifier
    Wallet: $:Item.Wallet
    Path: $:Item.Path
```

|Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... placeholders 🧠/ASSERT 🚦.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬ item.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/SEND 📬 msg.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<../../🤵🪣 Broker tables/🤵🪣 Tokens table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Remove@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/3 🤵🐌📣 Remove.md>)
|