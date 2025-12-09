# 🌬️🐌⏳ Push @ Buffer

> About
* Implements a [Buffer ⏳ helper domain](<../⏳ Buffer/⏳🤲 Buffer helper.md>)
* Used in [Stream @ Streamer 🌬️⏩🔔](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream/🌬️⏩🔔 Stream.md>) flow

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-streamer.dom
    To: any-buffer.dom
    Subject: Push@Buffer
    
Body:
    Subscriber: any-subscriber.dom
    Queue: <queue-uuid>
    Message: <encrypted-content>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|text| [Streamer 🌬️ domain](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) name
||`To`|text| [Buffer ⏳ helper domain](<../⏳ Buffer/⏳🤲 Buffer helper.md>) name
||`Subject`|text| `Push@Buffer`
|Body| `Subscriber`|text| [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔 Subscriber/🔔🎭 Subscriber role.md>) name
|| `Queue`| uuid | Queue from [`Queue@Buffer`](<🔔🐌⏳ Queue.md>)
| | `Message`|text| [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) encrypted with the [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔 Subscriber/🔔🎭 Subscriber role.md>) and encoded in Base64
|