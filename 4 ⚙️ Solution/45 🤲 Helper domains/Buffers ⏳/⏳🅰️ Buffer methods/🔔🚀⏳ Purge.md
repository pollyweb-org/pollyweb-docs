# 🌬️🚀⏳ Purge @ Buffer

> Implements a [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>)

> Removes all messages from the Queue create on [`Queue@Buffer`](<🔔🐌⏳ Queue.md>).

<br/> 

## Synchronous Call 🚀

```yaml
Header:
    From: any-subscriber.dom
    To: any-buffer.dom
    Subject: Purge@Buffer
Body:
    Queue: <queue-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string| [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) name name
||`To`|string| [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>) name
||`Subject`| string | `Purge@Buffer`
|Body|`Queue`| uuid | Queue from [`Queue@Buffer`](<🔔🐌⏳ Queue.md>)
|


<br/>

## Synchronous Response

```yaml
# empty
```
