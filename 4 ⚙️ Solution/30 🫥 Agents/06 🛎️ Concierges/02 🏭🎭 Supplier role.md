🏭 Supplier domain role FAQ
===

![](<00 📎 Assets/🛎️ Supplier.png>)

1. **What is a Supplier domain role in NLWeb?**

    A Supplier 🏭 is an [🪢 Integrator](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🔌🎭 Integrator role.md>) domain that exposes order APIs to accept asynchronous order requests from other domains.

    ---

1. **What are examples of Suppliers?**

    * [Printer 🖨️](<../../70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer supplier.md>) domains accept orders to print NFC/QR [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>), ship them to a destination, and manage the lifecycle of these Locators.

    * [KeyMaker 🔐](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/05  🔐🏭 Keymaker supplier.md>) domains accept requests to deliver and manage the lifecycle of [Padlock 🔒](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>).

    * [Courier 🛵](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/04 🍽️ Order pizza 🍕/08 🍕 Driver @ Road 🛵/02 🛵 Pick-up.md>) domains accept orders to deliver pizzas, as requested by a [Concierge 🛎️](<01 🛎️🫥 Concierge agent.md>). 

    ---

1. **What are examples of order requesters?**

    * When users have tasks to complete, [Concierge 🛎️](<01 🛎️🫥 Concierge agent.md>) domains send order requests to Suppliers 🏭 for them to perform steps in those tasks.

    ---

1. **How many responses are expected per order?**

    A request to a Supplier 🏭 will receive one or more asynchronous updated events.

    ---

1. **Are order rejections synchronous?**

    No. Adding an order to a Supplier 🏭 doesn't return a synchronous response.

    ---

1. **Can Suppliers answer natural language questions?**

    Yes, if that is supported by their API.

    ---

1. **Can Suppliers use other Suppliers for sub tasks?**

    Yes, Supplier 🏭 can use other sub-Suppliers if they want to - there's no restriction to do so.

    ---

1. **Can requesters know about the details of sub-Suppliers?**

    No. Requesters send order requests to Suppliers 🏭 but don't know which sub-Suppliers they speak with.

    ---

1. **How can Suppliers be implemented?**

    Suppliers 🏭 will typically:
    - use LLMs to understand requests in natural language;
    - use Agentic AI to orchestrate and execute the requests;
    - use crowd sourcing platforms like Amazon Mechanical Turk and Task Rabbit.

    ---
