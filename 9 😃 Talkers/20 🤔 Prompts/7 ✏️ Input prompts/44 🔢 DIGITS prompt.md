# 🔢 DIGITS prompt

> Part of [blocking input prompts 🤔](<../1 📘 Prompt specs/09 ✏️ as Input.md>)


<br/>

1. **What's a DIGITS prompt?**

    A `DIGITS`
    * is a [Prompt 🤔](<../../10 📘 Talker specs/20 🤔 Prompt.md>) 
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
    | ⊕ [`Details`](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | Has expandable [+] details.
    | 📎 [`Appendix`](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../1 📘 Prompt specs/09 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>


1. **What's the format of a [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    # Simplest.
    DIGITS|<statement> >> $placeholder
    ```

    | Argument| Purpose 
    |-|-
    | `<statement>`| Message to show to the user
    | `$placeholder`| Optional [$placeholder 💾](<../../30 🗃️ Talker data/10 💾 $Placeholder.md>) with the user's answer
    

    ```yaml
    # Comprehensive.
    DIGITS >> $placeholder:
        Statement: <statement>

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
    | `MinLength` | Optional [minimum length 📋](<../2 ✏️ Input specs/13 📋 Input validation.md>) | `1`
    | `MaxLength` | Optional [maximum length 📋](<../2 ✏️ Input specs/13 📋 Input validation.md>) | `5`
    | `Emoji` | Optional [alternative emoji 😶](<../2 ✏️ Input specs/14 😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | `Hint...`
    | `Nullable` | Optional [skip flag ⏭️](<../2 ✏️ Input specs/12 ⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | `<uuid>`
    

    ---
    <br/>



1. **What's an example of a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)?**

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | 😃 What's the code? | 🔢 0123
    [🫥 Agent](<../../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 What's the code? | 🔢 01234
    | [🛠️ Helper](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) | 🫥 What's the code? | 🔢 000
    |

    <br/>
    
    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    - DIGITS|What's the code? >> $code:
        MinLength: 3 # Server-side validation
        MaxLength: 5 # Server-side validation
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: DIGITS
    Statement: 😃 What's the code?
    ```


    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: 0123
    ```

    ---
    <br/>


