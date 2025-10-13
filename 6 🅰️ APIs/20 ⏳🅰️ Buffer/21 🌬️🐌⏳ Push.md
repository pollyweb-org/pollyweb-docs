# 🌬️🐌⏳ Push @ Buffer

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/76  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) flow

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
|Header|`From` | string | [Streamer 🌬️ domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Push@Buffer`
|Body| `Subscriber`| string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) name
|| `Queue`| uuid | Queue from [`Queue@Buffer`](<12 🔔🐌⏳ Queue.md>)
| | `Message`| string | [Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) encrypted with the [DKIM 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) and encoded in Base64
|