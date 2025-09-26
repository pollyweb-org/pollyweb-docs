# 🌬️⏩🔔 Consume @ Subscriber


> **Privacy**: When [Streamers 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) send messages to a [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>), [Streamers 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) encrypt the messages with the public key of the [🔔 Subscriber](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>),  ensuring that only the [🔔 Subscriber](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>) can decrypt them with the private key.


## Flow diagram

![Subscribe](<⚙️🌬️ Ingest.png>)


| # | Call | Notes
|-|-|-
| 1 | [🌬️🐌⏳ Updated @ Buffer](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/02 🌬️🐌Updated.md>) | The [Streamer 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) pushes to the [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>)
| 2 | [⏳🐌💼 Wake-up @ Consumer](<../../6 🅰️ APIs/87 🔔🅰️ Subscriber/04 ⏳🐌🔔 Wake-up.md>) | The [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) wakes up the [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) 
| 3 | [💼🐌⏳ Consume @ Buffer](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/04 👥🐌Consume.md>) | The [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) pulls all buffered messages
||

