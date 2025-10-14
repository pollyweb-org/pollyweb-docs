# ⏳🐌🔔 Wake-up @ Subscriber

> Implements the [Subscriber 🔔 domain role](<../../4 ⚙️ Solution/40 👥 Domains/42 Events/04 🔔🎭 Subscriber role.md>)

> Used in [Stream @ Streamer 🌬️⏩🔔](<../../5 ⏩ Flows/76  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) flow

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-buffer.com
    To: any-subscriber.com
    Subject: Wake-up@Subscriber
From:
    
```

|Object|Property|Type|Description
|-|-|-|-
|`Header`| `From`| string | [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/42 Events/03 ⏳🛠️ Buffer helper.md>) from [`Queue@Buffer`](<../20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>)
|| `To`| string | [Subscriber 🔔](<../../4 ⚙️ Solution/40 👥 Domains/42 Events/04 🔔🎭 Subscriber role.md>) from [`Queue@Buffer`](<../20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>)
|| `Subject` | string | `Wake-up@Subscriber`
|