# 🔔🚀⏳ Confirm @ Buffer

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/45 Helpers/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/76  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) flow

> Referenced by [Poll @ Buffer 🔔🚀](<22 🔔🚀⏳ Poll.md>)

> Needs to be synchronous for FIFO performance.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-subscriber.com
    To: any-buffer.com
    Subject: Confirm@Buffer
Body:
    Poll: <poll-uuid>
    Messages: 
        - <message-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/45 Helpers/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Confirm@Buffer`
|Body | `Poll` | uuid | Confirmed Poll (optional)
|| `Messages`| uuid[] | Confirmed Messages (optional)
|

<br/>

## Synchronous Response

```yaml
# empty
```
