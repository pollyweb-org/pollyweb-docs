# 🔔🚀⏳ Confirm @ Buffer

> Implements a [Buffer ⏳ helper domain](<../⏳🛠️ Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../../41 🎭 Domain Roles/75 🌬️ Streamers/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream.md>) flow

> Referenced by [Poll @ Buffer 🔔🚀](<🔔🚀⏳ Poll.md>)

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
|Header|`From` | string | [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/76 🔔 Subscribers/🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Confirm@Buffer`
|Body | `Poll` | uuid | Confirmed Poll (optional)
|| `Messages`| uuid[] | Confirmed Messages (optional)
|

<br/>

## Synchronous Response

```yaml
# empty
```
