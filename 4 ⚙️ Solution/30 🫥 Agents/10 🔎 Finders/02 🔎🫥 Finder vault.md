<!-- #TODO -->

🔎 Finder domains FAQ
===



1. **What is a Finder domain in NLWeb?**

    A Finder is 
    * any [Vault 🗄️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) 
    * that helps users find other domains on the NLWeb, 
    * sorting the findings according to users' preferences and context.

    ---
    <br/>

1. **How do Finders work?**
   
    ![](<00 📎 Assets/🔎 Finder.png>)

    ---
    <br/>

2. **How do Finders help to protect users?**

    [Broker 🤵 domains](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) leverage Finders to provide users with culturally-contextualized details and user feedback about [Host 🤗 domains](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) when a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) starts. 

    * Consider the following [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) excerpt from the [Buy water 🤝 use case](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>) as an example of a with an interaction with a  [Host 🤗 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>), right after the user has tapped a [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>).

    | Service    | Prompt | User
    | - | - | - |
    | | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>)
    | 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Host (4.3 ⭐) [+] | (expand)
    | 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Host (4.3 ⭐)  [-] <br/> This host sells shoes.<br/>- They were founded in 1987.<br/>- Joined NLWeb 2 years ago.<br/>User feedback:<br/>- Delivery 4.7⭐ by 357 users<br/>- Support 3.5⭐ by 21 users

    ---
    <br/>


5. **How do Finders help users with a search?**

    To search domains on a Finder, users use natural language, similar to ChatGPT.
    * Example: `find me a restaurant for tonight`.
    * Finders then show potential [Host 🤗 domains](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) for the user to initiate a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with.
    * After the user selection, Finders also show potential next steps for [navigation 🧭](<../07 🧭 Navigators/01 🧭🫥 Navigator agent.md>), available [services 🪢](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🪢🎭 Integrator role.md>), and [advertising 👀](<03 👀👥 Advertiser helper.md>).
    * Consider the following [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) excerpt of the [Find a bar 🤝 use case](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>) as an example.


    | Service | Prompt | User
    | - | - | - |
    | 🔎 [Finder](<02 🔎🫥 Finder vault.md>) | 😃 Hi! What do you need? | `a bar`
    | 🔎 [Finder](<02 🔎🫥 Finder vault.md>) | 💬 Here are suggestions: <br/> - [ Any Club 🕺 ] (4.4 ⭐) <br/> &nbsp; └ 👟 1.7km 🚪 10pm-5am <br/> - [ Any Bar 🍸 ] (4.8 ⭐) <br/> &nbsp; ├ 👟 1.7km 🚪 1pm-10pm <br/> &nbsp; ├ open bar from 8pm <br/> &nbsp; └ closes in ~1 hour <br/> - [ Find 🔎 ] alternatives | > Any Bar 🍸
    | 🔎 [Finder](<02 🔎🫥 Finder vault.md>) | 💬 Suggested next steps: <br/> - [ Get there 🧭 ] <br/> - [ Buy entry in advance ]  
   
    ---
    <br/>

6. **Where do Finders get information about other domains?**

    |[Streamer&nbsp;🎭](<../../40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>)|Purpose
    |-|-
    | [🕸&nbsp;Graphs](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) | Finders subscribe to [Graphs 🕸 domains](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) to receive updates on [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) across the NLWeb, including their public identity, [trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) relationships, and supported [integrations 🪢](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🪢🎭 Integrator role.md>). 
    | [🔥&nbsp;Firewalls](<../../40 👥 Domains/43 👍 Trusts/03 🔥🛠️ Firewall helper.md>) | Finders subscribe to [Firewall 🔥 domains](<../../40 👥 Domains/43 👍 Trusts/03 🔥🛠️ Firewall helper.md>) to quickly react to threats. 
    | [⭐&nbsp;Reviewers](<01 ⭐🫥 Reviewer vault.md>) | Finders subscribe to [Reviewer ⭐ domains](<01 ⭐🫥 Reviewer vault.md>) to receive updates of domain ranks across the NLWeb, as a result of user feedback. 
    | [👀&nbsp;Advertisers](<03 👀👥 Advertiser helper.md>) | Finders subscribe to [Advertiser 👀 domains](<03 👀👥 Advertiser helper.md>) to know which ads to show to users in addition to search results from [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>). 

    ---
    <br/>

7. **How do Finders get information about users?**

    * [Persona 🧢](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>): Finders ask users to share anonymized search preferences from their Personas, then index the search results accordingly.
    * [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>): Finders receive the user's current context from the Wallet, similar to what is sent to a Web 2.0 browser (e.g., time zone, country, state, approximate location).

    ---
    <br/>

8. **How do Finders filter and rank the results for users?**

    - **[trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)**: domains untrusted by the user's Broker are discarded;
    - **🔥 Threads**: domains blocked by firewalls may be discarded even when trusted;
    - **🧢 Preferences**: the user's preferences, as shared by the user's Profiler;
    - **📍 Proximity**: the distance to the user, based on the context shared by the Wallet;
    - **⭐ Rank**: the weighted rank of the domain based on feedback of similar users.

    ---
    <br/>


6. **Why not merge Finders and Graphs?**

    Finders leverage conversations with GenAI, requiring them to comply with contextualized Artificial Intelligence (AI) legislation (e.g., the European Union AI Act). 
    * Conversely, [Graph 🕸 domains](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) are typically AI-free, allowing to be more generic.


    ---
    <br/>
