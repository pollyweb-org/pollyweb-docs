# 🤵 OnTokenDeclined 📃 handler

<br/>

## Diagram

![alt text](<🤵 OnTokenDeclined ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenDeclined:

# Assert the item
- ASSERT|$Token:
    AllOf: Issuer, Hook
    UUIDs: Hook
    Texts: Issuer

# Notify the Issuer
- SEND:
    Header:
        To: $Token.Issuer
        Subject: Declined@Issuer
    Body:
        Hook: $Token.Hook  # Hook @ Issuer
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Declined@Issuer`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Declined 🤵🐌🎴/🎴 Declined 🐌 msg.md>) |
|