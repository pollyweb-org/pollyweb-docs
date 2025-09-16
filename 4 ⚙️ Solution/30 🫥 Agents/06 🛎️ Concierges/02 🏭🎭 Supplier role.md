🏭 Supplier domain role FAQ
===



1. **What is a Supplier domain role in NLWeb?**

    A [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) with a [Supplier 🏭 role](<02 🏭🎭 Supplier role.md>) is 
    * an [Integrator 🪢 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🪢🎭 Integrator role.md>) 
    * that exposes order APIs 
    * to accept asynchronous order requests from other [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

    ---
    <br/>

1. **How do Suppliers work?**

    ![](<00 📎 Assets/🛎️🏭 Supplier.png>)

    ---
    <br/>

2. **What are examples of Suppliers?**

    * [Printer 🖨️ suppliers](<../../70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) accept orders to print NFC/QR [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>), ship them to a destination, and manage the lifecycle of these Locators.

    * [KeyMaker 🔐 suppliers](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/05  🔐🏭 Keymaker supplier.md>) accept requests to deliver and manage the lifecycle of [Padlock 🔒 device](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>).

    * [Courier 🛵 suppliers](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/04 🍽️ Order pizza 🍕/08 🍕 Driver @ Road 🛵/02 🛵 Pick-up.md>) accept orders to deliver pizzas, as requested by a [Concierge 🛎️ domain](<01 🛎️🫥 Concierge agent.md>). 

    ---
    <br/>

3. **What are examples of order requesters?**

    * When users have tasks to complete, [Concierge 🛎️ domains](<01 🛎️🫥 Concierge agent.md>) send order requests to Suppliers 🏭 for them to perform steps in those tasks.

    ---
    <br/>

4. **How many responses are expected per order?**

    A request to a Supplier 🏭 will receive one or more asynchronous updated events.

    ---
    <br/>

5. **Are order rejections synchronous?**

    No. Adding an order to a Supplier 🏭 doesn't return a synchronous response.

    ---
    <br/>

6. **Can Suppliers answer natural language questions?**

    Yes, if that is supported by their API.

    ---
    <br/>

7. **Can Suppliers use other Suppliers for sub tasks?**

    Yes, Supplier 🏭 can use other sub-Suppliers if they want to - there's no restriction to do so.

    ---
    <br/>

8. **Can requesters know about the details of sub-Suppliers?**

    No. Requesters send order requests to Suppliers 🏭 but don't know which sub-Suppliers they speak with.

    ---
    <br/>

9.  **How can Suppliers be implemented?**

    Suppliers 🏭 will typically:
    - use LLMs to understand requests in natural language;
    - use Agentic AI to orchestrate and execute the requests;
    - use crowd sourcing platforms like Amazon Mechanical Turk and Task Rabbit.

    ---
    <br/>
