# 💰 AMOUNT prompt

> Part of [blocking input prompts 🤔](<09 🤔✨ with Input behavior.md>)


<br/>


1. **What's an AMOUNT prompt?**

    It's a [Prompt 🤔](<01 🤔 Prompt.md>) that shows the decimal input pad - e.g.:
    * [A taxi driver issues a bill for a ride 👨‍✈️](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/9 🚕 Driver @ Car 👨‍✈️/03 👨‍✈️ Bill wallet.md>)

    ---
    <br/>

1. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**


    Consider the following [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    AMOUNT|How much? >> my-var:
        MinValue: 0.00
        MaxValue: 1000000000
    ```

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How much? | 🔄 123
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 How much? | 🔄 123
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 How much? | 🔄 -54


    ---
    <br/>


1. **What's the format of a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    AMOUNT|<message> >> <key>:
        MinValue: <min-value>
        MaxValue: <max-value>
    ```
    
    ---
    <br/>


1. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: AMOUNT
    Message: <message>
    MinValue: <min-value>
    MaxValue: <max-value>
    ```

    ---
    <br/>

1. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    |Type| Example
    |-|-
    |decimal| `-123.45`
    |