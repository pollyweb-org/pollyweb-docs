# ⏳🐌🔔 Wake-up @ Subscriber

> Implements the [Subscriber 🔔 domain role](<../🔔🎭 Subscriber role.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../75 🌬️ Streamers/01 🌬️⏩🔔 Stream.md>) flow

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-buffer.com
    To: any-subscriber.com
    Subject: Wake-up@Subscriber
From:
    
```

|Object|Property|Type|Description
|-|-|-|-
|`Header`| `From`| string | [Buffer ⏳](<../../../45 🛠️ Helper domains/27 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) from [`Queue@Buffer`](<../../../../6 🅰️ APIs/20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>)
|| `To`| string | [Subscriber 🔔](<../🔔🎭 Subscriber role.md>) from [`Queue@Buffer`](<../../../../6 🅰️ APIs/20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>)
|| `Subject` | string | `Wake-up@Subscriber`
|