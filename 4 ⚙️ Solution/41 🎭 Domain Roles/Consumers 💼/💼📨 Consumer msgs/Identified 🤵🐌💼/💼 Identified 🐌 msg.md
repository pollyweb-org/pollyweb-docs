# 🤗 Identified@Host 🐌 msg

> About
* Implemented by the [`Identified` 📃 handler](<💼 Identified 📃 handler.md>)

<br/>

## Asynchronous Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-consumer.dom
    Subject: Identified@Consumer
    
Body:
    Identified: <hook-uuid>
```

|Object|Property|Type|Description | Origin
|-|-|-|-|-
| Header    |`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Identify@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Identify 💼🐌🤵/🤵 Identify 🐌 msg.md>)
|           |`To`|text| [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>) | [`Identify@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Identify 💼🐌🤵/🤵 Identify 🐌 msg.md>)
|           | `Subject`     | string    | `Identified@Consumer`
| Body      | `Identified`      | uuid      | [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>) hook | [`Identify@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Identify 💼🐌🤵/🤵 Identify 🐌 msg.md>)
|