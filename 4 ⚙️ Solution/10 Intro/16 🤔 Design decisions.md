Design Decisions
===

1. **What is NLWeb's approach to end-user natural language?**

    NLWeb is designed for Q&A flows (like ChatGPT), where a [Host 🤗 domain](<../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) asks the questions and defines the format that users are allowed to answer them. 
    

    ---
    <br/>

1. **What is NLWeb's approach to conversational commerce?**

    In NLWeb, [Wallet 🧑‍🦰 apps](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) are the way for users to communicate with [Host 🤗 domains](<../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>). 
    
    - Similar to [Meta's WhatsApp 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/10 💬 Chatting landscape/06 📺 WhatsApp business.md>), NLWeb [Wallet 🧑‍🦰 apps](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) allow users to keep a list of active [Chats 💬](<../35 💬 Chats/Chats 💬/💬 Chat.md>) with [Host 🤗 domains](<../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>). 

    - Like in [India's ONDC 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/09 🛒 Shopping landscape/01 📺 🇮🇳 India's ONDC.md>), domains can configure multiple types of user inputs - e.g., number, dropdown, calendar. 
    
    - New chats are opened with a [Locator 🔆](<../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) by scanning a [QR code ✨](<../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰✨ Wallet QR scan.md>) or by tapping an [NFC tag 🔆](<../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>). 
    
    - Users may accept [Tokens 🎫](<../30 🧩 Data/Tokens 🎫/🎫 Token.md>) issued by [Issuer 🎴 domains](<../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) - these tokens are stored offline and can be shared and validated by [Consumer 💼 domains](<../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>).


    ---
    <br/>


1. **What is NLWeb's approach to location-based interactions?**

    While NLWeb advocates for ambient computing, it does not advocate for the ambient to proactively initiate the interactions (e.g., showing personalized ads to a person when they are standing on a bus stop).
    
    - These solutions typically require either location features enabled on the user's phone (like accurate GPS location) or proximity features (like the proximity bluetooth feature used during the 2020 pandemic), both impacting the user's privacy and the battery life of their mobile devices.

    - Instead, NLWeb advocates for [Chat 💬](<../35 💬 Chats/Chats 💬/💬 Chat.md>) interactions to always start with the user's explicit intent, either by [scanning ✨ a QR code](<../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰✨ Wallet QR scan.md>) or by [tapping 🔆 an NFC tag](<../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>).

    ---
    <br/>


1. **What is NLWeb's approach to end-user autofill?**

    NLWeb advocates for domains to ask users for well-known common data types (e.g., address) instead of generic text values. 

    - Users [bind 🔗](<../30 🧩 Data/Binds 🔗/🔗 Bind.md>) their [Wallet 🧑‍🦰 app](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) to multiple [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) holding parts of their personal data (e.g., banks, hospitals, governments);

        - this mirrors real-world interactions, where citizens typically trust organizations to hold their personal data, from traditional  [medical records 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/01 🕵 Profiling landscape/05 📺 Medical records.md>) to digital [family photos 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/01 🕵 Profiling landscape/02 📺 Social media.md>).

    - However, users don't control the [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>), unlike in [Solid 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/05 📺 Berners-Lee vaults.md>) and [Affinidi 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/12 📺 Affinidi.md>);

        - this also mirrors real-world expectations, where citizens typically expect organizations to be responsible for the infrastructure required to hold their data, whatever any effort required from the citizen to manage or even know about such infrastructure.

    - Nonetheless, [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) may require users to provide a shared [Storage 🗃️ vault](<../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>) to store the user's data;
 
        - this is a [Solid 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/05 📺 Berners-Lee vaults.md>)-like user-centric [Vault 🗄️ domain](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) that other [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) may leverage to address [sovereignty 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/02 🏳️ Sovereignty landscape/00 🏳️ Sovereignty index.md>) regulations 
        - e.g., a US-based [Vault 🗄️ domain](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) may store the data of a German citizen in the citizen's Germany-based [Storage 🗃️ vault](<../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>).

    - Those [bounded 🔗](<../30 🧩 Data/Binds 🔗/🔗 Bind.md>) [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) allow users to quickly [autofill 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/06 📺 SSI form auto filling.md>) forms;

        - this is similar to the autofill feature of the [main web browsers 🖼️](<../../2 🏔️ Landscape/1 💼 Business landscape/04 👀 Advertising landscape/12 🖼️ Top-browsers.md>), but done in a distributed way instead of concentrating user data in a centralized cloud database owned by the browser's manufacturer.

    - Data is shared as data sets validated by [Schema Codes 🧩](<../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>), instead of as individual properties, thus not allowing [selective disclosure 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/07 📺 SSI selective disclosure.md>);

        - this also mirrors real-world interactions, where users typically hand-over to organization employees their physical documents with multiple data points (e.g., driver's license, passport).
  
    - [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) may allow users to change their stored data via the user's [Editor 🧑‍💻 domain](<../50 🫥 Agent domains/Editors 🧑‍💻/🧑‍💻🫥 Editor agent.md>);

        - this is a user-centric interface that allows a user to edit their data in multiple [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) from a single editor;

        - [Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) may require users to have a [Editor 🧑‍💻 domain](<../50 🫥 Agent domains/Editors 🧑‍💻/🧑‍💻🫥 Editor agent.md>) to avoid having to build a user interface.
    
    ---
    <br/>

1. **What is NLWeb's approach to end-user payments?**

    NLWeb integrates payments in [Chats 💬](<../35 💬 Chats/Chats 💬/💬 Chat.md>) between users and [Seller 💵 domains](<../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>). 
    
    - As preconditions, users must first bind their [Wallet 🧑‍🦰 apps](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) to one or more [Payer 💳 vaults](<../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) (e.g., their bank), while [Seller 💵 domains](<../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) must bind to [Collector 🏦 vaults](<../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) (e.g., a payment gateway). 

    - The payment is sent from the [user's Payer 💳 vault](<../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) (on behalf of the user) to the [Seller's Collector 🏦 vault](<../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) (on behalf of the [Seller 💵 domain](<../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>)). 
    
    In a [Chat 💬](<../35 💬 Chats/Chats 💬/💬 Chat.md>): 
    1. the [Seller 💵 domain](<../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) requests a payment amount (e.g., 123.45 USD) - the user accepts; 
    2. the [user's Payer 💳 vault](<../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>)  asks for the user's preferred payment method (e.g., my company card, my bank account, agreed credit note) - the user selects one; 
    3. depending on the risk associated (e.g., amount, Seller, date/time) the [user's Payer 💳 vault](<../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>)  may ask for an authentication method (e.g., face scan, OTP); 
    4. the [user's Payer 💳 vault](<../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) shares the receipt; 
    5. the [Seller 💵 domain](<../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) shares the order/invoice and delivers/promises the product/service.
 
    ---

<!--
    ---
1. **What is NLWeb's approach to ads?**

    NLWeb advocates for cross-selling on next-best actions for the user based on personalization and context awareness;
    
     - e.g., when buying an airline ticket, the airline may say *"it may take 30 minutes to pass security in Heathrow on Monday morning - do you want to buy fast-track for £12.50?"*. 
    
    For that, NLWeb supports supply and demand matching at the end of chats: 
    
    1. chat [Host 🤗 domain](<../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) sends a summary of the [Chat 💬](<../35 💬 Chats/Chats 💬/💬 Chat.md>) to the user's [Wallet 🧑‍🦰 app](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>); 
    2. the [Wallet 🧑‍🦰 app](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) generates a list of next-best actions based on user preferences and contextual awareness; 
    3. the [Wallet 🧑‍🦰 app](<../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) then maps the actions to available offers and generates a recommendation for the user. 

    ---

-->