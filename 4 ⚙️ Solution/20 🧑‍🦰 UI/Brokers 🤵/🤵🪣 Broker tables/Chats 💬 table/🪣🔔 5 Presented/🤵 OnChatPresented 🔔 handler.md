# 🤵 OnChatPresented 📃 handler

> Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that adds the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) to the [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)

<br/>  

## Diagram

![alt text](<🤵 OnChatPresented ⚙️ uml.png>)


## Script

```yaml
📃 OnChatPresented:

# Add the Broker to the chat
- SAVE|Broker.Chatters:
    .State: BROKER
    Chat: $Chat.ID
    Domain: $.Hosted.Domain
    Role: VAULT
```


|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Hello@Host` 🅰️ method](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|