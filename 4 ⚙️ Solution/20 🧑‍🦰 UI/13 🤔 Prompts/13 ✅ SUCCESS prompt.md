# Non-blocking result ✅

> Part of [Non-blocking status prompts 🤔](<02 Non-blocking prompts.md>)

<br/>

1. **What is a non-blocking SUCCESS?**

    This is an [INFO ℹ️ prompt](<11 ℹ️ INFO prompt.md>) that signals the user that the transaction is completed and there are no further inputs required - i.e., they can put down the phone.

    ---
    <br/>

1. **How do SUCCESS emojis work?**
   
    |Emoji | Usage | Details
    |-|-|-
    |✅ | `Host` | Similar to ℹ️ on [INFO ℹ️](<11 ℹ️ INFO prompt.md>)
    |☑️ | `Guest` | Similar to ⓘ on [INFO ℹ️](<11 ℹ️ INFO prompt.md>)

    ---
    <br/>


1. **What's an example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Consider the following [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>).
    
    ```yaml
    SUCCESS|Simple success.
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Simple success.
    | [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | ☑️ Simple success.
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | ☑️ Simple success.
    

    ---
    <br/>


2. **What are examples of SUCCESS?**

    |Type|Example
    |-|-
    | `Simple` | [Enter anonymously in casinos 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | `Options` |[Remove token 🎫 flow](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove token.md>)
    | `Guest`| [Board a bus during navigating 🚎](<../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/03 🚎 Traveler @ Bus/32 Board navigating.md>)
    || [Deliver an item left in a taxi 🚕](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/32. Deliver item.md>)
    | | [Pizza for home delivery 🍕](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>)

    ---
    <br/>


2. **What's the format for a [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>)?**

    ```yaml
    SUCCESS|<message>|<options> >> <key>:
        Details: <details>
    ```
    
    ---
    <br/>



3. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: SUCCESS
    Message: <message>
    Options: <options>
    Details: <details>
    ```

    ---
    <br/>

4. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    Answer: <selected-option> # if any
    ```
    
    ---
    <br/>
