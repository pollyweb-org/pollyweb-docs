# 🤗 OnChatDetails 🔔 handler

> About
* Part of the [`Host.Chats` 🪣 table](<../🪣 Chats/🤗 Host.Chats 🪣 table.md>)
* Calls the [`Chat@Broker` 🚀 call](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 🚀 call.md>) to get [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) details

<br/>

## Diagram

![alt text](<🤗 OnChatDetails ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnChatDetails:

# Assert the Chat key
- ASSERT $Chat:
    AllOf: Broker, Chat

# Call Chat@Broker
- SEND >> $details:
    Header:
        To: $Chat.Broker
        Subject: Chat@Broker
    Body:
        Chat: $Chat.Chat

# Save the details into the Item
- SAVE $Chat:

    # Details
    PublicKey: $details.PublicKey
    Timezone: $details.Timezone 
    Language: $details.Language

    # Locator
    Schema: $details.Schema
    Key: $details.Key
    Parameters: $details.Parameters

    # Shares
    SharedBinds: $details.Binds
    SharedTokens: $details.Tokens

# Progress the state
- RETURN: BINDS
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Chats`](<../🪣 Chats/🤗 Host.Chats 🪣 table.md>)