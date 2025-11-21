# 🎴 OnTokenIssued 📃 handler


## Diagram

![alt text](<🎴 OnTokenIssued ⚙️ uml.png>)


## Script

```yaml
📃 OnTokenIssued:

# Assert the Token
- ASSERT|$Token:
    AllOf: Broker, Chat, ID
    UUIDs: Chat, ID
    Texts: Broker

# Notify the Broker 🤵 about the issued Token
- SEND:
    Header:
        To: $Token.Broker
        Subject: Offer@Broker
    Body:
        Hook: $Token.ID
        Chat: $Token.Chat
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Issuer.Tokens`](<../🪣 Tokens/🗄️ Issuer.Tokens 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Offer@Broker` 🅰️ method](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
|