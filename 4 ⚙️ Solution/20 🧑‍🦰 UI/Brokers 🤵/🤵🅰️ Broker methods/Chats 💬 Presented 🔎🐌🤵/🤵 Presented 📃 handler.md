# 🤵📃 Presented

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Presented@Broker`](<🤵 Presented 🐌 msg.md>) method.

## Diagram

![alt text](<🤵 Presented ⚙️ uml.png>)

## Chat 

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ From another chat: <br/>- [Return] to original chat
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Tokens shared [-] <br/>- 🎟️ Any Token, by Any Issuer<br/>- 🪪 Another Token, by Another Issuer
|

## Script

```yaml
📃 Presented@Broker:

# Verify the message
- VERIFY|$.Msg

# Verify the required inputs
- ASSERT|$.Msg:
    OneOf: Chat
    UUIDs: Chat

# Read the chatter
- READ >> $chat:
    Set: Broker.Chatters
    Key: 
        Domain: $.Msg.From
        Chat: $.Msg.Chat
    Assert:
        Role: FINDER

# Process the Chat state
- SAVE|$chat:
    .State: PRESENTED
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSESS`](<../../🤵⏩ Broker flows/Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerChats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Markdown`](<../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/Markdown ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|