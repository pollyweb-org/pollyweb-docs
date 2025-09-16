Design Decisions
===

The following principles for distributed system design were borrowed from Amazon S3 and applied to NLWeb:
- **Decentralization**: Use fully decentralized techniques to remove scaling bottlenecks and single points of failure.
- **Asynchronism**: The system makes progress under all circumstances.
- **Autonomy**: The system is designed such that individual components can make decisions based on local information.
- **Local responsibility**: Each individual component is responsible for achieving its consistency; this is never the burden of its peers.
- **Controlled concurrency**: Operations are designed such that no or limited concurrency control is required.
- **Failure tolerant**: The system considers the failure of components to be a normal mode of operation, and continues operation with no or minimal interruption.
- **Controlled parallelism**: Abstractions used in the system are of such granularity that parallelism can be used to improve performance and robustness of recovery or the introduction of new nodes.
- **Decompose into small well-understood building blocks:** Do not try to provide a single service that does everything for everyone, but instead build small components that can be used as building blocks for other services.
- **Symmetry**: Nodes in the system are identical in terms of functionality, and require no or minimal node-specific configuration to function.
- **Simplicity**: The system should be made as simple as possible (but no simpler).



    ---

## FAQ


1. **What is NLWeb's approach to end-user natural language?**

    NLWeb is designed for Q&A flows (like ChatGPT), where a [Host 🤗](<../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) domain asks the questions and defines the format that users are allowed to answer them. 
    
    Although domains can implement their own chat logic, NLWeb advocates for domains to take advantage of pre-defined chat automations: 

    1. search to identify the user's intent in the beginning of a chat; 
    1. well-defined intent workflows; 
    1. schema-based CRUD navigation; 
    1. asset summarization to answer domain-specific queries; and 
    1. next best actions for cross-selling.

    ---

2. **What is NLWeb's approach to conversational commerce?**

    In NLWeb, [Wallet apps 🧑‍🦰](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets>) are the way for users to communicate with [Host 🤗](<../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) domains. 
    
    - Similar to Meta's [WhatsApp 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/10 💬 Chatting landscape/06 📺 WhatsApp business.md>), NLWeb [Wallet apps 🧑‍🦰](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets>) allow users to keep a list of active [Chats 💬](<../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with [Host 🤗](<../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) domains. 

    - Like in India's [ONDC 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/09 🛒 Shopping landscape/01 📺 🇮🇳 India's ONDC.md>), domains can configure multiple types of user inputs - e.g., number, dropdown, calendar. 
    
    - New chats are opened with a [Locator 🔆](<../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) by scanning a [QR code ✨](<../20 🧑‍🦰 UI/22 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) or by tapping an [NFC tag 🔆](<../20 🧑‍🦰 UI/22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>). 
    
    - Users may accept [Tokens 🎫](<../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) issued by [Issuer 🎴](<../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) domains - these tokens are stored offline and can be shared and validated by [Consumer 💼](<../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) domains.

    ---

3. **What is NLWeb's approach to end-user autofill?**

    NLWeb advocates for domains to ask users for well-known common data types (e.g., address) instead of generic text values. 

    - Users [bind 🔗](<../20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) their [Wallet app 🧑‍🦰](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets>) to multiple [Vaults 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) holding parts of their personal data (e.g., banks, hospitals, governments);

        - this mirrors real-world interactions, where citizens typically trust organizations to hold their personal data, from traditional  [medical records 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/01 🗂️ Profiling landscape/05 📺 Medical records.md>) to digital [family photos 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/01 🗂️ Profiling landscape/02 📺 Social media.md>).

    - However, users don't control the [Vaults 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>), unlike in [Solid 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/05 📺 Berners-Lee vaults.md>) and [Affinidi 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/12 📺 Affinidi.md>);

        - this also mirrors real-world expectations, where citizens typically expect organizations to be responsible for the infrastructure required to hold their data, whatever any effort required from the citizen to manage or even know about such infrastructure.

    - Nonetheless, [Vaults 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) may require users to provide a shared [Storage 📦](<../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) to store the user's data;
 
        - this is a [Solid 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/05 📺 Berners-Lee vaults.md>)-like user-centric [Vault 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) that other [Vaults 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) may leverage to address [sovereignty 📺](<../../2 🏔️ Landscape/1 💼 Business landscape/02 🏳️ Sovereignty landscape/00 🏳️ Sovereignty index.md>) regulations - e.g., a US-based [Vault 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) may store the data of a German citizen in the citizen's Germany-based [Storage 📦](<../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) agent.

    - Those [bounded 🔗](<../20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) [Vaults 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) allow users to quickly [autofill 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/06 📺 SSI form auto filling.md>) forms;

        - this is similar to the autofill feature of the [main web browsers 🖼️](<../../2 🏔️ Landscape/1 💼 Business landscape/04 👀 Advertising landscape/12 🖼️ Top-browsers.md>), but done in a distributed way instead of concentrating user data in a centralized cloud database owned by the browser's manufacturer.

    - Data is shared as data sets validated by [Schema Codes 🧩](<../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>), instead of as individual properties, thus not allowing [selective disclosure 📺](<../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/07 📺 SSI selective disclosure.md>);

        - this also mirrors real-world interactions, where users typically hand-over to organization employees their physical documents with multiple data points (e.g., driver's license, passport).
  
    - [Vaults 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) may allow users to change their stored data via the user's [Folder editor 🗂️](<../20 🧑‍🦰 UI/26 🗂️ Folders/01 🗂️ Folder editor.md>);

        - this is a user-centric interface that allows a user to edit their data in multiple [Vaults 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) from a single editor;

        - [Vaults 🗄️](<../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) may require users to have a [Folder editor 🗂️](<../20 🧑‍🦰 UI/26 🗂️ Folders/01 🗂️ Folder editor.md>) to avoid having to build a user interface.
    
    ---

4. **What is NLWeb's approach to end-user payments?**

    NLWeb integrates payments in chats between users and [Sellers 💵](<../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>). 
    
    - As preconditions, users must first bind their [Wallets 🧑‍🦰](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to one or more [Payer 💳](<../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) vaults (e.g., their bank), while [Seller 💵](<../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) domains must bind to [Collector 🏦](<../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) vaults (e.g., a payment gateway). 

    - The payment is sent from the [Payer 💳](<../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) (on behalf of the user) to the [Collector 🏦](<../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) (on behalf of the Seller). 
    
    In a chat: 
    1. the [Seller 💵](<../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) requests a payment amount (e.g., 123.45 USD) - the user accepts; 
    2. the [Payer 💳](<../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>)  asks for the user's preferred payment method (e.g., my company card, my bank account, agreed credit note) - the user selects one; 
    3. depending on the risk associated (e.g., amount, Seller, date/time) the [Payer 💳](<../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>)  may ask for an authentication method (e.g., face scan, OTP); 
    4. the [Payer 💳](<../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) shares the receipt; 
    5. the [Seller 💵](<../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) shares the order/invoice and delivers/promises the product/service.

    ---
5. **What is NLWeb's approach to subscriptions?**

    NLWeb supports subscriptions via [Payer 💳](<../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) and [Collector 🏦](<../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) domains (explore to the payment sections for details). 

    ---
6. **What is NLWeb's approach to ads?**

    NLWeb advocates for cross-selling on next-best actions for the user based on personalization and context awareness;
    
     - e.g., when buying an airline ticket, the airline may say *"it may take 30 minutes to pass security in Heathrow on Monday morning - do you want to buy fast-track for £12.50?"*. 
    
    For that, NLWeb supports supply and demand matching at the end of chats: 
    
    1. the chat [Host 🤗](<../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) sends a summary of the [Chat 💬](<../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) to the user's [Wallet app 🧑‍🦰](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets>); 
    2. the [Wallet 🧑‍🦰](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets>) generates a list of next-best actions based on user preferences and contextual awareness; 
    3. the [Wallet 🧑‍🦰](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets>) then maps the actions to available offers and generates a recommendation for the user. 

    ---

