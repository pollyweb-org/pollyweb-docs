# 🤵 Inform@Broker 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Inform@Broker` 🅰️ method](<🤵 Inform 🐌 msg.md>).
* Part of the [`Inform` ⏩ flow](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)
* Adds a new Form request to the [`Broker.Forms` 🪣 table](<../../🤵🪣 Broker tables/Forms 📝 table/🪣 Forms/🤵 Broker.Forms 🪣 table.md>) in state `INFORM`.

<br/>

## Diagram

![alt text](<🤵 Inform ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Inform@Broker:

# Verify the message
- VERIFY|$.Msg

# Assert the required inputs
- ASSERT|$.Msg:
    AllOf: Chat, Hook, Form
    UUIDs: Chat, Hook
    Texts: Form

# Get the Chatter
- READ >> $chatter:
    Set: Broker.Chatters
    Key: 
        Chat: $.Msg.Chat
        Domain: $.Msg.From
    Assert:
        Chat.State: ACTIVE

# Save the request
- SAVE|Broker.Forms:
    $.Msg.Chat:
    $.Msg.Hook:
    $.Msg.Form:
    Consumer: $.Msg.From
    .State: INFORM
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSESS`](<../../🤵⏩ Broker flows/Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) |  [`Broker.Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Broker.Forms`](<../../🤵🪣 Broker tables/Forms 📝 table/🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|