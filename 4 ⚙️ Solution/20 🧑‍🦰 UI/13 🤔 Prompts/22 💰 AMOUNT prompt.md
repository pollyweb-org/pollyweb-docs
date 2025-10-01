# 💰 AMOUNT prompt

> Part of [blocking input prompts 🤔](<03 Blocking input prompts.md>)


<br/>


1. **What's an AMOUNT prompt?**

    It's a [Prompt 🤔](<01 🤔 Prompt.md>) that shows the decimal input pad.

    ---
    <br/>

2. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**


    Consider the following [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>).
    
    ```yaml
    AMOUNT|How much? >> my-variable
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How much? | 🔄 123
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 How much? | 🔄 123
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 How much? | 🔄 -54


    Usage examples:
    * [A taxi driver issues a bill for a ride 👨‍✈️](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/9 🚕 Driver @ Car 👨‍✈️/03 👨‍✈️ Bill wallet.md>)

    ---
    <br/>


3. **What's the format of a [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>)?**

    ```yaml
    AMOUNT|<message> >> <key>:
        Details: <details>
        MinValue: <min-value>
        MaxValue: <max-value>
        Emoji: <emoji>
    ```
    
    ---
    <br/>


4. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: AMOUNT
    Message: <message>
    Details: <details>
    MinValue: <min-value>
    MaxValue: <max-value>
    Emoji: <emoji>
    ```

    ---
    <br/>

5. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    Answer: -123.45
    ```