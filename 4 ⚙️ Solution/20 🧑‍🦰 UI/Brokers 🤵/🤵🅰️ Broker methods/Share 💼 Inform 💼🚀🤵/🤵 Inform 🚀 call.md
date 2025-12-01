<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

# 💼🚀🤵 Inform @ Broker

> About
* Part of the [Consumer Inform ⏩ flow](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)

<br/>

## Synchronous Call 🚀

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
|Header|`From`|text| [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>)  | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`|string  | [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` |text| `Inform@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Form` |text| Form key || [`Form@`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Form/🕸 Form 🚀 call.md>)
|

## FAQ

1. **Why not an asynchronous message 🐌?**
   
    This has to be a blocking call,
    * otherwise the subsequent [`Bind@Broker` 🅰️ method](<../Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>) and [`Query@Broker` 🅰️ method](<../Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) calls may fail if the [`Inform@Broker` 🅰️ method](<🤵 Inform 🚀 call.md>) hasn't been processed yet.

    ---
    <br/>