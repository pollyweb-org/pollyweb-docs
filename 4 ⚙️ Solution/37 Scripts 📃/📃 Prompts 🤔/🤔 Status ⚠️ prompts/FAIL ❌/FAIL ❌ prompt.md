# ❌ Non-blocking `FAIL` 

> Part of [Non-blocking status prompts 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/8 ⚠️ as Status.md>)

<br/>

1. **What is a non-blocking FAIL?**

    A `FAIL` 
    * is like an [INFO ℹ️ prompt](<../INFO ℹ️/INFO ℹ️ prompt.md>) 
    * that signals the user that the transaction failed;
    * it's typically followed by a prompt to help the user fix the problem.

    ---
    <br/>


1. **What features does FAIL implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/4 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ⚠️ [`Status`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/8 ⚠️ as Status.md>) | Informs and continues the flow.
    
    ---
    <br/>



1. **What are usages of FAIL?**

    |Category|Use case
    |-|-
    | `Simple` | [Walk into a full restaurant 🍽️](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/44 🚪 Door: Walk in full.md>)
    ||[Recover an item from a taxi 🚕](<../../../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/31. Recover item.md>)
    ||[Hotel lift exit on wrong floor 🏨](<../../../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/04 🏨 Guest @ Lift 🛗/02 🛗 Exit on wrong floor.md>)
    || [Wrong venue for a show 🎭](<../../../../../3 🤝 Use Cases/10 🍿 Entertainment/Go to Theaters 🎭/20 Guest @ Door/22 Wrong venue.md>)
    | `Guest` | [Entering the wrong bus 🚎](<../../../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/03 🚎 Traveler @ Bus/33 Unboard navigating.md>)
    || [Withdraw cash from an ATM 🏧](<../../../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>)
    

    ---
    <br/>


1. **What's the syntax for a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    ```yaml
    # Inline
    FAIL|<text> 
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<text>` |  Message to show to the user. | `Error!`

    ```yaml
    # Multi-line 
    FAIL:
        Text: <text>
        
        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Appendix: {function}
    ```
    
    | Input| Purpose | Example
    |-|-|-
    | `Details` | Optional [expandable details ⊕](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/4 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Appendix` | Optional [file attachment 📎](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | `{/...}`

    ---
    <br/>



1. **What's an example of a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ❌ Simple failure.
    | [🤲 Helper](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲 Helper/🤲👥 Helper domain.md>) | ❌ Simple failure.
    |  [🗄️ Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | ❌ Simple failure.
    |

    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    📃 Example:
    - FAIL|Simple failure.
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ```yaml
    Format: FAIL
    Emoji: ❌ 
    Text: Simple failure.
    ```
    
    ---
    <br/>