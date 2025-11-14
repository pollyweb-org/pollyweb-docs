# 🤵 Freeze 📃 handler

> Purpose
* [Script 📃](<../Chats 💬 Chat 🤗🚀🤵/🤵 Chat 🚀 request.md>) that implements the [`Freeze@Broker` 🅰️ method](<🤵 Freeze 🐌 msg.md>).


## Flow

![alt text](<🤵 Freeze ⚙️ uml.png>)


## Script

```yaml
📃 Freeze@Broker:

# Assert the message
- ASSERT|$.Msg:
    - AllOf: Chat
    - UUIDs: Chat

# Verify the message
- VERIFY|$.Msg

# Get the chatter item
- READ >> $chatter:
    Set: Broker.Chatters
    Key: 
        Domain: $.Msg.From
        Chat: $.Msg.Chat

# Add the Chat details to the response
- SET|$chatter.Chat >> $resp:
    ID, PublicKey, Language, Timezone

# Add the Chatter details to the response
- SET|$chatter >> $resp:
    Key, Properties, Binds, Tokens

# Respond
- RETURN|$resp
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SET`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|  [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🤵 Broker.Chatters 🪣 table.md>) [`Wallets`](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>)
|[Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)|[`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|