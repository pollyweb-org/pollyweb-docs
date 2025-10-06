# 🔢 INT prompt

> Part of [blocking input prompts 🤔](<09 🤔✨ with Input behavior.md>)


<br/>

1. **What's an `INT` prompt?**

    It's a [Prompt 🤔](<01 🤔 Prompt.md>) 
    * that shows the numeric keypad
    * and allows for leading zeros;
    * e.g., `0123` for pins;
    * e.g., for UK phone numbers like `07482000000`.

    ---
    <br/>


1. **What features does `INT` implement?**

    | Feature | Details
    |-|-
    | [`Details`](<03 🤔✨ with Details.md>) | Has expandable [+] details.
    | [`Attachment`](<05 🤔📎 with Attachments.md>) | Has a PDF, PNG, or JPEG attachment.
    | [`Input` behavior](<09 🤔✨ with Input behavior.md>) | Waits for an answer from users.
    
    ---
    <br/>

1. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Consider the following [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    INT|What's the code? >> my-answer
    ```

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | 🔢 0123
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 What's the code? | 🔢 01234
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 What's the code? | 🔢 000
    |

    Usage example:
    * [Enter the item number at a vending machine 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)

    ---
    <br/>



1. **What's the format of a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    INT|<message> >> $placeholder:
        MinLength: <min-length>
        MaxLength: <max-length>
        MinValue: <min-value>
        MaxValue: <max-value>
    ```
    
    ---
    <br/>

