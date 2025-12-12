# 🤲 INVITE 📃 script

> About
* Implements the [`INVITE` ⌘ command](<🤲 INVITE ⌘ cmd.md>) for the [Consumer 💼 domain](<../../💼 Consumer/💼🎭 Consumer role.md>)

<br/>

## Diagram

![alt text](<🤲 INVITE ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .INVITE:
    Helper: any-helper.dom
    Schema: any-authority.dom/ANY-SCHEMA
    Context: {...}
```
Uses: [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)

<br/>

## Script

```yaml
📃 .INVITE:

# Default to $.Chat info
- DEFAULT $.Inputs:
    Broker: $.Chat.Broker
    Chat: $.Chat.ID

# Verify the inputs
- ASSERT $.Inputs:
    AllOf: Helper, Schema, Context, Broker, Chat
    UUIDs: Chat
    Texts: Broker, Helper, Schema
    Broker.IsDomain:
    Helper.IsDomain:
    Schema.IsSchema:

# Save the invite
- SAVE Consumer.Invites >> $invite:
    Broker: $.Chat.Broker
    Chat: $.Chat.ID
    Helper: $Domain
    Schema: $Schema
    Context: $Context

# Wait for Helped@Consumer
- WAIT >> $data:
    Hook: $invite.ID

# Return the received data
- RETURN: $data
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`WAIT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Invites`](<../../💼🪣 Consumer tables/Invites 🗄️ table/🪣 Invites/💼 Consumer.Invites 🪣 table.md>) 
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsDomain`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>) [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>)