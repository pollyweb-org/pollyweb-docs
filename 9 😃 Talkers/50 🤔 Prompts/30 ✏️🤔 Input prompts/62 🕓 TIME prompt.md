# 🕓 TIME prompt

> Part of [blocking input prompts 🤔](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/11 ✏️ Input behavior.md>)


<br/>


1. **What's a `TIME` prompt?**

    A `TIME`
    * is a [Prompt 🤔](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) 
    * that asks for a time
    * in the user's timezone (not UTC).

    ---
    <br/>


1. **What's the format of a [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/01 😃 Talker.md>)?**

    ```yaml
    TIME|<message> >> $placeholder
    ```
    
    |Argument| Details | Example 
    |-|-|-
    | `<message>`| The message to the user | `What time?`
    | `$placeholder`| The time in  ISO 8601 | `14:23:59` 
    
    ---
    <br/>

1. **What's an example of a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)?**


    Here's the [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/01 😃 Talker.md>).
    
    ```yaml
    TIME|What time? >> $time
    ```

    | Domain | [Prompt 🤔](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What time? | 🕓 10:30:00
    [🫥 Agent](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 What time? | 🕓 10:30:00
    | [🛠️ Helper](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 What time? | 🕓 10:30:00


    Usage examples:
    * [Book a taxi ride for tomorrow 🙋](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>)

    ---
    <br/>


1. **How to provide default time options in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)?**

    Mix with [ONE 1️⃣ prompts](<53 1️⃣ ONE prompt.md>), like in the following [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

    | Domain | [Prompt 🤔](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 [What time tomorrow?](<53 1️⃣ ONE prompt.md>) <br/> - [ 10:00 ] <br/> - [ 10:30 ] <br/> - [ Another ] time | > Another
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 When exactly? | 🕓 10:37:00
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Thanks!
    |

    <br/>

    The associated [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/01 😃 Talker.md>) would be the following.

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
    
