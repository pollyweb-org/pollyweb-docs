# 🤵 Prompt 📃 handler

> Purpose
* Implements the [`Prompt@Broker` 🅰️ method](<🤵 Prompt 🐌 msg.md>)

> Dependencies
* Depends on the [`PromptEmoji` 📃 script](<🤵 Prompt 📃 emoji.md>)

<br/>

## Script

```yaml
📃 Prompt@Broker:

# Verify the message
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg:
    AllOf: Chat, Emoji, Format, Hook
    UUIDs: Chat, Hook
    Texts: Emoji, Format
    Times: Expires

# Get the Chat participant
- READ >> $chatter:
    Set: BrokerChatters
    Key: 
        Chat: $.Msg.Chat
        Domain: $.Msg.From

# Get the Chat
- PUT|$chatter.Chat >> $chat

# Calculate the emoji
- RUN|PromptEmoji >> $emoji:
    Format: $.Msg.Format
    PromptEmoji: $.Msg.Emoji
    ChatEmoji: $chat.Emoji
    Role: $chatter.Role

# Forward to the notifier
- SEND: 
    Header:
        To: $chat.Notifier
        Subject: Prompt@Notifier    
    Body:
        Wallet: $chat.Wallet
        Chat: $.Msg.Chat
        Sender: $.Msg.From
        Hook: $.Msg.Hook
        Format: $.Msg.Format
        Emoji: $emoji
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🤵 BrokerChatters 🪣 table.md>) [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`PromptEmoji` 📃 script](<🤵 Prompt 📃 emoji.md>)
|
