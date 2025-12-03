# 🎴 OnTokenIssued 📃 handler

> Part of the [`Issuer.Tokens` 🪣 table](<../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🎴 OnTokenIssued ⚙️ uml.png>)


## Script

```yaml
📃 OnTokenIssued:

# Assert the Token
- ASSERT|$Token:
    AllOf: Broker, Chat, Schema, Starts
    UUIDs: Chat
    Texts: Broker, Schema
    Times: Starts, Expires

# Offer the Token to the Broker 🤵 
- SEND:
    Header:
        To: $Token.Broker
        Subject: Issue@Broker
    Body:
        Token: $Token.ID
        Chat: $Token.Chat
        Schema: $Token.Schema
        Starts: $Token.Starts
        Expires: $Token.Expires
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Issuer.Tokens`](<../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Issue@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>)
|