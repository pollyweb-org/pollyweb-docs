# 😶 Talker `EMOJI` command

> Implements the [🫥 Input emojis](<3 Prompts/25 ✏️📘 Input defintions/14 ✏️😶 Input emojis.md>) feature.

<br/>

1. **What is the EMOJI command?**

    An `EMOJI`
    * is a [Command ⌘](<03 Talker Flows/10 ⌘ Command.md>) 
    * that defaults all upcoming [Input prompts ✏️](<3 Prompts/10 🤔📘 Prompt definitions/09 ✏️ as Input.md>)
    * to [use another emoji 😶](<3 Prompts/25 ✏️📘 Input defintions/14 ✏️😶 Input emojis.md>) other than the default smile 😃 emoji.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    EMOJI|<emoji> 
    ```
    | Argument| Purpose | Example
    |-|-|-
    | `<emoji>` | Emoji for upcoming [Input prompts ✏️](<3 Prompts/10 🤔📘 Prompt definitions/09 ✏️ as Input.md>) | `😶`
    

    ---
    <br/>

1. **What's an example?**

    | [Domain](<../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<3 Prompts/10 🤔📘 Prompt definitions/01 🤔 Prompt.md>) | [User](<../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Joyful? [Yes, No] | > Yes
    | [🤗 Host](<../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Changing to neutral.
    | [🤗 Host](<../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😶 Now neutral? [Yes, No] | > Yes
    | [🤗 Host](<../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😶 Still neutral? [Yes, No] | > Yes
    |

    Here's the [Talker 😃](<01 😃 Talker.md>).

    ```yaml
    # 😃 Talker

    # Default prompt.
    - CONFIRM|Joyful? 

    # Change the emoji.
    - INFO|Changing to neutral.
    - EMOJI|😶
    
    # Confirm two sequential prompts.
    - CONFIRM|Now neutral?
    - CONFIRM|Still neutral?
    ```

    ---
    <br/>