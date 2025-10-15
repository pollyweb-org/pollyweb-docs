# 🌬️⏩🔔 Stream @ Streamer

> Used by [Manifest @ Domain 👥⏩🕸](<../30 👥⏩ Domains/04 👥⏩🕸 Manifest 📜.md>)


<br/>

## Flow diagram

![Subscribe](<.📎 Assets/⚙️🌬️ Ingest.png>)


| # | Call | Notes
|-|-|-
|1| [🔔🚀⏳ `Queue@Buffer`](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>) | [Subscribers 🔔](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) create a [Buffer ⏳](<../../4 ⚙️ Solution/45 Helpers/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) queue
|2| [🔔🐌🌬️ `Subscribe@Streamer`](<../../6 🅰️ APIs/86 🌬️🅰️ Streamer/01 🔔🐌🌬️ Subscribe.md>) | [Subscribers 🔔](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) subscribe to [Streamers 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/02 🌬️🎭 Streamer role.md>)
| 3 | [🌬️🐌⏳ `Push@Buffer`](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/21 🌬️🐌⏳ Push.md>) | [Streamers 🌬️](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/02 🌬️🎭 Streamer role.md>) push to [Buffers ⏳](<../../4 ⚙️ Solution/45 Helpers/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>)
| 4 | [⏳🐌🔔 `Wake-up@Subscriber`](<../../6 🅰️ APIs/87 🔔🅰️ Subscriber/04 ⏳🐌🔔 Wake-up.md>) | [Buffers ⏳](<../../4 ⚙️ Solution/45 Helpers/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) wake up [Subscribers 🔔](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>)
| 5 | [🔔🚀⏳ `Poll@Buffer`](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/22 🔔🚀⏳ Poll.md>) | [Subscribers 🔔](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) poll all buffered messages
|6| [🔔🚀⏳ `Confirm@Buffer`](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/23 🔔🚀⏳ Confirm.md>) | [Subscribers 🔔](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) confirm processed ones
||

## FAQ

1. **Why an async request for [`Queue@Buffer`](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/12 🔔🐌⏳ Queue.md>) ?**

    `Timeout` `Cost`

    [Buffer ⏳ domains](<../../4 ⚙️ Solution/45 Helpers/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) may require additional time to resource the compute and store to handle the queue. 
    * [Buffer ⏳ domains](<../../4 ⚙️ Solution/45 Helpers/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) should not be pressured to speed up under a synchronous request.
    * [Subscriber 🔔 domains](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) should not spend compute cost waiting for a synchronous response that may time out.
    
    ---
    <br/>

1. **How is privacy the Subscriber protected on [`Push@Buffer`](<../../6 🅰️ APIs/20 ⏳🅰️ Buffer/21 🌬️🐌⏳ Push.md>)?**

    `Public-key encryption` 
    
    When [Streamer 🌬️ domains](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/02 🌬️🎭 Streamer role.md>) send messages to [Buffer ⏳ domains](<../../4 ⚙️ Solution/45 Helpers/15 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>), 
    * the [Streamer 🌬️ domains](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/02 🌬️🎭 Streamer role.md>) encrypt the messages with the public key of the [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>), ensuring that only the [Subscriber 🔔 domain](<../../4 ⚙️ Solution/40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>) can decrypt them with the private key.

    ---
    <br/>