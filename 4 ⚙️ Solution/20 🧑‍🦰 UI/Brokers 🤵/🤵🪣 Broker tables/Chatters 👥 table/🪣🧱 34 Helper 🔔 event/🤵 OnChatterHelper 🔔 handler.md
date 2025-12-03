# 🤵 OnChatterHelper 🔔 handler

> Part of the [`Broker.Chatters` 🪣 table](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls the [`Invited@Helper` 🅰️ method](<../../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>)
  
<br/>

## Diagram

![alt text](<🤵 OnChatterHelper ⚙️ uml.png>)


## Script

```yaml
📃 OnChatterHelper:

# Rename for legibility
- PUT|$Item >> $chatter
- PUT|$Item.Chat >> $chat
- PUT|$Item.Chat.Wallet >> $wallet

# Invite the helper to the chat
- SEND:
    Header:
        To: $chatter.Domain
        Subject: Invited@Helper
    Body:
        Chat: $chat.ID.Require
        Inviter: $chat.Host.Require
        Schema: $chatter.Schema
        Hook: $chatter.Hook
        Inputs: $chatter.Inputs
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Invited@Helper` 🅰️ method](<../../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>)
|