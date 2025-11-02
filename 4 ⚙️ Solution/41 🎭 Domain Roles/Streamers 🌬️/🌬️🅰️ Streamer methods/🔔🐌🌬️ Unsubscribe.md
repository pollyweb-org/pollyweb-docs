# 🔔🐌🌬️ Unsubscribe @ Streamer

> Implements the [Streamer 🌬️ domain role](<../🌬️🎭 Streamer role.md>)


<br/>

## Async Message 🐌


```yaml
Header:
    From: any-subscriber.dom
    To: any-streamer.dom
    Subject: Unsubscribe@Streamer
Body:
    Stream: ANY-STREAM
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|domain| [Subscriber 🔔 domain](<../../Subscribers 🔔/🔔🎭 Subscriber role.md>) name
||`To`|domain| [Streamer 🌬️ domain](<../🌬️🎭 Streamer role.md>) name
|| `Subject` | string | `Unsubscribe@Streamer`
|Body | `Stream`| string |  Stream key on the [Streamer 🌬️](<../🌬️🎭 Streamer role.md>)
|