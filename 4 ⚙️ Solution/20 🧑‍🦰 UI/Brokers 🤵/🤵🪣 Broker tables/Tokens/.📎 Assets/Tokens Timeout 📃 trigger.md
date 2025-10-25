# 🤵📃 Token 🎫 timeout

> Purpose: 

* [Script 📃](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) to execute when a soft delete of [`Tokens` 🪣 table](<../🤵🪣 Tokens 🎫 table.md>) times out.
* Triggered by the [`Triggered@Talker` 🅰️ method](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Triggered.md>)

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
    Header:
        To: $wallet.Notifier
        Subject: Remove@Notifier
    Body:
        Wallet: $:Item.Wallet
        Path: $:Item.Path
```

|Needs ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`GET`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`SEND`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<../🤵🪣 Tokens 🎫 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Remove@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/3 🤵🐌📣 Remove.md>)
|