# 🔄 QUANTITY prompt

> Part of [blocking input prompts 🤔](<03 Blocking input prompts.md>)


<br/>

1. **What's an QUANTITY prompt?**

    It's a [Prompt 🤔](<01 🤔 Prompt.md>) that shows up and down arrows.

    ---
    <br/>

2. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Consider the following [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>).
    
    ```yaml
    QUANTITY|How many? >> my-variable
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | `0123`
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 What's the code? | `01234`
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 What's the code? | `000`

    ---
    <br/>



2. **What's the format of a [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>)?**

    ```yaml
    QUANTITY|<message> >> <key>:
        Details: <details>
        MinValue: <min-value>
        MaxValue: <max-value>
        Emoji: <emoji>
    ```
    
    ---
    <br/>


4. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: QUANTITY
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
    Answer: -123
    ```