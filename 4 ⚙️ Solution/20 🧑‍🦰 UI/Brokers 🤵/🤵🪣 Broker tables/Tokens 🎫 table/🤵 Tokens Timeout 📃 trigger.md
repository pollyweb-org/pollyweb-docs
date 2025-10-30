# 🤵📃 Token 🎫 timeout

> Purpose: 

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Script 📃/📃 Script.md>) to execute when a soft delete of [`Tokens` 🪣 table](<🤵 Tokens 🪣 table.md>) times out.
* Triggered by the [`Triggered@Talker` 🅰️ method](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Triggered.md>)

## How to call

```yaml
- RUN|TokenTimeout:
    Item: 
        Token: <token-uuid>
```

## Script

```yaml
📃 TokenTimeout:

# Assert the inputs
- ASSERT|$:Item:
    AllOf: Token, Wallet
    UUIDs: Token, Wallet

# Get the Wallet 🧑‍🦰
- GET >> $wallet:
    Set: BrokerWallets
    Key: $:Item.Wallet

# Remove from Wallet
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Remove@Notifier
    Body:
        Wallet: $:Item.Wallet
        Token: $:Item.Token
```

|Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<🤵 Tokens 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Remove@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>)
|