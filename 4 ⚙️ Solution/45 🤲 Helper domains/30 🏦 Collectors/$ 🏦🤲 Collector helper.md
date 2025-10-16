🏦 Collector domains
===

1. **What is a Collector domain in NLWeb?**

    A [Collector 🏦](<$ 🏦🤲 Collector helper.md>) is 
    * any [Helper 🤲 domain](<../$ 🤲 Helpers/🤲👥 Helper domain.md>) 
    * that other [domains 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) can leverage 
    * to collect payments from [Payer 💳 domains](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>);
    * e.g., a traditional bank, with a simple bank account.
    
    ---
    <br/>

1. **How do Collectors work?**

    ![](<../../50 🫥 Agent domains/60 💳 Payers/. 📎 Assets/💳 Collector.png>)

    |#|Step
    |-|-
    |1| A [Payer 💳 domain](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) receives an order to make a payment, either from a user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) in a business-to-consumer (B2C) transaction, or from a [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) in a business-to-business (B2B) transaction.
    |2| The [Payer 💳 domain](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) then performs a traditional payment to a [Collector 🏦 helper domain](<$ 🏦🤲 Collector helper.md>).
    |3| The [Collector 🏦 domain](<$ 🏦🤲 Collector helper.md>)issues a traditional receipt back to the [Payer 💳 domain](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>).
    |4| The [Collector 🏦 domain](<$ 🏦🤲 Collector helper.md>)notifies the recipient [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) that the payment was successful.

    ---
    <br/>

1. **Why are Collectors important?**

    [Collector 🏦 domains](<$ 🏦🤲 Collector helper.md>) offload from domains the undifferentiated heavy lifting of integrating B2B and B2C payment methods at a global scale:

    - e.g. for a restaurant business in Portugal to receive a 100€ payment from a Chinese tourist, they just need to request a 100€ token from their [Collector 🏦 domain](<$ 🏦🤲 Collector helper.md>) and share it with the tourist's [Payer 💳 agent](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>);
    - the tourist may decide to pay using China's WeChat, paying any eventual WeChat payment fees, but that's completely irrelevant for the business;
    - the restaurant may need to pay a fee to their [Collector 🏦 domain](<$ 🏦🤲 Collector helper.md>), but that's also completely irrelevant for the tourist.

    ---
    <br/>

1. **How does a domain withdraw its money from a Collector?**
    
    How a recipient [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) receives the money on their bank account depends on the [Collector 🏦 domain](<$ 🏦🤲 Collector helper.md>) - options are as follows.

    | Option | Example | Description
    |-|-|-
    | **Direct** | Visa | the [Payer 💳 domain](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) transfers directly to the recipient's bank account.
    | **Proxy** | G.Wallet | the [Payer 💳 domain](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) pays to the [Collector 🏦 domain](<$ 🏦🤲 Collector helper.md>), who then transfers to the recipients's bank account.
    | **Wallet** | PayPal | the [Payer 💳 domain](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) pays to the [Collector 🏦 domain](<$ 🏦🤲 Collector helper.md>), who holds the money until withdrawn by the recipient.

    ---
    <br/>

1. **What responsibilities do Collectors have with receipts?**

    For fiscal purposes, [Collector 🏦 domains](<$ 🏦🤲 Collector helper.md>) are responsible for:
    - issuing receipts on behalf of the [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>), 
    - sharing those receipts with the [Payer 💳 domains](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>),
    - and archiving those receipts for a given legal duration. 

    ---
    <br/>

1. **Do Collectors have invoicing responsibilities?**

    No.
    * [Collector 🏦 domains](<$ 🏦🤲 Collector helper.md>) don't have invoicing responsibilities on the NLWeb protocol, but they may implement the feature for simple invoices as an option when issuing receipts.
    * This is especially relevant for startups and SMBs.

    ---
    <br/>

1. **Can a Collector be use in boutique's cash register?**

    Yes. Here's a possible configuration for [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) admins:
    - add [🔆 NFC/QR Locators](<../../30 Data/15 🔆 Locators/$ 🔆 Locator.md>) on both sides of the counter;
    - issue cashier [Tokens 🎫](<../../30 Data/30 🎫 Tokens/🎫 Token.md>) from your [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>);
    - create check-out workflows for cashier and customers.

    Set the cashier workflow as follows:
    - 1/ cashiers tap the inner counter to start a chat:
    - 2/ cashiers select "checkout" and scan all items; 
    - 3/ cashiers confirm the total and ask the user to tap:

    Set the customer workflow as follows:
    |#| Step
    |-|-
    |1| customers tap the outer counter to start a chat;
    |2| the Host immediately charges customers with the total;
    |3| customers' [Payer 💳 agent](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) ask for the preferred payment method;
    |4| customers pay and see the receipt on their [Payer 💳 agent](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>). 


    ---
    <br/>


1. **Can a Seller implement the Collector API?**

    Yes, but that's not recommended. 
    - A [Collector 🏦 domain](<$ 🏦🤲 Collector helper.md>) may be better suited to sign wide international agreements with multiple [Payer 💳](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) and [Biller 🤝 domains](<../20 🤝 Billers/🤝🤲 Biller helper.md>), and support a multitude of payment options.

    ---
    <br/>


1. **Do Collectors accept split payments?**

    Yes, as in the following examples:
    * [🍽️ Split restaurant bill](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>);
    * [🚕 Split taxi ride](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/2 🚕 Customer @ Car/23. Split with friends.md>).
    
    
    The [Chat 💬](<../../35 Chats/12 💬 Chats/$ 💬 Chat.md>) will be similar to the following.

    | [Domain](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../35 Chats/20 🤔 Prompts/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    |...
    | 🤗 Host | ℹ️ Let me get you the bill.
    | 💳 [Payer](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $12.95 bill? 🧾 [No]  <br/>- [ ✂️ Split bill ] <br/>- ... | > Split bill
    | [🏦 Collector](<$ 🏦🤲 Collector helper.md>) | 😃 Slip by how many? | ↕️ 3
    | [🏦 Collector](<$ 🏦🤲 Collector helper.md>) | ⏳ Waiting for 3x $4.31... <br/>- [ pay my part ]  <br/> - [ cancel split ]| > pay my part
    | 💳 [Payer](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $4.33 partial bill? 🧾 [No] <br/>- [ card ABC ] + $0.10 <br/>- [ card DEF ] (free) | > card ABC
    | 💳 [Payer](<../../50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Add tip? [No, 10%, +] | > 10%
    | 🧢 [Persona](<../../50 🫥 Agent domains/70 🧢 Personas/🧢🫥 Persona agent.md>) | 🫥 Share name? [No] <br/> - [ 🧑‍🦰 personal ] <br/> - [ 💼 work ]  <br/> - [ 🦋 private ]     | > 🧑‍🦰 personal
    | [🏦 Collector](<$ 🏦🤲 Collector helper.md>) | ⓘ Your part paid, thanks! [+]
    | [🏦 Collector](<$ 🏦🤲 Collector helper.md>) | ⏳ Waiting for 2x $4.31... <br/>- [ list payer names ] <br/>- [ pay the reaming ] <br/> - [ cancel split ]
    | [🏦 Collector](<$ 🏦🤲 Collector helper.md>) | ⏳ Waiting for 1x $4.31... <br/>- [ list payer names ] <br/>- [ pay the reaming ] <br/> - [ cancel split ]
    | 🤗 Host       | ✅ Paid, thanks! [+]


    ---
    <br/>