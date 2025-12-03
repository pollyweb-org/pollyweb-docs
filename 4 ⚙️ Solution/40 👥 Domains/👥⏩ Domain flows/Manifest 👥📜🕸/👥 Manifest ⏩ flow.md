# 👥⏩🕸 Manifest 📜

> Part of [Domain 👥](<../../👥 Domain/👥 Domain.md>)

> Implements [domain Manifest 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>)

<br/>

## Flow diagram ⏩

![Manifest](<👥 Manifest ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🐌👂 `Updated@Listener`](<../../../45 🤲 Helper domains/Listeners 👂/👂📨 Listener msgs/👥🐌👂 Updated.md>) | [Domains 👥](<../../👥 Domain/👥 Domain.md>) notify [Manifest 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) changes
| 2 | [🌬️⏩🔔 Stream changes](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream/🌬️⏩🔔 Stream.md>) | [Listeners 👂](<../../../45 🤲 Helper domains/Listeners 👂/👂 Listener helper/👂🤲 Listener helper.md>) fan-out to [Subscribers 🔔](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔 Subscriber/🔔🎭 Subscriber role.md>)
||