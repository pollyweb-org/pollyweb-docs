# Non-blocking result ✅

> Part of [Non-blocking status prompts 🤔](<../1 📘 Prompt specs/08 ⚠️ as Status.md>)

<br/>

1. **What is a non-blocking SUCCESS?**

    A `SUCCESS` 
    * is like an [INFO ℹ️ prompt](<21 ℹ️ INFO prompt.md>) 
    * that signals the user that the transaction is completed 
    * and there are no further inputs required;
    * i.e., they can put down the phone.

    ---
    <br/>


1. **What are use cases of SUCCESS?**

    |Type|Example
    |-|-
    | `Simple` | [Enter anonymously in casinos 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | `Options` |[Remove token 🎫 flow](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove token.md>)
    | `Guest`| [Board a bus during navigating 🚎](<../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/03 🚎 Traveler @ Bus/32 Board navigating.md>)
    || [Deliver an item left in a taxi 🚕](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/32. Deliver item.md>)
    | | [Pizza for home delivery 🍕](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>)

    ---
    <br/>



1. **How do SUCCESS emojis work?**
   
    |Emoji | Usage | Details
    |-|-|-
    |✅ | `Host` | Similar to ℹ️ on [INFO ℹ️](<21 ℹ️ INFO prompt.md>)
    |☑️ | `Agent` | Similar to ⓘ on [INFO ℹ️](<21 ℹ️ INFO prompt.md>)

    ---
    <br/>



1. **What features does SUCCESS implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../1 📘 Prompt specs/04 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ⚠️ [`Status`](<../1 📘 Prompt specs/08 ⚠️ as Status.md>) | Informs and continues the flow.
    
    ---
    <br/>

1. **What's the format for a [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    # Inline
    SUCCESS|<statement> 
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<statement>` |  Message to show to the user. | `Done!`

    ```yaml
    # Multi-line 
    SUCCESS:
        Statement: <statement>
        
        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Appendix: {function}
    ```
    
    | Argument| Purpose | Example
    |-|-|-
    | `Details` | Optional [expandable details ⊕](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../1 📘 Prompt specs/04 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Appendix` | Optional [file attachment 📎](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | `{/...}`

    ---
    <br/>


1. **What's an example in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)?**

    
    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ✅ Simple success.
    | [🛠️ Helper](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/$ 🛠️ Helpers/🛠️👥 Helper domain.md>) | ✅ Simple success.
    | [🫥 Agent](<../../../4 ⚙️ Solution/50 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) | ☑️ Simple success.
    |
    
    <br/>

    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    # Talker 😃
    - SUCCESS|Simple success.
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: SUCCESS
    Statement: ✅ Simple success.
    ```
    
    ---
    <br/>

