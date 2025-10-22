# ✅ Non-blocking `SUCCESS` 

> Part of [Non-blocking status prompts 🤔](<../🤔⚙️ Prompt features/8 ⚠️ as Status.md>)

<br/>

1. **What is a non-blocking SUCCESS?**

    A `SUCCESS` 
    * is like an [INFO ℹ️ prompt](<INFO ℹ️ prompt.md>) 
    * that signals the user that the transaction is completed 
    * and there are no further inputs required;
    * i.e., they can put down the phone.

    ---
    <br/>


1. **What are use cases of SUCCESS?**

    |Type|Example
    |-|-
    | `Simple` | [Enter anonymously in casinos 🤝](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | `Options` |[Remove token 🎫 flow](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/💬🤵 Remove 🎫.md>)
    | `Guest`| [Board a bus during navigating 🚎](<../../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/03 🚎 Traveler @ Bus/32 Board navigating.md>)
    || [Deliver an item left in a taxi 🚕](<../../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/32. Deliver item.md>)
    | | [Pizza for home delivery 🍕](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>)

    ---
    <br/>



1. **How do SUCCESS emojis work?**
   
    |Emoji | Usage | Details
    |-|-|-
    |✅ | `Host` | Similar to ℹ️ on [INFO ℹ️](<INFO ℹ️ prompt.md>)
    |☑️ | `Agent` | Similar to ⓘ on [INFO ℹ️](<INFO ℹ️ prompt.md>)

    ---
    <br/>



1. **What features does SUCCESS implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../🤔⚙️ Prompt features/4 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ⚠️ [`Status`](<../🤔⚙️ Prompt features/8 ⚠️ as Status.md>) | Informs and continues the flow.
    
    ---
    <br/>

1. **What's the format for a [Talker 😃](<../../😃 Talkers/😃 Talker role.md>)?**

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
    | `Details` | Optional [expandable details ⊕](<../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../🤔⚙️ Prompt features/4 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Appendix` | Optional [file attachment 📎](<../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | `{/...}`

    ---
    <br/>


1. **What's an example in a [Chat 💬](<../../💬 Chats/💬 Chat.md>)?**

    
    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ Simple success.
    | [🤲 Helper](<../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | ✅ Simple success.
    | [🫥 Agent](<../../../50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) | ☑️ Simple success.
    |
    
    <br/>

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker role.md>).
    
    ```yaml
    # Talker 😃
    - SUCCESS|Simple success.
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: SUCCESS
    Statement: ✅ Simple success.
    ```
    
    ---
    <br/>

