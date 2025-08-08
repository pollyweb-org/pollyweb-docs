🔥 Firewall domains FAQ
===

![](<./📎 Assets/👍 Firewall.png>)

1. **What is a Firewall domain in NLWeb?**

    A Firewall is normal domain focused on blacklisting other domains to keep the ecosystem safe (e.g., national security entities). Admins of Firewalls are typically concerned about monitoring for bad behaviors from domains.

    ---

1. **How can domains leverage Firewalls?**

    Domains can inherit a Firewall's blacklist on their [Manifest 📜](<../44 📜 Manifests/01 📜 Domain Manifest.md>) - this overrides any direct or indirect trust relationship between domains, working as an instantaneous mechanism to cut the communication with the blacklisted domain. 

    ---

1. **Do Firewalls monitor Listeners and Graphs?**

    Yes. Firewalls subscribe to [Listeners 👂](<../44 📜 Manifests/02 👂👥 Listener helper.md>) and [Graphs 🕸](<../44 📜 Manifests/03 🕸👥 Graph helper.md>) to monitor their robustness, reliability, and conformity to the NLWeb protocol, revoking their trust when necessary (e.g., compare information about a random domain in three or more Listeners/Graphs to identify discrepancies).

    ---

1. **Do Firewalls monitor domain reputation?**

    Yes. Firewalls subscribe to [Reviewer ⭐](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) domains to monitor the behavior of domains, revoking their trust when necessary.

    ---

1. **Do Firewalls report on suspicions before blocking?**

    No. NLWeb advocates the usage of [Reviewer ⭐](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) domains to assess the level of trustworthiness of another domain.

    ---
