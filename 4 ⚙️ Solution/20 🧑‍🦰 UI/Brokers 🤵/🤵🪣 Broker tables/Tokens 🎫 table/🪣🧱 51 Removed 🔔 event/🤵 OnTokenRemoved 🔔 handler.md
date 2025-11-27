# 🤵 OnTokenRemoved 🔔 handler

> Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

> Part of the [`Broker.Tokens.Remove` ⏩ flow](<../🪣🧱 50 Remove ⏩ flow/🤵 Broker.Tokens.Remove ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnTokenRemoved ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenRemoved:

# Assert the inputs
- ASSERT|$Token:
    AllOf: Token, Issuer, Wallet
    UUIDs: Token, Wallet
    Texts: Issuer

# Inform the Issuer
- SEND:
    Header:
        To: $Token.Issuer
        Subject: Removed@Issuer
    Body:
        Token: $Token

# Inform the Notifier
- SEND:
    Header:
        To: $Token.Wallet.Notifier
        Subject: Removed@Notifier
    Body:
        Issuer: $Token.Issuer
        Path: $Token.Path
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) [`Broker.Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Removed@Issuer` 🅰️ method](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Removed 🤵🐌🎴/🎴 Removed 🐌 msg.md>) <br/> [`Remove@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>)
|