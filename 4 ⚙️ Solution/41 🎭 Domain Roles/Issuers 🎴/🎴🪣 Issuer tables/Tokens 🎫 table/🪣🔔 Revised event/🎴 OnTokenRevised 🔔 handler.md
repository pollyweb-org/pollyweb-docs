# 🎴 OnTokenRevised 📃 handler

> Part of the [`Issuer.Tokens` 🪣 table](<../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🎴 OnTokenRevised ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenRevised:

# Assert the Token
- ASSERT|$Token:
    - AllOf: Token, Status
    - UUIDs: Token
    - Status.IsIn(REVOKED, SUSPENDED, ACTIVE)

# Inform the Broker
- SEND:
    Header: 
        To: $Token.Broker
        Subject: Revise@Broker
    Body:
      Token: $Token.Token
      Status: $Token.Status
      Starts: $Token.Starts
      Expires: $Token.Expires
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Issuer.Tokens`](<../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |  [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>)
|
