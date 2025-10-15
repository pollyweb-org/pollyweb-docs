# 🔔🚀⏳ Poll @ Buffer

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/76  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) flow

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-subscriber.com
    To: any-buffer.com
    Subject: Poll@Buffer
Body:
    Queue: <queue-uuid>
    DLQ: False          # Optional, default False
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Poll@Buffer`
|Body| `Queue`| uuid | Queue from [`Queue@Buffer`](<12 🔔🐌⏳ Queue.md>)
|| `DLQ`| bool | From dead-letter-queue? 
|

<br/>

## Synchronous Response

```yaml
Poll: <poll-uuid>
Messages: 
    - ID: <message-uuid>
    - Content: <encrypted-message>
```

|Object|Property|Type|Description
|-|-|-|-
| Top | `Poll` | uuid | Poll ID for [`Confirm@Buffer`](<23 🔔🚀⏳ Confirm.md>)
||`Messages` | array | List of `Message` objects
| Message | `ID` | uuid | Message ID for [`Confirm@Buffer`](<23 🔔🚀⏳ Confirm.md>)
|| `Content` | string | [Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>) encrypted with the [DKIM 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) and encoded in Base64
|