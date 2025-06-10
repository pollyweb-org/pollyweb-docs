🔎 Finder domains FAQ
===

![](<00 ✅ 📎 Assets/🔎 Finder.png>)

1. **What is a Finder domain in NLWeb?**

    A Finder is a [Vault 🗄️](<../../20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>) domain that helps users find other domains on the NLWeb, sorting the findings according to users' preferences and context.

    ---

1. **How can users set up a Finder domain?**

    Similar to setting up a [Storage 📦](<../01 ✅ 📦 Storage/01 ✅ 📦🫥 Storage agent.md>) domain.

    ---

1. **Where do Finders get information about other domains?**

    * [Graphs 🕸](<../../40 ✅ 👥 Domains/44 ✅ 📜 Manifests/03 ✅ 🕸👥 Graph helper.md>): Finders subscribe to Graphs to receive updates on domain Manifests across the NLWeb, including their public identity, trust relationships, and supported integrations. 
    * [Firewalls 🔥](<../../40 ✅ 👥 Domains/43 ✅ 👍 Trusts/03 ✅ 🔥👥 Firewall helper.md>): Finders subscribe to Firewalls to quickly react to threats. 
    * [Reviewer ⭐](<01 ✅ ⭐🫥 Reviewer vault.md>): Finders subscribe to Reviewer to receive updates of domain ranks across the NLWeb, as a result of user feedback. 
    * [👀 Advertisers](<03 ⏳ 👀👥 Advertiser helper.md>): Finders subscribe to Advertisers to know which ads to show to users in addition to search results from Manifests. 

    ---

1. **How do Finders get information about users?**

    * [Persona 🧢](<../02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>): Finders ask users to share anonymized search preferences from their Personas, then index the search results accordingly.
    * [Wallet 🧑‍🦰](<../../20 ✅ 🧑‍🦰 UI/01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>): Finders receive the user's current context from the Wallet, similar to what is sent to a Web 2.0 browser (e.g., time zone, country, state, approximate location).

    ---

1. **How do Finders filter and rank the results for users?**

    - **[trust 👍](<../../40 ✅ 👥 Domains/43 ✅ 👍 Trusts/01 ✅ 👍 Domain Trust.md>)**: domains untrusted by the user's Broker are discarded;
    - **🔥 Threads**: domains blocked by firewalls may be discarded even when trusted;
    - **🧢 Preferences**: the user's preferences, as shared by the user's Profiler;
    - **📍 Proximity**: the distance to the user, based on the context shared by the Wallet;
    - **⭐ Rank**: the weighted rank of the domain based on feedback of similar users.

    ---

1. **How do users interact with their Finder domain?**

    To search domains on a Finder, users use natural language, similar to ChatGPT (e.g. `find me a restaurant for tonight`). 
    * Finders then show potential Hosts for the user to initiate a chat session with.

    ---

1. **Why not merge Finders and Graphs?**

    Finders leverage conversations with GenAI, requiring them to comply with contextualized Artificial Intelligence (AI) legislation (e.g., the European Union AI Act). 
    * Conversely, [Graphs 🕸](<../../40 ✅ 👥 Domains/44 ✅ 📜 Manifests/03 ✅ 🕸👥 Graph helper.md>) are typically AI-free, allowing to be more generic.

    ---

1. **How to build a Finder?**

    The following 2019 video by Google entitled "How Google Search Works (in 5 minutes)" is a good starting point about how to build a great search engine.

    https://github.com/user-attachments/assets/a068a5fe-a75a-4158-b76a-4820da6776c8


    

    ---
