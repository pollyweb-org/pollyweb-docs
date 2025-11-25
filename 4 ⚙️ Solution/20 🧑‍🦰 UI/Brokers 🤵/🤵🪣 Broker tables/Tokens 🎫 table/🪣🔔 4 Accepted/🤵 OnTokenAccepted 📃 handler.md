# 🤵 OnTokenAccepted 📃 handler


## Diagram

![alt text](<🤵 OnTokenAccepted ⚙️ uml.png>)


## Script

```yaml
📃 OnTokenAccepted:

# Assert the inputs
- ASSERT|$Token:
    AllOf: Wallet, Hook
    UUIDs: Wallet, Hook

# Ask the wallet to save the token
- SEND:
    Header:
        To: $Token.Wallet.Notifier
        Subject: Save@Notifier
    Body:
        Wallet: $Token.Wallet.ID
        Hook: $Token.Hook   # Hook at Issuer
        Token: $Token.ID    # ID at Broker
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Save@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|