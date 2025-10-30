# 📝 INFORM 📃 script

> Purpose
* [Script 📃](<../../📃 commands ⌘/Script 📃/📃 Script.md>) that implements [`INFORM`](<📝 INFORM ⌘ cmd.md>) command.

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
        Chat: $.Chat.Chat
        Form: $:Form
```

Needs||
|-|-
| [Commands ⌘](<../../📃 commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Inform@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)
| [Holder 🧠](<../../📃 holders 🧠/$Holder 🧠.md>) | [`.Chat`](<../../📃 holders 🧠/$.Chat 💬/💬 $.Chat 🧠 holder.md>)
|