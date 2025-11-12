# 🤗💬 Host.Chats 🪣 table

> Part of [Host 🤗 domain role](<../../🤗 Host role/🤗🎭 Host role.md>)

> Purpose
* Stores the content of [`Hello@Host`](<../../🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)

> Data access
* Saved by the [`CHAT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) command
* Loaded into the [`$.Chat` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Chats.yaml
Prefix: Host
Name: Chats
Key: Broker, Chat
```


## Example

Here's the [`READ` command](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Chats|<broker>,<chat-uuid>
Broker: any-broker.dom
Chat: <chat-uuid>
PublicKey: <public-key>
```

| Property | Type | Details
|-|-|-
| `Broker`  | string | 
| `Chat`    | uuid |
| `PublicKey` | string | From [`Hello@Host`](<../../🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| 

<br/>