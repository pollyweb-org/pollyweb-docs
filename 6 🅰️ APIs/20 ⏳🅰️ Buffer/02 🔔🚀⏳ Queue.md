# 🔔🚀⏳ Queue

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/78  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>)


<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-subscriber.com
    To: any-buffer.com
    Subject: Queue@Buffer
Body:
    Fifo: True
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Queue@Buffer`
|Body | `Queue`| uuid | Queue ID for [Push @ Buffer 🐌](<11 🌬️🐌⏳ Push.md>)
|| `Fifo` | bool | First-in-first-out?
|


## Synchronous Response

```yaml
Queue: UUID
```

|Object|Property|Type|Description
|-|-|-|-
| Top | `Queue` | uuid | Queue ID for [Push @ Buffer 🐌](<11 🌬️🐌⏳ Push.md>)
|