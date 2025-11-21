# 🤵 OnTokenRejected 📃 handler

## Diagram

![alt text](<🤵 OnTokenRejected ⚙️ uml.png>)

## Script

```yaml
📃 OnTokenRejected:

# Assert the item
- ASSERT|$Token:
    AllOf: Issuer, Hook
    UUIDs: Hook
    Texts: Issuer

# Notify the Issuer
- SEND:
    Header:
        To: $Token.Issuer
        Subject: Reject@Issuer
    Body:
        Hook: $Token.Hook  # Hook @ Issuer
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Reject@Issuer` 🅰️ method](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Rejected 🤵🐌🎴/🎴 Rejected 🐌 msg.md>) |
|