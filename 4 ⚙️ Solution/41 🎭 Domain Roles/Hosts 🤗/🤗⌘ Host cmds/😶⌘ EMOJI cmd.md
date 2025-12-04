# 😶 Talker `EMOJI` command

> About
* Implements the [Input emojis 😶](<../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶 Input emojis.md>) feature.


## FAQ

1. **What is the EMOJI command?**

    An `EMOJI`
    * is a [Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that defaults all upcoming [Input prompts ✏️](<../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>)
    * via the [`$.Chat` 🧠 holder](<../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) holder
    * in the [`PromptEmoji` 📃 script](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Chats 💬 Emoji 🤗🚀🤵/🤵 Emoji 🚀 call.md>)
    * to [use another emoji 😶](<../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶 Input emojis.md>) other than the default smile 😃 emoji.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    EMOJI|<emoji> 
    ```
    | Input| Purpose | Example
    |-|-|-
    | `<emoji>` | Emoji for upcoming [Input prompts ✏️](<../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | `😶`
    

    ---
    <br/>

1. **What's an example?**

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Joyful? [Yes, No] | > Yes
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Changing to neutral.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😶 Now neutral? [Yes, No] | > Yes
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😶 Still neutral? [Yes, No] | > Yes
    |

    Here's the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # Default prompt.
    - CONFIRM|Joyful? 

    # Change the emoji.
    - INFO|Changing to neutral.
    - EMOJI|😶
    
    # Confirm two sequential prompts.
    - CONFIRM|Now neutral?
    - CONFIRM|Still neutral?
    ```
    Uses: [`CONFIRM`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`EMOJI`](<😶⌘ EMOJI cmd.md>) [`INFO`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>