# 🆔 IDENTITY 📃 script

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`IDENTITY`](<🆔 IDENTIFY ⌘ cmd.md>) command.

<br/>


## Diagram

![alt text](<🆔 IDENTIFY ⚙️ uml.png>)

<br/>


## How to call

```yaml
- RUN .IDENTITY:
    Identity: any-identity.dom
    Biostamp: <biostamp-uuid>
```

<br/>


## Script

```yaml
📃 .IDENTITY:

# Assert the chat and identity inputs
- ASSERT $.Inputs:
    AllOf: $.Chat, Identity, Biostamp
    UUIDs: Biostamp
    Identity.IsDomain:

# Set a hook for the Identified@Consumer message
- PUT: .UUID >> $hook

# Send the Identify@Broker msg
- SEND:
    Header:
        To: $.Chat.Broker
        Subject: Identify@Broker
    Body:
        Chat: $.Chat.Chat
        Identity: $Identity
        Biostamp: $Biostamp
        Identified: $hook

# Wait for the Identified@Consumer msg
- WAIT: $hook
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`WAIT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsDomain`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.UUID`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/UUID ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Inputs`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>) 
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Identify@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Identify 💼🐌🤵/🤵 Identify 🐌 msg.md>) 