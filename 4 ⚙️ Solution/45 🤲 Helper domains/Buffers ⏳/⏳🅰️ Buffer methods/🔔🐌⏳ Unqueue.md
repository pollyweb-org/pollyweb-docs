# 🔔🐌⏳ Unqueue @ Buffer

> Implements a [Buffer ⏳ helper domain](<../⏳ Buffer/⏳🤲 Buffer helper.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-subscriber.dom
    To: any-buffer.dom
    Subject: Unqueue@Buffer
Body:
    Queue: <queue-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|text| [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) name
||`To`|text| [Buffer ⏳ helper domain](<../⏳ Buffer/⏳🤲 Buffer helper.md>) name
||`Subject`|text| `Unqueue@Buffer`
|Body | `Queue`| uuid | Queue from [`Queue@Buffer`](<🔔🐌⏳ Queue.md>)
|
