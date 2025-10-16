# 🕓 TIME prompt

> Part of [blocking input prompts 🤔](<../1 📘 Prompt specs/09 ✏️ as Input.md>)


<br/>


1. **What's a `TIME` prompt?**

    A `TIME`
    * is a [Prompt 🤔](<../../10 📘 Talker specs/20 🤔 Prompt.md>) 
    * that asks for a time
    * in the user's timezone (not UTC).

    ---
    <br/>


1. **What's the format of a [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    TIME|<statement> >> $placeholder
    ```
    
    |Argument| Details | Example 
    |-|-|-
    | `<statement>`| The message to the user | `What time?`
    | `$placeholder`| [$placeholder 💾](<../../30 🗃️ Talker data/10 💾 $Placeholder.md>) with  ISO 8601 time | `14:23:59` 
    
    ---
    <br/>

1. **What's an example of a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)?**


    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    TIME|What time? >> $time
    ```

    | Domain | [Prompt 🤔](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 😃 What time? | 🕓 10:30:00
    [🫥 Agent](<../../../4 ⚙️ Solution/50 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) | 🫥 What time? | 🕓 10:30:00
    | [🛠️ Helper](<../../../4 ⚙️ Solution/45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>) | 🫥 What time? | 🕓 10:30:00


    Usage examples:
    * [Book a taxi ride for tomorrow 🙋](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>)

    ---
    <br/>


1. **How to provide default time options in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)?**

    Mix with [ONE 1️⃣ prompts](<53 1️⃣ ONE prompt.md>), like in the following [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>).

    | Domain | [Prompt 🤔](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 😃 [What time tomorrow?](<53 1️⃣ ONE prompt.md>) <br/> - [ 10:00 ] <br/> - [ 10:30 ] <br/> - [ Another ] time | > Another
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 😃 When exactly? | 🕓 10:37:00
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ✅ Thanks!
    |

    <br/>

    The associated [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>) would be the following.

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
    
