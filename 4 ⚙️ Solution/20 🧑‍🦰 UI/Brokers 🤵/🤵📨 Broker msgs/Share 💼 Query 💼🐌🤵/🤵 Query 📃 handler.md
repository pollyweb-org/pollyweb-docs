# 🤵 Query 📃 handler

> Implementation
* Part of the [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>)
* Implements both the:
    * [`Share Bind` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>) 
    * [`Share Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>)
    * [`Share Token+ID` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token+ID 👉🆔💼/🧑‍🦰 Share Token+ID ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 Query ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Query@Handler:

# Verify the message
- VERIFY $.Msg

# Assert the message
- ASSERT $.Msg:
    AllOf: Chat, Query, Schemas
    UUIDs: Chat, Query
    Lists: Schemas
    Schemas.Each.IsSchema:

# Get the Chat
- READ >> $chat:
    Set: Broker.Chatters
    Key: 
        Chat: $.Msg.Chat
        Domain: $.Msg.From
    Assert: 
        Chat.STATE: ACTIVE

# Save que Query
- SAVE Broker.Queries:
    STATE: QUERIED
    Chat: $.Msg.Chat
    Query: $.Msg.Query
    Schemas: $.Msg.Schemas
    Consumer: $.Msg.From
```

|Users||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Queries`](<../../🤵🪣 Broker tables/Queries 💼 table/🪣 Queries/🤵 Broker.Queries 🪣 table.md>) [`Broker.Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|