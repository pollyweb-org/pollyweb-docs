# 🔔🐌🌬️ Unsubscribe @ Streamer

> Implements the [Streamer 🌬️ domain role](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>)


<br/>

## 🐌 Async Message


```yaml
Header:
    From: any-subscriber.com
    To: any-streamer.com
    Subject: Unsubscribe@Streamer
Body:
    Stream: ANY-STREAM
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) name
|| `To`| string | [Streamer 🌬️ domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) name
|| `Subject` | string | `Unsubscribe@Streamer`
|Body | `Stream`| string |  Stream key on the [Streamer 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>)
|