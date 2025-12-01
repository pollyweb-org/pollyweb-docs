# 💼🐌🤵 Inform @ Broker

> About
* Part of the [`Inform` ⏩ flow](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)
* Implemented by the [`Inform` 📃 handler](<🤵 Inform 📃 handler.md>)

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
    Hook: <hook-uuid>
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>)  | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | [`Informed@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Informed 🤵🐌💼/💼 Informed 🐌 msg.md>)
||`To`|string  | [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` |text| `Inform@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Form` |text| Form key || [`Form@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Form/🕸 Form 🚀 call.md>)
||`Hook`  | uuid    | Hook || [`Informed@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Informed 🤵🐌💼/💼 Informed 🐌 msg.md>)
|
