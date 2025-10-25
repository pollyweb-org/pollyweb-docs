# 💼🐌🤵 Inform @ Broker

> Part of the [Consumer Inform ⏩ flow](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Inform@Broker

Body:
    Chat: <chat-uuid>
    Form: AnyForm
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) name
||`To`       | string  | [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Subject` | string | `Inform@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Form` | string | Form key for [`Form@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Form.md>)
|