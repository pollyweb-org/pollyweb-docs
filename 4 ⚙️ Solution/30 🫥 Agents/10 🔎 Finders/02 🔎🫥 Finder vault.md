<!-- #TODO -->

🔎 Finder domains FAQ
===

![](<00 📎 Assets/🔎 Finder.png>)

1. **What is a Finder domain in NLWeb?**

    A Finder is 
    * any [Vault 🗄️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) 
    * that helps users find other domains on the NLWeb, 
    * sorting the findings according to users' preferences and context.

    ---


2. **Where do Finders get information about other domains?**

    |[Streamer&nbsp;🎭](<../../40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>)|Purpose
    |-|-
    | [🕸&nbsp;Graphs](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) | Finders subscribe to [Graphs 🕸 domains](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) to receive updates on [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) across the NLWeb, including their public identity, trust relationships, and supported integrations. 
    | [🔥&nbsp;Firewalls](<../../40 👥 Domains/43 👍 Trusts/03 🔥🛠️ Firewall helper.md>) | Finders subscribe to [Firewall 🔥 domains](<../../40 👥 Domains/43 👍 Trusts/03 🔥🛠️ Firewall helper.md>) to quickly react to threats. 
    | [⭐&nbsp;Reviewers](<01 ⭐🫥 Reviewer vault.md>) | Finders subscribe to [Reviewer ⭐ domains](<01 ⭐🫥 Reviewer vault.md>) to receive updates of domain ranks across the NLWeb, as a result of user feedback. 
    | [👀&nbsp;Advertisers](<03 👀👥 Advertiser helper.md>) | Finders subscribe to [Advertiser 👀 domains](<03 👀👥 Advertiser helper.md>) to know which ads to show to users in addition to search results from [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>). 

    ---

3. **How do Finders get information about users?**

    * [Persona 🧢](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>): Finders ask users to share anonymized search preferences from their Personas, then index the search results accordingly.
    * [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>): Finders receive the user's current context from the Wallet, similar to what is sent to a Web 2.0 browser (e.g., time zone, country, state, approximate location).

    ---

4. **How do Finders filter and rank the results for users?**

    - **[trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)**: domains untrusted by the user's Broker are discarded;
    - **🔥 Threads**: domains blocked by firewalls may be discarded even when trusted;
    - **🧢 Preferences**: the user's preferences, as shared by the user's Profiler;
    - **📍 Proximity**: the distance to the user, based on the context shared by the Wallet;
    - **⭐ Rank**: the weighted rank of the domain based on feedback of similar users.

    ---

5. **How do users interact with their Finder domain?**

    To search domains on a Finder, users use natural language, similar to ChatGPT 
    * e.g., `find me a restaurant for tonight`. 
    * Finders then show potential [Host 🤗 domains](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) for the user to initiate a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with.

    ---

6. **Why not merge Finders and Graphs?**

    Finders leverage conversations with GenAI, requiring them to comply with contextualized Artificial Intelligence (AI) legislation (e.g., the European Union AI Act). 
    * Conversely, [Graph 🕸 domains](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) are typically AI-free, allowing to be more generic.


    ---
