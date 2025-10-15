# 🔔🐌🌬️ Subscribe @ Streamer

> Implements the [Streamer 🌬️ domain role](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/02 🌬️🎭 Streamer role.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/76  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>)

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
|Header| `From`| string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) name
|| `To`| string | [Streamer 🌬️ domain](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/02 🌬️🎭 Streamer role.md>) name
|| `Subject` | string | `Subscribe@Streamer`
|Body | `Stream`| string | Stream key on the [Streamer 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/02 🌬️🎭 Streamer role.md>)
|| `Buffer`| string | [Buffer ⏳ domain](<../../4 ⚙️ Solution/45 Helpers/10 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) name
|| `Queue` | uuid | Callback for [Push@Buffer 🐌](<../20 ⏳🅰️ Buffer/21 🌬️🐌⏳ Push.md>)
|| `Filters`| object | Dictionary of filters (optional)
|