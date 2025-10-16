# 🔢 DIGITS prompt

> Part of [blocking input prompts 🤔](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>)


<br/>

1. **What's a DIGITS prompt?**

    A `DIGITS`
    * is a [Prompt 🤔](<../🤔 Prompt.md>) 
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
    | `Codes`| [Enter the item number at a vending machine 🏪](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)

    ---
    <br/>

1. **What features does DIGITS implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 📎 [`Appendix`](<../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>


1. **What's the format of a [Talker 😃](<../../😃 Talkers/😃 Talker.md>)?**

    ```yaml
    # Simplest.
    DIGITS|<statement> >> $placeholder
    ```

    | Argument| Purpose 
    |-|-
    | `<statement>`| Message to show to the user
    | `$placeholder`| Optional [$placeholder 💾](<../../😃 Talkers/😃💾 Talker data/10 💾 $Placeholder.md>) with the user's answer
    

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
    | `MinLength` | Optional [minimum length 📋](<../🤔✏️ Prompt input features/13 📋 Input validation.md>) | `1`
    | `MaxLength` | Optional [maximum length 📋](<../🤔✏️ Prompt input features/13 📋 Input validation.md>) | `5`
    | `Emoji` | Optional [alternative emoji 😶](<../🤔✏️ Prompt input features/14 😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Nullable` | Optional [skip flag ⏭️](<../🤔✏️ Prompt input features/12 ⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | `<uuid>`
    

    ---
    <br/>



1. **What's an example of a [Chat 💬](<../../💬 Chats/💬 Chat.md>)?**

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 What's the code? | 🔢 0123
    [🫥 Agent](<../../../50 🫥 Agent domains/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) | 🫥 What's the code? | 🔢 01234
    | [🤲 Helper](<../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | 🫥 What's the code? | 🔢 000
    |

    <br/>
    
    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker.md>).
    
    ```yaml
    - DIGITS|What's the code? >> $code:
        MinLength: 3 # Server-side validation
        MaxLength: 5 # Server-side validation
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: DIGITS
    Statement: 😃 What's the code?
    ```


    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: 0123
    ```

    ---
    <br/>


