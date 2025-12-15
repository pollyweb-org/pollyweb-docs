# 🤵 Invite@Broker 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Invite@Broker` 🐌 msg](<🤵 Invite 🐌 msg.md>)
* Inserts into the [`Broker.Invites` 🪣 table](<../../🤵🪣 Broker tables/Invites 🤲 table/🪣 Invites/🤵 Broker.Invites 🪣 table.md>) 

## Flow

![alt text](<🤵 Invite ⚙️ uml.png>)

## Script

```yaml
📃 Invite@Broker:

# Verify the message
- VERIFY $.Msg

# Assert the inputs
- ASSERT $.Msg:
    AllOf: Chat, Helper, Schema, Invite
    UUIDs: Chat, Invite
    Texts: Helper, Schema
    Helper.IsDomain:
    Schema.IsSchema:

# Confirm it's a chatter
- READ:
    Set: Broker.Chatters
    Key: 
        Chat: $.Msg.Chat
        Domain: $.Msg.From

# Add the invite
- SAVE Broker.Invites:
    Chat: $.Msg.Chat
    Consumer: $.Msg.From
    Invite: $.Msg.Invite
    Helper: $.Msg.Helper
    Schema: $.Msg.Schema
    State: .INVITED
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ 📃 script.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)  [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Broker.Invites`](<../../🤵🪣 Broker tables/Invites 🤲 table/🪣 Invites/🤵 Broker.Invites 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsDomain`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>) 
|