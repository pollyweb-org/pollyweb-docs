🔥 Firewall helper domains
===

1. **What is a Firewall domain in NLWeb?**

    A [Firewall 🔥 domain](<🔥🤲 Firewall helper.md>) is 
    * a [Helper 🤲 domain](<../$ Helpers 🤲/🤲👥 Helper domain.md>) 
    * focused on blacklisting other [Domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>)
    * to keep the ecosystem safe (e.g., national security entities). 

    Admins of [Firewall 🔥 helper domains](<🔥🤲 Firewall helper.md>) are typically concerned about 
    * monitoring and blocking potential bad behaviors from [domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>).

    ---
    <br/>

1. **How do Firewalls work?**

    ![](<../../30 🧩 Data/Trusts 🫡/.📎 Assets/🫡 Firewall.png>)

    |#|Step
    |-|-
    |1| [Firewall 🔥 domains](<🔥🤲 Firewall helper.md>) subscribe to the [domain-event streams 🌬️](<../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) of [Reviewer ⭐ domains](<../../50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>), [Listener 👂 domains](<../Listeners 👂/👂🤲 Listener helper.md>), and [Graph 🕸 domains](<../Graphs 🕸/🕸🤲 Graph helper.md>), eventually throttling them with a [Buffer ⏳ helper domain](<../Buffers ⏳/⏳🤲 Buffer helper.md>);
    |2| [Firewall 🔥 domains](<🔥🤲 Firewall helper.md>) then update the [Trust 🫡 list](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) in their [domain Manifest 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>), which is propagated down by the [Listener 👂 helper domains](<../Listeners 👂/👂🤲 Listener helper.md>) and subscribed by [Graph 🕸 helper domains](<../Graphs 🕸/🕸🤲 Graph helper.md>) and [Finder 🔎 vaults](<../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>).

    ---

1. **How can domains leverage Firewalls?**

    [Domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) can inherit a Firewall's blacklist on their [domain Manifest 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>);
    * this overrides any direct or indirect [Trust 🫡](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) relationship between [domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>), working as an instantaneous mechanism to cut the communication with the blacklisted domain. 

    ---
    <br/>

1. **Do Firewalls monitor Listeners and Graphs?**

    Yes. 
    * [Firewall 🔥 helper domains](<🔥🤲 Firewall helper.md>) subscribe to [Listener 👂 domain streams](<../Listeners 👂/👂🤲 Listener helper.md>) and [Graph 🕸 domain streams](<../Graphs 🕸/🕸🤲 Graph helper.md>) to monitor their robustness, reliability, and conformity to the NLWeb protocol, revoking their [Trust 🫡](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) when necessary;
        * e.g., compare information about a random [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) in three or more [Listener 👂 domains](<../Listeners 👂/👂🤲 Listener helper.md>) or [Graph 🕸 domains](<../Graphs 🕸/🕸🤲 Graph helper.md>) to identify discrepancies.

    ---
    <br/>

1. **Do Firewalls monitor domain reputation?**

    Yes. 
    * [Firewall 🔥 helper domains](<🔥🤲 Firewall helper.md>) subscribe to [Reviewer ⭐ domain streams](<../../50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) to monitor the behavior of [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>), revoking their [Trust 🫡](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) when necessary.

    ---
    <br/>

1. **Do Firewalls report on suspicions before blocking?**

    No. 
    * NLWeb advocates the usage of [Reviewer ⭐ domains](<../../50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) to assess the level of trustworthiness of another [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).

    ---
    <br/>


1. **What's an example of the Manifest of a Firewall domain?**

    The following is an example of 
    * a list of [Trust 🫡](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) REVOKES 
    * on malicious domains names 
    * in a [domain Manifest 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>)
    * from the [Any Firewall 🔥 manifest](<../../../8 📜 Manifests/🌐 Backbone/📜 any-firewall.dom.md>).

    ```yaml
    🤝: nlweb.dom/MANIFEST

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
          - atm.any-fintech.dom
    ```

    ---
    <br/>

1. **What should other domains add to their Manifests?**

    Other [domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) should add the following [Trust 🫡](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) to their [domain Manifest 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).

    ```yaml
    Trusts:
    - Action: INHERIT
      Domains:
        - any-firewall.org
    ```


    See the follow examples as a reference:
      * [🎰 Any Casino](<../../../8 📜 Manifests/🌐 Businesses/📜 casino.any-business.dom.md>)
      * [🇺🇸 U.S. Department of Health & Human Services](<../../../8 📜 Manifests/🌐 Vaults/📜 hhs.gov.md>)
      * [🇺🇳 Nation Members of Any IGO](<../../../8 📜 Manifests/👥 any-igo.dom/📜 nations.any-igo.dom.md>)
      * [🇪🇺 European Union](<../../../8 📜 Manifests/👥 europa.eu/📜 europa.eu/📜 europa.eu.md>)


    ---
    <br/>