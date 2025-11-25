# 🤵 OnTokenAccepted 📃 handler


## Diagram

![alt text](<🤵 OnTokenSaved ⚙️ uml.png>)


## Script

```yaml
📃 OnTokenAccepted:

# Assert the inputs
- ASSERT|$Token:
    AllOf: ID, Issuer, Hook
    UUIDs: ID, Hook
    Texts: Issuer

# Inform the Issuer
- SEND:
    Header:
        To: $Token.Issuer
        Subject: Accepted@Issuer
    Body:
        Hook: $Token.Hook  # Hook @ Issuer
        Token: $Token.ID   # Token.ID @ Broker
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Accepted@Issuer` 🅰️ method](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>)
|