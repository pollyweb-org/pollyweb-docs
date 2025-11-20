# 🤵 Prompt 📃 handler

> Purpose
* Implements the [`Prompt@Broker` 🅰️ method](<🤵 Prompt 🐌 msg.md>)

## Script

```yaml
📃 Prompt@Broker:

# Verify the message
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg:
    AllOf: Chat, Format, Hook
    UUIDs: Chat, Hook
    Texts: Emoji, Format
    Times: Expires

# Assert the Sender is a Chatter
- READ >> $chatter:
    Set: Broker.Chatters
    Key: 
        Chat: $.Msg.Chat
        Domain: $.Msg.From

# Assert the Chat is active
- ASSERT|$chatter.Chat:
    .State: ACTIVE

# Save the Prompt
- SAVE|Broker.Prompts:
    Chat: $.Msg.Chat
    Hook: $.Msg.Hook
    Role: $chatter.Role
    Emoji: $.Msg.Emoji
    Format: $.Msg.Format
    Sender: $.Msg.From
    Wallet: $chatter.Chat.Wallet
    Expires: $.Msg.Expires
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)  [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
|
