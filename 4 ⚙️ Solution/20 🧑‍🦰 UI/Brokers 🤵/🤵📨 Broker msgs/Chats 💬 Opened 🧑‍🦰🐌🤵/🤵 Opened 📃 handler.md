# 🤵 Opened 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Opened@Broker` 📨 msg](<🤵 Opened 🐌 msg.md>).

## Diagram

![alt text](<🤵 Opened ⚙️ uml.png>)

## Script

```yaml
📃 Opened@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Chat, PublicKey
    UUIDs: Chat, From
    Texts: PublicKey

# Get the Wallet
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $.Msg.From

# Verify the message with the Wallet's PublicKey
- VERIFY|$.Msg:
    PublicKey: $wallet.PublicKey

# Read the chat
- READ >> $chat:
    Set: Broker.Chats
    Key: $.Msg.Chat
    Assert: 
        Wallet: $wallet.ID

# Process the Chat state
- SAVE|$chat:
    .State: OPENED
    PublicKey: $.Msg.PublicKey
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSESS`](<../../🤵⏩ Broker flows/Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>)   [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|