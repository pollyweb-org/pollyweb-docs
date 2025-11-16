# 🔔🚀⏳ Confirm @ Buffer

> Implements a [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream/🌬️⏩🔔 Stream.md>) flow

> Referenced by [Poll @ Buffer 🔔🚀](<🔔🚀⏳ Poll.md>)

> Needs to be synchronous for FIFO performance.

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-subscriber.dom
    To: any-buffer.dom
    Subject: Confirm@Buffer
Body:
    Poll: <poll-uuid>
    Messages: 
        - <message-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|text| [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) name
||`To`|text| [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>) name
||`Subject`|text| `Confirm@Buffer`
|Body | `Poll` | uuid | Confirmed Poll (optional)
|| `Messages`| uuid[] | Confirmed Messages (optional)
|

<br/>

## Synchronous Response

```yaml
# empty
```
