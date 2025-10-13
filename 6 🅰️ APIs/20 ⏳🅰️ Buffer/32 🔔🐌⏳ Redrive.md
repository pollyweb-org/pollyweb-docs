# 🔔🐌⏳ Redrive @ Buffer

> Replays all messages in the dead-letter-queue.

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>)

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-subscriber.com
    To: any-buffer.com
    Subject: Redrive@Buffer
Body:
    Queue: <queue-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Replay@Buffer`
|Body| `Queue`| uuid | Queue from [`Queue@Buffer`](<12 🔔🐌⏳ Queue.md>) |
|