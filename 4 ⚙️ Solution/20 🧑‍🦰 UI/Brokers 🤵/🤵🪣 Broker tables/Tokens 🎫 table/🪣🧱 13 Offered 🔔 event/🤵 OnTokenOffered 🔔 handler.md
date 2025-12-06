# 🤵 OnTokenOffered 📃 handler

> Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that processes user response to an offered [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).
* Part of the [🤵 Broker.Tokens.Insert ⏩ flow](<../🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnTokenOffered ⚙️ uml.png>)


## Script

```yaml
📃 OnTokenOffered:

# Assert the inputs
- ASSERT|$Token:
    AllOf: Wallet, Token, Issuer, Accepted
    UUIDs: Wallet, Token
    Texts: Issuer
    Bools: Accepted

# Ignore if not accepted
- IFNOT|$Token.Accepted:
    RETURN|DECLINED

# Otherwise, ask the wallet to save the token
- SEND:
    Header:
        To: $Token.Wallet.Notifier
        Subject: Save@Notifier
    Body:
        Wallet: $Token.Wallet.ID
        Issuer: $Token.Issuer
        Token: $Token.Token   
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Save@Notifier`](<../../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|