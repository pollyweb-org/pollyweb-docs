# 🤵 Identify@Broker 📃 handler

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Identify@Broker` 🐌 msg](<🤵 Identify 🐌 msg.md>).

<br/>


## Diagram

![alt text](<🤵 Identify ⚙️ uml.png>)

<br/>


## Script

```yaml
📃 Identify@Broker:

# Assert the required inputs
- ASSERT $.Msg:
    AllOf: Chat, Identifier, Biostamp, Identified
    UUIDs: Chat, Biostamp, Identified

# Verify the message
- VERIFY $.Msg

# Get the Chatter
- READ >> $chatter:
    Set: Broker.Chatters
    Key: 
        Chat: $.Msg.Chat
        Domain: $.Msg.From
    Assert:
        Chat.STATE: ACTIVE

# Ask for the Identifier verification
- INVITE:
    Chat: $.Msg.Chat
    Broker: $.Hosted.Domain
    Helper: $Identifier
    Schema: .ID/VERIFY
    Context: 
        Biostamp: $.Msg.Biostamp

# Send the Identified@Consumer message
- SEND:
    Header: 
        To: $.Msg.From
        Subject: Identified@Consumer
    Body:
        Identified: $.Msg.Identified
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSESS`](<../../🤵⏩ Broker flows/Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>) [`INVITE`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INVITE 🤲/🤲 INVITE ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) |  [`Broker.Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) 
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`$.Hosted`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Identified@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Identified 🤵🐌💼/💼 Identified 🐌 msg.md>)
|