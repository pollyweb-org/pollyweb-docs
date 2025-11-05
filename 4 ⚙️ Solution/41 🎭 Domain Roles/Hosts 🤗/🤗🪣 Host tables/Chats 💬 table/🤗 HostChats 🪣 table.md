# 🤗🪣 Chats @ Host

> Part of [Host 🤗 domain role](<../../🤗 Host role/🤗🎭 Host role.md>)

> Stores the content of [`Hello@Host`](<../../🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)

<br/>

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

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Chats.yaml
Name: Chats
Key: Broker, Chat
```
