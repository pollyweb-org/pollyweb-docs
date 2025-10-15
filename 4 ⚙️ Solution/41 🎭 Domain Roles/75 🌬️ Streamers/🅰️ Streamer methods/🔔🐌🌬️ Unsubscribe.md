# 🔔🐌🌬️ Unsubscribe @ Streamer

> Implements the [Streamer 🌬️ domain role](<../🌬️🎭 Streamer role.md>)


<br/>

## Async Message 🐌


```yaml
Header:
    From: any-subscriber.com
    To: any-streamer.com
    Subject: Unsubscribe@Streamer
Body:
    Stream: ANY-STREAM
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | [Subscriber 🔔 domain](<../../76 🔔 Subscribers/🔔🎭 Subscriber role.md>) name
|| `To`| string | [Streamer 🌬️ domain](<../🌬️🎭 Streamer role.md>) name
|| `Subject` | string | `Unsubscribe@Streamer`
|Body | `Stream`| string |  Stream key on the [Streamer 🌬️](<../🌬️🎭 Streamer role.md>)
|