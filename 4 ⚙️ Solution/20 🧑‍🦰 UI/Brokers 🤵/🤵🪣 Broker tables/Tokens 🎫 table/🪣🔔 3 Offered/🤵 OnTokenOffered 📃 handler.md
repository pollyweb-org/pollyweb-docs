# 🤵 OnTokenOffered 📃 handler


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


IF|$Token.Accepted:
    Then: # Ask the wallet to save the token
        SEND:
            Header:
                To: $Token.Wallet.Notifier
                Subject: Save@Notifier
            Body:
                Wallet: $Token.Wallet.ID
                Issuer: $Token.Issuer
                Token: $Token.Token   
    Else:
        # Ignore the token
        SAVE|$Token:
            .State: DECLINED
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Save@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|