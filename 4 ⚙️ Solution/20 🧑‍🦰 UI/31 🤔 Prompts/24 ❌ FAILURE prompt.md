# Non-blocking failure ❌

> Part of [Non-blocking status prompts 🤔](<08 🤔⚠️ with Status behavior.md>)

<br/>

1. **What is a non-blocking FAILURE?**

    A `FAILURE` 
    * is like an [INFO ℹ️ prompt](<21 ℹ️ INFO prompt.md>) 
    * that signals the user that the transaction failed;
    * it's typically followed by a prompt to help the user fix the problem.

    ---
    <br/>


1. **What features does FAILURE implement?**

    | Feature | Details
    |-|-
    | [`Details`](<03 🤔⊕ with Details.md>) | Has expandable [+] details.
    | [`Options`](<04 🤔🔘 with Options.md>) | Has options for users to select.
    | [`Attachment`](<05 🤔📎 with Attachments.md>) | Has a PDF, PNG, or JPEG attachment.
    | [`Status` behavior](<08 🤔⚠️ with Status behavior.md>) | Informs and continues the flow.
    
    ---
    <br/>


1. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Consider the following [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    FAILURE|Simple failure.
    ```

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ❌ Simple failure.
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | ❌ Simple failure.
    | [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | ❌ Simple failure.
   
    

    ---
    <br/>

1. **What are usages of FAILURE?**

    |Category|Use case
    |-|-
    | `Simple` | [Walk into a full restaurant 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/44 🚪 Door: Walk in full.md>)
    ||[Recover an item from a taxi 🚕](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/31. Recover item.md>)
    ||[Hotel lift exit on wrong floor 🏨](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/04 🏨 Guest @ Lift 🛗/02 🛗 Exit on wrong floor.md>)
    || [Wrong venue for a show 🎭](<../../../3 🤝 Use Cases/10 🍿 Entertainment/Go to Theaters 🎭/20 Guest @ Door/22 Wrong venue.md>)
    | `Guest` | [Entering the wrong bus 🚎](<../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/03 🚎 Traveler @ Bus/33 Unboard navigating.md>)
    || [Withdraw cash from an ATM 🏧](<../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>)
    

    ---
    <br/>


1. **What's the format for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    FAILURE|<message>
    ```
    
    ---
    <br/>


