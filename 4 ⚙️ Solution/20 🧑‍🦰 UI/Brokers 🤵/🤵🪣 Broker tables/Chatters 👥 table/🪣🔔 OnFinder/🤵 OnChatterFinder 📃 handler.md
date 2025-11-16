# 🤵 OnChatterFinder 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls the [`Present@Finder` 🅰️ method](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
  
## Diagram

![alt text](<🤵 OnChatterFinder ⚙️ uml.png>)


## Script

```yaml
📃 OnChatterFinder:

# Rename for legibility
- PUT|$Item >> $chatter
- PUT|$Item.Chat >> $chat
- PUT|$Item.Chat.Wallet >> $wallet

# Ask the finder to introduce the Host
- SEND:
    Header:
        To: $chatter.Domain
        Subject: Present@Finder
    Body:
        Chat: $chat.ID
        Host: $chat.Host
        Language: $chat.Language
        Reviewer: $wallet.Reviewer
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Present@Finder` 🅰️ method](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
|