# ⏳🐌🔔 Wake-up @ Subscriber

> Implements the [Subscriber 🔔 domain role](<../🔔 Subscriber/🔔🎭 Subscriber role.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../Streamers 🌬️/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream/🌬️⏩🔔 Stream.md>) flow

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-buffer.dom
    To: any-subscriber.dom
    Subject: Wake-up@Subscriber
Body:
    
```

|Object|Property|Type|Description
|-|-|-|-
|`Header`|`From`|text| [Buffer ⏳](<../../../45 🤲 Helper domains/Buffers ⏳/⏳ Buffer/⏳🤲 Buffer helper.md>) from [`Queue@Buffer`](<../../../45 🤲 Helper domains/Buffers ⏳/⏳📨 Buffer msgs/🔔🐌⏳ Queue.md>)
||`To`|text| [Subscriber 🔔](<../🔔 Subscriber/🔔🎭 Subscriber role.md>) from [`Queue@Buffer`](<../../../45 🤲 Helper domains/Buffers ⏳/⏳📨 Buffer msgs/🔔🐌⏳ Queue.md>)
|| `Subject` |text| `Wake-up@Subscriber`
|
