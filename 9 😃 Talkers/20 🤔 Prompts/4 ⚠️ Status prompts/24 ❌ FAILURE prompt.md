# Non-blocking failure ❌

> Part of [Non-blocking status prompts 🤔](<../1 📘 Prompt specs/08 ⚠️ as Status.md>)

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
    | ⊕ [`Details`](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../1 📘 Prompt specs/04 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ⚠️ [`Status`](<../1 📘 Prompt specs/08 ⚠️ as Status.md>) | Informs and continues the flow.
    
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


1. **What's the format for a [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    # Inline
    FAILURE|<statement> 
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<statement>` |  Message to show to the user. | `Error!`

    ```yaml
    # Multi-line 
    FAILURE:
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



1. **What's an example of a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)?**

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | ❌ Simple failure.
    | [🛠️ Helper](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) | ❌ Simple failure.
    | [🫥 Agent](<../../../4 ⚙️ Solution/50 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) | ❌ Simple failure.
    |

    <br/>

    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    # Talker 😃
    - FAILURE|Simple failure.
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: FAILURE
    Statement: ❌ Simple failure.
    ```
    
    ---
    <br/>