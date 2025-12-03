# 🤵 Saved 📃 handler

> Purpose
* [Script 📃](<🤵 Saved 🐌 msg.md>) that implements the [`Saved@Broker` 🐌 msg](<🤵 Saved 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🤵 Saved ⚙️ uml.png>)

## Script

```yaml
📃 Saved@Broker:

# Assert the message
- ASSERT|$.Msg:
    AllOf: Token, Issuer, Path
    UUIDs: Token, Issuer, From
    Texts: Issuer, Path

# Get the Wallet
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Get the Token
- READ >> $token:
    Set: Broker.Tokens
    Key: 
        Issuer: $.Msg.Issuer
        Token: $.Msg.Token
    Assert:
        Wallet: $.Msg.From

# Cancel the scheduled deletion on Issue@
- SAVE|$token:
    .State: SAVED
    .Delete: 
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens `](<../../🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|
