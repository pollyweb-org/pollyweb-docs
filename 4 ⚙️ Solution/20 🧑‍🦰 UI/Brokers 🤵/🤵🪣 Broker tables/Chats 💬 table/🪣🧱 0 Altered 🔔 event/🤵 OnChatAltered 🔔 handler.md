# 🤵 OnChatAltered 🔔 handler

> Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that projects the [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    * of a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    * into the [`Broker.Frontend` 🪣 table](<../../Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>).




## Diagram

![alt text](<🤵 OnChatAltered ⚙️ uml.png>)



## Script

```yaml
📃 OnChatAltered:

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
- READ >> $frontend:
    Set: Broker.Frontend
    Key: $wallet.ID

# Replace only the Frontend Chats.
- SAVE|$frontend:
    Chats: $chats
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Frontend`](<../../Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) 
|