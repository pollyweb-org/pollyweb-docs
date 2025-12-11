# 🤵 OnTokenDeclined 📃 handler

> Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnTokenDeclined ⚙️ uml.png>)


## Script

```yaml
📃 OnTokenDeclined:

# Assert the inputs
- ASSERT $Token:
    AllOf: Token, Issuer
    UUIDs: Token
    Texts: Issuer

# Inform the Issuer it was declined
- SEND:
    Header:
        To: $Token.Issuer
        Subject: Offered@Issuer
    Body:
        Token: $Token.Token.Require
        Answer: DECLINED
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Offered@Issuer`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)
|