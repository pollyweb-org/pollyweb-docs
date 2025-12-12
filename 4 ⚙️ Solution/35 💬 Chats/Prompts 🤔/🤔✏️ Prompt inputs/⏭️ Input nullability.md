# ⏭️ Input nullability

> Part of [✏️ Input prompts](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>)

## FAQ

1. **How to define a mandatory input?**

    Inputs are mandatory by default.

    ---
    <br/>

1. **Can users reject a mandatory input prompt?**

    No. Like in a conversation between two persons, 
    * users can only stay silent 
    * or [abandon the conversation 👉](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Chats 💬/Abandon 💬🤵/🧑‍🦰 Abandon chat ⏩ flow.md>).

    ---
    <br/>


1. **What does a mandatory input look like?**

    Here's a [Chat 💬](<../../Chats 💬/💬 Chat.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 What's the code? | ` `
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ❌ Required input.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 What's the code? | `0123`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Your code is `0123`
    |

    <br/>
    
    Here's the [Script 📃](<../../Scripts 📃/Script 📃.md>).

    ```yaml
    # 😃 Talker
    - DIGITS: What's the code? >> $code
    - DONE: Your code is `{$code}`
    ```
    Uses: [`DIGITS`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DIGITS 🔢/🔢 DIGITS ⌘ cmd.md>) [`DONE`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
    
    ---
    <br/>



1. **How to define optional inputs?**

    [Input prompts ✏️](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>) 
    * can be made optional 
    * by setting the property `Nullable` to `True` or `Yes`.
    
    ---
    <br/>



1. **What does an optional input look like?**

    Here's a [Chat 💬](<../../Chats 💬/💬 Chat.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 What's the code? | ` `
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ You didn't provide a code.
    |

    <br/>

    Here's the [Script 📃](<../../Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    - DIGITS >> $code:
        Text: What's the code? 
        Nullable: True

    - IF $code:
        DONE: Your code is `{$code}`
    - ELSE:
        FAIL: You didn't provide a code.
    ```
    Uses: [`DIGITS`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DIGITS 🔢/🔢 DIGITS ⌘ cmd.md>) [`DONE`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`FAIL`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) [`IF`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) 

    <br/>

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ```yaml
    Format: DIGITS
    Emoji: 😃 
    Text: What's the code?
    ```

    ---
    <br/>
