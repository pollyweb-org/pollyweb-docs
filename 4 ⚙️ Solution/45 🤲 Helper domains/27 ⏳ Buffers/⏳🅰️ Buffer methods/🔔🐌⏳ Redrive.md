# 🔔🐌⏳ Redrive @ Buffer

> Replays all messages in the dead-letter-queue.

> Implements a [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>)

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
|Header|`From` | string | [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/76 🔔 Subscribers/🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>) name
||`Subject`| string | `Replay@Buffer`
|Body| `Queue`| uuid | Queue from [`Queue@Buffer`](<🔔🐌⏳ Queue.md>) |
|