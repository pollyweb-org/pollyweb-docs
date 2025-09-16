🔥 Firewall helper domains FAQ
===

1. **What is a Firewall domain in NLWeb?**

    A [Firewall 🔥 domain](<03 🔥🛠️ Firewall helper.md>) is 
    * a [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) 
    * focused on blacklisting other [Domains 👥](<../44 📜 Manifests/00 👥 Domain.md>)
    * to keep the ecosystem safe (e.g., national security entities). 

    Admins of [Firewall 🔥 helper domains](<03 🔥🛠️ Firewall helper.md>) are typically concerned about 
    * monitoring and blocking potential bad behaviors from [domains 👥](<../44 📜 Manifests/00 👥 Domain.md>).

    ---
    <br/>

1. **How do Firewalls work?**

    ![](<.📎 Assets/👍 Firewall.png>)

    |#|Step
    |-|-
    |1| [Firewall 🔥 domains](<03 🔥🛠️ Firewall helper.md>) subscribe to the [domain-event streams 🌬️](<../41 📨 Comms/02 🌬️🎭 Streamer role.md>) of [Reviewer ⭐ domains](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>), [Listener 👂 domains](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>), and [Graph 🕸 domains](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>), eventually throttling them with a [Buffer ⏳ helper domain](<../41 📨 Comms/03 ⏳🛠️ Buffer helper.md>);
    |2| [Firewall 🔥 domains](<03 🔥🛠️ Firewall helper.md>) then update the [Trust 👍 list](<01 👍 Domain Trust.md>) in their [domain Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>), which is propagated down by the [Listener 👂 helper domains](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>) and subscribed by [Graph 🕸 helper domains](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>) and [Finder 🔎 vaults](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>).

    ---

2. **How can domains leverage Firewalls?**

    [Domains 👥](<../44 📜 Manifests/00 👥 Domain.md>) can inherit a Firewall's blacklist on their [domain Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>);
    * this overrides any direct or indirect [Trust 👍](<01 👍 Domain Trust.md>) relationship between [domains 👥](<../44 📜 Manifests/00 👥 Domain.md>), working as an instantaneous mechanism to cut the communication with the blacklisted domain. 

    ---
    <br/>

3. **Do Firewalls monitor Listeners and Graphs?**

    Yes. 
    * [Firewall 🔥 helper domains](<03 🔥🛠️ Firewall helper.md>) subscribe to [Listener 👂 domain streams](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>) and [Graph 🕸 domain streams](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>) to monitor their robustness, reliability, and conformity to the NLWeb protocol, revoking their [Trust 👍](<01 👍 Domain Trust.md>) when necessary;
        * e.g., compare information about a random [domain 👥](<../44 📜 Manifests/00 👥 Domain.md>) in three or more [Listener 👂 domains](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>) or [Graph 🕸 domains](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>) to identify discrepancies.

    ---
    <br/>

4. **Do Firewalls monitor domain reputation?**

    Yes. 
    * [Firewall 🔥 helper domains](<03 🔥🛠️ Firewall helper.md>) subscribe to [Reviewer ⭐ domain streams](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) to monitor the behavior of [Host 🤗 domains](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>), revoking their [Trust 👍](<01 👍 Domain Trust.md>) when necessary.

    ---
    <br/>

5. **Do Firewalls report on suspicions before blocking?**

    No. 
    * NLWeb advocates the usage of [Reviewer ⭐ domains](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) to assess the level of trustworthiness of another [Host 🤗 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>).

    ---
    <br/>
