# 🤵 OnTokenAccepted 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the acceptance of a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) by a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
* Part of the [`Broker.Tokens.Insert` ⏩ flow](<../🪣⏩ Flows/1 Issue/🤵 Broker.Tokens.Issued ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnTokenSaved ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenAccepted:

# Assert the inputs
- ASSERT|$Token:
    AllOf: Issuer, Token
    UUIDs: Token
    Texts: Issuer

# Inform the Issuer
- SEND:
    Header:
        To: $Token.Issuer
        Subject: Offered@Issuer
    Body:
        Token: $Token.Token  
        Answer: ACCEPTED
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Offered@Issuer`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)
|