# 🔔🐌⏳ Redrive @ Buffer

> Replays all messages in the dead-letter-queue.

> Implements a [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>)

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-subscriber.dom
    To: any-buffer.dom
    Subject: Redrive@Buffer
Body:
    Queue: <queue-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|text| [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) name
||`To`|text| [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>) name
||`Subject`|text| `Replay@Buffer`
|Body| `Queue`| uuid | Queue from [`Queue@Buffer`](<🔔🐌⏳ Queue.md>) |
|