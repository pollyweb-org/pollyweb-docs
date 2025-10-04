# 👥⏩🕸 Manifest @ Domain

> Implements [domain Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>)

<br/>

## Flow diagram ⏩

![Manifest](<.📎 Assets/⚙️🕸 Manifest.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🐌👂 `Updated@Listener`](<../../6 🅰️ APIs/60 👂🅰️ Listener/01 👥🐌👂 Updated.md>) | [Domains 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) notify [Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) changes
| 2 | [🌬️⏩🔔 Stream changes](<../78  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) | [Listeners 👂](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/02 👂🛠️ Listener helper.md>) fan-out to  subscribers
||