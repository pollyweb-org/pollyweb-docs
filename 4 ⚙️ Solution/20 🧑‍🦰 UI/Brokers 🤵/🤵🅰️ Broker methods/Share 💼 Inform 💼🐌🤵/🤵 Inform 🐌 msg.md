<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

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

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|string| [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)  | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`|string  | [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` | string | `Inform@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Form` | string | Form key || [`Form@`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Form/👥🚀🕸 Form.md>)
|