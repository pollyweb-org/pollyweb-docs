👥 Domains
===

1. **What is a Domain in NLWeb?**

    In NLWeb, a [domain 👥](<👥 Domain.md>) is any public web service that
    * sends and receives domain [Messages 📨](<../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
    * exposes an API defined by a [Role 🎭](<👥🎭 Domain Role.md>)
    * and publishes a [domain Manifest 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).


    ---
    <br/>


1. **What flows are implemented by domains?**

    |Flow| Description
    |-|-
    |[👥⏩🌐 DNS config](<../👥⏩ Domain flows/DNS config 👥🌐/👥 DNS config ⏩ flow.md>) | Configure the domain [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>)
    |[👥⏩👥 Request Sync 🚀](<../👥⏩ Domain flows/Send Sync 👥🚀👥 /👥 Sync Request ⏩ flow.md>) | Send requests that wait for a response
    |[👥⏩👥 Send Async 🐌](<../👥⏩ Domain flows/Send Async 👥🐌👥/👥 Async Message ⏩ flow.md>) | Send event-driven commands or events
    |[👥⏩🕸 Manifest](<../👥⏩ Domain flows/Manifest 👥📜🕸/👥 Manifest ⏩ flow.md>) | Publish [domain Manifest 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) changes
    | [👥⏩🤝 Subscribe](<../../45 🤲 Helper domains/Billers 🤝/🤝⏩ Biller flows/👥⏩🤝 Domain Subscription.md>) | Sign subscriptions on [Biller 🤝 domains](<../../45 🤲 Helper domains/Billers 🤝/🤝🤲 Biller helper.md>)


    ---
    <br/>