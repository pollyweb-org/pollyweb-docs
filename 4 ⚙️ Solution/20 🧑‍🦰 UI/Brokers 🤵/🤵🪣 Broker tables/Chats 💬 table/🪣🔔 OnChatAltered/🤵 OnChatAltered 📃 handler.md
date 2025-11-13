# 🤵 OnChatAltered 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that projects the [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    * of a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    * into the [`Broker.Frontend` 🪣 table](<../../Frontend 📱 table/🤵 Broker.Frontend 🪣 table.md>).

> Flow 

* Triggered by the [`Raised@Itemizer` 🔔 event](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Raised.md>)


## Diagram

![alt text](<🤵 OnChatAltered ⚙️ uml.png>)

## How to call

```yaml
- RUN|OnChatAltered:
    Item: 
        ID: <chat-uuid>
        Wallet: <wallet-id>
```

## Script

```yaml
📃 OnChatAltered:

# Assert the inputs
- ASSERT|$Item:
    AllOf: ID, Wallet
    UUIDs: ID, Wallet

# Get the Wallet 🧑‍🦰
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $Item.Wallet

# Prepare the response
- PUT|$wallet.Chats >> $chats
    Chat: Chat
    Host: Host
    Host$: Host$
    SmallIcon: Host.SmallIcon
    BigIcon: Host.BigIcon

# Get the Wallet's Frontend
- GET >> $frontend:
    Set: Broker.Frontend
    Key: $wallet.ID
    Default: 

# Replace only the Frontend Chats.
- SET|$frontend:
    Chats: $chats
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Frontend`](<../../Frontend 📱 table/🤵 Broker.Frontend 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>) 
|