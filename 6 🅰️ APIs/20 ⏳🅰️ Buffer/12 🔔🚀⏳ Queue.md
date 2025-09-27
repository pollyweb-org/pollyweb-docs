# 🔔🚀⏳ Queue @ Buffer

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/78  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>)

> Reverted by [Unqueue @ Queue 🚀](<13 🔔🚀⏳ Unqueue.md>)

> To update a queue, re-use the `<queue-uuid>`

<br/>

## Synchronous Request 🚀

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
    Lifetime: 345600    # Optional, 4 days default
    Retries: 3          # Optional, only with DLQ
    Batch: 1            # Optional, 1 by default
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Queue@Buffer`
|Body |`Queue` | uuid | Queue for [Push @ Buffer](<21 🌬️🐌⏳ Push.md>)
|| `Fifo` | bool | Optional first in, first out? 
|| `DLQ`| bool | Optional dead-letter queue? 
|| `Replay` | bool | Optional store of confirmed messages
|| `Visibility`| int | Seconds to hide in-flight messages:<br/> - 30 seconds by default
|| `Lifetime`| int | Seconds to keep pending messages:<br/>- defaults to 4 days
|| `Retries`| int | Maximum retries before move to DLQ:<br/> - defaults to 3
|| `Batch`| int | Maximum messages per Poll:<br/>- defaults to 1
|

<br/>

## Synchronous Response

```yaml
# empty
```
