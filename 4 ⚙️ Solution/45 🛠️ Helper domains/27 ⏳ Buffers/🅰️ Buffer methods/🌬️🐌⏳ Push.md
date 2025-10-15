# 🌬️🐌⏳ Push @ Buffer

> Implements a [Buffer ⏳ helper domain](<../⏳🛠️ Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../../41 🎭 Domain Roles/75 🌬️ Streamers/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream.md>) flow

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-streamer.com
    To: any-buffer.com
    Subject: Push@Buffer
Body:
    Subscriber: any-subscriber.com
    Queue: <queue-uuid>
    Message: <encrypted-content>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Streamer 🌬️ domain](<../../../41 🎭 Domain Roles/75 🌬️ Streamers/🌬️🎭 Streamer role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Push@Buffer`
|Body| `Subscriber`| string | [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/76 🔔 Subscribers/🔔🎭 Subscriber role.md>) name
|| `Queue`| uuid | Queue from [`Queue@Buffer`](<🔔🐌⏳ Queue.md>)
| | `Message`| string | [Message 📨](<../../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>) encrypted with the [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/76 🔔 Subscribers/🔔🎭 Subscriber role.md>) and encoded in Base64
|