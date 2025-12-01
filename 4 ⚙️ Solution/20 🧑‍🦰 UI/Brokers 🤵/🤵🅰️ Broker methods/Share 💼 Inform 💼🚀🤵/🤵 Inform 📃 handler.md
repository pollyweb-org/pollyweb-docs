# 🤵 Inform@Broker 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Inform@Broker` 🅰️ method](<🤵 Inform 🐌 msg.md>).

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

# Call Form@Graph
- SEND >> $form:
    Header: 
        To: $.Hosted.Graph
        Subject: Form@Graph
    Body:
        Form: $.Msg.Form
        Domain: $.Msg.From
        Language: $chatter.Chat.Language

# Inform the user
- INFO: 
    Text: ...

# Ask for confirmation to proceed
- CONFIRM|Ready to continue?

# Tell the consumer to proceed
- SEND:
    Header: 
        To: $.Msg.From
        Subject: Informed@Consumer
    Body:
        Hook: $.Msg.Hook
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSESS`](<../../🤵⏩ Broker flows/Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>) [`CONFIRM`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Broker.Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|