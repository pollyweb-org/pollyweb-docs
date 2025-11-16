# 🔔🐌🌬️ Subscribe @ Streamer

> Implements the [Streamer 🌬️ domain role](<../🌬️🎭 Streamer role.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../🌬️⏩ Streamer flows/🌬️⏩🔔 Stream/🌬️⏩🔔 Stream.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-subscriber.dom
    To: any-streamer.dom
    Subject: Subscribe@Streamer
Body:
    Stream: ANY-STREAM
    Buffer: any-buffer.dom
    Queue: <queue-uuid>
    Filters: 
        Property1: Value1
        Property2: Value2
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|text| [Subscriber 🔔 domain](<../../Subscribers 🔔/🔔🎭 Subscriber role.md>) name
||`To`|text| [Streamer 🌬️ domain](<../🌬️🎭 Streamer role.md>) name
|| `Subject` |text| `Subscribe@Streamer`
|Body | `Stream`|text| Stream key on the [Streamer 🌬️](<../🌬️🎭 Streamer role.md>)
|| `Buffer`|text| [Buffer ⏳ domain](<../../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) name
|| `Queue` | uuid | Callback for [Push@Buffer 🐌](<../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🌬️🐌⏳ Push.md>)
|| `Filters`| object | Dictionary of filters (optional)
|