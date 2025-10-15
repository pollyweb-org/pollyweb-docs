# 👥⏩🕸 Manifest @ Domain

> Implements:
> <br/>• [Domain 👥](<../👥 Domain.md>)
> <br/>• [domain Manifest 📜](<../../44 📜 Manifests/$ 📜 Domain Manifest.md>)

<br/>

## Flow diagram ⏩

![Manifest](<.📎 Assets/⚙️🕸 Manifest.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🐌👂 `Updated@Listener`](<../../../45 🛠️ Helper domains/60 👂 Listeners/👂🅰️ Listener methods/👥🐌👂 Updated.md>) | [Domains 👥](<../👥 Domain.md>) notify [Manifest 📜](<../../44 📜 Manifests/$ 📜 Domain Manifest.md>) changes
| 2 | [🌬️⏩🔔 Stream changes](<../../../41 🎭 Domain Roles/75 🌬️ Streamers/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream.md>) | [Listeners 👂](<../../../45 🛠️ Helper domains/60 👂 Listeners/👂🛠️ Listener helper.md>) fan-out to [Subscribers 🔔](<../../../41 🎭 Domain Roles/76 🔔 Subscribers/🔔🎭 Subscriber role.md>)
||