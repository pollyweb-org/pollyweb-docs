# 🔠 MANY prompt

> Part of [blocking input prompts 🤔](<11 ✏️ Input behavior.md>)

<br/>

1. **What is a non-blocking SUCCESS?**

    A `SUCCESS` 
    * is like an [INFO ℹ️ prompt](<21 ℹ️ INFO prompt.md>) 
    * that signals the user that the transaction is completed 
    * and there are no further inputs required;
    * i.e., they can put down the phone.

    ---
    <br/>


1. **What are use cases of MANY?**

    |Type|Example
    |-|-
    | `Simple` |
    
    ---
    <br/>





1. **What features does SUCCESS implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<03 🤔⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<04 🤔🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Attachment`](<05 🤔📎 with Attachments.md>) | Has a PDF, PNG, or JPEG attachment.
    
    ---
    <br/>

1. **What's the format for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    # Simplest
    MANY|<message>|<options> >> $placeholder
       
       * Options are comma separated (e.g., `Milk, Sugar, Rice`)
       * Example: `MANY|What items?|Milk,Sugar,Rice >> items`
       * 
    ```

    ```yaml
    # Multi-line 
    SUCCESS:
        Message: <message>
    ```
    
    | Argument| Purpose | Example
    |-|-|-
    | `<message>` |  Message for the user. | `Done!`

    ---
    <br/>



1. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>)

    ---
    <br/>

1. **What are business cases?**

    |Category|Use case
    |-|-
    |

    ---
    <br/>


1. **What's the content for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    
    ```

    |Parameter|Details
    |-|-
    | 
    
    ---
    <br/>


1. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    
    ```

    ---
    <br/>

1. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    
    ```