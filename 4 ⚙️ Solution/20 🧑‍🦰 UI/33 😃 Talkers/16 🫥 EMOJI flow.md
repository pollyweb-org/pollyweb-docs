# 😶 Talker `EMOJI` command

> Implements the [🫥 Input emojis](<../31 🤔 Prompts/12 ✏️🫥 Input emojis.md>) feature.

<br/>

1. **What is the EMOJI command?**

    An `EMOJI`
    * is a [Command ⌘](<10 ⌘ Command.md>) 
    * that defaults all upcoming [Input prompts ✏️](<../31 🤔 Prompts/11 ✏️ Input behavior.md>)
    * to [use another emoji 😶](<../31 🤔 Prompts/12 ✏️🫥 Input emojis.md>) other than the default smile 😃 emoji.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    EMOJI|<emoji> 
    ```
    | Argument| Purpose | Example
    |-|-|-
    | `<emoji>` | Emoji for upcoming [Input prompts ✏️](<../31 🤔 Prompts/11 ✏️ Input behavior.md>) | `😶`
    

    ---
    <br/>

1. **What's an example?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Joyful? [Yes, No] | > Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Changing to neutral.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😶 Now neutral? [Yes, No] | > Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😶 Still neutral? [Yes, No] | > Yes
    |

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

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