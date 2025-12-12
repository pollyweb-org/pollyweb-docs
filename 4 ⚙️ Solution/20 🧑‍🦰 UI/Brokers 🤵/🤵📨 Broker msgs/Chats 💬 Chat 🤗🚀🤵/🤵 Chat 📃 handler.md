# 🤵📃 Chat 🚀 Broker

> Purpose
* [Script 📃](<🤵 Chat 🚀 call.md>) that implements the [`Chat@Broker` 📨 msg](<🤵 Chat 📃 handler.md>)
* Asserts the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) is a participant in the [`Broker.Chatters` 🪣 table](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)
* Returns part of the data from the [`Broker.Chats` 🪣 table](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)


## Flow

![alt text](<🤵 Chat ⚙️ uml.png>)

## Script

```yaml
📃 Chat@Broker:

# Assert the message
- ASSERT $.Msg:
    AllOf: Chat
    UUIDs: Chat

# Verify the message
- VERIFY $.Msg

# Get the chatter item
- READ >> $chatter:
    Set: Broker.Chatters
    Key: 
        Domain: $.Msg.From
        Chat: $.Msg.Chat

# Add the Chat details to the response
- PUT $chatter.Chat >> $resp:
    ID, PublicKey, Language, Timezone

# Add the Chatter details to the response
- PUT $chatter >> $resp:
    Key, Properties, Binds, Tokens

# Respond
- RETURN $resp
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)  [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|  [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Wallets`](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
|[Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)|[`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|