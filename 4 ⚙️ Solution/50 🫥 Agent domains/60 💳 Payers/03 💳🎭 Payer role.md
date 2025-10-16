💳🎭 Payer domain role
===

1. **What is a Payer domain in NLWeb?**

    A Payer 💳 is any [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) that sends payments to [Collector 🏦 domains](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>) under two categories:

    * **[Payer 💳🫥 agents](<04 💳🫥 Payer agent.md>)**: 
        * these are [Payer 💳 domains](<03 💳🎭 Payer role.md>) that act as [Agent 🫥 vaults](<../$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>)
        * for users with [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>), 
        * interacting in [Chats 💬](<../../35 Chats/💬 Chats/💬 Chat.md>) with [Seller 💵 hosts](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>).
      
    * **[Payer 💳🤲 Helpers](<../../45 🤲 Helper domains/70 💳 Payers/💳🤲 Payer helper.md>)**:
        * these are [Payer 💳 domains](<03 💳🎭 Payer role.md>) that act as [Helper 🤲 domains](<../../45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>)
        * for other [domains 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>), 
        * paying for agreements with [Biller 🤝 helpers](<../../45 🤲 Helper domains/20 🤝 Billers/🤝🤲 Biller helper.md>).

    ---
    <br/>
    

1. **How are currency conversions handled?**

    Payers 💳 are responsible for converting the currency to the price of the [Seller 💵 domain](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>).

    - [Seller 💵 domains](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>) always receive payments in their requested currency and in the exact amount requested.
  
    - Payers 💳 calculate the final amount to be paid by the user after the currency conversion from the selected payment method, plus conversion, transfer, and administrative fees.

    ---
    <br/>

1. **Why not leverage the Open Banking protocol?**

    While NLWeb follows the Open Banking rational for payments, it requires features not available in Open Banking;
    - e.g., the ability to jump between bank entities from within a [Chat 💬](<../../35 Chats/💬 Chats/💬 Chat.md>) in the user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).

    ---
    <br/>
    
1. **What responsibilities do Payers have with invoices?**

    None. 
    * [Collector 🏦 domains](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>) are responsible for invoices.

    ---
    <br/>
    
1. **How does a user bind to their traditional bank?**

    The bank needs to onboard into NLWeb as a [Payer 💳 domain](<03 💳🎭 Payer role.md>).

    ---
    <br/>
    
1. **What happens if a transaction is cancelled?**

    Typically, the money is reverted, but it depends on the relationship between the [Payer 💳 domain](<03 💳🎭 Payer role.md>) and the [Collector 🏦 domain](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>).

    ---
    <br/>
    
    
7.  **How does it differ from India's ONDC?**

    The [Open Network for Digital Commerce (ONDC) 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/09 🛒 Shopping landscape/01 📺 🇮🇳 India's ONDC.md>) is a centralized shared network specific for the retail industry in India. 
    - NLWeb can also address that niche, 
        - but NLWeb os a generalist, global, and distributed protocol based on natural language.  
    - Conversely, NLWeb is against any form of central governance for payments 
        - i.e., there should be multiple channels for [Payer 💳 domains](<03 💳🎭 Payer role.md>) and [Collector 🏦 domains](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>) to communicate;
        - e.g., if SWIFT doesn't work, send it via TransferWise.

    ---
    <br/>
    
8.  **Does NLWeb allow a user to type a credit card number?**

    Although technically possible, it is highly discouraged. 
    - NLWeb advocates for minimum user-typing during a transaction. 
    - Instead, businesses should rely on the user's payment vaults to handle the payment in a standard frictionless way within the check-out phase.

    ---
    <br/>
    
9.  **Does NLWeb allow users to pay with NFC contactless?**

    No. NLWeb does not use the standard payment NFC protocol. 
    
    - However, users can tap on a NLWeb [🔆 NFC Locator](<../../25 Locators/1 🔆 Locators/🔆 Locator.md>) with their devices to check out an NLWeb transaction, while continuing to use the device's standard NFC payments for traditional point of sale (POS) terminals. 
    
    - The user experience should be similar in both cases, but with NLWeb there is no need for businesses to acquire expensive payment terminals because the UX is in the user's device - only a passive NFC tag costing less than $1 is required.

    ---
    <br/>
    
1. **Does NLWeb allow for offline payments in airplanes?**

    No. NLWeb requires internet connectivity on the user's device. 
    
    - This will be a non-problem soon, as internet becomes ubiquitous. 
    - [Starlink 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/03 📺 Starlink @ phones.md>) and [Project Kuiper 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/04 📺 Amazon's Kuiper.md>) will provide internet [worldwide 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/01 📺 Starlink @ remote areas.md>) and [in airplanes 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/02 📺 Starlink @ airplanes.md>).
    - Cities will provide free public Wi-Fi underground, like the Elizabeth Line in London. 

    ---
    <br/>
    
1. **Do Payers transfer money to collectors, or pay by card?**

    [Payer 💳 domains](<03 💳🎭 Payer role.md>) and [Collector 🏦 domains](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>) may support multiple ways to transact. 
    
    - When multiple choices are possible, [Payer 💳 domains](<03 💳🎭 Payer role.md>) may ask the user for their preference. 
    - The exact payment method will depend on the transfer methods supported by both parties (e.g., SWIFT, TransferWise), and the user configurations supported by the [Payer 💳 domain](<03 💳🎭 Payer role.md>) (e.g., Visa, MasterCard, Brazilian Pix).

    ---
    <br/>
    
1. **Can a payment be reverted or cancelled?**

    Yes. 
    * [Collector 🏦 domains](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>) can initiate it, but [Payer 💳 domains](<03 💳🎭 Payer role.md>) can't.

    ---
    <br/>
    
1. **Can payments be done with credit/debit notes?**

    Yes, as long as the [Payer 💳 domain](<03 💳🎭 Payer role.md>) and the [Collector 🏦 domain](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>) support it.

    ---
    <br/>
    

    
1. **Why not use blockchain to perform the money transfer?**

    NLWeb discourages the usage of blockchain in this scenario for multiple reasons:

    - **simplicity:** if only two entities ([Payer 💳 domain](<03 💳🎭 Payer role.md>) and [Collector 🏦 domain](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>)) need to communicate, then two simple mutually authenticated API endpoints are enough to do the job.
  
    - **scalability:** blockchain's performance degrades as the number of parties increase, which is incompatible with a protocol supporting billions of users;
        - e.g., Sam Altman's [World 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/11 📺 Sam Altman's World.md>) moved from blockchain to an proprietary protocol in 2024 for their digital currency due to scalability limitations.
    
    - **geo-political resilience:** in the case of a international conflict, two sovereign nations don't want to depend on a third nation to "authorize" money transfers between the first two;
        - e.g., during the Russia-Ukraine conflict, the international community imposed SWIFT payment restrictions to Russia.

    ---
    <br/>
    
1. **How is money laundry prevented?**

    NLWeb leverages payment transfers to be made using existing platforms and transfers protocols that already have international guardrails implemented, thus inheriting these guardrails.

    ---
    <br/>

1. **Can Payers read card details from Persona vaults?**

    No.
    * For design simplicity, [Payer 💳 domains](<03 💳🎭 Payer role.md>) store user's card details instead of pulling them from [Persona 🧢 vaults](<../70 🧢 Personas/🧢🫥 Persona agent.md>) .
    * Storing card details required special security settings defined by PCI/DSS policies, which [Payer 💳 domains](<03 💳🎭 Payer role.md>) already hold but [Persona 🧢 vaults](<../70 🧢 Personas/🧢🫥 Persona agent.md>) would have to implement.

    ---
    <br/>


1. **Can a group split a bill in equal parts?**

    Yes, but split bills are managed by [Collector 🏦 domains](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>), as in the following examples:
      * [🍽️ Split restaurant bill ](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>);
      * [🚕 Split taxi ride](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/2 🚕 Customer @ Car/23. Split with friends.md>).
    
   

    ---
    <br/>
