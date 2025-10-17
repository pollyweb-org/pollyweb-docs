# 👥⏩🕸 Manifest 📜

> Part of [Domain 👥](<../👥 Domain.md>)

> Implements [domain Manifest 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest.md>)

<br/>

## Flow diagram ⏩

![Manifest](<.📎 Assets/⚙️🕸 Manifest.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🐌👂 `Updated@Listener`](<../../../45 🤲 Helper domains/Listeners 👂/👂🅰️ Listener methods/👥🐌👂 Updated.md>) | [Domains 👥](<../👥 Domain.md>) notify [Manifest 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest.md>) changes
| 2 | [🌬️⏩🔔 Stream changes](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream.md>) | [Listeners 👂](<../../../45 🤲 Helper domains/Listeners 👂/👂🤲 Listener helper.md>) fan-out to [Subscribers 🔔](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>)
||