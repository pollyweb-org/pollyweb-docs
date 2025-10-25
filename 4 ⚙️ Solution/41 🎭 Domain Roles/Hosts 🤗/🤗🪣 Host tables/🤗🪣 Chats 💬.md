# 🤗🪣 Chats @ Host

> Part of [Host 🤗 domain role](<../🤗🎭 Host role.md>)

> Stores the content of [`Hello@Host`](<../🤗🅰️ Host methods/🤵🐌🤗 Hello/🤗 Hello 🐌 msg.md>)

<br/>

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) result.

```yaml
# GET|Chats|<broker>,<chat-uuid>
Broker: any-broker.dom
Chat: <chat-uuid>
PublicKey: <public-key>
```

| Property | Type | Details
|-|-|-
| `Broker`  | string | 
| `Chat`    | uuid |
| `PublicKey` | string | From [`Hello@Host`](<../🤗🅰️ Host methods/🤵🐌🤗 Hello/🤗 Hello 🐌 msg.md>)
| 

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Chats.yaml
Name: Chats
Key: Broker, Chat
```
