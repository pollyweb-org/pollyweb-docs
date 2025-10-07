# 💰 AMOUNT prompt

> Part of [blocking input prompts 🤔](<11 ✏️ Input behavior.md>)


<br/>


1. **What's an AMOUNT prompt?**

    An `AMOUNT` 
    * is a [Prompt 🤔](<01 🤔 Prompt.md>) 
    * that shows the decimal input pad 
    * and returns a decimal - e.g. `-123.45`.

    ---
    <br/>

1. **What are AMOUNT use cases?**

    * [A taxi driver issues a bill for a ride 👨‍✈️](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/9 🚕 Driver @ Car 👨‍✈️/03 👨‍✈️ Bill wallet.md>)

    ---
    <br/>


1. **What features does AMOUNT implement?**

    | Feature | Details
    |-|-
    | [`Details`](<03 🤔⊕ with Details.md>) | Has expandable [+] details.
    | [`Attachment`](<05 🤔📎 with Attachments.md>) | Has a PDF, PNG, or JPEG attachment.
    | [`Input` behavior](<11 ✏️ Input behavior.md>) | Waits for an answer from users.
    
    ---
    <br/>

1. **What's the syntax of a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    AMOUNT|<message> >> <key>:
        MinValue: <min-value>
        MaxValue: <max-value>
    ```
    
    ---
    <br/>

1. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**



    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How much? | 🔄 123
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 How much? | 🔄 123
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 How much? | 🔄 -54
    |

    Consider the associated [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    AMOUNT|How much? >> $my-var:
        MinValue: 0.00
        MaxValue: 1000000000
    ```

    ---
    <br/>


