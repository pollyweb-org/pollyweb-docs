# 😶 Talker `EMOJI` command

> Implements the [Input emojis 😶](<😶 Input emojis.md>) feature.

<br/>

1. **What is the EMOJI command?**

    An `EMOJI`
    * is a [Command ⌘](<../../Scripts 📃/📃 basics/Command ⌘.md>) 
    * that defaults all upcoming [Input prompts ✏️](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>)
    * via the [`$.Chat` 🧠 holder](<../../Scripts 📃/📃 holders 🧠/$.Chat 💬/💬 $.Chat 🧠 holder.md>) holder
    * in the [`PromptEmoji` 📃 script](<../../Talkers 😃/😃⏩ Talker flows/Send Prompts 😃⏩🧑‍🦰/😃 Prompts 📃 emoji.md>)
    * to [use another emoji 😶](<😶 Input emojis.md>) other than the default smile 😃 emoji.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    EMOJI|<emoji> 
    ```
    | Input| Purpose | Example
    |-|-|-
    | `<emoji>` | Emoji for upcoming [Input prompts ✏️](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>) | `😶`
    

    ---
    <br/>

1. **What's an example?**

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Joyful? [Yes, No] | > Yes
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Changing to neutral.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😶 Now neutral? [Yes, No] | > Yes
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😶 Still neutral? [Yes, No] | > Yes
    |

    Here's the [Script 📃](<../../Scripts 📃/📃 basics/Script 📃.md>).

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