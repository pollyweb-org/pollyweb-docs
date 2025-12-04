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

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header    |`From`|text| {{Helper}} | {{Invited@Helper}}
|           |`To`|text| [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>) | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|           | `Subject`     | string    | `Queried@Consumer`
| Body      | `Query`        | uuid      | Hook | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|           | `Schema`      | string    | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Trusts@`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>)
|

## Synchronous Response

```yaml
Context: {...}
```