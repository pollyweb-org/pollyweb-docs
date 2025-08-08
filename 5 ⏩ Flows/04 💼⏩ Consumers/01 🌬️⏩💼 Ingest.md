# 🌬️⏩💼 Ingest @ [Consumer](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 💼 Consumers/04 💼🎭 Consumer role.md>)


## Privacy

- When [Streamers 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) send messages to a [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳👥 Buffer helper.md>)
    - [Streamers 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) encrypt the messages with the public key of the [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 💼 Consumers/04 💼🎭 Consumer role.md>)
    - ensuring that only the [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 💼 Consumers/04 💼🎭 Consumer role.md>) can decrypt them with the private key.


## Steps

| # | Call | Notes
|-|-|-
| 1 | [🌬️🐌⏳ Updated @ Buffer](<../../6 🅰️ APIs/03 ⏳🅰️  Buffer/02 🌬️🐌⏳ Updated.md>) | The [Streamer 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) pushes to the [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳👥 Buffer helper.md>)
| 2 | [⏳🐌💼 Wake-up @ Consumer](<../../6 🅰️ APIs/05 💼🅰️ Consumer/04 ⏳🐌💼 Wake-up.md>) | The [Buffer ⏳](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳👥 Buffer helper.md>) wakes up the [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 💼 Consumers/04 💼🎭 Consumer role.md>) 
| 3 | [💼🐌⏳ Consume @ Buffer](<../../6 🅰️ APIs/03 ⏳🅰️  Buffer/03 💼🐌⏳ Consume.md>) | The [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 💼 Consumers/04 💼🎭 Consumer role.md>) pulls all buffered messages
||


## Flow diagram

![Subscribe](<📎 Assets/⚙️🌬️ Ingest.png>)