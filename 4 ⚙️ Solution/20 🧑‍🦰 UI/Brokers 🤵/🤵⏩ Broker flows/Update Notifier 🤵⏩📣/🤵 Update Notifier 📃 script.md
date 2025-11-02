# 🤵📃 Update Notifier

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that calls [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>).

<br/>

## How to call

```yaml
RUN|Update-Notifier:
    wallet: $wallet
    Updates: [ CHATS, BINDS, TOKENS ]
```

## Script

```yaml
📃 Update-Notifier:

# Assert required inputs
- ASSERT|$.Inputs:
    OneOf: wallet, Updates
    Lists: Updates

# Assert the options
- ASSERT|$:Updates:
    Enum: CHATS, BINDS, TOKENS
    
# Tell the Notifier to perform updates
- SEND:
    Header:
        To: $:wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: $:wallet.ID
        Updates: $:Updates
```


Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Updated@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|