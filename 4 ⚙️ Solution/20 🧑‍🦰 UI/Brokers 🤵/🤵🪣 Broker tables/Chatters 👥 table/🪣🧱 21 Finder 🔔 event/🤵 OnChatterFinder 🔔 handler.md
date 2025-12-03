# 🤵 OnChatterFinder 🔔 handler

> Part of the [`Broker.Chatters` 🪣 table](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls the [`Present@Finder` 🐌 msg](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🤵 OnChatterFinder ⚙️ uml.png>)


## Script

```yaml
📃 OnChatterFinder:

# Ask the finder to introduce the Host
- SEND:
    Header:
        To: $Chatter.Domain
        Subject: Present@Finder
    Body:
        Chat: $Chatter.Chat.Require
        Host: $Chatter.Chat.Domain.Require
        Language: $Chatter.Chat.Language.Require
        Reviewer: $Chatter.Chat.Wallet.Reviewer.Require
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Present@Finder` 🐌 msg](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
|