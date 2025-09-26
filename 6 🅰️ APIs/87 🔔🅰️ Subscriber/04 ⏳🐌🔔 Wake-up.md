# ⏳🐌🔔 Wake-up @ Subscriber

> Implements the [Subscriber 🔔 domain role](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/78  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-buffer.com
    To: any-subscriber.com
    Subject: Wake-up@Subscriber
```

|Object|Property|Type|Description
|-|-|-|-
|`Header`| `From`| string | [Buffer ⏳ domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
|| `To`| string | [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) name
|| `Subject` | string | `Wake-up@Subscriber`
|