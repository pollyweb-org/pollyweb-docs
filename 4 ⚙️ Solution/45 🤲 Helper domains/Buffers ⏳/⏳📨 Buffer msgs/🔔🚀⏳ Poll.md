# 🔔🚀⏳ Poll @ Buffer

> About
* Implements a [Buffer ⏳ helper domain](<../⏳ Buffer/⏳🤲 Buffer helper.md>)
* Used in [Stream @ Streamer 🌬️⏩🔔](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream/🌬️⏩🔔 Stream.md>) flow

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-subscriber.dom
    To: any-buffer.dom
    Subject: Poll@Buffer
    
Body:
    Queue: <queue-uuid>
    DLQ: False          # Optional, default False
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|text| [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔 Subscriber/🔔🎭 Subscriber role.md>) name
||`To`|text| [Buffer ⏳ helper domain](<../⏳ Buffer/⏳🤲 Buffer helper.md>) name
||`Subject`|text| `Poll@Buffer`
|Body| `Queue`| uuid | Queue from [`Queue@Buffer`](<🔔🐌⏳ Queue.md>)
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
| Top | `Poll` | uuid | Poll ID for [`Confirm@Buffer`](<🔔🚀⏳ Confirm.md>)
| Messages | `ID` | uuid | Message ID for [`Confirm@Buffer`](<🔔🚀⏳ Confirm.md>)
|| `Content` |text| [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) encrypted with the [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔 Subscriber/🔔🎭 Subscriber role.md>) and encoded in Base64
|