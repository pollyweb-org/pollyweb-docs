<!-- #TODO -->

🔎 Finder domains
===



1. **What is a Finder domain in PollyWeb?**

    A Finder is 
    * any [Vault 🗄️ domain](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) 
    * that helps users find other domains on the PollyWeb, 
    * sorting the findings according to users' preferences and context.

    ---
    <br/>

1. **How do Finders work?**
   
    ![](<🔎🏞️ Finder img.png>)

    ---
    <br/>

1. **How do Finders help to protect users?**

    [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) leverage Finders to provide users with culturally-contextualized details and user feedback about [Host 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) when a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) starts. 

    * Consider the following [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) excerpt from the [Buy water 🤝 use case](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>) as an example of a with an interaction with a  [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>), right after the user has tapped a [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | | | 🔆 [tap](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    | 🔎 [Finder](<🔎 Finder 🫥 agent.md>) | ⓘ Any Host (4.3 ⭐) [+] | (expand)
    | 🔎 [Finder](<🔎 Finder 🫥 agent.md>) | ⓘ Any Host (4.3 ⭐)  [-] <br/> This host sells shoes.<br/>- They were founded in 1987.<br/>- Joined PollyWeb 2 years ago.<br/>User feedback:<br/>- Delivery 4.7⭐ by 357 users<br/>- Support 3.5⭐ by 21 users

    ---
    <br/>


1. **How do Finders help users with a search?**

    To search domains on a Finder, users use natural language, similar to ChatGPT.
    * Example: `find me a restaurant for tonight`.
    * Finders then show potential [Host 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) for the user to initiate a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with.
    * After the user selection, Finders also show potential next steps for [navigation 🧭](<../../Navigators 🧭/$ 🧭🫥 Navigator agent.md>), available [services 🪢](<../../../41 🎭 Domain Roles/Integrators 🪢/🪢🎭 Integrator role.md>), and [advertising 👀](<../../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>).
    * Consider the following [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) excerpt of the [Find a bar 🤝 use case](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>) as an example.


    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🔎 [Finder](<🔎 Finder 🫥 agent.md>) | 😃 Hi! What do you need? | `a bar`
    | 🔎 [Finder](<🔎 Finder 🫥 agent.md>) | 💬 Here are suggestions: <br/> - [ Any Club 🕺 ] (4.4 ⭐) <br/> &nbsp; └ 👟 1.7km 🚪 10pm-5am <br/> - [ Any Bar 🍸 ] (4.8 ⭐) <br/> &nbsp; ├ 👟 1.7km 🚪 1pm-10pm <br/> &nbsp; ├ open bar from 8pm <br/> &nbsp; └ closes in ~1 hour <br/> - [ Find 🔎 ] alternatives | > Any Bar 🍸
    | 🔎 [Finder](<🔎 Finder 🫥 agent.md>) | 💬 Suggested next steps: <br/> - [ Get there 🧭 ] <br/> - [ Buy ] entry in advance 
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Over to 🍸 Any Bar.
    | [ new chat ]
    | 🔎 [Finder](<🔎 Finder 🫥 agent.md>) | ⓘ Any Bar (4.4 ⭐) [+]
    | 🍸 Bar   | ℹ️ Buy entry request.
    | 🍸 Bar  | 😃 How many entries?
   
    ---
    <br/>

1. **Where do Finders get information about other domains?**

    |[Streamer&nbsp;🎭](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>)|Purpose
    |-|-
    | [🕸&nbsp;Graphs](<../../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>) | Finders subscribe to [Graphs 🕸 domains](<../../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>) to receive updates on [domain Manifests 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) across the PollyWeb, including their public identity, [trust 🫡](<../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) relationships, and supported [integrations 🪢](<../../../41 🎭 Domain Roles/Integrators 🪢/🪢🎭 Integrator role.md>). 
    | [🔥&nbsp;Firewalls](<../../../45 🤲 Helper domains/Firewalls 🔥/🔥🤲 Firewall helper.md>) | Finders subscribe to [Firewall 🔥 domains](<../../../45 🤲 Helper domains/Firewalls 🔥/🔥🤲 Firewall helper.md>) to quickly react to threats. 
    | [⭐&nbsp;Reviewers](<../../Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | Finders subscribe to [Reviewer ⭐ domains](<../../Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) to receive updates of domain ranks across the PollyWeb, as a result of user feedback. 
    | [👀&nbsp;Advertisers](<../../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) | Finders subscribe to [Advertiser 👀 domains](<../../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) to know which ads to show to users in addition to search results from [domain Manifests 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>). 

    ---
    <br/>

1. **How do Finders get information about users?**

    * [Persona 🧢](<../../Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>): Finders ask users to share anonymized search preferences from their Personas, then index the search results accordingly.
    * [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>): Finders receive the user's current context from the Wallet, similar to what is sent to a Web 2.0 browser (e.g., time zone, country, state, approximate location).

    ---
    <br/>

1. **How do Finders filter and rank the results for users?**

    - **[🫡 Trust](<../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)**: domains untrusted by the user's [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) are discarded;
    - **🔥 Threats**: domains blocked by [Firewalls 🔥](<../../../45 🤲 Helper domains/Firewalls 🔥/🔥🤲 Firewall helper.md>) may be discarded even when trusted;
    - **🧢 Preferences**: the user's preferences, as shared by the user's [Persona 🧢](<../../Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>);
    - **📍 Proximity**: the distance to the user, based on the context shared by the Wallet;
    - **⭐ Rank**: the weighted rank of the domain based on feedback of similar users.

    ---
    <br/>


1. **Why not merge Finders and Graphs?**

    Finders leverage conversations with artificial intelligence, requiring them to comply with contextualized Artificial Intelligence (AI) legislation (e.g., the European Union AI Act). 
    * Conversely, [Graph 🕸 domains](<../../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>) are typically AI-free, allowing to be more generic.


    ---
    <br/>
