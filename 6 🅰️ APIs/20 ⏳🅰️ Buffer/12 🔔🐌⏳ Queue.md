# 🔔🐌⏳ Queue @ Buffer

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/76  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) flow
> <br/>• Succeeded by [`Queued@Subscriber`](<../87 🔔🅰️ Subscriber/01 ⏳🐌🔔 Queued.md>)


<br/>

## Async Message 🐌

```yaml
Header:
    From: any-subscriber.com
    To: any-buffer.com
    Subject: Queue@Buffer
Body:
    Queue: <queue-uuid>
    Fifo: True          # Optional, False by default
    DLQ: True           # Optional, False by default
    Replay: True        # Optional, False by default
    Visibility: 30      # Optional, 30 seconds default
    Lifetime: 345600    # Optional, 3 days default
    Retries: 3          # Optional, only with DLQ
    Batch: 1            # Optional, 1 by default
```


|Object|Property|Type|Description|Default
|-|-|-|-|-
|Header|`From` | string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/76 🔔 Subscribers/04 🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Queue@Buffer`
|Body |`Queue` | uuid | Queue for [`Push@Buffer`](<21 🌬️🐌⏳ Push.md>)
|| `Fifo` | bool | First in, first out? | No
|| `DLQ`| bool | With dead-letter queue? | No
|| `Replay` | bool | Store confirmed messages? | No
|| `Visibility`| int | Seconds to hide in-flight msgs |  30 sec
|| `Lifetime`| int | Seconds to keep pending msgs | 3 days
|| `Retries`| int | Max retries before move to DLQ |3
|| `Batch`| int | Max messages per Poll | 1
|

<br/>



## FAQ

1. **Why isn't the `Queue` uuid returned?**

    This allows a queue to be updated by sending the same uuid.

    ---
    <br/>

1. **Is the `Queue` used for at-least-once delivery?**
    
    No. NLWeb requests are already idempotent with the `Correlation` property of [Messages 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>)

    ---
    <br/>

1. **How to delete a queue?**

    Queues are reverted with [`Unqueue@Buffer`](<13 🔔🐌⏳ Unqueue.md>).

    ---
    <br/>