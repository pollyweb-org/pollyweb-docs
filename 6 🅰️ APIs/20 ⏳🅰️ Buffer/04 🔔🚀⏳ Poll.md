# 🔔🚀⏳ Poll @ Buffer

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/78  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>)

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-subscriber.com
    To: any-buffer.com
    Subject: Poll@Buffer
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Poll@Buffer`
|

<br/>

## Synchronous Response

```yaml
PollID: <poll-uuid>
Messages: 
    - MessageID: <message-uuid>
    - Message: <encrypted-message>
```

|Object|Property|Type|Description
|-|-|-|-
| Top | `PollID` | UUID | Poll ID for [Confirm@Buffer 🚀](<05 🔔🚀⏳ Confirm.md>).
||`Messages` | list | List of Message objects.
| Message | `MessageID` | UUID | Message ID for [Confirm@Buffer 🚀](<05 🔔🚀⏳ Confirm.md>).
|| `Message` | string | [Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) encrypted with the [DKIM 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) and encoded in Base64.
|