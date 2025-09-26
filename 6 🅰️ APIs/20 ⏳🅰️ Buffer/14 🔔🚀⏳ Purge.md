# 🌬️🚀⏳ Purge @ Buffer

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>)

> Removes all messages from the Queue create on [Queue @ Buffer](<12 🔔🚀⏳ Queue.md>).

<br/> 

## Synchronous Request 🚀

```yaml
Header:
    From: any-subscriber.com
    To: any-buffer.com
    Subject: Purge@Buffer
Body:
    Queue: <queue-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) name name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Purge@Buffer`
|Body|`Queue`| uuid | Queue from [Queue @ Buffer](<12 🔔🚀⏳ Queue.md>)
|


<br/>

## Synchronous Response

```yaml
# empty
```
