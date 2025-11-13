# 🌬️⏩🔔 Stream @ Streamer

> Used by [Manifest @ Domain 👥⏩🕸](<../../../../40 👥 Domains/👥⏩ Domain flows/Manifest 👥📜🕸/👥 Manifest ⏩ flow.md>)


<br/>

## Flow diagram

![Subscribe](<../../.📎 Assets/⚙️🌬️ Ingest.png>)


| # | Call | Notes
|-|-|-
|1| [🔔🚀⏳ `Queue@Buffer`](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🔔🐌⏳ Queue.md>) | [Subscribers 🔔](<../../../Subscribers 🔔/🔔🎭 Subscriber role.md>) create a [Buffer ⏳](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) queue
|2| [🔔🐌🌬️ `Subscribe@Streamer`](<../../🌬️🅰️ Streamer methods/🔔🐌🌬️ Subscribe.md>) | [Subscribers 🔔](<../../../Subscribers 🔔/🔔🎭 Subscriber role.md>) subscribe to [Streamers 🌬️](<../../🌬️🎭 Streamer role.md>)
| 3 | [🌬️🐌⏳ `Push@Buffer`](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🌬️🐌⏳ Push.md>) | [Streamers 🌬️](<../../🌬️🎭 Streamer role.md>) push to [Buffers ⏳](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>)
| 4 | [⏳🐌🔔 `Wake-up@Subscriber`](<../../../Subscribers 🔔/🔔🅰️ Subscriber methods/⏳🐌🔔 Wake-up.md>) | [Buffers ⏳](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) wake up [Subscribers 🔔](<../../../Subscribers 🔔/🔔🎭 Subscriber role.md>)
| 5 | [🔔🚀⏳ `Poll@Buffer`](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🔔🚀⏳ Poll.md>) | [Subscribers 🔔](<../../../Subscribers 🔔/🔔🎭 Subscriber role.md>) poll all buffered messages
|6| [🔔🚀⏳ `Confirm@Buffer`](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🔔🚀⏳ Confirm.md>) | [Subscribers 🔔](<../../../Subscribers 🔔/🔔🎭 Subscriber role.md>) confirm processed ones
||

## FAQ

1. **Why an async request for [`Queue@Buffer`](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🔔🐌⏳ Queue.md>) ?**

    `Timeout` `Cost`

    [Buffer ⏳ domains](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) may require additional time to resource the compute and store to handle the queue. 
    * [Buffer ⏳ domains](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) should not be pressured to speed up under a synchronous request.
    * [Subscriber 🔔 domains](<../../../Subscribers 🔔/🔔🎭 Subscriber role.md>) should not spend compute cost waiting for a synchronous response that may time out.
    
    ---
    <br/>

1. **How is privacy the Subscriber protected on [`Push@Buffer`](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/🌬️🐌⏳ Push.md>)?**

    `Public-key encryption` 
    
    When [Streamer 🌬️ domains](<../../🌬️🎭 Streamer role.md>) send messages to [Buffer ⏳ domains](<../../../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>), 
    * the [Streamer 🌬️ domains](<../../🌬️🎭 Streamer role.md>) encrypt the messages with the public key of the [Subscriber 🔔 domain](<../../../Subscribers 🔔/🔔🎭 Subscriber role.md>), ensuring that only the [Subscriber 🔔 domain](<../../../Subscribers 🔔/🔔🎭 Subscriber role.md>) can decrypt them with the private key.

    ---
    <br/>