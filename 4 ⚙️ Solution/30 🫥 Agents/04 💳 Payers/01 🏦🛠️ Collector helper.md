🏦 Collector domains FAQ
===

1. **What is a Collector domain in NLWeb?**

    A [Collector 🏦](<01 🏦🛠️ Collector helper.md>) is 
    * any [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) 
    * that other [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) can leverage 
    * to collect payments from [Payer 💳 domains](<03 💳🎭 Payer role.md>);
    * e.g., a traditional bank, with a simple bank account.
    
    ---

1. **How do Collectors work?**

    ![](<00 📎 Assets/💳 Collector.png>)

    |#|Step
    |-|-
    |1| A [Payer 💳 domain](<03 💳🎭 Payer role.md>) receives an order to make a payment, either from a user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) in a business-to-consumer (B2C) transaction, or from a [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) in a business-to-business (B2B) transaction.
    |2| The [Payer 💳 domain](<03 💳🎭 Payer role.md>) then performs a traditional payment to a [Collector 🏦 helper domain](<01 🏦🛠️ Collector helper.md>).
    |3| The [Collector 🏦 domain](<01 🏦🛠️ Collector helper.md>)issues a traditional receipt back to the [Payer 💳 domain](<03 💳🎭 Payer role.md>).
    |4| The [Collector 🏦 domain](<01 🏦🛠️ Collector helper.md>)notifies the recipient [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) that the payment was successful.
    ---

2. **Why are Collectors important?**

    [Collector 🏦 domains](<01 🏦🛠️ Collector helper.md>) offload from domains the undifferentiated heavy lifting of integrating B2B and B2C payment methods at a global scale:

    - e.g. for a restaurant business in Portugal to receive a 100€ payment from a Chinese tourist, they just need to request a 100€ token from their [Collector 🏦 domain](<01 🏦🛠️ Collector helper.md>) and share it with the tourist's [Payer 💳 agent](<03 💳🎭 Payer role.md>);
    - the tourist may decide to pay using China's WeChat, paying any eventual WeChat payment fees, but that's completely irrelevant for the business;
    - the restaurant may need to pay a fee to their [Collector 🏦 domain](<01 🏦🛠️ Collector helper.md>), but that's also completely irrelevant for the tourist.

    ---

3. **How does a domain withdraw its money from a Collector?**
    
    How a recipient [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) receives the money on their bank account depends on the [Collector 🏦 domain](<01 🏦🛠️ Collector helper.md>) - options are as follows.

    | Option | Example | Description
    |-|-|-
    | **Direct** | Visa | the [Payer 💳 domain](<03 💳🎭 Payer role.md>) transfers directly to the recipient's bank account.
    | **Proxy** | G.Wallet | the [Payer 💳 domain](<03 💳🎭 Payer role.md>) pays to the [Collector 🏦 domain](<01 🏦🛠️ Collector helper.md>), who then transfers to the recipients's bank account.
    | **Wallet** | PayPal | the [Payer 💳 domain](<03 💳🎭 Payer role.md>) pays to the [Collector 🏦 domain](<01 🏦🛠️ Collector helper.md>), who holds the money until withdrawn by the recipient.

    ---

4. **What responsibilities do Collectors have with receipts?**

    For fiscal purposes, [Collector 🏦 domains](<01 🏦🛠️ Collector helper.md>) are responsible for:
    - issuing receipts on behalf of the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>), 
    - sharing those receipts with the [Payer 💳 domains](<03 💳🎭 Payer role.md>),
    - and archiving those receipts for a given legal duration. 

    ---

5. **Do Collectors have invoicing responsibilities?**

    No.
    * [Collector 🏦 domains](<01 🏦🛠️ Collector helper.md>) don't have invoicing responsibilities on the NLWeb protocol, but they may implement the feature for simple invoices as an option when issuing receipts.
    * This is especially relevant for startups and SMBs.

    ---

6. **Can a Collector be use in boutique's cash register?**

    Yes. Here's a possible configuration for [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) admins:
    - add [🔆 NFC/QR Locators](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) on both sides of the counter;
    - issue cashier [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) from your [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>);
    - create check-out workflows for cashier and customers.

    Set the cashier workflow as follows:
    - 1/ cashiers tap the inner counter to start a chat:
    - 2/ cashiers select "checkout" and scan all items; 
    - 3/ cashiers confirm the total and ask the user to tap:

    Set the customer workflow as follows:
    - 1/ customers tap the outer counter to start a chat;
    - 2/ the Host immediately charges customers with the total;
    - 3/ customers' [Payer 💳 agent](<03 💳🎭 Payer role.md>) ask for the preferred payment method;
    - 4/ customers pay and see the receipt on their [Payer 💳 agent](<03 💳🎭 Payer role.md>). 


    ---

1. **Can a Collector be use in a supermarket self-checkout?**

    Yes. Here's a possible configuration for [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) admins:
    - add [NFC/QR Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) on the checkout stations;
    - create a check-out workflow for customers.

    Set the customer workflow as follows:
    - 1/ customers tap the checkout station to start a chat;
    - 2/ customers select "scan" and scan all items;
    - 3/ customers select "pay" and accept the total;
    - 4/ customers' [Payer 💳 agent](<03 💳🎭 Payer role.md>) ask for the preferred payment method;
    - 5/ customers pay and see the receipt on their [Payer 💳 agent](<03 💳🎭 Payer role.md>).

    ---

2. **Can a Seller implement the Collector API?**

    Yes, but that's not recommended. 
    - A [Collector 🏦 domain](<01 🏦🛠️ Collector helper.md>) may be better suited to sign wide international agreements with multiple [Payer 💳](<03 💳🎭 Payer role.md>) and [Biller 🤝 domains](<06 🤝🛠️ Biller helper.md>), and support a multitude of payment options.

    ---
