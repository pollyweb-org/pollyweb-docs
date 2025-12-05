# 🤵 Invite 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Invite@Broker` 🐌 msg](<🤵 Invite 🐌 msg.md>)

## Flow

![alt text](<🤵 Invite ⚙️ uml.png>)

## Script

```yaml
📃 Invite@Broker:

# Verify the message
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Chat, Helper, Schema, Invite
    UUIDs: Chat, Invite
    Texts: Helper, Schema
    Helper.IsDomain:
    Schema.IsSchema:

# Get the chat
- READ >> $chat:
    Set: Broker.Chats
    Key: $.Msg.Chat
    Assert: 
        Host: $.Msg.From # Only from the host
        .State: ACTIVE   # While the chat is active



```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CONFIRM`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ 📃 script.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Broker.Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)
|