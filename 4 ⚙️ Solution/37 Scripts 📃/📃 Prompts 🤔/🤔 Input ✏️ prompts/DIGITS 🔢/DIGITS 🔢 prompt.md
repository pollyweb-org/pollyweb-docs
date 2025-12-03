# 🔢 DIGITS prompt

> Part of [blocking input prompts 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>)


<br/>

1. **What's a DIGITS prompt?**

    A `DIGITS`
    * is a [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) 
    * that shows the numeric keypad
    * and allows for leading zeros.
  
    Examples:
    * `0123` for pins,
    * UK phone numbers like `07482000000`.

    ---
    <br/>

1. **What are use cases for DIGITS?**

    | Scenario | Details
    |-|-
    | `Codes`| [Enter the item number at a vending machine 🏪](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)

    ---
    <br/>

1. **What features does DIGITS implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 📎 [`Appendix`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>


1. **What's the syntax of a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)?**

    ```yaml
    # Simplest.
    DIGITS|<text> >> $holder
    ```

    | Input| Purpose 
    |-|-
    | `<text>`| Message to show to the user
    | `$holder`| Optional [holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the user's answer
    

    ```yaml
    # Comprehensive.
    DIGITS >> $holder:
        Text: <text>

        # Specific optional properties
        MinLength: int
        MaxLength: int

        # Generic optional properties
        Emoji: emoji
        Details: string
        Nullable: bool
        Appendix: {function}
    ```
    
    | Input| Purpose | Example
    |-|-|-
    | `MinLength` | Optional [minimum length 📋](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/📋 Input validation.md>) | `1`
    | `MaxLength` | Optional [maximum length 📋](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/📋 Input validation.md>) | `5`
    | `Emoji` | Optional [alternative emoji 😶](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Nullable` | Optional [skip flag ⏭️](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | `<uuid>`
    

    ---
    <br/>



1. **What's an example of a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 What's the code? | 🔢 0123
    [🫥 Agent](<../../../../50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) | 🫥 What's the code? | 🔢 01234
    | [🤲 Helper](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲 Helper/🤲👥 Helper domain.md>) | 🫥 What's the code? | 🔢 000
    |

    <br/>
    
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    - DIGITS|What's the code? >> $code:
        MinLength: 3 # Server-side validation
        MaxLength: 5 # Server-side validation
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ```yaml
    Format: DIGITS
    Emoji: 😃 
    Text: What's the code?
    ```


    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    Answer: 0123
    ```

    ---
    <br/>


