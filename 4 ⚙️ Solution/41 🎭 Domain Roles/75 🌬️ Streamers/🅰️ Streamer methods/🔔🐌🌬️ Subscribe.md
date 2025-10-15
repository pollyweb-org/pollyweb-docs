# 🔔🐌🌬️ Subscribe @ Streamer

> Implements the [Streamer 🌬️ domain role](<../🌬️🎭 Streamer role.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../⏩ Streamer flows/🌬️⏩🔔 Stream.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-subscriber.com
    To: any-streamer.com
    Subject: Subscribe@Streamer
Body:
    Stream: ANY-STREAM
    Buffer: any-buffer.com
    Queue: <queue-uuid>
    Filters: 
        Property1: Value1
        Property2: Value2
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | [Subscriber 🔔 domain](<../../76 🔔 Subscribers/🔔🎭 Subscriber role.md>) name
|| `To`| string | [Streamer 🌬️ domain](<../🌬️🎭 Streamer role.md>) name
|| `Subject` | string | `Subscribe@Streamer`
|Body | `Stream`| string | Stream key on the [Streamer 🌬️](<../🌬️🎭 Streamer role.md>)
|| `Buffer`| string | [Buffer ⏳ domain](<../../../45 🛠️ Helper domains/27 ⏳ Buffers/⏳🛠️ Buffer helper.md>) name
|| `Queue` | uuid | Callback for [Push@Buffer 🐌](<../../../45 🛠️ Helper domains/27 ⏳ Buffers/🅰️ Buffer methods/🌬️🐌⏳ Push.md>)
|| `Filters`| object | Dictionary of filters (optional)
|