# 🔔🐌🌬️ Subscribe @ Streamer

## Async Message 🐌


```yaml
Header:
    From: any-subscriber.com
    To: any-streamer.com
    Subject: Register@Streamer
Body:
    Buffer: any-buffer.com
    Queue: <queue-uuid>
    Filters: 
        Property1: Value1
        Property2: Value2
```

|Object|Property|Type|Description
|-|-|-|-
|`Header`| `From`| string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) name
|| `To`| string | [Streamer 🌬️ domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) name
|| `Subject` | string | `Subscribe@Streamer`
|Body | `Buffer`| string | [Buffer ⏳ domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
|| `Queue` | UUID | Callback for [Push@Buffer 🐌](<../20 ⏳🅰️ Buffer/02 🌬️🐌⏳ Push.md>)
|| `Filters`| map | Dictionary of filters
|