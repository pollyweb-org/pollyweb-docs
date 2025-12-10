# 🤲 Help@Helper 📃 handler

> About
* Part of the [Helper 🤲 domain](<../../🤲 Helper/🤲🎭 Helper role.md>)
* Implements the [`Help@Helper` 🐌 msg](<🤲 Help 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🤲 Help ⚙️ uml.png>)


<br/>


## Script

```yaml
📃 Help@Helper:

# Assert the message
- ASSERT|$.Msg:
    AllOf: Chat, Invite, Schema, Consumer
    UUIDs: Chat, Invite
    Schema.IsSchema:
    Consumer.IsDomain:

# Verify the signature
- VERIFY|$.Msg

# Check if the Broker is trustworthy
- TRUSTS|$.Msg.From:
    Schema: .BROKER

# Register the help request
- SAVE|Helper.Helps:
    .State: INVITED
    Chat: $.Msg.Chat
    Broker: $.Msg.From
    Schema: $.Msg.Schema
    Invite: $.Msg.Invite
    Consumer: $.Msg.Consumer
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |[`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE 📃 script.md>) [`TRUSTS`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Helper.Helps`](<../../🤲🪣 Helper tables/Helps 🤲 table/🪣 Helps/🤲 Helper.Helps 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsDomain`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsLanguage`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsLanguage ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`BROKER`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🧩 Broker schemas/🧩 BROKER.md>)
|