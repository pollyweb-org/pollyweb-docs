# 😶 Talker `EMOJI` command

> Implements the [🫥 Input emojis](<14 😶 Input emojis.md>) feature.

<br/>

1. **What is the EMOJI command?**

    An `EMOJI`
    * is a [Command ⌘](<../../😃 Talkers/😃⚙️ Talker cmds/⌘ Command.md>) 
    * that defaults all upcoming [Input prompts ✏️](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>)
    * to [use another emoji 😶](<14 😶 Input emojis.md>) other than the default smile 😃 emoji.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    EMOJI|<emoji> 
    ```
    | Argument| Purpose | Example
    |-|-|-
    | `<emoji>` | Emoji for upcoming [Input prompts ✏️](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>) | `😶`
    

    ---
    <br/>

1. **What's an example?**

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Joyful? [Yes, No] | > Yes
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Changing to neutral.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😶 Now neutral? [Yes, No] | > Yes
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😶 Still neutral? [Yes, No] | > Yes
    |

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker.md>).

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