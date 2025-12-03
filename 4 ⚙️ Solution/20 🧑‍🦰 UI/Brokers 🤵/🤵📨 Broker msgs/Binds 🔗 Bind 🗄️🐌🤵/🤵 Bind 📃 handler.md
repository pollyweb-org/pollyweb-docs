# 🤵 Bind 📃 handler

> Purpose
* Implements the [`Bind@Broker` 📨 msg](<🤵 Bind 🐌 msg.md>)
* Inserts into the [`Broker.Binds` 🪣 table](<../../🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)

<br/>

## Flow

![alt text](<🤵 Bind ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Bind@Broker:

# Verify the signature
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Chat, Hook, Schemas
    UUIDs: Chat, Hook
    Texts: Schema

# Get the chat
- READ >> $chat:
    Set: Broker.Chats
    Key: $.Msg.Chat

# Check if it's the host
- ASSERT|$.Msg:
    From: $chat.Host

# Save the bind
- SAVE|Broker.Binds:

    # Bind lifecycle
    .State: OFFERED
    .Delete: 1 hour

    # From Bind@Broker
    Hook: $.Msg.Hook 
    Chat: $.Msg.Chat
    Vault: $.Msg.From
    Schema: $.Msg.Schema

    # From Hello@Host
    Wallet: $chat.Wallet
    Language: $chat.Language
```

Uses||
|-|-
[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Binds`](<../../🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) [`Wallets`](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|

