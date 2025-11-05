# 🕓 TIME prompt

> Part of [blocking input prompts 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>)


<br/>


1. **What's a `TIME` prompt?**

    A `TIME`
    * is a [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) 
    * that asks for a time
    * in the user's timezone (not UTC).

    ---
    <br/>


1. **What's the syntax of a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)?**

    ```yaml
    TIME|<text> >> $holder
    ```
    
    |Input| Details | Example 
    |-|-|-
    | `<text>`| The message to the user | `What time?`
    | `$holder`| [holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the time | `14:23:59` 
    
    ---
    <br/>

1. **What's an example of a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)?**


    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    TIME|What time? >> $time
    ```

    | Domain | [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 What time? | 🕓 10:30:00
    [🫥 Agent](<../../../../50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) | 🫥 What time? | 🕓 10:30:00
    | [🤲 Helper](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | 🫥 What time? | 🕓 10:30:00


    Usage examples:
    * [Book a taxi ride for tomorrow 🙋](<../../../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>)

    ---
    <br/>


1. **How to provide default time options in a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)?**

    Mix with [ONE 1️⃣ prompts](<../ONE 1️⃣/ONE 1️⃣ prompt.md>), like in the following [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

    | Domain | [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 [What time tomorrow?](<../ONE 1️⃣/ONE 1️⃣ prompt.md>) <br/> - [ 10:00 ] <br/> - [ 10:30 ] <br/> - [ Another ] time | > Another
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 When exactly? | 🕓 10:37:00
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Thanks!
    |

    <br/>

    The associated [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) would be the following.

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
    
