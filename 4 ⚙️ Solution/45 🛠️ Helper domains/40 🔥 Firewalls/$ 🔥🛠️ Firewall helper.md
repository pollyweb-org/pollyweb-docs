🔥 Firewall helper domains
===

1. **What is a Firewall domain in NLWeb?**

    A [Firewall 🔥 domain](<$ 🔥🛠️ Firewall helper.md>) is 
    * a [Helper 🛠️ domain](<../$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) 
    * focused on blacklisting other [Domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>)
    * to keep the ecosystem safe (e.g., national security entities). 

    Admins of [Firewall 🔥 helper domains](<$ 🔥🛠️ Firewall helper.md>) are typically concerned about 
    * monitoring and blocking potential bad behaviors from [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>).

    ---
    <br/>

1. **How do Firewalls work?**

    ![](<../../40 👥 Domains/43 👍 Trusts/.📎 Assets/👍 Firewall.png>)

    |#|Step
    |-|-
    |1| [Firewall 🔥 domains](<$ 🔥🛠️ Firewall helper.md>) subscribe to the [domain-event streams 🌬️](<../../41 🎭 Domain Roles/75 🌬️ Streamers/🌬️🎭 Streamer role.md>) of [Reviewer ⭐ domains](<../../50 🫥 Agents/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>), [Listener 👂 domains](<../60 👂 Listeners/👂🛠️ Listener helper.md>), and [Graph 🕸 domains](<../50 🕸 Graphs/🕸🛠️ Graph helper.md>), eventually throttling them with a [Buffer ⏳ helper domain](<../27 ⏳ Buffers/⏳🛠️ Buffer helper.md>);
    |2| [Firewall 🔥 domains](<$ 🔥🛠️ Firewall helper.md>) then update the [Trust 👍 list](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) in their [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>), which is propagated down by the [Listener 👂 helper domains](<../60 👂 Listeners/👂🛠️ Listener helper.md>) and subscribed by [Graph 🕸 helper domains](<../50 🕸 Graphs/🕸🛠️ Graph helper.md>) and [Finder 🔎 vaults](<../../50 🫥 Agents/40 🔎 Finders/🔎🫥 Finder agent.md>).

    ---

1. **How can domains leverage Firewalls?**

    [Domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) can inherit a Firewall's blacklist on their [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>);
    * this overrides any direct or indirect [Trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) relationship between [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>), working as an instantaneous mechanism to cut the communication with the blacklisted domain. 

    ---
    <br/>

1. **Do Firewalls monitor Listeners and Graphs?**

    Yes. 
    * [Firewall 🔥 helper domains](<$ 🔥🛠️ Firewall helper.md>) subscribe to [Listener 👂 domain streams](<../60 👂 Listeners/👂🛠️ Listener helper.md>) and [Graph 🕸 domain streams](<../50 🕸 Graphs/🕸🛠️ Graph helper.md>) to monitor their robustness, reliability, and conformity to the NLWeb protocol, revoking their [Trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) when necessary;
        * e.g., compare information about a random [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) in three or more [Listener 👂 domains](<../60 👂 Listeners/👂🛠️ Listener helper.md>) or [Graph 🕸 domains](<../50 🕸 Graphs/🕸🛠️ Graph helper.md>) to identify discrepancies.

    ---
    <br/>

1. **Do Firewalls monitor domain reputation?**

    Yes. 
    * [Firewall 🔥 helper domains](<$ 🔥🛠️ Firewall helper.md>) subscribe to [Reviewer ⭐ domain streams](<../../50 🫥 Agents/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) to monitor the behavior of [Host 🤗 domains](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>), revoking their [Trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) when necessary.

    ---
    <br/>

1. **Do Firewalls report on suspicions before blocking?**

    No. 
    * NLWeb advocates the usage of [Reviewer ⭐ domains](<../../50 🫥 Agents/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) to assess the level of trustworthiness of another [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>).

    ---
    <br/>


1. **What's an example of the Manifest of a Firewall domain?**

    The following is an example of 
    * a list of [Trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) REVOKES 
    * on malicious domains names 
    * in a [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>)
    * from the [Any Firewall 🔥 manifest](<../../../8 📜 Manifests/🌐 Backbone/📜 any-firewall.org.md>).

    ```yaml
    🤝: nlweb.org/MANIFEST

    About:
      Domain: any-firewall.org
      Name: Any Firewall

    Trusts:
      - Title: Block malicious domains from collecting, and vaults from sharing.
        Action: REVOKE
        Domains:
          - imgur.com
          - torrentfreak.com
          - requestservice.live
          - atm.any-fintech.org
    ```

    ---
    <br/>

1. **What should other domains add to their Manifests?**

    Other [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) should add the following [Trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) to their [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).

    ```yaml
    Trusts:
    - Action: INHERIT
      Domains:
        - any-firewall.org
    ```


    See the follow examples as a reference:
      * [🎰 Any Casino](<../../../8 📜 Manifests/🌐 Businesses/📜 casino.any-business.org.md>)
      * [🇺🇸 U.S. Department of Health & Human Services](<../../../8 📜 Manifests/🌐 Vaults/📜 hhs.gov.md>)
      * [🇺🇳 Nation Members of Any IGO](<../../../8 📜 Manifests/👥 any-igo.org/📜 nations.any-igo.org.md>)
      * [🇪🇺 European Union](<../../../8 📜 Manifests/👥 europa.eu/📜 europa.eu/📜 europa.eu.md>)


    ---
    <br/>