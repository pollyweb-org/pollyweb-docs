# 🤗 Informed@Host 🐌 msg

> About
* Part of the [💼 `Inform` ⏩ flow](<../../💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)

<br/>

## Asynchronous Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-host.dom
    Subject: Informed@Host
    
Body:
    Hook: <hook-uuid>
```

|Object|Property|Type|Description | Origin
|-|-|-|-|-
| Header    |`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Inform@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)
|           |`To`|text| [Host 🤗](<../../../Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | [`Emojied@`](<../../../Hosts 🤗/🤗📨 Host msgs/Emojied 🤵🐌🤗/🤗 Emojied 🐌 msg.md>)
|           | `Subject`     | string    | `Informed@Host`
| Body      | `Hook`      | uuid      | Hook | [`Inform@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)
|