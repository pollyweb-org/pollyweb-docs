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

    | Industry | Use case|
    |-|-
    | `Taxi`| [A taxi driver issues a bill for a ride 👨‍✈️](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/9 🚕 Driver @ Car 👨‍✈️/03 👨‍✈️ Bill wallet.md>)

    ---
    <br/>


1. **What features does AMOUNT implement?**

    | Feature | Details
    |-|-
    |  ⊕ [`Details`](<03 🤔⊕ with Details.md>) | Has expandable [+] details.
    |  📎 [`Attachment`](<05 🤔📎 with Attachments.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<11 ✏️ Input behavior.md>) | Waits for an answer from users.
    
    ---
    <br/>

1. **What's the syntax of a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    # Simplest.
    AMOUNT|<message>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<message>`| Message to show to the user

    ```yaml
    # Comprehensive.
    AMOUNT >> $placeholder:
        Message: <message>
        MinValue: <min-value>
        MaxValue: <max-value>
        Precision: <precision>
        Currency: <currency>
        Locale: <locale>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `$placeholder`| Placeholder with the user's answer
    | `<min-value>` | Optional minimum value | `-100`
    | `<max-value>` | Optional maximum value | `100`
    | `<precision>`| Rounded decimals (default is 2) | `2`
    | `<currency>` | Optional ISO 4217 currency | `USD`
    | `<locale>`| Optional CLDR locale <br/> - defaults to the [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) language | `en-US`
    
    ---
    <br/>

1. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**



    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How much? | 🔄 1234.5678
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 How much? | 🔄 12345.6
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 How much? | 🔄 -54.456
    |

    <br/>

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    # 😃 Talker 
    AMOUNT|How much?:
        MinValue: -100.00
        MaxValue: 1000000000
        Precision: 5  # Server-side only
        Currency: USD # Server-side only
        Locale: en-US # Server-side only
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: AMOUNT
    Message: 😃 How much?
    MinValue: -100.00
    MaxValue: 1000000000
    ```


    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: 1234.5678
    ```


    ---
    <br/>


1. **How does Precision work?**

    