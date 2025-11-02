# 🤵 Prompt 📃 handler

> Purpose
* Implements the [`Prompt@Broker` 🅰️ method](<🤵 Prompt 🐌 msg.md>)

> Dependencies
* Depends on the [`PromptEmoji` 📃 script](<🤵 Prompt 📃 emoji.md>)

<br/>

## Script

```yaml
# Verify the message
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg:
    AllOf: Chat, Emoji, Format, Hook
    UUIDs: Chat, Hook
    Texts: Emoji, Format
    Times: Expires

# Get the Chat participant
- GET >> $chatter:
    Set: BrokerChatters
    Key: 
        Chat: $.Msg.Chat
        Domain: $.Msg.From

# Get the Chat
- EVAL|$chatter.Chat >> $chat

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

Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🤵 BrokerChatters 🪣 table.md>) [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) | [`PromptEmoji` 📃 script](<🤵 Prompt 📃 emoji.md>)
|
