# 👥⏩🕸 Manifest @ Domain

> Implements:
> <br/>• [Domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>)
> <br/>• [domain Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>)

<br/>

## Flow diagram ⏩

![Manifest](<.📎 Assets/⚙️🕸 Manifest.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🐌👂 `Updated@Listener`](<../../6 🅰️ APIs/60 👂🅰️ Listener/01 👥🐌👂 Updated.md>) | [Domains 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) notify [Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) changes
| 2 | [🌬️⏩🔔 Stream changes](<../76  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) | [Listeners 👂](<../../4 ⚙️ Solution/42 Backbone/10 👂 Listeners/$ 👂🛠️ Listener helper.md>) fan-out to [Subscribers 🔔](<../../4 ⚙️ Solution/41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>)
||