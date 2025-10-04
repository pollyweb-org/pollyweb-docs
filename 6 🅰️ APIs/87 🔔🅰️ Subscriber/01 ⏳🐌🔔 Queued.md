# ⏳🐌🔔 Queued @ Subscriber

> Implements the [Subscriber 🔔 domain role](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/78  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) flow
> <br/>• Preceded by [`Queue@Buffer`](<../20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>)


<br/>

## 🐌 Async Message


```yaml
Header:
    From: any-buffer.com
    To: any-subscriber.com
    Subject: Wake-up@Subscriber
Body:
    Queue: <queue-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|`Header`| `From`| string | [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) from [`Queue@Buffer`](<../20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>)
|| `To`| string | [Subscriber 🔔](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) from [`Queue@Buffer`](<../20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>)
|| `Subject` | string | `Queued@Subscriber`
|Body | `Queue`| uuid | Queue from [`Queue@Buffer`](<../20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>)
|
