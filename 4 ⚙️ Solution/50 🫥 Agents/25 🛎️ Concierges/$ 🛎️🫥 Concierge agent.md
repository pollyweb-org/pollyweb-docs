🛎️ Concierge agent domains
===


1. **What are Concierge domains in NLWeb?**

    A [Concierge 🛎️ domain](<$ 🛎️🫥 Concierge agent.md>) is
    * a user's [Agent 🫥 vault](<../$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) 
    * that functions like a personal work-order system for users, 
    * allowing [Host 🤗 domains](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) to add tasks to the user's queue without a clear definition of how those tasks will be executed.

    ---
    <br/>

1. **What are examples for Concierge usages in NLWeb?**

    |Domain|Usage
    |-|-
    | [Custodian 🧳](<../35 🧳 Custodians/$ 🧳🫥 Custodian agent.md>) | Help users recover a lost [Thing 💠](<../../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>).
    | [Vitalogist 💖](<../95 💖 Vitalogists/$ 💖🫥 Vitalogist agent.md>) | Book exams and medical appointments for users.
    | [Pizzeria 🍕](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>) |Find a courier for delivery.

    ---
    <br/>


1. **How do Concierges handle inbound tasks?**

    ![](<. 📎 Assets/🛎️🫥 Concierge.png>)

    | #| Category|Step
    |-|-|-
    |1| `Chat`| On [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with a [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>), the user asks for a task that requires the help of a [Supplier 🏭 domain](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>) (e.g., deliver a pizza).
    |2| `Task` | The [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) invokes the user's [Concierge 🛎️ agent](<$ 🛎️🫥 Concierge agent.md>) to handle the task (e.g., find a courier to deliver the pizza).
    |3| `Find`| The [Concierge 🛎️ agent](<$ 🛎️🫥 Concierge agent.md>) creates a strategy to execute the task, and ask the user's [Finder 🔎 agent](<../40 🔎 Finders/$ 🔎🫥 Finder agent.md>) to find suitable [Supplier 🏭 domains](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>) for the steps require to perform the task.
    |4| `Sort`| The [Concierge 🛎️ agent](<$ 🛎️🫥 Concierge agent.md>) asks the user's [Curator 🧚 agent](<../30 🧚 Curators/$ 🧚🫥 Curator agent.md>) to filter and sort the list of [Supplier 🏭 domains](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>)  according to the user's preferences and restrictions.
    |5| `Agree`| The [Concierge 🛎️ agent](<$ 🛎️🫥 Concierge agent.md>) reviews the execution plan based on the sorted [Supplier 🏭 domains](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>), and asks the user to select one or more options for the suggested strategy.
    |6| `Submit` | The [Concierge 🛎️ agent](<$ 🛎️🫥 Concierge agent.md>) orders the products or services directly from the [Supplier 🏭 domains](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>).
    |7| `Monitor`| The [Concierge 🛎️ agent](<$ 🛎️🫥 Concierge agent.md>) monitors the lifecycle of the orders sent to the [Supplier 🏭 domains](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>) and notify the user about changes.

    ---
    <br/>


1. **How do Concierges receive task requests?**

    [Concierge 🛎️ agents](<$ 🛎️🫥 Concierge agent.md>) receive tasks in natural text; 
    - e.g., book an appointment with a cardiologist.

    ---
    <br/>

1. **How do Concierges prevent task spam?**

    [Concierge 🛎️ agents](<$ 🛎️🫥 Concierge agent.md>) ask users to confirm any inbound work order from a [domain 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>). 
    - For frequent [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>), users can ask their [Concierge 🛎️ agent](<$ 🛎️🫥 Concierge agent.md>) to always trust or always ban the task-requester domain.

    ---
    <br/>

1. **Do Concierges speak in natural language with Suppliers?**

    No necessarily. 
    
    * [Concierge 🛎️ agents](<$ 🛎️🫥 Concierge agent.md>) look at the supplied services exposed in the [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) of [Supplier 🏭 domains](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>), which may or may not support natural language requests. 
    
    * If necessary, [Concierge 🛎️ agents](<$ 🛎️🫥 Concierge agent.md>) translate the user's natural language request into a structure API request using JSON or XML.

    ---
    <br/>

1. **Can Concierges orchestrate tasks with multiple Suppliers?**

    Yes. 
    * [Concierge 🛎️ agents](<$ 🛎️🫥 Concierge agent.md>) create strategies to be performed by one or more [Supplier 🏭 domains](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>).

    ---
    <br/>

1. **Can Concierges know about the details of sub-Suppliers?**

    No. 
    * [Concierge 🛎️ agents](<$ 🛎️🫥 Concierge agent.md>) speak with [Supplier 🏭 domains](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>), but don't know which sub-Suppliers they speak with.

    ---
    <br/>

1. **How can Concierges be implemented?**

    [Concierge 🛎️ agents](<$ 🛎️🫥 Concierge agent.md>) will typically:
    - understand requests in natural language;
    - orchestrate and execute the requests;
    - use crowd sourcing platforms like Amazon Mechanical Turk and Task Rabbit.

    ---
    <br/>
