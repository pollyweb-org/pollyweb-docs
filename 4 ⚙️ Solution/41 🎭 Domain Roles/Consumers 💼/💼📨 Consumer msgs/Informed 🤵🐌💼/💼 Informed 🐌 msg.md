# 🤗 Informed@Host 🐌 msg

> About
* Part of the [💼 `Inform` ⏩ flow](<../../💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)

<br/>

## Asynchronous Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-consumer.dom
    Subject: Informed@Consumer
    
Body:
    Hook: <hook-uuid>
```

|Object|Property|Type|Description | Origin
|-|-|-|-|-
| Header    |`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | [`Inform@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)
|           |`To`|text| [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>) | [`Inform@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)
|           | `Subject`     | string    | `Informed@Consumer`
| Body      | `Hook`      | uuid      | Hook | [`Inform@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)
|