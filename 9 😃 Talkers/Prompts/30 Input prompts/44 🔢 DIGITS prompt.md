# 🔢 DIGITS prompt

> Part of [blocking input prompts 🤔](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/11 ✏️ Input behavior.md>)


<br/>

1. **What's a DIGITS prompt?**

    A `DIGITS`
    * is a [Prompt 🤔](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) 
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
    | `Codes`| [Enter the item number at a vending machine 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)

    ---
    <br/>

1. **What features does DIGITS implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/03 🤔⊕ with Details.md>) | Has expandable [+] details.
    | 📎 [`Appendix`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/05 🤔📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/11 ✏️ Input behavior.md>) | Waits for an answer from users.
    
    ---
    <br/>


1. **What's the format of a [Talker 😃](<../../01 😃 Talker.md>)?**

    ```yaml
    # Simplest.
    DIGITS|<message> >> $placeholder
    ```

    | Argument| Purpose 
    |-|-
    | `<message>`| Message to show to the user
    | `$placeholder`| Optional placeholder with the user's answer
    

    ```yaml
    # Comprehensive.
    DIGITS >> $placeholder:
        Message: <message>

        # Specific optional properties
        MinLength: int
        MaxLength: int

        # Generic optional properties
        Emoji: emoji
        Details: string
        Nullable: bool
        Appendix: {function}
    ```
    
    | Argument| Purpose | Example
    |-|-|-
    | `MinLength` | Optional [minimum length 📋](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/13 ✏️📋 Input validation.md>) | `1`
    | `MaxLength` | Optional [maximum length 📋](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/13 ✏️📋 Input validation.md>) | `5`
    | `Emoji` | Optional [alternative emoji 😶](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/14 ✏️😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/03 🤔⊕ with Details.md>) | `Hint...`
    | `Nullable` | Optional [skip flag ⏭️](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/12 ✏️⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/05 🤔📎 with Appendix.md>) | `<uuid>`
    

    ---
    <br/>



1. **What's an example of a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)?**

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../0../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Promp../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | 🔢 0123
    [🫥 Agent](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 What's the code? | 🔢 01234
    | [🛠️ Helper](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 What's the code? | 🔢 000
    |

    <br/>
    
    Here's the [Talker 😃](<../../01 😃 Talker.md>).
    
    ```yaml
    - DIGITS|What's the code? >> $code:
        MinLength: 3 # Server-side validation
        MaxLength: 5 # Server-side validation
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: DIGITS
    Message: 😃 What's the code?
    ```


    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: 0123
    ```

    ---
    <br/>


