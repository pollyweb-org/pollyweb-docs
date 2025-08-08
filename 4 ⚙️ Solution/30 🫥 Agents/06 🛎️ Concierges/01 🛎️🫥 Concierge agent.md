🛎️ Concierge domains FAQ
===

![](<00 📎 Assets/🛎️ Concierge.png>)

1. **What are Concierge domains in NLWeb?**

    A Concierge domain is a [Vault 🗄️](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) that functions like a personal work-order system for users, allowing domains to add tasks to the user's queue without a clear definition of how those tasks will be executed; 
    - e.g., if someone activates the recovery mode on a user's lost glasses, that creates a task on the user's Concierge to pick up the glasses.

    ---

1. **What are examples for Concierge usages in NLWeb?**

    - [Custodian 🎩](<../../70 🌳 Ambient/71 💠 Brand Things/05 🎩🗄️ Custodian vault.md>) domains leverage Concierges 🛎️ to help users recover a lost [Thing 💠](<../../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>).

    - [Vitalogist 💖](<../09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) domains leverage Concierges 🛎️ to book exams and medical appointments for users.

    - [Pizzerias 🍕](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/04 🍽️ Order pizza 🍕/01 🍕 Customer @ Home 🏠/01 🏠 Order pizza.md>) leverage Concierges 🛎️ to find a courier for delivery.

    ---

1. **How do Concierges receive task requests?**

    Concierges receive tasks in natural text - e.g., book an appointment with a cardiologist.

    ---

1. **How do Concierges prevent task spam?**

    Concierges ask users to confirm any inbound work order from a domain. For frequent domains, users can ask their Concierge to always trust or always ban the task-requester domain.

    ---

1. **How do Concierges handle inbound tasks?**

    Concierges take the following steps to handle inbound tasks:
    - 1/ create a strategy (i.e., line of thought) to execute the task;
    - 2/ ask the user's [Finder 🔎](<../10 🔎 Finders/02 🔎🫥 Finder vault.md>) to find suitable [Suppliers 🏭](<02 🏭🎭 Supplier role.md>) for the steps require to perform the task;
    - 3/ ask the user's [Persona 🧢](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) to filter and sort the list of Suppliers according to the user's preferences and restrictions;
    - 4/ review the execution plan based on the Suppliers available;
    - 5/ ask the user to select one or more options for the suggested strategy;
    - 6/ order the product or service directly from the Suppliers;
    - 7/ monitor the lifecycle of the task and notify the user about changes.

    ---

1. **Do Concierges speak in natural language with Suppliers?**

    No necessarily. 
    
    * Concierges look at the supplied services exposed in the Manifest of [Suppliers 🏭](<02 🏭🎭 Supplier role.md>), which may or may not support natural language requests. 
    
    * If necessary, Concierges translate the user's natural language request into a structure API request using JSON or XML.

    ---

1. **Can Concierges orchestrate tasks with multiple Suppliers?**

    Yes. Concierges create strategies to be performed by one or more [Suppliers 🏭](<02 🏭🎭 Supplier role.md>).

    ---

1. **Can Concierges know about the details of sub-Suppliers?**

    No. Concierges speak with [Suppliers 🏭](<02 🏭🎭 Supplier role.md>), but don't know which sub-Suppliers they speak with.

    ---

1. **How can Concierges be implemented?**

    Concierges will typically:
    - use GenAI to understand requests in natural language;
    - use GenAI agents to orchestrate and execute the requests;
    - use crowd sourcing platforms like Amazon Mechanical Turk and Task Rabbit.

    ---
