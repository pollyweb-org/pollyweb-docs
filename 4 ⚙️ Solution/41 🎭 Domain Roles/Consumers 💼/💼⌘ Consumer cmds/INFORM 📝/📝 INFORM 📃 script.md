# 📝 INFORM 📃 script

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements [`INFORM`](<📝 INFORM ⌘ cmd.md>) command.

<br/>

# Flow

![alt text](<📝 INFORM ⚙️ uml.png>)

## How to run?

```yaml
- RUN|.INFORM:
    Form: AnyKey
```

## Script

```yaml
📃 .INFORM:

# Assert inputs
- ASSERT|$.Inputs:
    AllOf: Form
    Texts: Form

# Send the INFORM message
- SEND:
    Header:
        To: $.Chat.Broker
        Subject: Inform@Broker
    Body:
        Chat: $.Chat.ID
        Form: $Form
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Inform@Broker` 🐌 msg](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)
| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>)  [`$.Inputs`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|