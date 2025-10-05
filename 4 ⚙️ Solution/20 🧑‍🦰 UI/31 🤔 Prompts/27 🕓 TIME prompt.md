# 🕓 TIME prompt

> Part of [blocking input prompts 🤔](<03 Blocking input prompts.md>)


<br/>


1. **What's an AMOUNT prompt?**

    It's a [Prompt 🤔](<01 🤔 Prompt.md>) that asks for a time.

    ---
    <br/>

1. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**


    Consider the following [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    TIME|What time? >> my-variable
    ```

    | Domain | [Prompt 🤔](<01 🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What time? | 🕓 10:30:00
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 What time? | 🕓 10:30:00
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 What time? | 🕓 10:30:00


    Usage examples:
    * [Book a taxi ride for tomorrow 🙋](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>)

    ---
    <br/>


1. **How to provide default time options in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Mix with [ONE 1️⃣ prompts](<25 1️⃣ ONE prompt.md>), like in the following [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>).

    | Domain | [Prompt 🤔](<01 🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 [What time tomorrow?](<25 1️⃣ ONE prompt.md>) <br/> - [ 10:00 ] <br/> - [ 10:30 ] <br/> - [ Another ] time | > Another
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 When exactly? | 🕓 10:37:00
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Thanks!
    |

    <br/>

    The associated [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) would be the following.

    ```yaml
    💬 Schedule for tomorrow:
    - ONE|What time tomorrow?|{TimeOptions} >> my-var
    - CASE|{$my-var}:
        Another: TIME|When exactly? >> my-var
    - SUCCESS|Thanks!
    ```

    ```python
    # 🐍 Python handler
    def talkerHandler(args):
        match args['Function']:
            case 'TimeOptions':
                return [
                    "10:00",
                    "10:30",
                    "Another"
                ]
    ```

    ---
    <br/>
    

4. **What's the format of a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    TIME|<message> >> <key>:
        Details: <details>
        MinValue: <min-value>
        MaxValue: <max-value>
        Emoji: <emoji>
    ```
    
    ---
    <br/>


4. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: TIME
    Message: <message>
    Details: <details>
    MinValue: <min-value>
    MaxValue: <max-value>
    Emoji: <emoji>
    ```

    ---
    <br/>

1. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    |Type| Example | Format | Details
    |-|-|-|-
    | time| `14:23:59Z` | `HH:MM:SSZ` | ISO 8601 in UTC timezone
    |