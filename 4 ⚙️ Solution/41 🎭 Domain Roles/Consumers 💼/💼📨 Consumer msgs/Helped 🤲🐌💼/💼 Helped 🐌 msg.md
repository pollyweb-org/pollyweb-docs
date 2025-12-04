# 🧑‍🦰🐌💼 Helped @ Consumer

> About
* Implemented by the [`Helped` 📃 script](<💼 Helped 📃 handler.md>)



<br/>

## Async Message 🐌

```yaml
Header:
    From: any-helper.dom
    To: any-consumer.dom
    Subject: Helped@Consumer

Body: 
    Invite: <invite-uuid>
    Help: {data}
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    |`From`|text| [Helper 🤲](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲 Helper/🤲👥 Helper domain.md>) name | [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
|           |`To`|text| [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>) name | [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
|           | `Subject`     | string    | `Helped@Consumer`
| Body      | `Invite`        | uuid      | [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>)  hook | [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
|   | `Help` | any | Help data
|


