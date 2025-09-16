🔥 Firewall domains FAQ
===

1. **What is a Firewall domain in NLWeb?**

    A Firewall 🔥 is a [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) focused on blacklisting other [Domains 👥](<../44 📜 Manifests/00 👥 Domain.md>) to keep the ecosystem safe (e.g., national security entities). 
    * Admins of Firewalls 🔥 are typically concerned about monitoring for bad behaviors from domains.

    ---

1. **How do Firewalls work?**

    ![](<.📎 Assets/👍 Firewall.png>)

    |#|Step
    |-|-
    |1| Firewalls 🔥 subscribe to the [domain-event streams 🌬️](<../41 📨 Comms/02 🌬️🎭 Streamer role.md>) of [Reviewer ⭐ domains](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>), [Listener 👂 helpers](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>), and [Graph 🕸 helpers](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>), eventually throttling them with a [Buffer ⏳ helper](<../41 📨 Comms/03 ⏳🛠️ Buffer helper.md>);
    |2| Firewalls 🔥 then update the [Trust 👍 list](<01 👍 Domain Trust.md>) in their [Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>), which is propagated down by the [Listener 👂 helpers](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>) and subscribed by [Graph 🕸 helpers](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>) and [Finder 🔎 vaults](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>).

    ---

2. **How can domains leverage Firewalls?**

    [Domains 👥](<../44 📜 Manifests/00 👥 Domain.md>) can inherit a Firewall's blacklist on their [Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>);
    * this overrides any direct or indirect [Trust 👍](<01 👍 Domain Trust.md>) relationship between [Domains 👥](<../44 📜 Manifests/00 👥 Domain.md>), working as an instantaneous mechanism to cut the communication with the blacklisted domain. 

    ---

3. **Do Firewalls monitor Listeners and Graphs?**

    Yes. 
    * Firewalls 🔥 subscribe to [Listeners 👂](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>) and [Graphs 🕸](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>) to monitor their robustness, reliability, and conformity to the NLWeb protocol, revoking their [Trust 👍](<01 👍 Domain Trust.md>) when necessary;
        * e.g., compare information about a random [domain 👥](<../44 📜 Manifests/00 👥 Domain.md>) in three or more [Listeners 👂](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>) or [Graphs 🕸](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>) to identify discrepancies.

    ---

4. **Do Firewalls monitor domain reputation?**

    Yes. 
    * Firewalls 🔥 subscribe to [Reviewer ⭐ domains](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) to monitor the behavior of [Host 🤗 domains](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>), revoking their [Trust 👍](<01 👍 Domain Trust.md>) when necessary.

    ---

5. **Do Firewalls report on suspicions before blocking?**

    No. 
    * NLWeb advocates the usage of [Reviewer ⭐ domains](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) to assess the level of trustworthiness of another [Host 🤗 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>).

    ---
