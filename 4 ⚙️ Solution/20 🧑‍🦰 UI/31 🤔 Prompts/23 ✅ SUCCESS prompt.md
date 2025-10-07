# Non-blocking result ✅

> Part of [Non-blocking status prompts 🤔](<08 🤔⚠️ with Status behavior.md>)

<br/>

1. **What is a non-blocking SUCCESS?**

    A `SUCCESS` 
    * is like an [INFO ℹ️ prompt](<21 ℹ️ INFO prompt.md>) 
    * that signals the user that the transaction is completed 
    * and there are no further inputs required;
    * i.e., they can put down the phone.

    ---
    <br/>


1. **What features does SUCCESS implement?**

    | Feature | Details
    |-|-
    | [`Details`](<03 🤔⊕ with Details.md>) | Has expandable [+] details.
    | [`Options`](<04 🤔🔘 with Options.md>) | Has options for users to select.
    | [`Attachment`](<05 🤔📎 with Attachments.md>) | Has a PDF, PNG, or JPEG attachment.
    | [`Status` behavior](<08 🤔⚠️ with Status behavior.md>) | Informs and continues the flow.
    
    ---
    <br/>


1. **How do SUCCESS emojis work?**
   
    |Emoji | Usage | Details
    |-|-|-
    |✅ | `Host` | Similar to ℹ️ on [INFO ℹ️](<21 ℹ️ INFO prompt.md>)
    |☑️ | `Agent` | Similar to ⓘ on [INFO ℹ️](<21 ℹ️ INFO prompt.md>)

    ---
    <br/>


1. **What's an example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    SUCCESS|Simple success.
    ```

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Simple success.
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | ✅ Simple success.
    | [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | ☑️ Simple success.
    

    ---
    <br/>


1. **What are examples of SUCCESS?**

    |Type|Example
    |-|-
    | `Simple` | [Enter anonymously in casinos 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | `Options` |[Remove token 🎫 flow](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove token.md>)
    | `Guest`| [Board a bus during navigating 🚎](<../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/03 🚎 Traveler @ Bus/32 Board navigating.md>)
    || [Deliver an item left in a taxi 🚕](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/32. Deliver item.md>)
    | | [Pizza for home delivery 🍕](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>)

    ---
    <br/>


1. **What's the format for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    SUCCESS|<message>
    ```
    
    ---
    <br/>

