# 🤵 OnTokenAccepted 📃 trigger

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 

> Flow 

* Triggered by the [`Triggered@Itemizer` 🔔 event](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Triggered.md>)


## Diagram

![alt text](<🤵 OnTokenAccepted ⚙️ uml.png>)


## How to call

```yaml
- RUN|OnTokenAccepted:
    Item: 
        ID: <token-uuid>
        Wallet: <wallet-id>
        Status: ACTIVE
    Changes:
        Status: OFFERED
```

## Script

```yaml
📃 OnTokenAccepted:

# Assert the inputs
- ASSERT|$Item:
    AllOf: ID, Wallet
    UUIDs: ID, Wallet

# Assert if Status: OFFERED -> ACTIVE
- IF:
    Assert: 
        $Changes.Status: OFFERED
        $Item.Status: ACTIVE
    Else: RETURN

# Inform the Issuer
- SEND:
    Header:
        To: $Item.Issuer
        Subject: Accepted@Issuer
    Body:
        Token: $Item.Token
        Hook: $token.Hook
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Wallets` 🪣 table](<../../Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Updated@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|