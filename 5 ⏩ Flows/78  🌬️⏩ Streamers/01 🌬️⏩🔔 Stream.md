# 🌬️⏩🔔 Stream @ Streamer

> Used by [Manifest @ Domain 👥⏩🕸](<../30 👥⏩ Domains/04 👥⏩🕸 Manifest.md>)

> **Privacy**: When [Streamer 🌬️ domains](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) send messages to a [Buffer ⏳ domains](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>), the [Streamer 🌬️ domains](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) encrypt the messages with the public key of the [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>),  ensuring that only the [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) can decrypt them with the private key.

<br/>

## Flow diagram

![Subscribe](<⚙️🌬️ Ingest.png>)


| # | Call | Notes
|-|-|-
| 0 | [🔔🐌🌬️ Subscribe @ Streamer](<../../6 🅰️ APIs/86 🌬️🅰️ Streamer/01 🔔🐌🌬️ Subscribe.md>) | The [Subscriber 🔔](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) subscribes to a stream.
| 1 | [🌬️🐌⏳ Push @ Buffer](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/02 🌬️🐌⏳ Push.md>) | The [Streamer 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) pushes to the [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>).
| 2 | [⏳🐌🔔 Wake-up @ Subscriber](<../../6 🅰️ APIs/87 🔔🅰️ Subscriber/04 ⏳🐌🔔 Wake-up.md>) | The [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) wakes up the [Subscriber 🔔](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>).
| 3 | [🔔🚀⏳ Poll @ Buffer](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/04 🔔🚀⏳ Poll.md>) | The [Subscriber 🔔](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) polls all buffered messages.
|4| [🔔🚀⏳ Confirm @ Buffer](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/05 🔔🚀⏳ Confirm.md>) | The [Subscriber 🔔](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) confirms the processed ones.
||

