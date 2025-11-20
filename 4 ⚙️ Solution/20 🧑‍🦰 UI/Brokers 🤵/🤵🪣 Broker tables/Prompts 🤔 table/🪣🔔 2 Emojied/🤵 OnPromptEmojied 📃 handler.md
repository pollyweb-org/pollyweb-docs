# 🤵 OnPromptEmojied 📃 handler


## Script

```yaml
📃 OnPromptEmojied:

# Assert the message
- ASSERT|$Prompt:
    AllOf: Hook, Chat
    UUIDs: Hook, Chat
    Texts: Format, Emoji

# Verify the Prompt's Chat
- ASSERT|$Prompt.Chat:
    AllOf: Notifier, Wallet
    Texts: Notifier
    UUIDs: Wallet

# Verify the Prompt's Chatter
- ASSERT|$Prompt.Chatter:
    AllOf: Domain
    Texts: Domain

# Forward to the notifier
- SEND: 
    Header:
        To: $Prompt.Chat.Notifier
        Subject: Prompt@Notifier    
    Body:
        Chat: $Prompt.Chat
        Hook: $Prompt.Hook
        Emoji: $Prompt.Emoji
        Format: $Prompt.Format
        Wallet: $Prompt.Chat.Wallet
        Sender: $Prompt.Chatter.Domain
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CALL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`PromptEmoji` 📃 script](<🤵 Prompt 📃 emoji.md>)
|
