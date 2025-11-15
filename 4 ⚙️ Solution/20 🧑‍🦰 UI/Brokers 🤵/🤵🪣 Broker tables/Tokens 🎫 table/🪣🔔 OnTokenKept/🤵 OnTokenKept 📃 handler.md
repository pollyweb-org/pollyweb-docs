# 🤵 OnTokenAccepted 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls the [`Accepted@Issuer` 🅰️ method](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>)

> Flow 

* Triggered by the [`Raised@Itemizer` 🔔 event](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Raised.md>)


## Diagram

![alt text](<🤵 OnTokenKept ⚙️ uml.png>)


## How to call

```yaml
- RUN|OnTokenAccepted:
    Item: 
        ID: <token-uuid>
        Wallet: <wallet-id>
        Status: ACTIVE
    New:
        Status: ACTIVE
    Old:
        Status: OFFERED
```

## Script

```yaml
📃 OnTokenAccepted:

# Assert the inputs
- ASSERT|$Item:
    AllOf: ID, Issuer, Hook
    UUIDs: ID, Hook
    Texts: Issuer

# Inform the Issuer
- SEND:
    Header:
        To: $Item.Issuer
        Subject: Accepted@Issuer
    Body:
        Hook: $Item.Hook  # Hook @ Issuer
        Token: $Item.ID   # Token.ID @ Broker
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Wallets` 🪣 table](<../../Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Accepted@Issuer` 🅰️ method](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>)
|