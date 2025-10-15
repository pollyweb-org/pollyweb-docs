🏭 Supplier domain role
===



1. **What is a Supplier domain role in NLWeb?**

    A [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) with a [Supplier 🏭 role](<$ 🏭🎭 Supplier role.md>) is 
    * an [Integrator 🪢 domain](<../35 🪢 Integrators/$ 🪢🎭 Integrator role.md>) 
    * that exposes order APIs 
    * to accept asynchronous order requests from other [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>).

    ---
    <br/>

1. **How do Suppliers work?**

    ![](<../../50 🫥 Agents/25 🛎️ Concierges/. 📎 Assets/🛎️🏭 Supplier.png>)

    ---
    <br/>

1. **What are examples of Suppliers?**

    * [Printer 🖨️ suppliers](<../../45 🛠️ Helper domains/75 🖨️ Printers/$ 🖨️🛠️ Printer helper.md>) accept orders to print NFC/QR [Locators 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>), ship them to a destination, and manage the lifecycle of these Locators.

    * [KeyMaker 🔐 suppliers](<../../45 🛠️ Helper domains/58 🔐 Keymakers/05  🔐🏭 Keymaker supplier.md>) accept requests to deliver and manage the lifecycle of [Padlock 🔒 device](<../../70 🌳 Ambient/75 🔒 Padlocks/01 🔒 Padlock device.md>).

    * [Courier 🛵 suppliers](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/82 🛵 Driver: Pick-up.md>) accept orders to deliver pizzas, as requested by a [Concierge 🛎️ domain](<../../50 🫥 Agents/25 🛎️ Concierges/$ 🛎️🫥 Concierge agent.md>). 

    ---
    <br/>

1. **What are examples of order requesters?**

    * When users have tasks to complete, [Concierge 🛎️ domains](<../../50 🫥 Agents/25 🛎️ Concierges/$ 🛎️🫥 Concierge agent.md>) send order requests to [Supplier 🏭 domains](<$ 🏭🎭 Supplier role.md>) for them to perform steps in those tasks.

    ---
    <br/>

1. **How many responses are expected per order?**

    A request to a [Supplier 🏭 domain](<$ 🏭🎭 Supplier role.md>) will receive one or more asynchronous updated events.

    ---
    <br/>

1. **Are order rejections synchronous?**

    No. Adding an order to a [Supplier 🏭 domain](<$ 🏭🎭 Supplier role.md>) doesn't return a synchronous response.

    ---
    <br/>

1. **Can Suppliers answer natural language questions?**

    Yes, if that is supported by their API.

    ---
    <br/>

1. **Can Suppliers use other Suppliers for sub tasks?**

    Yes, [Supplier 🏭 domains](<$ 🏭🎭 Supplier role.md>) can use other sub-Suppliers if they want to - there's no restriction to do so.

    ---
    <br/>

1. **Can requesters know about the details of sub-Suppliers?**

    No. Requesters send order requests to [Supplier 🏭 domains](<$ 🏭🎭 Supplier role.md>) but don't know which sub-Suppliers they speak with.

    ---
    <br/>

9.  **How can Suppliers be implemented?**

    [Supplier 🏭 domains](<$ 🏭🎭 Supplier role.md>) will typically:
    - use LLMs to understand requests in natural language;
    - use Agentic AI to orchestrate and execute the requests;
    - use crowd sourcing platforms like Amazon Mechanical Turk and Task Rabbit.

    ---
    <br/>
