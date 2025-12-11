# ✅ Non-blocking `DONE` 

> Part of [Non-blocking status prompts 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/8 ⚠️ as Status.md>)

<br/>

1. **What is a non-blocking DONE?**

    A `DONE` 
    * is like an [INFO ℹ️ prompt](<../INFO ℹ️/INFO ℹ️ prompt.md>) 
    * that signals the user that the transaction is completed 
    * and there are no further inputs required;
    * i.e., they can put down the phone.

    ---
    <br/>


1. **What are use cases of DONE?**

    |Type|Example
    |-|-
    | `Simple` | [Enter anonymously in casinos 🤝](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | `Options` |[Remove token 🎫 flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>)
    | `Guest`| [Board a bus during navigating 🚎](<../../../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/03 🚎 Traveler @ Bus/32 Board navigating.md>)
    || [Deliver an item left in a taxi 🚕](<../../../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/32. Deliver item.md>)
    | | [Pizza for home delivery 🍕](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>)

    ---
    <br/>



1. **How do DONE emojis work?**
   
    |Emoji | Usage | Details
    |-|-|-
    |✅ | `Host` | Similar to ℹ️ on [INFO ℹ️](<../INFO ℹ️/INFO ℹ️ prompt.md>)
    |☑️ | `Agent` | Similar to ⓘ on [INFO ℹ️](<../INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>



1. **What features does DONE implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/4 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ⚠️ [`Status`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/8 ⚠️ as Status.md>) | Informs and continues the flow.
    
    ---
    <br/>

1. **What's the syntax for a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    ```yaml
    # Inline
    DONE <text> 
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<text>` |  Message to show to the user. | `Done!`

    ```yaml
    # Multi-line 
    DONE:
        Text: <text>
        
        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Appendix: {...}
    ```
    
    | Input| Purpose | Example
    |-|-|-
    | `Details` | Optional [expandable details ⊕](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/4 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Appendix` | Optional [file attachment 📎](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | `{/...}`

    ---
    <br/>


1. **What's an example in a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)?**

    
    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Simple success.
    | [🤲 Helper](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) | ✅ Simple success.
    |  [🗄️ Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | ☑️ Simple success.
    |
    
    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    📃 Example:
    - DONE Simple success.
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ```yaml
    Format: DONE
    Emoji: ✅ 
    Text: Simple success.
    ```
    
    ---
    <br/>

