#TODO

Design Decisions
===

The following principles for distributed system design were borrowed from Amazon S3 and applied to NLWeb:
- **Decentralization**: Use fully decentralized techniques to remove scaling bottlenecks and single points of failure.
- **Asynchrony**: The system makes progress under all circumstances.
- **Autonomy**: The system is designed such that individual components can make decisions based on local information.
- **Local responsibility**: Each individual component is responsible for achieving its consistency; this is never the burden of its peers.
- **Controlled concurrency**: Operations are designed such that no or limited concurrency control is required.
- **Failure tolerant**: The system considers the failure of components to be a normal mode of operation, and continues operation with no or minimal interruption.
- **Controlled parallelism**: Abstractions used in the system are of such granularity that parallelism can be used to improve performance and robustness of recovery or the introduction of new nodes.
- **Decompose into small well-understood building blocks:** Do not try to provide a single service that does everything for everyone, but instead build small components that can be used as building blocks for other services.
- **Symmetry**: Nodes in the system are identical in terms of functionality, and require no or minimal node-specific configuration to function.
- **Simplicity**: The system should be made as simple as possible (but no simpler).



    ---
1. **What is NLWeb's approach to digital signatures?**

    NLWeb advocates for files to be shared in PDF or PNG, with a Token added to the metadata of the PDF. Both PDF and PNG formats support custom metadata, so senders can sign the files and receivers can verify the file's signature.

1. **What is NLWeb's approach to end-user natural language?**

    NLWeb is designed for Q&A flows (like ChatGPT), where the domain asks the questions and defines the format that users are allowed to answer them. 
    
    Although domains can implement their own chat logic, NLWeb advocates for domains to take advantage of pre-defined chat automations: 
    - 1/ search to identify the user's intent in the beginning of a chat; 
    - 2/ well-defined intent workflows; 
    - 3/ schema-based CRUD navigation; 
    - 4/ asset summarization to answer domain-specific queries; and 
    - 5/ next best actions for cross-selling.

1. **What is NLWeb's approach to conversational commerce?**

    In NLWeb, wallets are the way to communicate with domains. Similar to Meta's WhatsApp, wallets allow users to keep a list of active chats with domains. 
    * Like in India's ONDC, domains can configure multiple types of user inputs (e.g., number, dropdown, calendar). 
    * New chats are opened by scanning a QR code or by tapping an NFC tag. 
    * Users may accept tokens issued by domains - these tokens are stored offline and can be shared and validated by other domains.

1. **What is NLWeb's approach to end-user autofill?**

    NLWeb advocates for domains to ask users for well-known common data types (e.g., address) instead of generic text values. Users bind their wallets to vaults holding their personal data (e.g., banks, hospitals, governments) but users don't control the vaults (unlike in Solid). A user may bind to multiple vaults holding multiple data types. Those bounded vaults allow users to quickly fill out forms.

    ---
1. **What is NLWeb's approach to end-user payments?**

    NLWeb integrates payments in chats between users and [Sellers 💵](<../30 🫥 Agents/04 💳 Payers/02 💵🎭 Seller role.md>). As preconditions, users must first bind their [Wallets 🧑‍🦰](<../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to one or more payment vaults (e.g., their bank), while Seller domains must bind to collection vaults (e.g., a payment gateway). The payment is sent from the [Payer 💳](<../30 🫥 Agents/04 💳 Payers/01 💳🫥 Payer agent.md>) (on behalf of the user) to the [Collector 🏦](<../30 🫥 Agents/04 💳 Payers/03 🏦👥 Collector helper.md>) (on behalf of the Seller). 
    
    In a chat: 
    - 1/ the Seller requests a payment amount (e.g., 123.45 USD) - the user accepts; 
    - 2/ the Payer asks for the user's preferred payment method (e.g., my company card, my bank account, agreed credit note) - the user selects one; 
    - 3/ depending on the risk associated (e.g., amount, Seller, date/time) the Payer may ask for an authentication method (e.g., face scan, OTP); 
    - 4/ the Payer shares the receipt; 
    - 5/ the Seller shares the order/invoice and delivers/promises the product/service.

    ---
1. **What is NLWeb's approach to subscriptions?**

    NLWeb supports subscriptions via Payer and Collector domains (explore to the payment sections for details). 

    ---
1. **What is NLWeb's approach to ads?**

    NLWeb advocates for cross-selling on next-best actions for the user based on personalization and context awareness (e.g., when buying an airline ticket, the airline may say "it may take 30 minutes to pass security in Heathrow on Monday morning - do you want to buy fast-track for £12.50"). 
    
    For that, NLWeb supports supply and demand matching at the end of chats: 
    - 1/ the chat Host sends a summary of the conversation to the user's wallet; 
    - 2/ the wallet generates a list of next-best actions based on user preferences and contextual awareness; 
    - 3/ the wallet then maps the actions to available offers and generates a recommendation for the user. 