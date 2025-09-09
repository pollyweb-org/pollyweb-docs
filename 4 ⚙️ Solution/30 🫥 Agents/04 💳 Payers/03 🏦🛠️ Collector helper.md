🏦 Collector domains FAQ
===

![](<00 📎 Assets/💳 Collector.png>)

1. **What is a Collector domain in NLWeb?**

    A Collector 🏦 is a [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that other [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) can leverage to collect payments. 
    
    * These can be traditional banks, with a simple bank account.
    * Incoming payments are sent by [Payer 💳 domains](<02 💳🎭 Payer role.md>), on behalf of users and [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).
    
    ---

2. **Why are Collectors important?**

    Collectors 🏦 offload from domains the undifferentiated heavy lifting of integrating B2B and B2C payment methods at a global scale:

    - e.g. for a restaurant business in Portugal to receive a 100€ payment from a Chinese tourist, they just need to request a 100€ token from their Collector 🏦 and share it with the tourist's [Payer 💳 agent](<02 💳🎭 Payer role.md>);
    - the tourist may decide to pay using China's WeChat, paying any eventual WeChat payment fees, but that's completely irrelevant for the business;
    - the restaurant may need to pay a fee to their Collector 🏦, but that's also completely irrelevant for the tourist.

    ---

3. **How does a domain withdraw its money?**
    
    It depends on the Collector 🏦 - options may be:
    - **Direct:** the [Payer 💳 domain](<02 💳🎭 Payer role.md>) pays directly to the domain's bank account.
    - **Proxy:** the [Payer 💳 domain](<02 💳🎭 Payer role.md>) pays to the Collector 🏦, who then transfers to the domain's bank account.
    - **Wallet:** the [Payer 💳 domain](<02 💳🎭 Payer role.md>) pays to the Collector 🏦, who holds the money until withdrawn by the domain.

    ---

4. **What responsibilities do Collectors have with receipts?**

    For fiscal purposes, Collectors 🏦 are responsible for:
    - issuing receipts on behalf of the domain, 
    - sharing those receipts with the [Payer 💳 domains](<02 💳🎭 Payer role.md>),
    - and archiving those receipts for a given legal duration. 

    ---

5. **Do Collectors have invoicing responsibilities?**

    No.
    * Collectors 🏦 don't have invoicing responsibilities on the NLWeb protocol, but they may implement the feature for simple invoices as an option when issuing receipts.
    * This is especially relevant for startups and SMBs.

    ---

6. **Can a Collector be use in boutique's cash register?**

    Yes. Here's a possible configuration for domain admins:
    - add [🔆 NFC/QR Locators](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) on both sides of the counter;
    - issue cashier [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) from your domain;
    - create check-out workflows for cashier and customers.

    Set the cashier workflow as follows:
    - 1/ cashiers tap the inner counter to start a chat:
    - 2/ cashiers select "checkout" and scan all items; 
    - 3/ cashiers confirm the total and ask the user to tap:

    Set the customer workflow as follows:
    - 1/ customers tap the outer counter to start a chat;
    - 2/ the Host immediately charges customers with the total;
    - 3/ customers' [Payer 💳 agent](<02 💳🎭 Payer role.md>) ask for the preferred payment method;
    - 4/ customers pay and see the receipt on their [Payer 💳 agent](<02 💳🎭 Payer role.md>). 


    ---

1. **Can a Collector be use in a supermarket self-checkout?**

    Yes. Here's a possible configuration for domain admins:
    - add [NFC/QR Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) on the checkout stations;
    - create a check-out workflow for customers.

    Set the customer workflow as follows:
    - 1/ customers tap the checkout station to start a chat;
    - 2/ customers select "scan" and scan all items;
    - 3/ customers select "pay" and accept the total;
    - 4/ customers' [Payer 💳 agent](<02 💳🎭 Payer role.md>) ask for the preferred payment method;
    - 5/ customers pay and see the receipt on their [Payer 💳 agent](<02 💳🎭 Payer role.md>).

    ---

2. **Can a Seller implement the Collector API?**

    Yes, but that's not recommended. 
    - A Collector 🏦 may be better suited to sign wide international agreements with multiple [Payer 💳](<02 💳🎭 Payer role.md>) and [Biller 🤝](<06 🤝🛠️ Biller helper.md>) domains, and support a multitude of payment options.

    ---
