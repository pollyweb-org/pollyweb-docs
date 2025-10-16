# 💼🐌🤵 Inform @ Broker

> Part of the [Consumer Inform ⏩ flow](<../../../../41 🎭 Domain Roles/27 💼 Consumers/💼⏩ Consumer flows/💼⏩🧑‍🦰 Inform 📝.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-consumer.com
    To: any-broker.com
    Subject: Inform@Broker

Body:
    ChatID: <chat-uuid>
    Form: AnyForm
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) name
||`To`       | string  | [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Hello@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Subject` | string | `Inform@Broker`
|Body|`ChatID`   | uuid    | [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Form` | string | Form key for [`Form@Graph`](<../../../50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Form.md>)
|