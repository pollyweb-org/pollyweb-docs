💳 Payer domains FAQ
===

1. **What is a Payer domain in NLWeb?**

    A Payer 💳 is a [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) that performs payments to [Collector 🏦 domains](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>) under the following responsibilities.

    * **[Payer 💳🫥 agents](<03 💳🫥 Payer agent.md>)**: 
      * Payers 💳 act as [Agent 🫥 vaults](<../00 Entities/🫥 Agent vault.md>)
      * for users with [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), 
      * interacting in [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with [Seller 💵 hosts](<01 💵🎭 Seller role.md>).
    
    * **[Payer 💳🛠️ helpers](<04 💳🛠️ Payer helper.md>)**:
      * Payers 💳 act as [Helper 🛠️ domains](<../00 Entities/🛠️ Helper domain.md>)
      * for other [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>), 
      * paying for agreements with [Biller 🤝 helpers](<06 🤝🛠️ Biller helper.md>).

    ---
    
2. **How are user payments processed for users?**

    ![](<00 📎 Assets/💳 Payer.png>)

    On NLWeb, payment transactions with users are handled between:
    * [Sellers 💵](<01 💵🎭 Seller role.md>) -  these are [Consumer 💼](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) domains that request payments;
    * Payers 💳 - these are user-bound [Vaults 🗄️](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) with access to the user's money; and
    * [Collector 🏦 helpers](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>) - these are [Helper 🛠️ domains](<../00 Entities/🛠️ Helper domain.md>) able to deposit money on the [Sellers 💵](<01 💵🎭 Seller role.md>) bank account. 
    
    Upon check-out, 
    - 1/ the [Seller 💵](<01 💵🎭 Seller role.md>) registers the upcoming payment to their [Collector 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>), 
    - 2/ the [Seller 💵](<01 💵🎭 Seller role.md>) requests a payment from the user, 
    - 3/ the user delegates the payment to a Payer 💳, 
    - 4/ the user's Payer 💳 transfers the money to the [Seller's 💵](<01 💵🎭 Seller role.md>) [Collector 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>), and 
    - 5/ the [Collector 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>) notifies the [Seller 💵](<01 💵🎭 Seller role.md>) that the transaction was paid.

    ---

3. **What user problems do Payers solve?**

    Read the [User challenges 🧑 ](<../../../2 🏔️ Landscape/1 💼 Business landscape/05 💳 Payments landscape/01 🧑 User challenges.md>) section of the [Payments landscape FAQ 💳](<../../../2 🏔️ Landscape/1 💼 Business landscape/05 💳 Payments landscape/00 💳 Payments index.md>).

    ---
    
4. **What responsibilities do Payers have in a payment?**

    Payers 💳 are responsible for:
    - receiving payment requests from [Collectors 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>);
    - memorizing the user's available payment methods;
    - collecting the payment from the user's selected payment method:
        - e.g., Visa, American Express, Google Pay, Brazilian Pix, Portuguese MBWay;
    - collecting any additional fees to pay the user's selected payment method;
    - converting the user's payment to the Collectors currency;
    - transferring the payment to Collectors over an agreed transfer protocol: 
        - e.g., national bank transfer, internal SWIFT, TransferWise, Western Union;
    - storing the payment receipts on behalf of users.

    ---

5. **How are currency conversions handled?**

    Payers 💳 are responsible for converting the currency to the [Seller's 💵](<01 💵🎭 Seller role.md>) price.

    - [Sellers 💵](<01 💵🎭 Seller role.md>) always receive payments in their requested currency and in the exact amount requested.
  
    - Payers 💳 calculate the final amount to be paid by the user after the currency conversion from the selected payment method, plus conversion, transfer, and administrative fees.

    ---

6. **Why not leverage the Open Banking protocol?**

    While NLWeb follows the Open Banking rational for payments, it requires features not available in Open Banking;
    - e.g., the ability to jump between bank entities from within a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) in the user's [Wallet app 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    
7. **What responsibilities do Payers have with invoices?**

    None. [Collectors 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>) are responsible for invoices.

    ---
    
8. **How does a user bind to their traditional bank?**

    The bank needs to onboard into NLWeb as a Payer 💳.

    ---
    
9. **What happens if a transaction is cancelled?**

    Typically, the money is reverted, but it depends on the relationship between the Payer 💳 and the [Collector 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>).

    ---
    
    
10. **How does it differ from India's ONDC?**

    The [Open Network for Digital Commerce (ONDC) 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/09 🛒 Shopping landscape/01 📺 🇮🇳 India's ONDC.md>) is a centralized shared network specific for the retail industry in India. 
    - NLWeb can also address that niche, 
        - but NLWeb os a generalist, global, and distributed protocol based on natural language.  
    - Conversely, NLWeb is against any form of central governance for payments 
        - i.e., there should be multiple channels for Payers 💳 and [Collectors 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>) to communicate;
        - e.g., if SWIFT doesn't work, send it via TransferWise.

    ---
    
11. **Does NLWeb allow a user to type a credit card number?**

    Although technically possible, it is highly discouraged. 
    - NLWeb advocates for minimum user-typing during a transaction. 
    - Instead, businesses should rely on the user's payment vaults to handle the payment in a standard frictionless way within the check-out phase.

    ---
    
12. **Does NLWeb allow users to pay with NFC contactless?**

    No. NLWeb does not use the standard payment NFC protocol. 
    
    - However, users can tap on a NLWeb [🔆 NFC Locator](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) with their devices to check out an NLWeb transaction, while continuing to use the device's standard NFC payments for traditional point of sale (POS) terminals. 
    
    - The user experience should be similar in both cases, but with NLWeb there is no need for businesses to acquire expensive payment terminals because the UX is in the user's device - only a passive NFC tag costing less than $1 is required.

    ---
    
13. **Does NLWeb allow for offline payments in airplanes?**

    No. NLWeb requires internet connectivity on the user's device. 
    
    - This will be a non-problem soon, as internet becomes ubiquitous. 
    - [Starlink 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/03 📺 Starlink @ phones.md>) and [Project Kuiper 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/04 📺 Amazon's Kuiper.md>) will provide internet [worldwide 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/01 📺 Starlink @ remote areas.md>) and [in airplanes 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/02 📺 Starlink @ airplanes.md>).
    - Cities will provide free public Wi-Fi underground, like the Elizabeth Line in London. 

    ---
    
14. **Do Payers transfer money to collectors, or pay by card?**

    Payers 💳 and [Collectors 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>) may support multiple ways to transact. 
    
    - When multiple choices are possible, Payers 💳 may ask the user for their preference. 
    - The exact payment method will depend on the transfer methods supported by both parties (e.g., SWIFT, TransferWise), and the user configurations supported by the Payer 💳 (e.g., Visa, MasterCard, Brazilian Pix).

    ---
    
15. **Can a payment be reverted or cancelled?**

    Yes. [Collectors 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>) can do initiate it, but Payers 💳 can't.

    ---
    
16. **Can payments be done with credit/debit notes?**

    Yes, as long as the Payer 💳 and the [Collector 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>) support it.

    ---
    
17. **After a payment, do users receive the Seller's receipt?**

    No. 
    
    - Receipts and invoices are created by the [Seller 💵](<01 💵🎭 Seller role.md>)'s [Collector 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>) domain, and are sent to the user's Payer 💳 domain. 
    
    - Users should ask their Payer 💳 domain for the receipt:
        - e.g., a payment gateway may allow the receipts to be downloaded from the transaction list on their website, or they can send each receipt to a chat window every time there is a payment. 
    
    - For user data protection and device storage optimization, NLWeb discourages domains from sending receipts via chat to be downloaded on the device.

    ---
    
18. **Why not use blockchain to perform the money transfer?**

    NLWeb discourages the usage of blockchain in this scenario for multiple reasons:

    - **simplicity:** if only two entities (Payer 💳 and [Collector 🏦](<../01 📦 Storage/03 🏦🛠️ Collector helper.md>)) need to communicate, then two simple mutually authenticated API endpoints are enough to do the job.
  
    - **scalability:** blockchain's performance degrades as the number of parties increase, which is incompatible with a protocol supporting billions of users;
        - e.g., Sam Altman's [World 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/11 📺 Sam Altman's World.md>) moved from blockchain to an proprietary protocol in 2024 for their digital currency due to scalability limitations.
    
    - **geo-political resilience:** in the case of a international conflict, two sovereign nations don't want to depend on a third nation to "authorize" money transfers between the first two;
        - e.g., during the Russia-Ukraine conflict, the international community imposed SWIFT payment restrictions to Russia.

    ---
    
19. **How is money laundry prevented?**

    NLWeb leverages payment transfers to be made using existing platforms and transfers protocols that already have international guardrails implemented, thus inheriting these guardrails.

    ---

20. **Can Payers read card details from Persona vaults?**

    No.

    - For design simplicity, Payers 💳 store user's card details instead of pulling them from [Persona 🧢](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) vaults.
    - Storing card details required special security settings defined by PCI/DSS policies, which Payers already hold but [Persona 🧢](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) vaults would have to implement.

---