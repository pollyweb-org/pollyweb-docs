# 🤵 Prompt 📃 handler

> About
* Implements the [`Prompt@Broker` 🐌 msg](<🤵 Prompt 🐌 msg.md>)

> Triggers
* [`OnPromptInserted` 🔔 handler](<../../🤵🪣 Broker tables/Prompts 🤔 table/🪣🔔 1 Inserted/🤵 OnPromptInserted 🔔 handler.md>)
* [`OnPromptEmojied` 🔔 handler](<../../🤵🪣 Broker tables/Prompts 🤔 table/🪣🔔 2 Emojied/🤵🤔 OnPromptEmojied 🔔 handler.md>)

<br/>

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
    Format: $.Msg.Format
    Sender: $.Msg.From
    Wallet: $chatter.Chat.Wallet
    Expires: $.Msg.Expires
    Notifier: $chatter.Chat.Wallet.Notifier
    # Emojis
    ChatEmoji: $chatter.Chat.Emoji
    PromptEmoji: $.Msg.Emoji
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) |  [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Prompts`](<../../🤵🪣 Broker tables/Prompts 🤔 table/🪣 Prompts/🤵🤔 Broker.Prompts 🪣 table.md>) [`Wallets`](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
|
