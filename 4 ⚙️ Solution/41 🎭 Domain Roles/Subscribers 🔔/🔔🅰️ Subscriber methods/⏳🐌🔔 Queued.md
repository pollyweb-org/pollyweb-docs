# ⏳🐌🔔 Queued @ Subscriber

> Implements the [Subscriber 🔔 domain role](<../🔔🎭 Subscriber role.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../Streamers 🌬️/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream.md>) flow
> <br/>• Preceded by [`Queue@Buffer`](<../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🔔🐌⏳ Queue.md>)


<br/>

## Async Message 🐌


```yaml
Header:
    From: any-buffer.dom
    To: any-subscriber.dom
    Subject: Wake-up@Subscriber
Body:
    Queue: <queue-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|`Header`| `From`| string | [Buffer ⏳](<../../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) from [`Queue@Buffer`](<../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🔔🐌⏳ Queue.md>)
|| `To`| string | [Subscriber 🔔](<../🔔🎭 Subscriber role.md>) from [`Queue@Buffer`](<../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🔔🐌⏳ Queue.md>)
|| `Subject` | string | `Queued@Subscriber`
|Body | `Queue`| uuid | Queue from [`Queue@Buffer`](<../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🔔🐌⏳ Queue.md>)
|
