# 🗄️🚀💼 Invited @ Consumer

> About
* Implements the [Consumer 💼 domain](<../../💼 Consumer/💼🎭 Consumer role.md>)
* Implemented by the [`Invited` 📃 handler](<💼 Invited 📃 handler.md>)

<br>

## Synchronous Call 🚀

```yaml
Header:
    From: any-vault.dom
    To: any-consumer.dom
    Subject: Invited@Consumer

Body:
    Invite: <invite-uuid>
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    |`From`|text| [Helper 🤲](<../../../Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) name | [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
|           |`To`|text| [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>) name | [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
|           | `Subject`     | string    | `Invited@Consumer`
| Body      | `Invite`        | uuid      | [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>)  hook | [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
|

<br/>

## Synchronous Response

```yaml
Context: {...}
```