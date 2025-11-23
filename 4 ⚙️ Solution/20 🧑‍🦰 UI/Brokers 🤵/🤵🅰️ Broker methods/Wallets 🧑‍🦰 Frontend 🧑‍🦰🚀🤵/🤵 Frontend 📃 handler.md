# 🤵📃 Frontend 🚀 Broker

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Frontend@Broker` 🅰️ method](<🤵 Frontend 🚀 call.md>).

## Flow

![alt text](<🤵 Frontend ⚙️ uml.png>)

## Script

```yaml
📃 Frontend@Broker:

- ASSERT|$.Msg:
    UUIDs: From

# Get the frontend item
- READ >> $frontend:
    Set: Broker.Frontend
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $frontend.PublicKey

# Return the frontend data
- RETURN|$frontend:
    Chats, Binds, Tokens
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|  [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Frontend`](<../../🤵🪣 Broker tables/Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)
|[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|