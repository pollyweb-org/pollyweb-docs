# 🔔🐌⏳ Unqueue @ Buffer

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-subscriber.com
    To: any-buffer.com
    Subject: Unqueue@Buffer
Body:
    Queue: <queue-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/76 🔔 Subscribers/04 🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Unqueue@Buffer`
|Body | `Queue`| uuid | Queue from [`Queue@Buffer`](<12 🔔🐌⏳ Queue.md>)
|
